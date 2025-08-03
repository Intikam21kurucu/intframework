import requests
from bs4 import BeautifulSoup

class WPChecker:
    def __init__(self, url):
        """URL'yi işleyip normalize eder ve otomatik olarak kontrol işlemini başlatır"""
        self.url = url if url.startswith(("http://", "https://")) else "http://" + url
        self.run()

    def get_http_status(self):
        """Siteye erişilebilir olup olmadığını HTTP koduyla kontrol eder"""
        try:
            response = requests.get(self.url, timeout=5)
            return response.status_code
        except requests.exceptions.RequestException:
            return None

    def is_wordpress(self):
        """Web sitesinin WordPress olup olmadığını anlamak için çeşitli kontroller yapar"""
        try:
            response = requests.get(self.url, timeout=5)

            # 1. wp-content veya wp-includes içeriğini kontrol et
            if "wp-content" in response.text or "wp-includes" in response.text:
                return True

            # 2. Meta Generator etiketi kontrolü
            soup = BeautifulSoup(response.text, "html.parser")
            generator = soup.find("meta", {"name": "generator"})
            if generator and "WordPress" in generator["content"]:
                return True

            # 3. WordPress login sayfası olup olmadığını kontrol et
            login_page = requests.get(f"{self.url}/wp-login.php", timeout=5)
            if login_page.status_code == 200 and "wordpress" in login_page.text.lower():
                return True

            # 4. XML-RPC desteği var mı kontrol et
            xml_rpc = requests.get(f"{self.url}/xmlrpc.php", timeout=5)
            if xml_rpc.status_code == 405:
                return True

            return False
        except requests.exceptions.RequestException:
            return None

    def get_wp_version(self):
        """WordPress sürümünü tespit eder"""
        try:
            response = requests.get(self.url, timeout=5)
            soup = BeautifulSoup(response.text, "html.parser")
            generator = soup.find("meta", {"name": "generator"})
            if generator and "WordPress" in generator["content"]:
                return generator["content"]

            return None
        except requests.exceptions.RequestException:
            return None
            pass

    def find_users(self):
        """WordPress kullanıcı adlarını tespit eder"""
        try:
            api_url = f"{self.url.rstrip('/')}/wp-json/wp/v2/users"
            response = requests.get(api_url, timeout=5)
            if response.status_code == 200:
                return [user["name"] for user in response.json()]
            return []
        except requests.exceptions.RequestException:
            return None

    def run(self):
        """Sınıf çağrıldığında otomatik olarak çalıştırılacak fonksiyon"""
        print(f"\n[+] Checking {self.url}...\n")

        status = self.get_http_status()
        if status:
            print(f"[✓] HTTP Status: {status}")
        else:
            print("[✗] Unable to reach the site.")
            return

        is_wp = self.is_wordpress()
        if is_wp:
            print("[✓] WordPress detected!")
        else:
            print("[✗] This site does not appear to be running WordPress.")
            return

        wp_version = self.get_wp_version()
        if wp_version:
            print(f"[✓] WordPress Version: {wp_version}")
        else:
            print("[✗] Unable to determine WordPress version.")

        users = self.find_users()
        if users:
            print(f"[✓] Found users: {', '.join(users)}")
        else:
            print("[✗] No WordPress users found.")

# Kullanıcıdan URL al ve WPChecker başlat
if __name__ == "__main__":
    url = input("Enter the URL to scan: ").strip()
    WPChecker(url)