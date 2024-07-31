import argparse
import socket
import threading

def scan(ip):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, 135))
        if result == 0:
            print(f"Device found at IP: {ip}")
        sock.close()
    except socket.error:
        pass

def main():
    parser = argparse.ArgumentParser(description="Simple Network Scanner")
    parser.add_argument("network", help="Network to scan (e.g. 192.168.1.0/24)")
    args = parser.parse_args()
    
    ip_range = args.network.split('.')
    base_ip = ".".join(ip_range[:3]) + "."
    
    threads = []
    for i in range(1, 255):
        ip = base_ip + str(i)
        t = threading.Thread(target=scan, args=(ip,))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()

if __name__ == "__main__":
    main()