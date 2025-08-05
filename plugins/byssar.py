import argparse
import requests
import json
import sys
import time
from urllib.parse import urlparse
from prompt_toolkit import prompt
from prompt_toolkit.validation import Validator, ValidationError
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()

# --- Validators ---
class URLValidator(Validator):
    def validate(self, document):
        url = document.text.strip()
        if not (url.startswith("http://") or url.startswith("https://")):
            raise ValidationError(message="URL must start with http:// or https://", cursor_position=0)

class HTTPMethodValidator(Validator):
    def validate(self, document):
        method = document.text.upper()
        valid_methods = ["GET", "POST", "PUT", "DELETE", "HEAD", "OPTIONS", "PATCH"]
        if method not in valid_methods:
            raise ValidationError(message=f"Invalid HTTP method: {method}", cursor_position=0)

LANGS = {
    "en": {
        "welcome": "HTTP Header Spoofing & Bypass Tool - intSpLoiT Plugin",
        "url_prompt": "Target URL:",
        "method_prompt": "HTTP Method:",
        "invalid_url": "Invalid URL! Must start with http:// or https://",
        "header_add": "Add a header? (y/n):",
        "header_key": "Header key:",
        "header_val": "Header value:",
        "data_add": "Add POST/PUT data? (y/n):",
        "data_key": "Data key:",
        "data_val": "Data value:",
        "sending_request": "Sending request to {url} with method {method}...",
        "response_status": "Response Status Code:",
        "response_len": "Content Length:",
        "response_headers": "Response Headers:",
        "response_json": "Response JSON:",
        "response_text_search": "Search keyword in response body (press Enter to skip):",
        "keyword_found": "Keyword found!",
        "keyword_not_found": "Keyword not found or no keyword entered.",
        "save_response": "Save response to file? (y/n):",
        "saved_file": "Saved response to file: {filename}",
        "error": "Error:",
        "invalid_method": "Invalid HTTP method!",
        "yes": "y",
        "no": "n",
        "bypass_test": "Bypass Header Tests",
        "bypass_header": "Header",
        "status": "Status",
        "server": "Server",
        "path_scan": "Common Path Scan",
        "path": "Path",
        "use_interactive": "Use interactive mode? (y/n):",
        "language_prompt": "Select language (en/tr/ru/ar/de):",
        "goodbye": "Exiting. Goodbye!",
        "help_text": "Run with -h for options. Example:\npython3 tool.py -u https://example.com -X GET --language tr --scan",
    },
    "tr": {
        "welcome": "HTTP Header Spoofing & Bypass Aracı - intSpLoiT Eklentisi",
        "url_prompt": "Hedef URL:",
        "method_prompt": "HTTP Metodu:",
        "invalid_url": "Geçersiz URL! http:// veya https:// ile başlamalıdır.",
        "header_add": "Header eklemek ister misin? (e/h):",
        "header_key": "Header anahtarı:",
        "header_val": "Header değeri:",
        "data_add": "POST/PUT verisi eklemek ister misin? (e/h):",
        "data_key": "Veri anahtarı:",
        "data_val": "Veri değeri:",
        "sending_request": "{url} adresine {method} metodu ile istek gönderiliyor...",
        "response_status": "Yanıt Durum Kodu:",
        "response_len": "İçerik Uzunluğu:",
        "response_headers": "Yanıt Headerları:",
        "response_json": "JSON Yanıtı:",
        "response_text_search": "Yanıt metninde kelime ara (boş bırakmak için Enter):",
        "keyword_found": "Kelime bulundu!",
        "keyword_not_found": "Kelime bulunamadı veya girilmedi.",
        "save_response": "Yanıt dosyaya kaydedilsin mi? (e/h):",
        "saved_file": "Yanıt dosyaya kaydedildi: {filename}",
        "error": "Hata:",
        "invalid_method": "Geçersiz HTTP metodu!",
        "yes": "e",
        "no": "h",
        "bypass_test": "Bypass Header Testleri",
        "bypass_header": "Header",
        "status": "Durum",
        "server": "Sunucu",
        "path_scan": "Yaygın Yol Taraması",
        "path": "Yol",
        "use_interactive": "Etkileşimli mod kullanılsın mı? (e/h):",
        "language_prompt": "Dil seç (en/tr/ru/ar/de):",
        "goodbye": "Çıkılıyor. Hoşça kal!",
        "help_text": "Seçenekler için -h ile çalıştırın. Örnek:\npython3 tool.py -u https://example.com -X GET --language tr --scan",
    },
    "ru": {
        "welcome": "Инструмент подделки HTTP заголовков и обхода - плагин intSpLoiT",
        "url_prompt": "Целевой URL:",
        "method_prompt": "HTTP метод:",
        "invalid_url": "Неверный URL! Должен начинаться с http:// или https://",
        "header_add": "Добавить заголовок? (д/н):",
        "header_key": "Ключ заголовка:",
        "header_val": "Значение заголовка:",
        "data_add": "Добавить данные POST/PUT? (д/н):",
        "data_key": "Ключ данных:",
        "data_val": "Значение данных:",
        "sending_request": "Отправка запроса на {url} с методом {method}...",
        "response_status": "Код ответа:",
        "response_len": "Длина содержимого:",
        "response_headers": "Заголовки ответа:",
        "response_json": "JSON ответ:",
        "response_text_search": "Поиск слова в теле ответа (нажмите Enter для пропуска):",
        "keyword_found": "Слово найдено!",
        "keyword_not_found": "Слово не найдено или не введено.",
        "save_response": "Сохранить ответ в файл? (д/н):",
        "saved_file": "Ответ сохранён в файл: {filename}",
        "error": "Ошибка:",
        "invalid_method": "Неверный HTTP метод!",
        "yes": "д",
        "no": "н",
        "bypass_test": "Тесты обхода заголовков",
        "bypass_header": "Заголовок",
        "status": "Статус",
        "server": "Сервер",
        "path_scan": "Сканирование общих путей",
        "path": "Путь",
        "use_interactive": "Использовать интерактивный режим? (д/н):",
        "language_prompt": "Выберите язык (en/tr/ru/ar/de):",
        "goodbye": "Выход. До свидания!",
        "help_text": "Запустите с -h для опций. Пример:\npython3 tool.py -u https://example.com -X GET --language ru --scan",
    },
    "ar": {
        "welcome": "أداة تزوير رؤوس HTTP وتجاوز الحجب - مكون intSpLoiT",
        "url_prompt": "رابط الهدف:",
        "method_prompt": "طريقة HTTP:",
        "invalid_url": "رابط غير صالح! يجب أن يبدأ بـ http:// أو https://",
        "header_add": "هل تريد إضافة رأس؟ (ن/ل):",
        "header_key": "مفتاح الرأس:",
        "header_val": "قيمة الرأس:",
        "data_add": "هل تريد إضافة بيانات POST/PUT؟ (ن/ل):",
        "data_key": "مفتاح البيانات:",
        "data_val": "قيمة البيانات:",
        "sending_request": "إرسال طلب إلى {url} بطريقة {method}...",
        "response_status": "رمز الاستجابة:",
        "response_len": "طول المحتوى:",
        "response_headers": "رؤوس الاستجابة:",
        "response_json": "استجابة JSON:",
        "response_text_search": "ابحث عن كلمة في نص الاستجابة (اضغط Enter للتخطي):",
        "keyword_found": "تم العثور على الكلمة!",
        "keyword_not_found": "الكلمة غير موجودة أو لم يتم إدخالها.",
        "save_response": "هل تريد حفظ الاستجابة في ملف؟ (ن/ل):",
        "saved_file": "تم حفظ الاستجابة في الملف: {filename}",
        "error": "خطأ:",
        "invalid_method": "طريقة HTTP غير صالحة!",
        "yes": "ن",
        "no": "ل",
        "bypass_test": "اختبارات تجاوز رؤوس HTTP",
        "bypass_header": "الرأس",
        "status": "الحالة",
        "server": "الخادم",
        "path_scan": "مسح المسارات الشائعة",
        "path": "المسار",
        "use_interactive": "استخدام الوضع التفاعلي؟ (ن/ل):",
        "language_prompt": "اختر اللغة (en/tr/ru/ar/de):",
        "goodbye": "الخروج. وداعًا!",
        "help_text": "شغّل مع -h للاطلاع على الخيارات. مثال:\npython3 tool.py -u https://example.com -X GET --language ar --scan",
    },
    "de": {
        "welcome": "HTTP Header Spoofing & Bypass Tool - intSpLoiT Plugin",
        "url_prompt": "Ziel-URL:",
        "method_prompt": "HTTP Methode:",
        "invalid_url": "Ungültige URL! Muss mit http:// oder https:// beginnen.",
        "header_add": "Header hinzufügen? (j/n):",
        "header_key": "Header Schlüssel:",
        "header_val": "Header Wert:",
        "data_add": "POST/PUT Daten hinzufügen? (j/n):",
        "data_key": "Daten-Schlüssel:",
        "data_val": "Daten-Wert:",
        "sending_request": "Sende Anfrage an {url} mit Methode {method}...",
        "response_status": "Antwort-Statuscode:",
        "response_len": "Inhaltslänge:",
        "response_headers": "Antwort-Header:",
        "response_json": "Antwort im JSON-Format:",
        "response_text_search": "Schlüsselwort im Antworttext suchen (Enter zum Überspringen):",
        "keyword_found": "Schlüsselwort gefunden!",
        "keyword_not_found": "Schlüsselwort nicht gefunden oder nicht eingegeben.",
        "save_response": "Antwort in Datei speichern? (j/n):",
        "saved_file": "Antwort gespeichert in Datei: {filename}",
        "error": "Fehler:",
        "invalid_method": "Ungültige HTTP Methode!",
        "yes": "j",
        "no": "n",
        "bypass_test": "Bypass Header Tests",
        "bypass_header": "Header",
        "status": "Status",
        "server": "Server",
        "path_scan": "Scan gängiger Pfade",
        "path": "Pfad",
        "use_interactive": "Interaktiver Modus verwenden? (j/n):",
        "language_prompt": "Sprache auswählen (en/tr/ru/ar/de):",
        "goodbye": "Beenden. Auf Wiedersehen!",
        "help_text": "Mit -h starten für Optionen. Beispiel:\npython3 tool.py -u https://example.com -X GET --language de --scan",
    }
}

# --- Sabitler ---
BYPASS_HEADERS = [
    {"X-Forwarded-For": "127.0.0.1"},
    {"X-Originating-IP": "127.0.0.1"},
    {"X-Remote-IP": "127.0.0.1"},
    {"X-Client-IP": "127.0.0.1"},
    {"True-Client-IP": "127.0.0.1"},
    {"X-Host": "127.0.0.1"},
    {"X-Forwarded-Host": "127.0.0.1"},
]

COMMON_PATHS = [
    "/", "/admin", "/login", "/dashboard", "/cpanel", "/config", "/server-status", "/api", "/.git/"
]

VALID_METHODS = ["GET", "POST", "PUT", "DELETE", "HEAD", "OPTIONS", "PATCH"]

DEFAULT_TIMEOUT = 10

# --- Yardımcı Fonksiyonlar ---

def parse_key_value_list(kv_list):
    """
    ['key:value', 'key=value'] formatlarını dict'e çevirir.
    Hatalı formatları görmezden gelir.
    """
    result = {}
    if not kv_list:
        return result
    for item in kv_list:
        if ":" in item:
            k, v = item.split(":", 1)
        elif "=" in item:
            k, v = item.split("=", 1)
        else:
            continue
        result[k.strip()] = v.strip()
    return result

def build_headers(base_headers=None, extra_headers=None, user_agent=None):
    """
    Header dictionary oluşturur.
    Base headerlar, ekstra headerlar ile güncellenir.
    User-Agent özel olarak ayarlanabilir.
    """
    headers = {
        "User-Agent": "intSpLoiT-HeaderSpoofer/1.0",
        "Accept": "*/*",
        "Connection": "close",
    }

    if base_headers:
        headers.update(base_headers)

    if user_agent:
        headers["User-Agent"] = user_agent

    if extra_headers:
        headers.update(extra_headers)

    return headers

def safe_request(method, url, headers=None, data=None, timeout=DEFAULT_TIMEOUT, verify_ssl=True):
    """
    Güvenli HTTP isteği. Hata olursa (timeout, bağlantı, vb.) None ve hata mesajı döner.
    """
    try:
        response = requests.request(method, url, headers=headers, data=data, timeout=timeout, verify=verify_ssl)
        return response, None
    except requests.RequestException as e:
        return None, str(e)

# --- Kullanıcıdan Veri Alma ---

def prompt_headers(lang_msgs):
    """
    Kullanıcıdan interaktif header girişini alır.
    """
    headers = {}
    while True:
        yn = prompt(lang_msgs["header_add"] + " ").lower()
        if yn != lang_msgs["yes"]:
            break
        key = prompt(lang_msgs["header_key"] + " ")
        val = prompt(lang_msgs["header_val"] + " ")
        if key and val:
            headers[key] = val
    return headers

def prompt_data(lang_msgs):
    """
    Kullanıcıdan interaktif POST/PUT/PATCH data girişini alır.
    """
    data = {}
    while True:
        yn = prompt(lang_msgs["data_add"] + " ").lower()
        if yn != lang_msgs["yes"]:
            break
        key = prompt(lang_msgs["data_key"] + " ")
        val = prompt(lang_msgs["data_val"] + " ")
        if key:
            data[key] = val
    return data if data else None

def interactive_input(lang_msgs):
    """
    İnteraktif modda URL, metod, header ve data ister.
    Validatorlar ile hatalı giriş engellenir.
    """
    url = prompt(lang_msgs["url_prompt"] + " ", validator=URLValidator())
    method = prompt(lang_msgs["method_prompt"] + " ", validator=HTTPMethodValidator(), default="GET").upper()
    headers = prompt_headers(lang_msgs)
    data = None
    if method in ["POST", "PUT", "PATCH"]:
        data = prompt_data(lang_msgs)
    return url, method, headers, data

# --- Ana İşlemler ---

def display_response(response, lang_msgs, keyword=None):
    """
    Gelen HTTP cevabını detaylı ve görsel olarak gösterir.
    JSON içeriği varsa prettify eder.
    İstenirse içerikte keyword arar.
    Dosyaya kaydetme opsiyonu sunar.
    """
    if not response:
        console.print(f"[red]{lang_msgs['error']} Unknown error or no response.[/red]")
        return

    console.rule(lang_msgs["response_status"])
    console.print(f"[green]{lang_msgs['response_status']}[/green]: {response.status_code}")
    console.print(f"[green]{lang_msgs['response_len']}[/green]: {len(response.content)}")
    console.print(Panel.fit(lang_msgs["response_headers"]))

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Header")
    table.add_column("Value")
    for k, v in response.headers.items():
        table.add_row(k, v)
    console.print(table)

    ctype = response.headers.get("Content-Type", "").lower()
    if "application/json" in ctype:
        try:
            json_data = response.json()
            console.print(Panel.fit(lang_msgs["response_json"]))
            console.print(json.dumps(json_data, indent=2, ensure_ascii=False))
        except Exception:
            console.print(f"[yellow]{lang_msgs['error']} JSON parse failed[/yellow]")
    else:
        if keyword is None:
            keyword = prompt(lang_msgs["response_text_search"] + " ")
        if keyword:
            if keyword in response.text:
                console.print(f"[green]{lang_msgs['keyword_found']}[/green]")
            else:
                console.print(f"[red]{lang_msgs['keyword_not_found']}[/red]")

    save = prompt(lang_msgs["save_response"] + " ").lower()
    if save == lang_msgs["yes"]:
        filename = urlparse(response.url).netloc.replace(".", "_") + ".html"
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(response.text)
            console.print(f"[blue]{lang_msgs['saved_file'].format(filename=filename)}[/blue]")
        except Exception as e:
            console.print(f"[red]{lang_msgs['error']} File save failed: {e}[/red]")

def bypass_tests(url, lang_msgs, timeout=DEFAULT_TIMEOUT, verify_ssl=True):
    """
    Belirlenen bypass headerlarını teker teker gönderir,
    sonuçları tablolayarak gösterir.
    """
    console.rule(lang_msgs["bypass_test"])
    table = Table(title=lang_msgs["bypass_test"], show_header=True, header_style="bold cyan")
    table.add_column(lang_msgs["bypass_header"])
    table.add_column(lang_msgs["status"])
    table.add_column(lang_msgs["server"])

    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
        task = progress.add_task("[cyan]Running bypass header tests...", total=len(BYPASS_HEADERS))
        for hdr in BYPASS_HEADERS:
            key, val = next(iter(hdr.items()))
            resp, err = safe_request("GET", url, headers={key: val}, timeout=timeout, verify_ssl=verify_ssl)
            if resp:
                status = str(resp.status_code)
                server = resp.headers.get("Server", "N/A")
            else:
                status = "Error"
                server = err
            table.add_row(key, status, server)
            progress.advance(task)
            time.sleep(0.15)
    console.print(table)

def path_scan(url, lang_msgs, timeout=DEFAULT_TIMEOUT, verify_ssl=True):
    """
    COMMON_PATHS listesindeki yolları hedefe tarar,
    sonuçları tablolayarak gösterir.
    """
    console.rule(lang_msgs["path_scan"])
    table = Table(title=lang_msgs["path_scan"], show_header=True, header_style="bold green")
    table.add_column(lang_msgs["path"])
    table.add_column(lang_msgs["status"])
    table.add_column(lang_msgs["server"])

    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
        task = progress.add_task("[green]Scanning common paths...", total=len(COMMON_PATHS))
        for path in COMMON_PATHS:
            full_url = url.rstrip('/') + path
            resp, err = safe_request("GET", full_url, timeout=timeout, verify_ssl=verify_ssl)
            if resp:
                status = str(resp.status_code)
                server = resp.headers.get("Server", "N/A")
            else:
                status = "Error"
                server = err
            table.add_row(path, status, server)
            progress.advance(task)
            time.sleep(0.15)
    console.print(table)

# --- Ana plugin fonksiyonu ---

def plugin_main(args, LANGS):
    lang_msgs = LANGS[args.language]

    console.print(Panel.fit(f"[bold cyan]{lang_msgs['welcome']}[/bold cyan]"))

    # İnteraktif mod
    if args.interactive:
        url, method, base_headers, data = interactive_input(lang_msgs)
    else:
        url = args.url
        method = args.method.upper()
        base_headers = parse_key_value_list(args.header)
        data = parse_key_value_list(args.data) if method in ["POST", "PUT", "PATCH"] else None
        if not url:
            console.print(f"[red]{lang_msgs['error']} URL is required if not in interactive mode.[/red]")
            return

    # URL doğrulama
    if not (url.startswith("http://") or url.startswith("https://")):
        console.print(f"[red]{lang_msgs['invalid_url']}[/red]")
        return

    # Metod doğrulama
    if method not in VALID_METHODS:
        console.print(f"[red]{lang_msgs['invalid_method']}[/red]")
        return

    # Ekstra header ve User-Agent
    extra_headers = parse_key_value_list(args.extra_header)
    headers = build_headers(base_headers, extra_headers, user_agent=args.user_agent)

    console.print(f"[blue]{lang_msgs['sending_request'].format(url=url, method=method)}[/blue]")

    response, error = safe_request(method, url, headers=headers, data=data, timeout=args.timeout, verify_ssl=not args.no_verify)
    if error or not response:
        console.print(f"[red]{lang_msgs['error']} {error}[/red]")
        return

    display_response(response, lang_msgs, keyword=args.keyword)

    bypass_tests(url, lang_msgs, timeout=args.timeout, verify_ssl=not args.no_verify)

    if args.scan:
        path_scan(url, lang_msgs, timeout=args.timeout, verify_ssl=not args.no_verify)

    console.print(f"[green]{lang_msgs['goodbye']}[/green]")

# --- Plugin Sınıfı ---

class Plugin:
    def __init__(self):
        self.name = "HeaderBypass"
        self.commands = {
            "byssar": {
                "func": self.run,
                "desc": "HTTP Header Spoofing and Bypass Scanner",
                "usage": (
                    "headerbypass -u <url> -X GET --scan "
                    "--language tr -i --extra-header X-Test:Value "
                    "--user-agent 'CustomAgent/1.0' --timeout 15 --no-verify "
                    "--keyword 'secret'"
                ),
            }
        }

    def run(self, arg_list):
        import argparse

        parser = argparse.ArgumentParser(
            prog="byssar",
            description="HTTP Header Spoofing & Bypass Tool - intSpLoiT Plugin",
            formatter_class=argparse.RawTextHelpFormatter
        )

        # Temel URL ve HTTP metodları
        parser.add_argument("-u", "--url", help="Target URL (must start with http:// or https://)")
        parser.add_argument("-X", "--method", default="GET", help="HTTP Method (GET, POST, PUT, DELETE, etc.)")

        # Header yönetimi
        parser.add_argument(
            "--header", nargs="*", default=[],
            help="Base headers to send with request, format: 'Key:Value' or 'Key=Value'"
        )
        parser.add_argument(
            "--extra-header", nargs="*", default=[],
            help="Extra headers to add or override base headers, format: 'Key:Value' or 'Key=Value'"
        )
        parser.add_argument(
            "--user-agent", type=str, default=None,
            help="Custom User-Agent string to override default"
        )

        # Veri (body) gönderimi
        parser.add_argument(
            "--data", nargs="*", default=[],
            help="Data for POST/PUT/PATCH requests, format: 'key=value'"
        )

        # İleri seçenekler
        parser.add_argument(
            "-i", "--interactive", action="store_true",
            help="Run in interactive mode to input all options step-by-step"
        )
        parser.add_argument(
            "--scan", action="store_true",
            help="Scan common admin/login paths after main request"
        )
        parser.add_argument(
            "--keyword", type=str, default=None,
            help="Search keyword in response body (skips interactive prompt if given)"
        )
        parser.add_argument(
            "--timeout", type=int, default=10,
            help="Request timeout in seconds (default: 10)"
        )
        parser.add_argument(
            "--no-verify", action="store_true",
            help="Disable SSL certificate verification (useful for self-signed certs)"
        )
        parser.add_argument(
            "--language", choices=["en", "tr", "ru", "ar", "de"], default="en",
            help="Language for prompts and messages"
        )

        args = parser.parse_args(arg_list)

        # Dışardan LANGS eklenecek varsayımıyla ana fonksiyon çağrısı
        from sys import exit

        try:
            # LANGS dışardan eklenecek, main fonksiyona çağrı yapılacak
            # Burada plugin_main fonksiyonu yukarıda tanımlanmalı ve LANGS parametresi almalı
            # Örnek kullanım:
            plugin_main(args, LANGS)
        except Exception as e:
            console.print(f"[red][!] Fatal error: {e}[/red]")
            exit(1)

        return ""