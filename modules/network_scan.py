#!/usr/bin/env python3
import socket
from ping3 import ping
import netifaces
import ipaddress
import subprocess
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import Fore, Style, init
import platform

# Colorama'yı başlat
init(autoreset=True)

# Başlıkları Yazdır
def print_header():
    print(Fore.GREEN + "Network Scanner")
    print(Fore.CYAN + "IP Address    | Device Name        | Status")
    print(Fore.CYAN + "---------------------------------------------")

# 1. Socket ile Port Kontrolü
def is_device_active_by_port(ip, port=80):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
        return result == 0
    except Exception:
        return False

# 2. Ping ile Kontrol
def is_device_active_by_ping(ip):
    try:
        response = ping(ip, timeout=1)
        return response is not None
    except Exception:
        return False

# 3. Yerel IP Aralığı ile Tarama
def get_local_ip_range():
    try:
        iface = netifaces.interfaces()[0]
        iface_info = netifaces.ifaddresses(iface)
        ip = iface_info[netifaces.AF_INET][0]['addr']
        netmask = iface_info[netifaces.AF_INET][0]['netmask']
        network = ipaddress.ip_network(f"{ip}/{netmask}", strict=False)
        return [str(ip) for ip in network.hosts()]
    except Exception:
        return []

# 4. `subprocess` ile Ping Komutu
def ping_using_subprocess(ip):
    try:
        output = subprocess.check_output(["ping", "-c", "1", ip], stderr=subprocess.STDOUT, universal_newlines=True)
        return "1 packets transmitted, 1 received" in output
    except subprocess.CalledProcessError:
        return False

# 5. `requests` ile HTTP İsteği
def is_device_active_by_http(ip):
    try:
        response = requests.get(f"http://{ip}", timeout=1)
        return response.status_code == 200
    except requests.RequestException:
        return False

# 6. `BeautifulSoup` ile Web Sayfası Kontrolü
def check_http_status_using_bs(ip):
    try:
        response = requests.get(f"http://{ip}", timeout=1)
        soup = BeautifulSoup(response.text, 'html.parser')
        return response.status_code == 200 and soup.title is not None
    except requests.RequestException:
        return False

# 7. `socket` ile DNS Sorgulaması
def is_device_active_by_dns(ip):
    try:
        socket.gethostbyaddr(ip)
        return True
    except socket.herror:
        return False

# 8. Cihaz Adı Alma
def get_device_name(ip):
    if ip == get_local_ip():
        return platform.node()  # Cihaz adını almak için platform modülünü kullan
    device_names = {
        "192.168.1.1": "Router",
        "192.168.1.254": "Modem",
        # Daha fazla varsayılan IP ve isim ekleyebilirsiniz
    }
    return device_names.get(ip, "Unknown Device")

# Cihazın kendi IP adresini alma
def get_local_ip():
    try:
        iface = netifaces.interfaces()[0]
        iface_info = netifaces.ifaddresses(iface)
        return iface_info[netifaces.AF_INET][0]['addr']
    except Exception:
        return "Unknown IP"

# Cihazları Tarama
def scan_network():
    local_ips = get_local_ip_range()
    print_header()
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(scan_ip, ip): ip for ip in local_ips}
        
        for future in as_completed(futures):
            ip = futures[future]
            try:
                future.result()
            except Exception as e:
                print(f"Error scanning {ip}: {e}")

def scan_ip(ip):
    status = []
    
    if is_device_active_by_port(ip):
        status.append('Port Active')
    if is_device_active_by_ping(ip):
        status.append('Ping Active')
    if ping_using_subprocess(ip):
        status.append('Subprocess Ping Successful')
    if is_device_active_by_http(ip):
        status.append('HTTP Active')
    if check_http_status_using_bs(ip):
        status.append('BeautifulSoup HTTP Active')
    if is_device_active_by_dns(ip):
        status.append('DNS Active')
    
    device_name = get_device_name(ip)
    status_str = ', '.join(status) if status else 'Inactive'
    print(f"{Fore.YELLOW}{ip:<15} | {Fore.WHITE}{device_name:<20} | {Fore.GREEN if status else Fore.RED}{status_str}")

# Tarama Başlat
if __name__ == "__main__":
    scan_network()