import scapy.all as scapy
import argparse
import json
import geoip2.database
from datetime import datetime

# GeoIP veritabanı
GEOIP_DB = "GeoLite2-City.mmdb"  # IP konumu için GeoLite2 kullanılıyor

# Log formatı (SIEM uyumlu JSON)
def log_event(event_type, src_ip, dst_ip, protocol, details):
    log_data = {
        "timestamp": datetime.utcnow().isoformat(),
        "event_type": event_type,
        "source_ip": src_ip,
        "destination_ip": dst_ip,
        "protocol": protocol,
        "details": details
    }
    print(json.dumps(log_data, indent=4))

# GeoIP konum tespiti
def get_geoip(ip):
    try:
        with geoip2.database.Reader(GEOIP_DB) as reader:
            response = reader.city(ip)
            return f"{response.city.name}, {response.country.name}"
    except:
        return "Unknown"

# Paket analiz fonksiyonu
def packet_callback(packet):
    if packet.haslayer(scapy.IP):
        src_ip = packet[scapy.IP].src
        dst_ip = packet[scapy.IP].dst
        protocol = packet[scapy.IP].proto
        geo_src = get_geoip(src_ip)
        geo_dst = get_geoip(dst_ip)

        # Şifrelenmiş trafik analizi (TLS, SSH, VPN)
        if packet.haslayer(scapy.TCP):
            sport = packet[scapy.TCP].sport
            dport = packet[scapy.TCP].dport

            if dport in [443, 8443]:  # TLS/SSL trafiği
                log_event("Encrypted TLS Traffic", src_ip, dst_ip, "TLS/SSL", f"Geo: {geo_src} -> {geo_dst}")

            elif dport in [22]:  # SSH trafiği
                log_event("Encrypted SSH Traffic", src_ip, dst_ip, "SSH", f"Geo: {geo_src} -> {geo_dst}")

            elif dport in [1194, 500, 4500]:  # VPN bağlantıları (OpenVPN, IPsec)
                log_event("Encrypted VPN Traffic", src_ip, dst_ip, "VPN", f"Geo: {geo_src} -> {geo_dst}")

        # Şifrelenmemiş protokoller (HTTP, FTP, Telnet, SMTP)
        if packet.haslayer(scapy.Raw):
            raw_data = packet[scapy.Raw].load.decode(errors="ignore")

            if "login" in raw_data.lower() or "password" in raw_data.lower():
                log_event("Cleartext Credentials", src_ip, dst_ip, "UNENCRYPTED", raw_data[:100])

        # Şüpheli trafik tespiti
        if packet.haslayer(scapy.TCP) and packet[scapy.TCP].flags == 2:  # SYN paketi
            log_event("Possible SYN Scan", src_ip, dst_ip, "TCP", "SYN packet detected")

        if packet.haslayer(scapy.ARP):  # ARP Spoofing
            log_event("Possible ARP Spoofing", src_ip, dst_ip, "ARP", "Unusual ARP traffic detected")

        if packet.haslayer(scapy.DNS) and packet[scapy.UDP].sport == 53:  # DNS Tünelleme
            log_event("Possible DNS Tunneling", src_ip, dst_ip, "DNS", "High-frequency DNS requests")

# Argümanlar
parser = argparse.ArgumentParser(description="Advanced Packet Analyzer")
parser.add_argument("-i", "--interface", required=True, help="Network interface to capture packets (e.g., eth0, wlan0)")
args = parser.parse_args()

# Paket yakalama
print(f"[*] Listening on interface {args.interface}...")
scapy.sniff(iface=args.interface, store=False, prn=packet_callback)