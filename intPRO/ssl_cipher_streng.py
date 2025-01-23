import ssl
import socket
from colorama import Fore, Style

def ssl_cipher_strength(url):
    try:
        context = ssl.create_default_context()
        # Connect to the URL over port 443 (HTTPS)
        conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=url)
        conn.connect((url, 443))
        cipher = conn.cipher()  # Get the cipher used in the connection
        return f"{Fore.GREEN}Cipher Strength: {cipher[0]}{Style.RESET_ALL}, Protocol: {cipher[1]}"
    except Exception as e:
        return f"{Fore.RED}Error: {e}{Style.RESET_ALL}"

def ssl_cipher_strength_module():
    print(f"{Fore.GREEN}SSL/TLS Cipher Strength Checker Module Started!{Style.RESET_ALL}")
    
    while True:
        # Get user input for commands
        module = input(f"{Fore.RED + Style.BRIGHT}int4{Style.RESET_ALL} PRO({Fore.RED + Style.BRIGHT}SSLCipherStrength{Style.RESET_ALL}) > ")
        
        if module.lower() == "exit":
            print(f"{Fore.YELLOW}Exiting the module...{Style.RESET_ALL}")
            break
        
        elif module.startswith("checkcipher "):
            try:
                # Extract the URL from the command
                _, target_url = module.split(" ")
                # Get the cipher information for the target URL
                cipher_info = ssl_cipher_strength(target_url)
                print(f"{Fore.YELLOW}Cipher info for {target_url}: {cipher_info}{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED}$USAGE#: checkcipher <TARGET_URL>{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}$USAGE#: checkcipher <TARGET_URL>{Style.RESET_ALL}")

if __name__ == "__main__":
    ssl_cipher_strength_module()