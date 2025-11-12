# lib/intai/summarizer.py
"""
Gelişmiş, geri uyumlu ve Android-dostu extractive/hibrit özetleyici.
Kullanım arayüzü korunur: summarize(text, max_sentences=3)

Özellikler:
- Gelişmiş pipeline: TF-IDF + TextRank + clustering + keyword extraction
- Eksik kütüphane durumunda hafif fallback (orijinal frekans tabanlı algoritma)
- Exploit/incident raporları için özel çıkarım ve yapılandırılmış özet (JSON)
- Opsiyonel abstractive adımı (kullanılabilir model varsa)
- Android/Termux'ta çalışabilecek şekilde koşullara uyumlu tasarım
"""

from typing import List, Tuple, Dict, Any
import re
import math
from collections import Counter, defaultdict

# --- Hafif tokenizasyon / cümle bölme (orijinal davranışı korur) ---
_SENTENCE_SPLIT_RE = re.compile(r'(?<=[.!?])\s+')

def split_sentences(text: str) -> List[str]:
    sentences = [s.strip() for s in _SENTENCE_SPLIT_RE.split(text) if s.strip()]
    return sentences

def tokenize_words(text: str) -> List[str]:
    # Türkçe karakterleri, Latin genişletmeleri ve rakamları izin ver
    text = re.sub(r'[^0-9a-zA-ZığüşöçıİĞÜŞÖÇßàáâäãåāéèêëėîïíìôöōõùúûüçñ\-]', ' ', text.lower())
    words = [w for w in text.split() if len(w) > 1]
    return words

# --- Dynamic import: gelişmiş pipeline için gerekli kütüphaneler opsiyonel ---
_HAS_SKLEARN = True
_HAS_NETWORKX = True
_HAS_NUMPY = True
_HAS_TRANSFORMERS = True

try:
    import numpy as np
except Exception:
    _HAS_NUMPY = False

try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
except Exception:
    _HAS_SKLEARN = False

try:
    import networkx as nx
except Exception:
    _HAS_NETWORKX = False

try:
    # transformers yalnızca opsiyonel abstractive adımı için
    from transformers import pipeline as hf_pipeline
except Exception:
    _HAS_TRANSFORMERS = False

# --- Basit, frekans tabanlı scorer (fallback) - mevcut kodun evrimleşmiş hali ---
def _freq_score_sentences(text: str) -> List[Tuple[str, float]]:
    sentences = split_sentences(text)
    words = tokenize_words(text)
    if not words or not sentences:
        return []
    freq = Counter(words)
    maxf = max(freq.values())
    for k in list(freq.keys()):
        freq[k] = freq[k] / maxf
    scores = []
    for s in sentences:
        s_words = tokenize_words(s)
        if not s_words:
            scores.append((s, 0.0))
            continue
        s_score = sum(freq.get(w, 0.0) for w in s_words) / math.sqrt(len(s_words))
        scores.append((s, s_score))
    return scores

# --- Gelişmiş TextRank + TF-IDF scorer (varsa kullanılır) ---
def _textrank_score_sentences(sentences: List[str]) -> List[Tuple[str, float]]:
    # Eğer gerekli kütüphaneler yoksa hata fırlatmaz; çağıran kontrol eder.
    if not sentences:
        return []
    vectorizer = TfidfVectorizer(stop_words='turkish')  # Türkçe stop-word'ler kullanılır (sklearn varsa)
    tfidf_matrix = vectorizer.fit_transform(sentences)
    sim_matrix = cosine_similarity(tfidf_matrix)
    # similarity matrisini normalize etme (gürültüden temizlemek için)
    if _HAS_NUMPY:
        sim_matrix = np.nan_to_num(sim_matrix)
    if _HAS_NETWORKX:
        nx_graph = nx.from_numpy_array(sim_matrix)
        scores = nx.pagerank(nx_graph, max_iter=200)
        return [(sentences[i], scores.get(i, 0.0)) for i in range(len(sentences))]
    else:
        # networkx yoksa manuel PageRank uygulaması (basit)
        n = len(sentences)
        # normalize sim_matrix rows
        ranks = [1.0 / n] * n
        damping = 0.85
        for _ in range(40):
            new_ranks = [(1 - damping) / n] * n
            for i in range(n):
                row_sum = sum(sim_matrix[i])
                if row_sum == 0:
                    continue
                for j in range(n):
                    # pagerank contribution from j to i
                    col_sum = sum(sim_matrix[:, j]) if _HAS_NUMPY else sum(sim_matrix[k][j] for k in range(n))
                    if col_sum == 0:
                        continue
                    contrib = damping * (sim_matrix[i][j] / col_sum) * ranks[j]
                    new_ranks[i] += contrib
            ranks = new_ranks
        return [(sentences[i], ranks[i]) for i in range(n)]

# --- Cümle kümeleme ile çeşitliliği sağlama ---
def _select_diverse_top(sentences: List[str], scored: List[Tuple[str, float]], top_n: int) -> List[str]:
    """
    Aynı konudan tekrarlı cümleler çıkmasını engellemek için basit kümeleme mantığı.
    - yüksek puanlı cümleleri iteratif seçer, her seçilen cümle ile çok benzer cümleleri eşiğe göre elemine eder.
    - sklearn yoksa sadece puana göre seçer.
    """
    if not scored:
        return []
    # sıralı (en yüksekten)
    scored_sorted = sorted(scored, key=lambda x: x[1], reverse=True)
    selected = []
    blocked = set()

    # similarity matrix yalnızca sklearn varsa hesaplanır
    sim_matrix = None
    if _HAS_SKLEARN and len(sentences) > 1:
        try:
            vectorizer = TfidfVectorizer(stop_words='turkish')
            tfidf = vectorizer.fit_transform(sentences)
            sim_matrix = cosine_similarity(tfidf)
        except Exception:
            sim_matrix = None

    for cand, _score in scored_sorted:
        if len(selected) >= top_n:
            break
        if cand in blocked:
            continue
        # seç
        selected.append(cand)
        # benzer cümleleri blokla (eşik 0.75)
        if sim_matrix is not None:
            idx = sentences.index(cand)
            for j, simv in enumerate(sim_matrix[idx]):
                if simv >= 0.75:
                    blocked.add(sentences[j])
    # Eğer yeterince seçilemediyse geri kalan en iyi cümlelerden ekle
    if len(selected) < top_n:
        extras = [s for s, _ in scored_sorted if s not in selected]
        selected.extend(extras[:(top_n - len(selected))])
    return selected[:top_n]

# --- Anahtar kelime çıkarımı (basit ve opsiyonel) ---
def extract_keywords(text: str, top_k: int = 8) -> List[str]:
    words = tokenize_words(text)
    if not words:
        return []
    freq = Counter(words)
    # basit stop-word filtresi: çok kısa veya sayısal kelimeler zaten atılıyor
    most = [w for w, _ in freq.most_common(top_k * 3)]
    # eğer sklearn varsa tfidf ile daha kaliteli seç
    if _HAS_SKLEARN:
        try:
            sentences = split_sentences(text)
            vectorizer = TfidfVectorizer(stop_words='turkish', ngram_range=(1,2))
            tfidf = vectorizer.fit_transform(sentences)
            scores = tfidf.sum(axis=0).A1
            idxs = scores.argsort()[::-1][:top_k]
            features = vectorizer.get_feature_names_out()
            keywords = [features[i] for i in idxs]
            return keywords
        except Exception:
            pass
    # fallback: frekansa göre
    keys = []
    for w in most:
        if len(keys) >= top_k:
            break
        if all(ch.isdigit() for ch in w):
            continue
        keys.append(w)
    return keys

# --- Opsiyonel abstractive adımı (sistemde transformer yoksa devre dışı) ---
def _abstractive_refine(paragraph: str, max_length: int = 160) -> str:
    """
    Eğer transformers kütüphanesi mevcutsa basitçe bir summarization pipeline çağır.
    Android'de model indirmek çok ağır olabilir; bu adım opsiyoneldir.
    """
    if not _HAS_TRANSFORMERS:
        return paragraph  # yoksa olduğu gibi dön
    try:
        summarizer = hf_pipeline("summarization", model="t5-small", device=-1)
        out = summarizer(paragraph, max_length=max_length, min_length=30, do_sample=False)
        if out and isinstance(out, list):
            return out[0].get("summary_text", paragraph)
        return paragraph
    except Exception:
        return paragraph

# --- Ana summarize fonksiyonu (kullanım arayüzü korunur) ---
def summarize(text: str, max_sentences: int = 3) -> str:
    """
    Genel özet fonksiyonu. Arka planda mümkünse gelişmiş pipeline'ı kullanır,
    değilse hafif frekans tabanlı yönteme düşer.
    """
    if not text or not text.strip():
        return ""

    sentences = split_sentences(text)
    if not sentences:
        return ""

    # Gelişmiş pipeline tercih edilir
    use_advanced = _HAS_SKLEARN and _HAS_NETWORKX
    try:
        if use_advanced:
            scored = _textrank_score_sentences(sentences)
            # seçimi diverse yap
            selected = _select_diverse_top(sentences, scored, max_sentences)
        else:
            # fallback
            scored = _freq_score_sentences(text)
            selected = _select_diverse_top(sentences, scored, max_sentences)
    except Exception:
        # Herhangi bir hata fallback'e düşsün
        scored = _freq_score_sentences(text)
        selected = _select_diverse_top(sentences, scored, max_sentences)

    # Orijinal sıraya göre düzenle
    final = [s for s in sentences if s in selected]
    # Eğer abstractive iyileştirme uygunsa (opsiyonel) paragrafa çevirip düzelt
    paragraph = " ".join(final)
    refined = _abstractive_refine(paragraph)
    # Eğer refineler çok kısa veya çok farklıysa fallback olarak paragrafı kullan
    if refined and len(refined.split()) > 5:
        return refined
    return paragraph

# --- Exploit / incident raporu için özel özet fonksiyonu ---
def summarize_exploit_report(text: str, style: str = 'concise') -> Dict[str, Any]:
    """
    Exploit raporları için mantıklı, yapılandırılmış özet çıkarır.
    Döndürdüğü yapı:
    {
      "summary": "...",                # kısa insan okunur özet
      "keywords": [...],
      "fields": {                      # bulunan/çıkarılan alanlar
         "target": "...",
         "vulnerability": "...",
         "exploit_steps": [...],
         "impact": "...",
         "evidence": [...],
         "recommendations": [...]
      },
      "confidence": 0.0                # kabaca 0..1
    }

    - style: 'concise'|'detailed'
    """
    sentences = split_sentences(text)
    if not sentences:
        return {"summary": "", "keywords": [], "fields": {}, "confidence": 0.0}

    # 1) Anahtar kelimeler
    keywords = extract_keywords(text, top_k=10)

    # 2) Basit alan çıkarımı için regex ve anahtar kelime kalıpları
    fields = {
        "target": None,
        "vulnerability": None,
        "exploit_steps": [],
        "impact": None,
        "evidence": [],
        "recommendations": []
    }

    # regex tabanlı basit çıkarımlar (IP, URL, CVE, komut, path)
    ip_re = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
    url_re = re.compile(r'https?://[^\s,;]+')
    cve_re = re.compile(r'\bCVE-\d{4}-\d+\b', re.IGNORECASE)
    cmd_re = re.compile(r'`([^`]+)`|(?:sudo\s+[^\n\r]+)|(?:/bin/[^ \n\r]+)')
    # hedef (örnek: target: 10.0.0.1, host=..., domain: ...)
    for s in sentences:
        low = s.lower()
        if 'target' in low or 'hedef' in low or 'host' in low or 'domain' in low:
            if not fields["target"]:
                # extract first ip/url
                ip = ip_re.search(s)
                url = url_re.search(s)
                if ip:
                    fields["target"] = ip.group(0)
                elif url:
                    fields["target"] = url.group(0)
                else:
                    # fallback: kelime sonrası
                    parts = s.split(':', 1)
                    if len(parts) > 1:
                        fields["target"] = parts[1].strip()
        if not fields["vulnerability"]:
            # CVE varsa
            cve = cve_re.search(s)
            if cve:
                fields["vulnerability"] = cve.group(0)
        # exploit adımları için "adım", "step", "exploit", "payload", "use" gibi kelimelere bak
        if any(k in low for k in ['step', 'adım', 'exploit', 'payload', 'poC', 'poc', 'usage', 'kullanım', 'attack']):
            fields["exploit_steps"].append(s)
        # evidence
        if any(k in low for k in ['log', 'çıktı', 'output', 'screenshot', 'ekran görüntü', 'detection', 'evidence', 'kanıt']):
            fields["evidence"].append(s)
        # recommendations
        if any(k in low for k in ['recommend', 'öneri', 'fix', 'patch', 'mitigate', 'çözüm', 'yama', 'apply', 'implement']):
            fields["recommendations"].append(s)
        # impact
        if any(k in low for k in ['impact', 'etki', 'risk', 'seviy', 'critical', 'high', 'medium', 'low', 'confidential']):
            if not fields["impact"]:
                fields["impact"] = s

    # 3) Eğer alanlar boşsa keyword/cümle bazlı fallback atama
    if not fields["vulnerability"]:
        # anahtar kelimeler arasında CVE veya vulnerability-like ifadeyi bul
        for kw in keywords:
            if 'cve' in kw.lower():
                fields["vulnerability"] = kw
                break
    # hedef yoksa IP/URL arayıp ata
    if not fields["target"]:
        ipm = ip_re.search(text)
        urlm = url_re.search(text)
        if ipm:
            fields["target"] = ipm.group(0)
        elif urlm:
            fields["target"] = urlm.group(0)

    # 4) Özet metin: önce extractive özet sonra gerekirse abstractive refine
    # concise: en önemli 2 cümle + vulnerability ve impact vurgusu
    raw_summary = ""
    try:
        # extractive en iyi cümleler
        top_count = 2 if style == 'concise' else 4
        extract = summarize(text, max_sentences=top_count)
        raw_summary = extract
    except Exception:
        raw_summary = " ".join(sentences[:top_count])

    # 5) Mantıklı ek açıklama / yapılandırılmış cümleler oluştur
    structured_lines = []
    if fields["target"]:
        structured_lines.append(f"Hedef: {fields['target']}.")
    if fields["vulnerability"]:
        structured_lines.append(f"Zafiyet: {fields['vulnerability']}.")
    if fields["impact"]:
        structured_lines.append(f"Etkisi: {fields['impact']}.")
    if fields["exploit_steps"]:
        structured_lines.append(f"İstismar adımları (örnek): {fields['exploit_steps'][0] if fields['exploit_steps'] else ''}")

    # son özet
    summary_parts = [raw_summary] + structured_lines
    summary_text = " ".join([p for p in summary_parts if p])

    # confidence: basit heuristic
    confidence = 0.2
    if fields["vulnerability"]:
        confidence += 0.35
    if fields["exploit_steps"]:
        confidence += 0.2
    if fields["evidence"]:
        confidence += 0.15
    confidence = min(1.0, confidence)

    return {
        "summary": summary_text,
        "keywords": keywords,
        "fields": fields,
        "confidence": round(confidence, 2)
    }

# --- Küçük yardımcı: özet + anahtar kelimeler tek çağrıda ---
def summarize_with_keywords(text: str, max_sentences: int = 3) -> Dict[str, Any]:
    return {
        "summary": summarize(text, max_sentences=max_sentences),
        "keywords": extract_keywords(text, top_k=8)
    }

# --- Eğer geliştirici modu veya test gerekiyorsa örnek kullanım fonksiyonu ---
def _example_usage():
    sample = ("Target: 10.0.0.45. The application is vulnerable to SQL Injection. "
              "Exploit: send ' OR '1'='1 to the login form. Evidence: error message shows SQL syntax. "
              "Impact: full DB disclosure. Recommendation: parameterized queries and input validation.")
    print("SUMMARY:")
    print(summarize(sample))
    print("\nEXPLOIT REPORT SUMMARY:")
    from pprint import pprint
    pprint(summarize_exploit_report(sample))

# Bu dosya doğrudan çalıştırılırsa örnek göster
if __name__ == "__main__":
    _example_usage()