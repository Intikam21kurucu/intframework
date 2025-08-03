import requests
import re

class WPVersionScanner:
    def __init__(self, url):
        """URL'yi işleyip normalize eder"""
        self.url = url if url.startswith(("http://", "https://")) else "http://" + url
        self.version = None

    def detect_from_meta_tag(self):
        """Sayfa kaynak kodundaki meta etiketlerinden WP sürümünü bulmaya çalışır"""
        try:
            response = requests.get(self.url, timeout=5)
            match = re.search(r'<meta name="generator" content="WordPress (\d+\.\d+(\.\d+)?)"', response.text)
            if match:
                self.version = match.group(1)
        except requests.exceptions.RequestException:
            pass

    def detect_from_readme(self):
        """readme.html dosyasından WP sürümünü alır"""
        try:
            response = requests.get(f"{self.url}/readme.html", timeout=5)
            match = re.search(r"Version (\d+\.\d+(\.\d+)?)", response.text)
            if match:
                self.version = match.group(1)
        except requests.exceptions.RequestException:
            pass

    def detect_from_version_php(self):
        """wp-includes/version.php dosyasından WP sürümünü alır"""
        try:
            response = requests.get(f"{self.url}/wp-includes/version.php", timeout=5)
            match = re.search(r"\$wp_version = '(\d+\.\d+(\.\d+)?)';", response.text)
            if match:
                self.version = match.group(1)
        except requests.exceptions.RequestException:
            pass

    def detect_from_rss(self):
        """RSS feed üzerinden WP sürümünü tespit eder"""
        try:
            response = requests.get(f"{self.url}/feed/", timeout=5)
            match = re.search(r"<generator>https://wordpress.org/\?v=(\d+\.\d+(\.\d+)?)</generator>", response.text)
            if match:
                self.version = match.group(1)
        except requests.exceptions.RequestException:
            pass

    def detect_from_http_headers(self):
        """HTTP başlıklarında WordPress sürümünü arar"""
        try:
            response = requests.head(self.url, timeout=5)
            server_header = response.headers.get("X-Powered-By", "")
            match = re.search(r"WordPress/(\d+\.\d+(\.\d+)?)", server_header)
            if match:
                self.version = match.group(1)
        except requests.exceptions.RequestException:
            pass

    def run(self):
        """Tüm sürüm tespit metodlarını çalıştırır"""
        self.detect_from_meta_tag()
        self.detect_from_readme()
        self.detect_from_version_php()
        self.detect_from_rss()
        self.detect_from_http_headers()

        return {
            "wordpress_version": self.version
        }