import socket
import re
import threading
import argparse

try:
    from scapy.all import ARP, Ether, srp
    scapy_available = True
except ImportError:
    scapy_available = False

def get_mac(ip):
    """Fetches the MAC address of an IP (requires Scapy)."""
    if not scapy_available:
        return "MAC scanning requires 'scapy' (install it with 'pip install scapy')"
    
    arp = ARP(pdst=ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp
    result = srp(packet, timeout=2, verbose=False)[0]

    for sent, received in result:
        return received.hwsrc

    return "Unknown MAC"

def parse_ssdp_response(response):
    """Extracts essential details from SSDP responses."""
    server = re.search(r'SERVER: (.+)', response)
    location = re.search(r'LOCATION: (.+)', response)
    
    server_info = server.group(1) if server else "Unknown"
    location_info = location.group(1) if location else "Unknown"
    
    return server_info, location_info

def ssdp_discover(timeout, save_results, get_mac_addr, custom_port):
    """Scans for SSDP devices on the network."""
    message = b'M-SEARCH * HTTP/1.1\r\n' \
              b'HOST: 239.255.255.250:1900\r\n' \
              b'MAN: "ssdp:discover"\r\n' \
              b'ST: ssdp:all\r\n' \
              b'MX: 3\r\n\r\n'

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(timeout)
    sock.sendto(message, ("239.255.255.250", 1900))

    found_devices = []

    def listen_for_responses():
        """Handles incoming SSDP responses."""
        nonlocal found_devices
        try:
            while True:
                data, addr = sock.recvfrom(1024)
                response = data.decode()
                server, location = parse_ssdp_response(response)

                mac_addr = get_mac(addr[0]) if get_mac_addr else "MAC scanning disabled"
                result = f"\n[+] Device Found: {addr[0]}\n" \
                         f"    ├── Server: {server}\n" \
                         f"    ├── Location: {location}\n" \
                         f"    ├── MAC Address: {mac_addr}\n"

                if result not in found_devices:
                    found_devices.append(result)
                    print(result)
        except socket.timeout:
            pass

    listener_thread = threading.Thread(target=listen_for_responses)
    listener_thread.start()
    listener_thread.join()

    print(f"\n[✓] Scan completed. Devices found: {len(found_devices)}\n")

    if save_results and found_devices:
        with open("ssdp_results.txt", "w") as f:
            for device in found_devices:
                f.write(device + "\n")
        print("[+] Results saved to 'ssdp_results.txt'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advanced SSDP Network Scanner")
    parser.add_argument("-t", "--timeout", type=int, default=5, help="Scanning timeout (default: 5 seconds)")
    parser.add_argument("-s", "--save", action="store_true", help="Save results to a file")
    parser.add_argument("-m", "--mac", action="store_true", help="Retrieve MAC addresses")
    parser.add_argument("-p", "--port", type=int, help="Perform a basic TCP port scan")

    args = parser.parse_args()
    
    ssdp_discover(timeout=args.timeout, save_results=args.save, get_mac_addr=args.mac, custom_port=args.port)