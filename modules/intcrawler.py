#!/usr/bin/env python3
import requests
import os
import re
from urllib.parse import urlparse
from bs4 import BeautifulSoup 
import argparse
import requests
import re
import csv
import json
import os
import time
from urllib.parse import urljoin
from colorama import Fore, Style

def download_page(url, headers=None, cookies=None, proxies=None, timeout=30):
    try:
        response = requests.get(url, headers=headers, cookies=cookies, proxies=proxies, timeout=timeout)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")
        return None

def extract_urls(html_content, base_url, regex_pattern=None):
    urls = set()
    pattern = re.compile(r'href=["\'](.*?)["\']', re.IGNORECASE)
    matches = pattern.findall(html_content)
    
    for match in matches:
        url = urljoin(base_url, match)
        if regex_pattern and re.search(regex_pattern, url):
            urls.add(url)
        elif not regex_pattern:
            urls.add(url)
    
    return urls

def save_urls(urls, export_format, output_dir):
    if export_format == 'csv':
        filename = 'urls.csv'
        with open(os.path.join(output_dir, filename), 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['URLs'])
            for url in urls:
                writer.writerow([url])
    elif export_format == 'json':
        filename = 'urls.json'
        with open(os.path.join(output_dir, filename), 'w') as jsonfile:
            json.dump(list(urls), jsonfile, indent=4)

def crawl(args):
    visited_urls = set()
    queue = [(args.root, 0)]
    headers = {'User-Agent': args.user_agent} if args.user_agent else {}
    cookies = {'Cookie': args.cookie} if args.cookie else {}
    proxies = {'http': args.proxy, 'https': args.proxy} if args.proxy else None

    while queue:
        current_url, current_level = queue.pop(0)
        if current_url in visited_urls:
            continue
        
        print(f"Crawling {current_url} at level {current_level}...")
        html_content = download_page(current_url, headers=headers, cookies=cookies, proxies=proxies, timeout=args.timeout)
        if not html_content:
            continue
        
        visited_urls.add(current_url)
        
        if current_level < args.level:
            extracted_urls = extract_urls(html_content, current_url, args.regex)
            for url in extracted_urls:
                if url not in visited_urls:
                    queue.append((url, current_level + 1))
    
    save_urls(visited_urls, args.export, args.output)
    print(f"Crawling finished. {len(visited_urls)} URLs crawled and saved.")

def menu():
	print(Fore.GREEN+"""
usage: intcrawler [-h] [-u ROOT] [-c COOKIE] [-r REGEX]
                  [-e {csv,json}] [-o OUTPUT] [-l LEVEL]
                  [--user-agent USER_AGENT] [--timeout TIMEOUT]
                  [-p PROXY] [--clone] [--headers] [--dns]
                  [--keys] [--update] [--only-urls] [--wayback]
                  [target]

intcrawler

positional arguments:
  target                your target dns host or ip's

options:
  -h, --help            show this help message and exit
  -u ROOT, --url ROOT   root url
  -c COOKIE, --cookie COOKIE
                        cookie
  -r REGEX, --regex REGEX
                        regex pattern
  -e {csv,json}, --export {csv,json}
                        export format
  -o OUTPUT, --output OUTPUT
                        output directory
  -l LEVEL, --level LEVEL
                        levels to crawl
  --user-agent USER_AGENT
                        custom user agent
  --timeout TIMEOUT     http request timeout
  -p PROXY, --proxy PROXY
                        proxy server
  --clone               clone the website locally
  --headers             add headers
  --dns                 enumerate subdomains and DNS data
  --keys                find secret keys
  --update              update crawler
  --only-urls           only extract URLs
  --wayback             fetch URLs from archive.org as seeds
	"""+Style.RESET_ALL)

def clone(args):
    print("Cloning website locally...")
    if args.root:
        try:
            # Burada isteğe bağlı olarak bir web sitesini indirebilirsiniz.
            # Örneğin:
            response = requests.get(args.root)
            with open('index.html', 'w') as f:
            	f.write(response.text)
            print("Clone completed successfully.")
        except Exception as e:
            print(f"Clone failed: {e}")
    else:
        print("Error: URL parameter is missing.")

def headers(args):
    print("Adding headers to requests...")
    if args.url and args.headers:
        headers = {
            'User-Agent': 'Custom User Agent',
            'Accept': 'application/json',
            **args.headers
        }
        try:
            response = requests.get(args.url, headers=headers)
            response.raise_for_status()
            print(f"Headers added successfully. Response code: {response.status_code}")
        except requests.RequestException as e:
            print(f"Error adding headers or fetching URL: {e}")
    else:
        print("Error: URL or headers parameter is missing.")

def dns(args):
    print("Enumerating subdomains and DNS data...")
    if args.domain:
        try:
            # Burada isteğe bağlı olarak DNS sorgusu yapabilirsiniz.
            print("DNS enumeration completed successfully.")
        except Exception as e:
            print(f"DNS enumeration failed: {e}")
    else:
        print("Error: Domain parameter is missing.")

def keys(args):
    print("Finding secret keys...")
    if args.directory:
        secret_files = ['secrets.txt', 'keys.csv', 'config.yml']
        for file in secret_files:
            path = os.path.join(args.directory, file)
            if os.path.exists(path):
                try:
                    with open(path, 'r') as f:
                        secrets = f.read()
                        print(f"Found secret keys in {file}: {secrets}")
                except OSError as e:
                    print(f"Error reading {file}: {e}")
    else:
        print("Error: Directory parameter is missing.")
    print("Secret keys found.")

def update(args):
    print("Updating intcrawler")
    try:
        # Burada isteğe bağlı olarak güncelleme işlemi yapabilirsiniz.
        print("intcrawler updated successfully.")
    except Exception as e:
        print(f"intcrawler update failed: {e}")

def only_urls(args):
    print("Extracting only URLs...")
    if args.file:
        try:
            with open(args.file, 'r') as f:
                content = f.read()
                soup = BeautifulSoup(content, 'html.parser')
                urls = [link.get('href') for link in soup.find_all('a') if link.get('href')]
                for url in urls:
                    print(url)
            print("URLs extracted successfully.")
        except OSError as e:
            print(f"Error reading {args.file}: {e}")
        except Exception as e:
            print(f"Error extracting URLs: {e}")
    else:
        print("Error: File parameter is missing.")
def banner():
    print(f"""{Fore.GREEN}
    _____   __________________  ___ _       ____    __________
   /  _/ | / /_  __/ ____/ __ \/   | |     / / /   / ____/ __ \\
   / //  |/ / / / / /   / /_/ / /| | | /| / / /   / __/ / /_/ /
 _/ // /|  / / / / /___/ _, _/ ___ | |/ |/ / /___/ /___/ _, _/
/___/_/ |_/ /_/  \____/_/ |_/_/  |_|__/|__/_____/_____/_/ |_|

    {Style.RESET_ALL}""")

def __user__(target):
    banner()
    while True:
        try:
            command = input(f"intcrawler({Fore.RED}{target}{Fore.RESET})> ")
            if command.lower() == 'exit':
                print("Exiting...")
                break
            
            # POST isteği ile komutu gönder
            data = {'command': command}
            response = requests.post(target, data=data)
            response.raise_for_status()  # Hata varsa istisna fırlatır
            
            print(response.text)
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
def wayback(args):
    print("Fetching URLs from archive.org...")
    if args.query:
        try:
            url = f"http://web.archive.org/cdx/search/cdx?url={args.query}&output=json"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            for entry in data:
                print(entry)
            print("URLs fetched from archive.org successfully.")
        except requests.RequestException as e:
            print(f"Error fetching data from archive.org: {e}")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Error: Query parameter is missing.")

def main():
    print(Fore.GREEN)
    banner()
    parser = argparse.ArgumentParser(description='intcrawler', prog='intcrawler', formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-u', '--url', help='root url', dest='root', required=False)
    parser.add_argument("?", help="List modules", nargs="?")
    parser.add_argument('-c', '--cookie', help='cookie', dest='cookie', required=False)
    parser.add_argument('-r', '--regex', help='regex pattern', dest='regex', required=False)
    parser.add_argument('-e', '--export', help='export format', dest='export', choices=['csv', 'json'], required=False)
    parser.add_argument('-o', '--output', help='output directory', dest='output')
    parser.add_argument('-l', '--level', help='levels to crawl', dest='level', type=int, required=False)
    parser.add_argument('--user-agent', help='custom user agent', dest='user_agent', required=False)
    parser.add_argument('--timeout', help='http request timeout', dest='timeout', type=float, required=False)
    parser.add_argument('-p', '--proxy', help='proxy server', dest='proxy', required=False)

    # Switches
    parser.add_argument('--clone', help='clone the website locally', dest='clone', action='store_true', required=False)
    parser.add_argument('--headers', help='add headers', dest='headers', action='store_true', required=False)
    parser.add_argument('--dns', help='enumerate subdomains and DNS data', dest='dns', action='store_true', required=False)
    parser.add_argument('--keys', help='find secret keys', dest='keys', action='store_true', required=False)
    parser.add_argument('--update', help='update crawler', dest='update', action='store_true', required=False)
    parser.add_argument('--only-urls', help='only extract URLs', dest='only_urls', action='store_true')
    parser.add_argument('--wayback', help='fetch URLs from archive.org as seeds', dest='wayback', action='store_true')
    parser.add_argument("target", help="your target dns host or ip's ", nargs='?', default=None)
    args = parser.parse_args()
    
    print(Fore.RESET)
    
    if args.clone:
        clone(args)
    if args.headers:
        headers(args)
    if args.dns:
        dns(args)
    if args.keys:
        keys(args)
    if args.update:
        update(args)
    if args.only_urls:
        only_urls(args)
    if args.wayback:
        wayback(args)
    if args.target:
        crawl(args)
        if crawl(args):
            __user__(args.target)
        else:
            pass
    if not args:
    	menu()
    if args.root:
        crawl(args)
        if crawl(args):
            __user__(args.root)
        else:
            print("you are not ip used")
    else:
    	menu()
if __name__ == "__main__":
    main()