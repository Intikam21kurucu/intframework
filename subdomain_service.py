# subdomain_service.py
"""
IntFramework Subdomain Scanner – Velgrath Edition
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

SAFE_DOMAIN_REGEX = re.compile(r"^(?!-)(?!.*--)[A-Za-z0-9.-]{1,253}$")

EXECUTOR = ThreadPoolExecutor(max_workers=150)


def validate_domain(domain: str) -> bool:
    return bool(SAFE_DOMAIN_REGEX.match(domain))


# ------------------------------------------------------------
# 1) WORDLIST BRUTE FORCE ENGINE
# ------------------------------------------------------------

def brute_force_engine(domain: str):
    wordlist = [
        "www", "mail", "dev", "test", "api", "app", "vpn", "cpanel",
        "admin", "cdn", "gateway", "stage", "beta", "static",
        "backup", "m", "blog", "db"
    ]
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
# 3) OSINT Passive API Engine (osint.sh)
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
# 4) DNS-Based Wildcard Resolver Engine
# ------------------------------------------------------------

def resolver_engine(domain: str):
    test_subs = ["a", "random", "xyz", "check"]
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

def multi_engine_subdomain_scan(domain: str):
    if not validate_domain(domain):
        return []

    results = set()

    engines = [
        brute_force_engine,
        crt_engine,
        passive_osint_engine,
        resolver_engine
    ]

    futures = [EXECUTOR.submit(engine, domain) for engine in engines]

    for f in futures:
        try:
            for sub in f.result():
                results.add(sub)
        except:
            pass

    return sorted(results)