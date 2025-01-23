#!/usr/bin/env python3
import socket
import requests
import subprocess
import re
import os
from colorama import *

init(autoreset=True)

def print_prompt(message, color=Fore.WHITE):
    print(f"{color}[intBase] {message}{Fore.RESET}")

def print_options(lhosts, lports):
    print(f"{Fore.CYAN}=================== OPTIONS ==================={Fore.RESET}")
    print(f"  {Fore.GREEN}TARGET{Fore.RESET}      : {lhosts if lhosts else 'N/A'}")
    print(f"  {Fore.GREEN}PORT{Fore.RESET}        : {lports if lports else 'N/A'}")
    print(f"{Fore.CYAN}-----------------------------------------------{Fore.RESET}")
    print(f"  {Fore.YELLOW}HTTP{Fore.RESET}        : {'Yes' if lports == 80 else 'No'}")
    print(f"  {Fore.YELLOW}HTTPS{Fore.RESET}       : {'Yes' if lports == 443 else 'No'}")
    print(f"  {Fore.YELLOW}SSH{Fore.RESET}         : {'Yes' if lports == 22 else 'No'}")
    print(f"{Fore.CYAN}-----------------------------------------------{Fore.RESET}")
    print(f"  {Fore.MAGENTA}DESCRIPTION{Fore.RESET} : ")
    print(f"    - Target IP for the attack")
    print(f"    - Port to be used for the attack")
    print(f"    - Use HTTP for payload if port is 80")
    print(f"    - Use HTTPS for secure payload if port is 443")
    print(f"    - Use SSH for remote access if port is 22")
    print(f"{Fore.CYAN}=============================================== {Fore.RESET}")

def os_detect(ip):
    print_prompt(f"{ip} OS detection starting for the IP address...", Fore.YELLOW)

    try:
        # Check with HTTP Header
        http_os = None
        try:
            response = requests.get(f"http://{ip}", timeout=1)
            server_header = response.headers.get("Server")
            if server_header:
                print_prompt(f"HTTP server information for {ip}: {server_header}", Fore.CYAN)
                if "Windows" in server_header:
                    http_os = "Windows"
                elif "Linux" in server_header or "Unix" in server_header:
                    http_os = "Linux/Unix"
                elif "Android" in server_header:
                    http_os = "Android"
                elif "iPhone" in server_header or "iOS" in server_header:
                    http_os = "iOS"
                elif "Apache" in server_header:
                    http_os = "Likely Linux/Unix with Apache"
                elif "nginx" in server_header:
                    http_os = "Likely Linux/Unix with Nginx"
        except requests.exceptions.RequestException:
            print_prompt("HTTP request failed.", Fore.RED)

        # Check TCP connections to specific ports
        tcp_os = None
        ports = [22, 80, 443]  # SSH, HTTP, HTTPS
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                if port == 22:
                    print_prompt(f"SSH is open on {ip}.", Fore.GREEN)
                    tcp_os = "Likely Linux"
                elif port == 80:
                    print_prompt(f"HTTP is open on {ip}.", Fore.GREEN)
                    tcp_os = "Likely Linux or Windows"
                elif port == 443:
                    print_prompt(f"HTTPS is open on {ip}.", Fore.GREEN)
                    tcp_os = "Likely Linux or Windows"
            sock.close()

        # Combine results
        if http_os:
            final_os = http_os
        elif tcp_os:
            final_os = tcp_os
        else:
            final_os = "No information"

        print_prompt(f"Estimated operating system for {ip}: {final_os}", Fore.BLUE)
        return final_os

    except Exception as e:
        print_prompt(f"An error occurred: {e}", Fore.RED)

# Function to obtain the TTL value of a device given its IP address
def obtener_ttl(direccion_ip):
    try:
        # Set parameter for the ping command based on OS
        parametro = "-n" if os.name == "nt" else "-c"
        resultado = subprocess.check_output(['ping', parametro, '1', direccion_ip], universal_newlines=True)
        ttl_match = re.search(r'ttl=(\d+)', resultado, re.IGNORECASE)
        if ttl_match:
            ttl = int(ttl_match.group(1))
            return ttl
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}Error al ejecutar el comando ping: {e}{Fore.RESET}")
    except ValueError:
        print(f"{Fore.RED}Error al procesar el TTL.{Fore.RESET}")
    return None

def determinar_so(ip, ttl):
    print(f"{Fore.YELLOW}Identificadores de dispositivos{Fore.RESET}\n")
    ttl = int(ttl)
    print(f"{Fore.RED}[!] {ip}{Fore.RESET}")
    if ttl <= 64:
        print(f"{Fore.GREEN}[*] TTL({ttl}){Fore.RESET}")
        print(f"{Fore.GREEN}[*] OS: Linux{Fore.RESET}")
    elif ttl <= 128:
        print(f"{Fore.GREEN}[*] TTL({ttl}){Fore.RESET}")
        print(f"{Fore.GREEN}[*] OS: Windows{Fore.RESET}")
    else:
        print(f"{Fore.GREEN}[*] TTL({ttl}){Fore.RESET}")
        print(f"{Fore.GREEN}[*] OS: Solaris/Aix{Fore.RESET}")

# Usage example
if __name__ == "__main__":
    ip = input(f"{Fore.RED + Style.BRIGHT}int4{Fore.RESET} {Fore.BLUE}os_detector{Fore.RESET}[{Fore.YELLOW}Enter IP{Fore.RESET}] >{Style.RESET_ALL}")
    port = int(input(f"{Fore.RED + Style.BRIGHT}int4{Fore.RESET} {Fore.BLUE}os_detector{Fore.RESET}[{Fore.YELLOW}Enter Port{Fore.RESET}] >{Style.RESET_ALL}"))
    print_options(ip, port)
    
    os_detect(ip)  # Start OS detection

    ttl = obtener_ttl(ip)  # Obtain the TTL value
    if ttl is not None:
        determinar_so(ip, ttl)  # Determine the OS based on TTL
    else:
        print(f"{Fore.RED}No se pudo obtener el TTL.{Fore.RESET}")