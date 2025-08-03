import requests
import re

class WPThemeScanner:
    def __init__(self, url):
        """URL'yi işleyip normalize eder"""
        self.url = url if url.startswith(("http://", "https://")) else "http://" + url
        self.theme_name = None

    def detect_theme_from_source(self):
        """Sayfa kaynağında tema izlerini arar"""
        try:
            response = requests.get(self.url, timeout=5)
            match = re.search(r"/wp-content/themes/([^/]+)/", response.text)
            if match:
                self.theme_name = match.group(1)
        except requests.exceptions.RequestException:
            pass

    def get_theme_version(self):
        """Tema sürümünü style.css veya readme.txt dosyasından alır"""
        if not self.theme_name:
            return None

        possible_files = [
            f"{self.url}/wp-content/themes/{self.theme_name}/style.css",
            f"{self.url}/wp-content/themes/{self.theme_name}/readme.txt"
        ]

        for file_url in possible_files:
            try:
                response = requests.get(file_url, timeout=5)
                if response.status_code == 200:
                    version_match = re.search(r"Version:\s*([\d.]+)", response.text)
                    if version_match:
                        return version_match.group(1)
            except requests.exceptions.RequestException:
                pass

        return None

    def run(self):
        """Tüm tarama işlemlerini başlatır"""
        self.detect_theme_from_source()
        theme_version = self.get_theme_version()

        return {
            "theme": self.theme_name,
            "version": theme_version
        }