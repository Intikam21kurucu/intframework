from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())

def start_packet_sniffing(interface):
    sniff(iface=interface, prn=packet_callback, store=0)

if __name__ == "__main__":
    interface = "eth0"  # Ağ arayüzü
    start_packet_sniffing(interface)