"""
IntFramework Subdomain Scanner – Velgrath Edition
Flask Integration Compatible
Multi‑Engine Enumeration:
 - Wordlist brute‑force
 - DNS resolve scanning
 - Certificate transparency API
 - Passive OSINT API
"""

from __future__ import annotations
import socket
import requests
import threading
from concurrent.futures import ThreadPoolExecutor
import re

# Güvenli domain regex
SAFE_DOMAIN_REGEX = re.compile(r"^(?!-)(?!.*--)[A-Za-z0-9.-]{1,253}$")

# ThreadPool Executor
EXECUTOR = ThreadPoolExecutor(max_workers=150)

# ------------------------------------------------------------
# DOMAIN VALIDATION
# ------------------------------------------------------------
def validate_domain(domain: str) -> bool:
    return bool(SAFE_DOMAIN_REGEX.match(domain.strip()))

# ------------------------------------------------------------
# 1) WORDLIST BRUTE FORCE ENGINE
# ------------------------------------------------------------
def brute_force_engine(domain: str, wordlist_choice: str = "small"):
    """Wordlist motoru ile alt domain tarama"""
    small = ["www","mail","dev","test","api","app","vpn","cpanel"]
    medium = small + ["admin","cdn","gateway","stage","beta","static"]
    large = medium + ["backup","m","blog","db"]

    # Wordlist seçim
    wordlist = {"small": small, "medium": medium, "large": large}.get(wordlist_choice, small)
    results = []

    def check(sub):
        fqdn = f"{sub}.{domain}"
        try:
            socket.gethostbyname(fqdn)
            results.append(fqdn)
        except:
            pass

    EXECUTOR.map(check, wordlist)
    return results

# ------------------------------------------------------------
# 2) CERTIFICATE TRANSPARENCY ENGINE
# ------------------------------------------------------------
def crt_engine(domain: str):
    try:
        url = f"https://crt.sh/?q=%25.{domain}&output=json"
        resp = requests.get(url, timeout=6)
        data = resp.json()

        subs = set()
        for entry in data:
            name = entry.get("name_value")
            if name:
                for line in name.split("\n"):
                    if domain in line:
                        subs.add(line.strip())
        return list(subs)
    except:
        return []

# ------------------------------------------------------------
# 3) OSINT Passive API ENGINE
# ------------------------------------------------------------
def passive_osint_engine(domain: str):
    try:
        url = f"https://osint.sh/subdomain/?domain={domain}"
        resp = requests.get(url, timeout=6)
        js = resp.json()
        subs = js.get("subdomains", [])
        return subs if isinstance(subs, list) else []
    except:
        return []

# ------------------------------------------------------------
# 4) DNS-BASED WILDCARD RESOLVER ENGINE
# ------------------------------------------------------------
def resolver_engine(domain: str):
    test_subs = ["a","random","xyz","check"]
    results = []

    for s in test_subs:
        fqdn = f"{s}.{domain}"
        try:
            socket.gethostbyname(fqdn)
            results.append(fqdn)
        except:
            pass
    return results

# ------------------------------------------------------------
# MASTER FUNCTION (Tüm motorları birleştirir)
# ------------------------------------------------------------
def multi_engine_subdomain_scan(domain: str, engines: list[str] = None, wordlist_choice: str = "small"):
    """
    Multi-engine subdomain tarama.
    - engines: ['brute_force','crt','osint','resolver']
    - wordlist_choice: small, medium, large
    """
    if not validate_domain(domain):
        return []

    results = set()
    if engines is None:
        engines = ["brute_force","crt","osint","resolver"]

    engine_map = {
        "brute_force": lambda: brute_force_engine(domain, wordlist_choice),
        "crt": lambda: crt_engine(domain),
        "osint": lambda: passive_osint_engine(domain),
        "resolver": lambda: resolver_engine(domain)
    }

    futures = [EXECUTOR.submit(engine_map[e]) for e in engines if e in engine_map]

    for f in futures:
        try:
            for sub in f.result():
                results.add(sub)
        except:
            pass

    return sorted(results)