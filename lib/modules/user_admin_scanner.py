import requests
import re

class WPUserAdminScanner:
    def __init__(self, url):
        """URL'yi işleyip normalize eder"""
        self.url = url if url.startswith(("http://", "https://")) else "http://" + url
        self.users = []
        self.admin_user = None

    def detect_users_from_api(self):
        """WordPress REST API ile kullanıcıları bulur"""
        try:
            response = requests.get(f"{self.url}/wp-json/wp/v2/users", timeout=5)
            if response.status_code == 200:
                users = response.json()
                for user in users:
                    self.users.append(user.get("name", "Bilinmeyen Kullanıcı"))
                    if user.get("id") == 1:
                        self.admin_user = user.get("name")
        except requests.exceptions.RequestException:
            pass

    def detect_users_from_author_enum(self):
        """?author=1 gibi yazar ID’leri ile kullanıcıları bulur"""
        for user_id in range(1, 11):  # İlk 10 ID’yi deniyoruz
            try:
                response = requests.get(f"{self.url}/?author={user_id}", timeout=5, allow_redirects=True)
                if response.status_code == 200:
                    match = re.search(r"/author/([^/]+)/", response.url)
                    if match:
                        username = match.group(1)
                        if username not in self.users:
                            self.users.append(username)
                        if user_id == 1:
                            self.admin_user = username
            except requests.exceptions.RequestException:
                pass

    def run(self):
        """Tüm kullanıcı ve admin tespit metodlarını çalıştırır"""
        self.detect_users_from_api()
        self.detect_users_from_author_enum()

        return {
            "users": self.users,
            "admin": self.admin_user
        }