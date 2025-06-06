import time
import random
from colorama import Fore, Style

class Plugin:
    def __init__(self):
        self.name = "Adaptive Attack Plugin"
        self.commands = {
            "scan_target": {
                "func": self.scan_target_command,
                "desc": "Performs reconnaissance on the target (OS, ports, services, vulnerabilities).",
                "usage": "scan_target <target_ip>"
            },
            "analyze_vector": {
                "func": self.analyze_vector_command,
                "desc": "Recommends the best attack module and payload based on reconnaissance data.",
                "usage": "analyze_vector <target_ip>"
            },
            "adaptive_attack": {
                "func": self.adaptive_attack_command,
                "desc": "Automatically performs reconnaissance, analysis, and attack.",
                "usage": "adaptive_attack <target_ip>"
            },
            "attack_status": {
                "func": self.attack_status_command,
                "desc": "Displays the status of the last attack.",
                "usage": "attack_status"
            }
        }
        self.last_attack_result = None
        self.last_target_info = None
        self.last_chosen_vector = None

    def scan_target_command(self, args):
        if not args:
            return f"{Fore.RED}[!] Target IP not specified.{Style.RESET_ALL}"
        target_ip = args[0]
        print(f"{Fore.CYAN}[+] Starting reconnaissance on {target_ip}...{Style.RESET_ALL}")

        info = self.scan_target(target_ip)
        self.last_target_info = info

        print(f"{Fore.GREEN}[✓] Reconnaissance completed. Detected information:{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}    [>] Operating System: {info['os']}")
        print(f"    [>] Open Ports: {', '.join(map(str, info['open_ports']))}")
        print(f"    [>] Services: {', '.join(info['services'])}")
        print(f"    [>] Vulnerabilities: {', '.join(info['vulnerabilities'])}{Style.RESET_ALL}")

        return f"{Fore.BLUE}[*] Reconnaissance successfully completed.{Style.RESET_ALL}"

    def analyze_vector_command(self, args):
        if not args:
            return f"{Fore.RED}[!] Target IP not specified.{Style.RESET_ALL}"
        target_ip = args[0]
        print(f"{Fore.CYAN}[+] Starting attack vector analysis for {target_ip}...{Style.RESET_ALL}")

        if not self.last_target_info or self.last_target_info.get("ip") != target_ip:
            self.last_target_info = self.scan_target(target_ip)

        mod, payload = self.select_attack_vector(self.last_target_info)
        self.last_chosen_vector = (mod, payload)

        if mod:
            print(f"{Fore.GREEN}[✓] Recommended module: {mod}")
            print(f"{Fore.YELLOW}[>] Recommended payload: {payload}{Style.RESET_ALL}")
            return f"{Fore.BLUE}[*] Vector analysis completed. Attack vector ready.{Style.RESET_ALL}"
        else:
            return f"{Fore.RED}[!] No suitable attack vector found.{Style.RESET_ALL}"

    def adaptive_attack_command(self, args):
        if not args:
            return f"{Fore.RED}[!] Target IP not specified.{Style.RESET_ALL}"
        target_ip = args[0]
        print(f"{Fore.CYAN}[+] Starting fully automated attack on {target_ip}...{Style.RESET_ALL}")

        info = self.scan_target(target_ip)
        self.last_target_info = info

        mod, payload = self.select_attack_vector(info)
        self.last_chosen_vector = (mod, payload)

        if not mod:
            return f"{Fore.RED}[!] Automatic attack failed: no suitable module found.{Style.RESET_ALL}"

        print(f"{Fore.CYAN}[+] Attack vector determined: Module = {mod}, Payload = {payload}{Style.RESET_ALL}")
        result = self.launch_attack(target_ip, mod, payload)
        self.last_attack_result = result

        print(f"{Fore.GREEN}[✓] Attack completed. Result:\n{result}{Style.RESET_ALL}")
        return f"{Fore.BLUE}[*] Adaptive attack successfully completed.{Style.RESET_ALL}"

    def attack_status_command(self, args):
        if self.last_attack_result:
            return f"{Fore.GREEN}[*] Last attack result:\n{self.last_attack_result}{Style.RESET_ALL}"
        else:
            return f"{Fore.YELLOW}[!] No attack has been executed yet.{Style.RESET_ALL}"

    # --- Helper Methods ---

    def scan_target(self, ip):
        print(f"{Fore.LIGHTBLUE_EX}    [*] Scanning OS...")
        time.sleep(1)
        print(f"    [*] Analyzing open ports...")
        time.sleep(1)
        print(f"    [*] Detecting service versions...")
        time.sleep(1)
        print(f"    [*] Performing vulnerability scan...{Style.RESET_ALL}")
        time.sleep(2)

        info = {
            "ip": ip,
            "os": random.choice(["Linux", "Windows", "Ubuntu", "Debian"]),
            "open_ports": random.sample([21, 22, 23, 80, 443, 445, 3306], 3),
            "services": random.sample(["ssh", "http", "https", "ftp", "mysql"], 3),
            "vulnerabilities": random.sample(
                ["CVE-2020-12345", "CVE-2019-6789", "CVE-2021-40444", "CVE-2022-1388"], 2)
        }
        return info

    def select_attack_vector(self, system_info):
        os_type = system_info.get("os", "").lower()
        ports = system_info.get("open_ports", [])
        vulns = system_info.get("vulnerabilities", [])

        if "linux" in os_type and 22 in ports:
            return ("ssh_bruteforce", "default_ssh_payload")
        if 80 in ports:
            return ("web_exploit", "php_shell_reverse")
        if 445 in ports:
            return ("smb_exploit", "eternalblue_payload")
        if vulns:
            return ("vuln_exploit", vulns[0])

        return (None, None)

    def launch_attack(self, ip, module, payload):
        print(f"{Fore.LIGHTBLUE_EX}    [*] Loading module: {module}")
        time.sleep(1)
        print(f"    [*] Preparing payload: {payload}")
        time.sleep(1)
        print(f"    [*] Connecting to target...")
        time.sleep(2)

        success = random.choice([True, True, False])  # 66% success chance
        if success:
            return f"{Fore.GREEN}[✓] Successful attack on {ip} using '{module}'. Payload: {payload}{Style.RESET_ALL}"
        else:
            return f"{Fore.RED}[X] Attack on {ip} failed. Module: {module}, Payload: {payload}{Style.RESET_ALL}"