import argparse
import requests

class DirScanner:
    def __init__(self, url, wordlist):
        self.url = url
        self.wordlist = wordlist

    def scan(self):
        with open(self.wordlist, 'r') as file:
            directories = file.read().splitlines()

        for directory in directories:
            target_url = f"{self.url}/{directory}"
            try:
                response = requests.get(target_url)
                if self.is_vulnerable(response):
                    print(f"[+] Found: {target_url} (Status Code: {response.status_code})")
            except requests.RequestException as e:
                print(f"[-] Error: {e}")

    def is_vulnerable(self, response):
        return response.status_code in [200, 301, 302, 403, 404]

def main():
    parser = argparse.ArgumentParser(description='Directory Scanner')
    parser.add_argument('url', type=str, help='Base URL of the website to scan')
    parser.add_argument('wordlist', type=str, help='Path to the wordlist file')
    args = parser.parse_args()

    scanner = DirScanner(args.url, args.wordlist)
    scanner.scan()

if __name__ == '__main__':
    main()