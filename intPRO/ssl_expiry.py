import ssl
import socket
from datetime import datetime
from colorama import Fore, Style

def ssl_certificate_expiry(url):
    try:
        context = ssl.create_default_context()
        conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=url)
        conn.connect((url, 443))
        cert = conn.getpeercert()
        expiry_date = cert['notAfter']
        expiry_date = datetime.strptime(expiry_date, "%b %d %H:%M:%S %Y GMT")
        return expiry_date
    except Exception as e:
        return f"{Fore.RED}Error: {e}{Style.RESET_ALL}"

def ssl_certificate_expiry_module():
    print(f"{Fore.GREEN}SSL Certificate Expiry Checker Module Started!{Style.RESET_ALL}")
    
    while True:
        module = input(f"{Fore.RED + Style.BRIGHT}int4{Style.RESET_ALL} PRO({Fore.RED + Style.BRIGHT}SSLExpiryChecker{Style.RESET_ALL}) > ")
        
        if module.lower() == "exit":
            print(f"{Fore.YELLOW}Exiting the module...{Style.RESET_ALL}")
            break
        
        elif module.startswith("checkexpiry "):
            try:
                _, target_url = module.split(" ")
                expiry_date = ssl_certificate_expiry(target_url)
                if isinstance(expiry_date, datetime):
                    print(f"{Fore.YELLOW}SSL Certificate for {target_url} expires on: {expiry_date}{Style.RESET_ALL}")
                else:
                    print(expiry_date)
            except ValueError:
                print(f"{Fore.RED}Invalid input! Correct usage: checkexpiry <URL>{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Invalid command: {module}{Style.RESET_ALL}")
if __name__ == "__main__" or "main":
	ssl_certificate_expiry_module()