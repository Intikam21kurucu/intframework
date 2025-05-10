#!/usr/bin/env python3
from flask import Flask, render_template, request
import subprocess
import os
import socket
from concurrent.futures import ThreadPoolExecutor

app = Flask(__name__)

# Güvenlik kontrolü için fonksiyon
def is_safe_input(user_input):
    return "../" not in user_input and ";" not in user_input and "|" not in user_input


app = Flask(__name__)

def scan_port(port, target_ip):
    """Verilen IP adresi ve port için bağlantı sağlanıp sağlanamadığını kontrol eder."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((target_ip, port))
        return port, True
    except:
        return port, False
    finally:
        s.close()

@app.route('/nmap', methods=['GET', 'POST'])
def nmap():
    """IP tarama sayfası için route."""
    if request.method == 'POST':
        ip = request.form.get('ip')
        ports = request.form.get('ports', '')

        # IP adresi ve portlar girilmiş mi?
        if not ip:
            return render_template('nmap.html', result="IP address is required.")

        # Portlar belirtilmediyse tüm portlar taranır
        if not ports:
            ports = range(1, 65536)
        else:
            ports = list(map(int, ports.split(',')))  # Verilen portları listeye çevirir

        # Portları paralel olarak taramak için ThreadPoolExecutor kullanılır
        with ThreadPoolExecutor(max_workers=100) as executor:
            results = executor.map(lambda port: scan_port(port, ip), ports)

        # Sonuçları formatla ve ekrana yazdır
        open_ports = [f"Port {port} is open" for port, is_open in results if is_open]

        if open_ports:
            result = "\n".join(open_ports)
        else:
            result = "No open ports found."

        return render_template('nmap.html', result=result)

    return render_template('nmap.html')

# Ana sayfa route'u
@app.route('/')
def home():
    return render_template('menu.html')

# İletişim sayfası route'u
@app.route('/contact')
def contact():
    return render_template('contact.html')

# DNS Lookup sayfası
@app.route('/dns_lookup')
def dns_lookup():
    return render_template('dns_lookup.html')

# Subdomain Lookup sayfası
@app.route('/subdomain_lookup')
def subdomain_lookup():
    return render_template('subdomain_lookup.html')


# Dokümanlar sayfası
@app.route('/docs')
def docs():
    return render_template('docs.html')

# İndir sayfası
@app.route('/download')
def download():
    return render_template('download.html')

# Gizlilik politikası sayfası
@app.route('/privacy_policy')
def privacy_policy():
    return render_template('privacy_policy.html')

# Used Services sayfası
@app.route('/used_services')
def used_services():
    return render_template('used_services.html')

# Whois geçmişi sayfası
@app.route('/whois_history')
def whois_history():
    return render_template('whois_history.html')

# Menü sayfası
@app.route('/menu')
def menu():
    return render_template('menu.html')

if __name__ == "__main__":
    app.run(debug=True)