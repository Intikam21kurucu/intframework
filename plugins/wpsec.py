from colorama import Fore, Style, init
from lib.modules.checker import WPChecker
from lib.modules.plugin_scanner import WPPluginScanner
from lib.modules.theme_scanner import WPThemeScanner
from lib.modules.version_scanner import WPVersionScanner
from lib.modules.user_password_finder import WPUserPasswordFinder
from lib.modules.sql_xss_scanner import WPSQLXSSScanner
from lib.modules.bruteforce import WPBruteforce
from lib.modules.database_scanner import WPDatabaseScanner
from lib.modules.user_password_file_scanner import WPUser
from lib.modules.user_enum import WPUserEnumerator
import socket
import time
import sys

init()

class WPScannerPlugin:
    def __init__(self):
        self.name = "wpsec"
        self.commands = {
            "wpsec": {
                "func": self.run,
                "desc": "Scan a WordPress site for security issues",
                "usage": "wpsec <url> [-m quick|default|deep] [--log] [--sql] [--xss] [--brute <list>] [--timeout <sec>] [--verbose]"
            }
        }

    def animate(self, text, delay=0.07):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

    def run(self, args):
        import argparse
        parser = argparse.ArgumentParser(prog="wpsec", add_help=False)
        parser.add_argument("url", help="Target WordPress site URL")
        parser.add_argument("-m", "--mode", choices=["quick", "default", "deep"], default="default")
        parser.add_argument("--log", action="store_true")
        parser.add_argument("--sql", action="store_true")
        parser.add_argument("--xss", action="store_true")
        parser.add_argument("--brute", help="Password list for brute-force")
        parser.add_argument("--timeout", type=int, default=5)
        parser.add_argument("--verbose", action="store_true")

        try:
            opts = parser.parse_args(args)
        except SystemExit:
            print("[!] Invalid arguments. Usage: wpsec <url> [-m quick|default|deep] [--log] [--sql] [--xss] [--brute <list>] [--timeout <sec>] [--verbose]")
            return

        scanner = WPScanner(opts.url, opts.mode, opts.log, opts.timeout, opts.verbose)

        if opts.sql:
            scanner.animate("💀 │ Running SQL Injection scan...")
            scanner.results["sql_xss"] = WPSQLXSSScanner(opts.url, sql_scan=True, timeout=opts.timeout).run()
            scanner.show_results()
            return
        if opts.xss:
            scanner.animate("💀 │ Running XSS scan...")
            scanner.results["sql_xss"] = WPSQLXSSScanner(opts.url, xss_scan=True, timeout=opts.timeout).run()
            scanner.show_results()
            return
        if opts.brute:
            scanner.animate("🚨 │ Running brute-force attack...")
            scanner.results["bruteforce"] = WPBruteforce(opts.url, [], password_list=opts.brute, timeout=opts.timeout).run()
            scanner.show_results()
            return

        scanner.run_scan()

class WPScanner:
    def __init__(self, url, mode, log, timeout=5, verbose=False):
        self.url = url.rstrip('/')
        self.ip = self.get_ip()
        self.mode = mode
        self.log = log
        self.timeout = timeout
        self.verbose = verbose
        self.results = {}

    def get_ip(self):
        try:
            return socket.gethostbyname(self.url.replace("http://", "").replace("https://", ""))
        except socket.gaierror:
            return "Unknown"

    def animate(self, text, delay=0.07):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

    def check_wp(self):
        self.animate(f"Checking if {self.url} is a WordPress site...")
        result = WPChecker(self.url).run()
        if result is None:
            self.results["is_wordpress"] = False
            return False
        self.results["is_wordpress"] = result.get("is_wordpress", False)
        return self.results["is_wordpress"]

    def scan_ports(self):
        ports = [80, 443, 21, 22, 3306, 8080, 1900]
        open_ports = []
        self.animate("Scanning open ports...")
        for port in ports:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(1)
                    if s.connect_ex((self.ip, port)) == 0:
                        open_ports.append(port)
                        print(f"[+] Port {port} is OPEN")
            except:
                pass
        self.results["open_ports"] = open_ports

    def run_scan(self):
        print(f"\n[+] Target: {self.url} ({self.ip})")
        try:
            if not self.check_wp():
                print("[!] Not a WordPress site. Exiting... Press y to continue anyway.")
                sk = input("wp (do you want pass?)[y/N] >").strip().lower()
                if sk != "y":
                    return
        except EOFError:
            pass

        if self.mode in ["quick", "default", "deep"]:
            self.scan_ports()
        if self.mode in ["default", "deep"]:
            self.results["plugins"] = WPPluginScanner(self.url).run()
            self.results["themes"] = WPThemeScanner(self.url).run()
            self.results["wp_version"] = WPVersionScanner(self.url).run()
            self.results["user_enum"] = WPUserEnumerator(self.url).run()
        if self.mode == "deep":
            self.results["users_passwords"] = WPUserPasswordFinder(self.url).run()
            self.results["sql_xss"] = WPSQLXSSScanner(self.url, timeout=self.timeout).run()
            self.results["bruteforce"] = WPBruteforce(self.url, self.results["users_passwords"].get("users", []), timeout=self.timeout).run()
            self.results["db_user"] = WPUser(self.url).run()
        self.show_results()

    def show_results(self):
        def print_section(title, data):
            print(f"\n[+] {title}:")
            if isinstance(data, list):
                for item in data:
                    print(f" └── {item}")
            else:
                print(f" └── {data if data else 'None'}")

        print_section("WP Version", self.results.get("wp_version", "N/A"))
        print_section("Open Ports", self.results.get("open_ports", []))
        print_section("Plugins", self.results.get("plugins", []))
        print_section("Themes", self.results.get("themes", []))
        print_section("Users", self.results.get("users_passwords", {}).get("users", []))
        print_section("SQL/XSS Vulns", self.results.get("sql_xss", []))
        print_section("Bruteforce Results", self.results.get("bruteforce", "None"))
        print_section("Database Paths", self.results.get("db_user", None))
        print_section("Enumerated Users", self.results.get("user_enum", []))

        if self.log:
            with open("scan_results.log", "w") as f:
                def write_section(title, data):
                    f.write(f"\n[+] {title}:\n")
                    if isinstance(data, list):
                        for item in data:
                            f.write(f" └── {item}\n")
                    else:
                        f.write(f" └── {data if data else 'None'}\n")

                write_section("WP Version", self.results.get("wp_version", "N/A"))
                write_section("Open Ports", self.results.get("open_ports", []))
                write_section("Plugins", self.results.get("plugins", []))
                write_section("Themes", self.results.get("themes", []))
                write_section("Users", self.results.get("users_passwords", {}).get("users", []))
                write_section("SQL/XSS Vulns", self.results.get("sql_xss", []))
                write_section("Bruteforce Results", self.results.get("bruteforce", "None"))
                write_section("Database Paths", self.results.get("db_user", None))
                write_section("Enumerated Users", self.results.get("user_enum", []))
            print("[+] Results saved to scan_results.log")

class Plugin(WPScannerPlugin):
    pass
          
