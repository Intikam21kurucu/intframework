import requests
import re

class WPPluginScanner:
    def __init__(self, url):
        """URL'yi işleyip normalize eder"""
        self.url = url if url.startswith(("http://", "https://")) else "http://" + url
        self.plugins = []

    def detect_plugins_from_source(self):
        """Sayfa kaynağında eklenti izlerini arar"""
        try:
            response = requests.get(self.url, timeout=5)
            plugin_matches = re.findall(r"/wp-content/plugins/([^/]+)/", response.text)
            self.plugins.extend(set(plugin_matches))  # Tekrar edenleri engelle
        except requests.exceptions.RequestException:
            pass

    def check_plugin_directories(self):
        """Bazı yaygın eklenti yollarını kontrol eder"""
        common_plugins = [
            "woocommerce", "yoast-seo", "elementor", "wpforms", "wordfence",
            "jetpack", "contact-form-7", "akismet", "updraftplus", "wp-super-cache"
        ]

        for plugin in common_plugins:
            url = f"{self.url}/wp-content/plugins/{plugin}/"
            try:
                response = requests.get(url, timeout=5)
                if response.status_code == 200:
                    self.plugins.append(plugin)
            except requests.exceptions.RequestException:
                pass

    def check_plugin_versions(self):
        """Bulunan eklentilerin sürümlerini tespit etmeye çalışır"""
        plugin_versions = {}
        for plugin in self.plugins:
            version_url = f"{self.url}/wp-content/plugins/{plugin}/readme.txt"
            try:
                response = requests.get(version_url, timeout=5)
                if response.status_code == 200:
                    version_match = re.search(r"Stable tag:\s*([\d.]+)", response.text)
                    if version_match:
                        plugin_versions[plugin] = version_match.group(1)
            except requests.exceptions.RequestException:
                pass

        return plugin_versions

    def run(self):
        """Tüm tarama işlemlerini başlatır"""
        self.detect_plugins_from_source()
        self.check_plugin_directories()
        plugin_versions = self.check_plugin_versions()

        return {
            "plugins": list(set(self.plugins)),  # Tekrar edenleri temizle
            "versions": plugin_versions
        }