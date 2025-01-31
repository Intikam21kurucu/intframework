from scapy.all import *
from scapy.layers.dot11 import Dot11, Dot11Beacon, Dot11ProbeResp

class WLANScanner:
    def __init__(self, interface):
        self.interface = interface

    def scan(self):
        print("Scanning for WLAN networks...")
        sniff(iface=self.interface, prn=self.packet_handler, timeout=10)

    def packet_handler(self, packet):
        if packet.haslayer(Dot11Beacon):
            ssid = packet[Dot11Beacon].info.decode(errors='ignore')
            bssid = packet[Dot11].addr2
            channel = int(ord(packet[Dot11Elt:3].info))
            print(f"SSID: {ssid}, BSSID: {bssid}, Channel: {channel}")
        elif packet.haslayer(Dot11ProbeResp):
            ssid = packet[Dot11ProbeResp].info.decode(errors='ignore')
            bssid = packet[Dot11].addr2
            print(f"SSID: {ssid}, BSSID: {bssid}")

def main():
    import argparse
    parser = argparse.ArgumentParser(description='WLAN Scanner')
    parser.add_argument('interface', type=str, help='Network interface to use for scanning (e.g., wlan0)')
    args = parser.parse_args()

    scanner = WLANScanner(args.interface)
    scanner.scan()

if __name__ == '__main__':
    main()