import socket
import concurrent.futures
import ipaddress

def get_hostname(ip):
    """IP adresinin hostname'ini bulur."""
    try:
        return socket.gethostbyaddr(ip)[0]
    except (socket.herror, socket.gaierror):
        return None

def scan_ip(ip):
    """Tek bir IP'nin hostname'ini alır ve gösterir."""
    hostname = get_hostname(ip)
    if hostname:
        print(f"[+] {ip} → Hostname: {hostname}")
    else:
        print(f"[-] {ip} → Hostname bulunamadı.")

def generate_ip_list(start_ip, end_ip):
    """IP aralığı oluşturur."""
    start = ipaddress.IPv4Address(start_ip)
    end = ipaddress.IPv4Address(end_ip)
    return [str(ip) for ip in range(int(start), int(end) + 1)]

def scan_network(ip_range):
    """Belirtilen IP aralığında hostname taraması yapar."""
    if '-' in ip_range:
        start_ip, end_ip = ip_range.split('-')
        ip_list = generate_ip_list(start_ip.strip(), end_ip.strip())
    else:
        ip_list = [ip_range]

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(scan_ip, ip_list)

if __name__ == "__main__":
    # Tek bir IP veya IP aralığı belirtebilirsin.
    ip_range = "192.168.1.1-50"  # Tek bir IP kullanmak istersen: "8.8.8.8"
    scan_network(ip_range)