from colorama import Fore, Style, init
import requests
import json
import time
init(autoreset=True)
def subdomain_harvester():
    print(f"{Fore.GREEN}Subdomain Harvester Module Started!{Style.RESET_ALL}")
    print(f"Start with : harvest (domain or site)")
    while True:
        module = input(f"{Fore.RED + Style.BRIGHT}int4{Style.RESET_ALL} PRO({Fore.RED }SubdomainHarvester{Style.RESET_ALL}) > ")

        if module.lower() == "exit":
            print(f"{Fore.YELLOW}Exiting the module...{Style.RESET_ALL}")
            break
        
        elif module.startswith("harvest "):
            domain = module.split(" ")[1]
            print(f"{Fore.YELLOW}Harvesting subdomains for: {domain}{Style.RESET_ALL}")

            subdomains = set()

            # 1. Using crt.sh
            print(f"{Fore.CYAN}Searching via crt.sh...{Style.RESET_ALL}")
            try:
                url = f"https://crt.sh/?q=%25.{domain}&output=json"
                response = requests.get(url)
                if response.status_code == 200:
                    crt_data = response.json()
                    for item in crt_data:
                        subdomains.add(item['name_value'])
                else:
                    print(f"{Fore.RED}Error with crt.sh API!{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}Error with crt.sh API: {e}{Style.RESET_ALL}")

            # 2. Using HackerTarget
            print(f"{Fore.CYAN}Searching via HackerTarget...{Style.RESET_ALL}")
            try:
                url = f"https://api.hackertarget.com/hostsearch/?q={domain}"
                response = requests.get(url)
                if response.status_code == 200:
                    lines = response.text.splitlines()
                    for line in lines:
                        subdomain = line.strip().split(",")[0]
                        subdomains.add(subdomain)
                else:
                    print(f"{Fore.RED}Error with HackerTarget API!{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}Error with HackerTarget API: {e}{Style.RESET_ALL}")

            # 3. Using DNSdumpster
            print(f"{Fore.CYAN}Searching via DNSdumpster...{Style.RESET_ALL}")
            try:
                url = f"https://dnsdumpster.com/static/map/{domain}"
                response = requests.get(url)
                if response.status_code == 200:
                    dns_data = response.text
                    # A basic method to extract subdomains from HTML (requires improvement)
                    subdomains.update(extract_subdomains_from_html(dns_data))
                else:
                    print(f"{Fore.RED}Error with DNSdumpster API!{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}Error with DNSdumpster API: {e}{Style.RESET_ALL}")

            # Display collected subdomains
            print(f"{Fore.GREEN}Found Subdomains:{Style.RESET_ALL}")
            for subdomain in subdomains:
                print(f"  - {subdomain}")
        else:
            print(f"{Fore.RED}Invalid command: {module}{Style.RESET_ALL}")


def extract_subdomains_from_html(html_data):
    """
    A simple method to extract subdomains from HTML content.
    It will need adjustments to properly parse the HTML content.
    """
    import re
    subdomains = set()
    pattern = r"\b(?:\w+\.){1,2}\w+\.\w+\b"  # Simple regex for domains
    matches = re.findall(pattern, html_data)
    for match in matches:
        subdomains.add(match)
    return subdomains
if __name__ == "__main__" or "main":
	subdomain_harvester()