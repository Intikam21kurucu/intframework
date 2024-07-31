import socket
import argparse

def scan_ports(ip, ports):
    print(f"Scanning {ip} for open ports...")
    open_ports = []
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # Timeout for socket connection
            result = s.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
    
    if open_ports:
        print("Open ports:")
        for port in open_ports:
            print(f"Port {port} is open")
    else:
        print("No open ports found.")

def main():
    parser = argparse.ArgumentParser(description='Scan ports on a given IP address.')
    parser.add_argument('ip', type=str, help='The IP address to scan.')
    parser.add_argument('-p', '--ports', type=int, nargs='+', help='List of ports to scan (e.g. -p 22 80 443)', required=True)
    args = parser.parse_args()
    
    scan_ports(args.ip, args.ports)

if __name__ == '__main__':
    main()