import requests
from urllib.parse import urljoin
from colorama import Fore, Style

# Terminal renkleri
RED = Fore.RED
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
CYAN = Fore.CYAN
RESET = Style.RESET_ALL

class WPSQLXSSScanner:
    def __init__(self, url, timeout=5, xss_scan=False):
        self.url = url.rstrip("/")
        self.vulnerable_urls = {"sql": [], "xss": []}
        self.test_payloads = {
            "sql": ["'", '"', " OR 1=1 --", " OR '1'='1' --"],
            "xss": ['<script>alert("XSS")</script>', '"><script>alert(1)</script>']
        }

    def check_vulnerability(self, test_url, payload_type, payload):
        """Belirli bir URL'ye yük enjekte ederek SQL veya XSS açığı olup olmadığını kontrol eder."""
        try:
            response = requests.get(test_url, timeout=5)
            if response.status_code == 200:
                if payload_type == "sql" and "mysql" in response.text.lower():
                    print(f"{RED}🔥 SQL Injection Found: {test_url} {RESET}")
                    self.vulnerable_urls["sql"].append(test_url)
                elif payload_type == "xss" and payload in response.text:
                    print(f"{YELLOW}⚠️ XSS Found: {test_url} {RESET}")
                    self.vulnerable_urls["xss"].append(test_url)
        except requests.RequestException:
            pass

    def run(self):
        """WordPress URL'leri üzerinde SQL ve XSS güvenlik açıklarını tarar."""
        print(f"\n{CYAN}🔍 Scanning for SQL Injection and XSS vulnerabilities...{RESET}")

        # Örnek URL parametreleri
        test_paths = ["/?id=", "/?page=", "/?post=", "/wp-content/plugins/", "/wp-json/wp/v2/users/"]

        for path in test_paths:
            for payload_type, payloads in self.test_payloads.items():
                for payload in payloads:
                    test_url = urljoin(self.url, path) + payload
                    self.check_vulnerability(test_url, payload_type, payload)

        return self.vulnerable_urls