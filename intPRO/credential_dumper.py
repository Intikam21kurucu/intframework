from colorama import Fore, Style
import os
import re

def credential_dumper():
    print(f"{Fore.GREEN}Credential Dumper Module Started!{Style.RESET_ALL}")
    print("start with: dump (path)")
    while True:
        module = input(f"{Fore.RED + Style.BRIGHT}int4{Style.RESET_ALL} PRO({Fore.RED + Style.BRIGHT}CredentialDumper{Style.RESET_ALL}) > ")

        if module.lower() == "exit":
            print(f"{Fore.YELLOW}Exiting the module...{Style.RESET_ALL}")
            break
        
        elif module.startswith("dump "):
            file_path = module.split(" ")[1]
            print(f"{Fore.YELLOW}Dumping credentials from: {file_path}{Style.RESET_ALL}")
            
            if not os.path.isfile(file_path):
                print(f"{Fore.RED}Error: File not found!{Style.RESET_ALL}")
                continue

            try:
                with open(file_path, 'r') as file:
                    contents = file.readlines()
                    credentials = extract_credentials(contents)
                    if credentials:
                        print(f"{Fore.GREEN}Found Credentials:{Style.RESET_ALL}")
                        for cred in credentials:
                            print(f"  - {cred}")
                    else:
                        print(f"{Fore.RED}No credentials found in the file.{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}Error occurred: {e}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Invalid command: {module}{Style.RESET_ALL}")


def extract_credentials(file_contents):
    """
    This function will scan for possible username and password patterns in the file content.
    Example patterns include 'username: password' or 'user: pass'.
    """
    credentials = []
    username_pattern = r"(\w+):\s*(\w+)"
    email_pattern = r"([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})"
    password_pattern = r"password\s*=\s*(\w+)"

    for line in file_contents:
        # Look for username:password pattern
        match = re.search(username_pattern, line)
        if match:
            credentials.append(f"Username: {match.group(1)}, Password: {match.group(2)}")
        
        # Look for email pattern
        match = re.search(email_pattern, line)
        if match:
            credentials.append(f"Email: {match.group(1)}")
        
        # Look for password assignment pattern
        match = re.search(password_pattern, line)
        if match:
            credentials.append(f"Password: {match.group(1)}")

    return credentials
if __name__ == "__main__" or "main":
	credential_dumper()