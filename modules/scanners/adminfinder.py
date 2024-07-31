import argparse
import requests

admin_paths = [
    'admin/', 'admin.php', 'admin.html', 'admin/login.php', 'admin/login.html', 'admin_area/',
    'admin_area/login.php', 'admin_area/login.html', 'adminpanel/', 'adminpanel.php', 'adminpanel.html',
    'administrator/', 'administrator.php', 'administrator.html', 'cpanel/', 'cpanel.php', 'cpanel.html',
    'controlpanel/', 'controlpanel.php', 'controlpanel.html', 'admin1/', 'admin1.php', 'admin1.html',
    'admin2/', 'admin2.php', 'admin2.html', 'admin_login/', 'admin_login.php', 'admin_login.html',
    'adminhome/', 'adminhome.php', 'adminhome.html', 'admincontrol/', 'admincontrol.php', 'admincontrol.html',
    'admin_area/admin.php', 'admin_area/admin.html'
]

class AdminFinder:
    def __init__(self, url):
        self.url = url if url.endswith('/') else url + '/'

    def find_admin(self):
        for path in admin_paths:
            full_url = self.url + path
            try:
                response = requests.get(full_url)
                if response.status_code == 200:
                    print(f'[+] Admin panel found: {full_url}')
            except requests.RequestException as e:
                print(f'[-] Error: {e}')

def main():
    parser = argparse.ArgumentParser(description='Admin Panel Finder')
    parser.add_argument('url', type=str, help='Base URL of the website to scan')
    args = parser.parse_args()
    
    admin_finder = AdminFinder(args.url)
    admin_finder.find_admin()

if __name__ == '__main__':
    main()