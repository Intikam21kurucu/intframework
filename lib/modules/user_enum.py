import requests
from urllib.parse import urljoin
from colorama import Fore, Style
import sys

# Terminal renkleri
RED = Fore.RED
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
CYAN = Fore.CYAN
RESET = Style.RESET_ALL

class WPUserEnumerator:
    def __init__(self, url, user_count=10):
        self.url = url.rstrip("/")
        self.user_count = user_count
        self.users = []

    def find_user(self, user_id):
        """Belirtilen user ID ile kullanıcı bilgilerini çeker"""
        try:
            test_url = urljoin(self.url, f"/?author={user_id}")
            response = requests.get(test_url, timeout=5)

            if response.status_code == 200:
                username = self.extract_username(response.text)
                if username:
                    return {"id": user_id, "username": username}
        except requests.RequestException:
            pass
        return None

    def extract_username(self, html):
        """Sayfa içeriğinden kullanıcı adını bulmaya çalışır"""
        start_tag = "/author/"
        end_tag = "/"

        if start_tag in html:
            try:
                user = html.split(start_tag)[1].split(end_tag)[0]
                return user
            except IndexError:
                return None
        return None

    def enumerate_users(self):
        """Belirtilen user_count kadar kullanıcıyı tespit eder"""
        for user_id in range(1, self.user_count + 1):
            user_info = self.find_user(user_id)
            if user_info:
                self.users.append(user_info)

        return self.users

    def display_results(self):
        """Terminalde renkli ve kutulu şekilde çıktıyı gösterir"""
        if not self.users:
            print(f"{RED}[ERROR]: No users found!{RESET}")
            return

        # En uzun username belirleme
        max_length = max(len(user["username"]) for user in self.users)

        print(f"{CYAN}┌───────┬─{'─' * max_length}─┐{RESET}")
        print(f"{CYAN}│  ID   │ Username{' ' * (max_length - 8)} │{RESET}")
        print(f"{CYAN}├───────┼─{'─' * max_length}─┤{RESET}")

        for user in self.users:
            space_padding = " " * (max_length - len(user["username"]))
            print(f"{GREEN}│  {user['id']:<4} │ {user['username']}{space_padding} │{RESET}")

        print(f"{CYAN}└───────┴─{'─' * max_length}─┘{RESET}")

# Terminalden çalıştırıldığında
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"{RED}Usage: python script.py <target_url>{RESET}")
        sys.exit(1)

    target_url = sys.argv[1]
    enumerator = WPUserEnumerator(target_url)
    enumerator.enumerate_users()
    enumerator.display_results()