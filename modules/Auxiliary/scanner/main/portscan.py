import socket
from concurrent.futures import ThreadPoolExecutor
import argparse

def scan_port(port, target_ip):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((target_ip, port))
        return port, True
    except:
        return port, False
    finally:
        s.close()

def main():
    parser = argparse.ArgumentParser(description="Basit bir port tarayıcı")
    parser.add_argument("target_ip", type=str, help="Taranacak IP adresi")
    parser.add_argument("-p", "--ports", type=int, nargs='*', help="Taralacak portlar. Belirtilmezse tüm portlar taranır (1-65535).")

    args = parser.parse_args()
    target_ip = args.target_ip
    ports = args.ports

    if ports is None:
        ports = range(1, 65536)
    else:
        ports = list(set(ports))  # Aynı portu birden fazla kez taramamak için set kullanıp listeye çeviriyoruz

    with ThreadPoolExecutor(max_workers=100) as executor:
        results = executor.map(lambda port: scan_port(port, target_ip), ports)

    for port, is_open in results:
        if is_open:
            print(f"Port {port} is open")

if __name__ == "__main__":
    main()