#!/usr/bin/env python3
"""
IntFramework Web Control Panel
Velgrath 🔱 – Global Accessible Secure Web Utility

- Flask based modular web interface
- Hardened input validation
- Multi-threaded port scanner
- Auto self-ping keep-alive system
- Professional routing structure
- Template-driven UI
"""

from __future__ import annotations
from flask import Flask, render_template, request
import subprocess
import socket
import requests
import threading
import time
import os
from concurrent.futures import ThreadPoolExecutor
# ============================================================
#  MARKDOWN VIEWER (SAFE & STRONG)
# ============================================================

import markdown
from functools import lru_cache
from flask import abort, render_template

# Ayarlar
REPO_ROOT = "intframework"
DOC_DIR = os.path.join(REPO_ROOT, "Documentation")
VALID_EXT = (".md", ".MD", ".markdown")



# ============================================================
#  FLASK INSTANCE
# ============================================================

app = Flask(
    __name__,
    template_folder='templates',
    static_folder='static'
)
# ============================================================
#  SUBDOMAIN SCANNER PAGE
# ============================================================

@app.route('/subdomain_lookup', methods=['GET', 'POST'])
def subdomain_lookup():
    """
    Subdomain Scanner for IntFramework Web Panel
    Velgrath 🔱 – Multi-engine enumeration (Wordlist, CRT, OSINT, Resolver)
    Flask template form ile tam uyumlu.
    """
    if request.method == 'POST':
        domain = request.form.get('domain', '').strip()
        wordlist = request.form.get('wordlist', 'small').strip()
        engines_selected = request.form.getlist('engines')

        # Güvenlik kontrolü
        if not domain or not is_safe_input(domain) or not validate_domain(domain):
            return render_template('subdomain_lookup.html',
                                   result="Invalid or unsafe domain input.")

        if not engines_selected:
            engines_selected = ["brute_force", "crt", "osint", "resolver"]

        # Motorları Çalıştır
        try:
            results = multi_engine_subdomain_scan(
                domain=domain,
                engines=engines_selected,
                wordlist_choice=wordlist
            )

            if results:
                output = "\n".join(results)
            else:
                output = "No subdomains detected."

        except Exception as e:
            output = f"Engine Error: {str(e)}"

        return render_template('subdomain_lookup.html', result=output)

    # GET request
    return render_template('subdomain_lookup.html')
def find_markdown_files():
    """
    Finds all .md files in root and Documentation folder.
    Returns dict { 'display_name': 'absolute_path' }
    """
    md_files = {}

    # Root-level md
    for f in os.listdir(REPO_ROOT):
        if f.endswith(VALID_EXT):
            md_files[f] = os.path.join(REPO_ROOT, f)

    # Documentation folder md
    if os.path.isdir(DOC_DIR):
        for f in os.listdir(DOC_DIR):
            if f.endswith(VALID_EXT):
                md_files[f"Documentation/{f}"] = os.path.join(DOC_DIR, f)

    return md_files


@lru_cache(maxsize=256)
def load_markdown_safe(path: str) -> str:
    """
    Safely reads a Markdown file and converts it to HTML.
    Protected against path traversal.
    """
    abs_repo = os.path.abspath(REPO_ROOT)
    abs_path = os.path.abspath(path)

    if not abs_path.startswith(abs_repo):
        abort(403)  # Forbidden

    if not os.path.exists(abs_path):
        abort(404)

    with open(abs_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Markdown → HTML conversion
    html = markdown.markdown(
        content,
        extensions=["fenced_code", "tables", "codehilite", "toc"]
    )

    return html


# Flask Routes

@app.route("/docs")
def docs_index():
    """
    List all Markdown files
    """
    files = find_markdown_files()
    return render_template("index.html", md_files=files)


@app.route("/docs/view/<path:filename>")
def docs_view(filename):
    """
    View a single Markdown file
    """
    files = find_markdown_files()
    if filename not in files:
        abort(404)

    html_content = load_markdown_safe(files[filename])
    return render_template("viewer.html", filename=filename, content=html_content)


# ============================================================
#  SECURITY UTILITIES
# ============================================================

def is_safe_input(value: str) -> bool:
    """
    Basic server-side input sanitation.
    Prevents traversal, shell-injection and piping attempts.
    """
    if not value:
        return False

    blacklist = ["../", ";", "|", "`", "$(", ")>", "<", "&", "%"]
    return not any(bad in value for bad in blacklist)


# ============================================================
#  KEEP-ALIVE SYSTEM FOR HOSTED PLATFORMS (Render, Replit...)
# ============================================================

def keep_alive_service():
    """
    Prevents Render or similar cloud hosting platforms
    from putting the service to sleep.
    """
    url = "https://intframeworkweb.onrender.com"
    while True:
        try:
            print("[KeepAlive] Sending self-ping...")
            requests.get(url, timeout=10)
        except Exception:
            pass
        time.sleep(300)  # 5 minutes sleep


# ============================================================
#  PORT SCANNING ENGINE
# ============================================================

def scan_single_port(port: int, target_ip: str):
    """
    Attempts connecting to a single port on given IP.
    Returns tuple (port, True/False)
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    try:
        sock.connect((target_ip, port))
        return port, True
    except Exception:
        return port, False
    finally:
        sock.close()


def perform_port_scan(target: str, ports):
    """
    Multi-threaded port scanning using ThreadPoolExecutor.
    """
    results = []

    with ThreadPoolExecutor(max_workers=200) as executor:
        for port, status in executor.map(lambda p: scan_single_port(p, target), ports):
            if status:
                results.append(port)

    return results


# ============================================================
#  ROUTES
# ============================================================

@app.route('/')
def home():
    """
    Main Menu Page
    """
    return render_template('menu.html')


@app.route('/menu')
def menu():
    return render_template('menu.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/dns_lookup')
def dns_lookup():
    return render_template('dns_lookup.html')


@app.route('/subdomain_lookup')
def subdomain_lookup():
    return render_template('subdomain_lookup.html')


@app.route('/docs')
def docs():
    return render_template('docs.html')


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
#  NMAP / PORT SCAN PAGE
# ============================================================
@app.route('/nmap', methods=['GET', 'POST'])
def nmap_page():
    """
    Manual port scanning implemented without external binaries.
    Uses Python socket to test connectivity.
    Enhanced HTML output for better visualization.
    """
    if request.method == 'POST':
        target_ip = request.form.get('ip', '').strip()
        port_str = request.form.get('ports', '').strip()

        # Input validation
        if not target_ip or not is_safe_input(target_ip):
            return render_template('nmap.html', result="Invalid or missing IP address.")

        # Port list parsing
        if not port_str:
            ports = range(1, 65536)
        else:
            try:
                ports = [int(p.strip()) for p in port_str.split(',') if p.strip().isdigit()]
                if not ports:
                    raise ValueError
            except ValueError:
                return render_template('nmap.html', result="Invalid port format.")

        # Perform Scan
        open_ports = perform_port_scan(target_ip, ports)

        # Generate stylish HTML output
        if open_ports:
            html_output = "<h3>Open Ports</h3>"
            html_output += "<div class='port-container'>"
            for p in open_ports:
                html_output += f"""
                <div class='port-box'>
                    <span class='port-number'>{p}</span>
                    <span class='port-status'>OPEN</span>
                </div>
                """
            html_output += "</div>"
        else:
            html_output = """
            <div class="no-port-box">
                No open ports detected.
            </div>
            """

        return render_template('nmap.html', result=html_output)

    return render_template('nmap.html')

# ============================================================
#  SERVER START
# ============================================================

if __name__ == "__main__":

    # Self-ping thread
    threading.Thread(target=keep_alive_service, daemon=True).start()

    # Flask Run
    app.run(
        debug=True,            # Disable on production
        host="0.0.0.0",
        port=10000
    )