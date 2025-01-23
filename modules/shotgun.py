#!/usr/bin/env python3
import argparse
import socket
import colorama
from colorama import Fore, Style, init
def make_red_bold(text):
    return f"{Style.BRIGHT}{Fore.RED}{text}{Style.RESET_ALL}"

# Örnek kullanım
def send_bytes_to_ip(target_ip, target_port, byte_size, timeout=3):
    """Belirtilen süre içinde belirtilen boyutta bir byte dizisi gönderir.

    Args:
        target_ip (str): Hedef IP adresi.
        target_port (int): Hedef port numarası.
        byte_size (int): Gönderilecek byte dizisinin boyutu.
        timeout (int): Bağlantı süresi sınırı (varsayılan: 3 saniye).
    """
    # Byte dizisi oluştur
    message = b"A" * byte_size  # Örnek olarak 'A' karakteri byte dizisini kullanıyoruz

    # TCP soketi oluştur
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)  # Bağlantı süresi sınırı

    try:
        # Hedef IP ve port'a bağlan
        sock.connect((target_ip, target_port))

        # Byte dizisini gönder
        sock.sendall(message)

        print(f"{byte_size} byte's message true {target_ip}:{target_port} adresses connected.")
    except socket.timeout:
        print(f"Hata: Bağlantı zaman aşımına uğradı ({timeout} saniye içinde bağlantı sağlanamadı).")
    except Exception as e:
        print(f"Hata: Mesaj gönderilirken bir hata oluştu: {str(e)}")
    finally:
        sock.close()

if __name__ == "__main__":
    # Argümanları ayrıştırma
    parser = argparse.ArgumentParser(description="SHOTGUN", prog="shotgun")
    parser.add_argument("lhost", help="Mesajın gönderileceği hedef IP adresi (LHOST=(IP) formatında)")
    parser.add_argument("lport", type=int, help="Mesajın gönderileceği hedef port numarası (LPORT=(port) formatında)")
    parser.add_argument("bytes", type=int, help="Gönderilecek byte dizisinin boyutu")
    args = parser.parse_args()

    # Hedef IP adresini ve port numarasını ayrıştırma
    target_ip = args.lhost.split("=")[1]
    byte_size = args.bytes.split("=")[1]
    target_port = args.lport.split("=")[1]

    # Byte dizisini belirtilen IP adresine ve porta gönder (en fazla 3 saniye içinde)
    send_bytes_to_ip(target_ip, int(target_port), byte_size, timeout=3)
    print(make_red_bold("SHOTTED!"))