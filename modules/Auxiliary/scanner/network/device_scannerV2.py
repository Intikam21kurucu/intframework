import socket
import argparse
import json
import time
import concurrent.futures
import platform
import subprocess

# Varsayılan port listesi (Değiştirilebilir)
DEFAULT_PORTS = [21, 22, 53, 80, 443, 3389]

def ping_ip(ip):
    """Ping atarak IP'nin aktif olup olmadığını kontrol eder."""
    param = "-n" if platform.system().lower() == "windows" else "-c"
    try:
        output = subprocess.run(["ping", param, "1", "-W", "1", ip], capture_output=True, text=True)
        return ip if "ttl=" in output.stdout.lower() else None
    except:
        return None

def check_ip(ip, ports):
    """Belirtilen IP adresine TCP bağlantısı yaparak aktif olup olmadığını kontrol eder."""
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            if not s.connect_ex((ip, port)):  # Eğer bağlantı başarılıysa
                return ip
    return None

def get_local_ip():
    """Cihazın bulunduğu yerel IP adresini alır."""
    try:
        hostname = socket.gethostname()
        return socket.gethostbyname(hostname)
    except socket.error:
        return None

def scan_network(base_ip, start, end, ports, threads, output_file, use_ping):
    """Belirtilen IP aralığında tarama yapar."""
    print(f"\n\033[96m[*] Scanning {base_ip}.{start}-{end} on ports {ports}...\033[0m\n")

    active_ips = []
    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        # Eğer ping kullanılacaksa önce ping testi yap, sonra port taraması yap
        results = executor.map(lambda ip: ping_ip(ip) if use_ping else check_ip(ip, ports), 
                               [f"{base_ip}.{i}" for i in range(start, end + 1)])

    for ip in results:
        if ip:
            print(f"\033[92m[+] Active: {ip}\033[0m")
            active_ips.append(ip)

    if output_file and active_ips:
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        output_path = f"{output_file}-{timestamp}.json"
        with open(output_path, "w") as file:
            json.dump(active_ips, file, indent=4)
        print(f"\n\033[94m[*] Results saved to {output_path}\033[0m")

    elapsed_time = time.time() - start_time
    print(f"\n\033[96m[*] Scan completed in {elapsed_time:.2f} seconds.\033[0m")

# Argparse ile komut satırı argümanlarını al
def parse_args():
    parser = argparse.ArgumentParser(description="Advanced Network Scanner (No Root Required)")
    parser.add_argument("-n", "--network", help="Base network (e.g., 192.168.1)")
    parser.add_argument("-s", "--start", type=int, default=1, help="Start IP range (default: 1)")
    parser.add_argument("-e", "--end", type=int, default=254, help="End IP range (default: 254)")
    parser.add_argument("-p", "--ports", type=str, default=",".join(map(str, DEFAULT_PORTS)), 
                        help="Comma-separated list of ports to check (default: common ports)")
    parser.add_argument("-t", "--threads", type=int, default=50, help="Number of threads (default: 50)")
    parser.add_argument("-o", "--output", help="Save results to a JSON file")
    parser.add_argument("--ping", action="store_true", help="Use ping instead of TCP scan")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()

    # Eğer ağ belirtilmemişse, otomatik algıla
    base_ip = args.network if args.network else ".".join(get_local_ip().split(".")[:3])
    port_list = list(map(int, args.ports.split(",")))  # Kullanıcının belirttiği portları al

    scan_network(base_ip, args.start, args.end, port_list, args.threads, args.output, args.ping)