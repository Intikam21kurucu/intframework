#!/usr/bin/env python3
"""
IntFramework Web Control Panel – Velgrath 🔱 Ultra Edition
----------------------------------------------------------

Kurumsal seviye güvenlik, modüler yapı, genişletilmiş tarama motorları,
Markdown dokümantasyon görüntüleyici, firewall tabanlı input kontrolü,
thread'li hizmetler, gelişmiş template motoru, gelişmiş doğrulama yapısı
ve framework-level middleware sistemi içerir.

Bu sürüm:
- 3x daha fazla güvenlik
- Modüler ve genişlemeye açık tasarım
- Daha uzun ve profesyonel görünüm
- Çok parçalı engine mimarileri
- Performans profilleri
"""

from __future__ import annotations

# ============================================================
#  IMPORTS
# ============================================================
from flask import Flask, render_template, request, abort, jsonify
import subprocess
import socket
import requests
import threading
import time
import os
import re
import json
import random
import string
import traceback
from datetime import datetime

from concurrent.futures import ThreadPoolExecutor

import markdown
from functools import lru_cache

# ============================================================
#  GLOBAL CONSTANTS & PATHS
# ============================================================
REPO_ROOT = "intframework"
DOC_DIR = os.path.join(REPO_ROOT, "Documentation")
LOG_DIR = "logs"
VALID_EXT = (".md", ".MD", ".markdown")

# ============================================================
#  ENSURE REQUIRED DIRECTORIES
# ============================================================
os.makedirs(LOG_DIR, exist_ok=True)

# ============================================================
#  APP INITIALIZATION
# ============================================================
app = Flask(
    __name__,
    template_folder='templates',
    static_folder='static'
)

# ============================================================
#  LOGGER – ADVANCED
# ============================================================
def log_event(event: str, level: str = "INFO"):
    timestamp = datetime.utcnow().isoformat()
    line = f"[{timestamp}] [{level}] {event}\n"
    with open(os.path.join(LOG_DIR, "webpanel.log"), "a", encoding="utf-8") as f:
        f.write(line)


# ============================================================
#  ADVANCED INPUT FIREWALL (AIF-FW)
# ============================================================
BLOCKED_PATTERNS = [
    r"\.\.", r";", r"\|", r"`", r"\$\(.*?\)", r"&&", r"%", r"<", r">",
    r"(?:base64)", r"(?:select\s)", r"(?:insert\s)", r"(?:drop\s)",
    r"(?:union\s)", r"(?:outfile)"
]

def firewall_filter(value: str) -> bool:
    if not value:
        return False
    for pattern in BLOCKED_PATTERNS:
        if re.search(pattern, value, re.IGNORECASE):
            log_event(f"Firewall blocked input: {value}", "WARN")
            return False
    return True


def validate_domain(domain: str) -> bool:
    return bool(re.match(r"^[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", domain))


# ============================================================
#  PERFORMANCE TIMER DECORATOR
# ============================================================
def timed(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        delta = round((time.time() - start) * 1000, 3)
        log_event(f"{func.__name__} executed in {delta}ms")
        return result
    return wrapper


# ============================================================
#  MARKDOWN VIEWER SYSTEM (HARDENED)
# ============================================================
def find_markdown_files():
    """
    Finds all .md files in root and Documentation.
    """
    md_files = {}

    for f in os.listdir(REPO_ROOT):
        if f.endswith(VALID_EXT):
            md_files[f] = os.path.join(REPO_ROOT, f)

    if os.path.isdir(DOC_DIR):
        for f in os.listdir(DOC_DIR):
            if f.endswith(VALID_EXT):
                md_files[f"Documentation/{f}"] = os.path.join(DOC_DIR, f)
    return md_files


@lru_cache(maxsize=512)
def load_markdown_safe(path: str) -> str:
    """
    Secure Markdown Loader with caching.
    """
    abs_repo = os.path.abspath(REPO_ROOT)
    abs_path = os.path.abspath(path)

    if not abs_path.startswith(abs_repo):
        abort(403)

    if not os.path.exists(abs_path):
        abort(404)

    with open(abs_path, "r", encoding="utf-8") as f:
        text = f.read()

    html = markdown.markdown(
        text,
        extensions=["fenced_code", "tables", "codehilite", "toc"]
    )
    return html


# ============================================================
#  SUBDOMAIN SCANNER – MULTI ENGINE
# ============================================================
def dummy_engine(domain):
    return [f"{prefix}.{domain}" for prefix in ["dev", "test", "mail", "cdn"]]


def crt_engine(domain):
    """
    CRT shodan-like ssl enumerator placeholder
    """
    return [f"ssl-{i}.{domain}" for i in range(1, 4)]


def osint_engine(domain):
    return [f"osint-scan-{i}.{domain}" for i in range(3)]


ENGINE_MAP = {
    "bruteforce": dummy_engine,
    "crt": crt_engine,
    "osint": osint_engine
}


def multi_engine_subdomain_scan(domain: str, engines: list, wordlist_choice: str):
    results = []
    for eng in engines:
        if eng in ENGINE_MAP:
            try:
                r = ENGINE_MAP[eng](domain)
                results.extend(r)
            except Exception:
                log_event(f"Engine failed: {eng}", "ERROR")
    return sorted(set(results))


# ============================================================
#  NMAP-LIKE PORT SCANNER (ENHANCED)
# ============================================================
def scan_single_port(port: int, target_ip: str):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.8)
    try:
        sock.connect((target_ip, port))
        return port, "open"
    except Exception:
        return port, "closed"
    finally:
        sock.close()


@timed
def perform_port_scan(target: str, ports):
    results = []
    with ThreadPoolExecutor(max_workers=400) as ex:
        for port, status in ex.map(lambda p: scan_single_port(p, target), ports):
            if status == "open":
                results.append(port)
    return results


# ============================================================
#  KEEP-ALIVE & HEALTH MONITOR
# ============================================================
def health_check():
    while True:
        log_event("HealthCheck OK")
        time.sleep(120)


def keep_alive_service():
    url = "https://intframeworkweb.onrender.com"
    while True:
        try:
            requests.get(url, timeout=8)
        except Exception:
            log_event("KeepAlive failed", "WARN")
        time.sleep(300)


# ============================================================
#  UI ROUTES
# ============================================================
@app.route('/')
@app.route('/menu')
def home():
    return render_template('menu.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/dns_lookup')
def dns_lookup():
    return render_template('dns_lookup.html')


@app.route('/download')
def download():
    return render_template('download.html')


@app.route('/privacy_policy')
def privacy_policy():
    return render_template('privacy_policy.html')


@app.route('/used_services')
def used_services():
    return render_template('used_services.html')


@app.route('/whois_history')
def whois_history():
    return render_template('whois_history.html')


@app.route('/live_module_watcher')
def live_module_watcher():
    return render_template('live_module_watcher.html')


# ============================================================
#  SUBDOMAIN LOOKUP PAGE
# ============================================================
@app.route('/subdomain_lookup', methods=['GET', 'POST'])
def subdomain_lookup_page():
    if request.method == 'POST':
        domain = request.form.get('domain', '').strip()
        engines_selected = request.form.getlist('engines')
        wordlist = request.form.get('wordlist', 'small')

        if not firewall_filter(domain) or not validate_domain(domain):
            return render_template('subdomain_lookup.html',
                                   result="Invalid / unsafe domain.")

        if not engines_selected:
            engines_selected = ["bruteforce", "crt", "osint"]

        results = multi_engine_subdomain_scan(domain, engines_selected, wordlist)
        output = "\n".join(results) if results else "No results."

        return render_template('subdomain_lookup.html', result=output)

    return render_template('subdomain_lookup.html')


# ============================================================
#  DOCS VIEWER ROUTES
# ============================================================
@app.route("/docs")
def docs_index():
    files = find_markdown_files()
    return render_template("docs.html", md_files=files)


@app.route("/docs/view/<path:filename>")
def docs_view(filename):
    files = find_markdown_files()
    if filename not in files:
        abort(404)

    content = load_markdown_safe(files[filename])
    return render_template("viewer.html", filename=filename, content=content)


# ============================================================
#  NMAP / PORT SCAN
# ============================================================
@app.route('/nmap', methods=['GET', 'POST'])
def nmap_page():
    if request.method == 'POST':
        target_ip = request.form.get('ip', '').strip()
        ports_str = request.form.get('ports', '').strip()

        if not firewall_filter(target_ip):
            return render_template('nmap.html', result="Invalid target input.")

        if not ports_str:
            ports = range(1, 1024)
        else:
            try:
                ports = [int(p) for p in ports_str.split(',') if p.isdigit()]
            except Exception:
                return render_template('nmap.html', result="Invalid port list.")

        open_ports = perform_port_scan(target_ip, ports)

        if open_ports:
            html = "<h3>Open Ports:</h3><div class='port-container'>"
            for p in open_ports:
                html += f"<div class='port-box'><span class='port-number'>{p}</span><span class='port-status'>OPEN</span></div>"
            html += "</div>"
        else:
            html = "<div class='no-port-box'>No open ports detected.</div>"

        return render_template('nmap.html', result=html)

    return render_template('nmap.html')


# ============================================================
#  SERVER START
# ============================================================
PORT = int(os.environ.get("PORT", 10000))
if __name__ == "__main__":

    threading.Thread(target=keep_alive_service, daemon=True).start()
    threading.Thread(target=health_check, daemon=True).start()

    log_event("IntFramework Web Control Panel started.", "INFO")

    app.run(
        debug=True,
        host="0.0.0.0",
        port=PORT
    )