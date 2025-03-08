# Title: is smb vulnerable? Check it!
# test: good
import socket
import struct
import sys
from netaddr import IPNetwork
import threading

# SMBGhost Paketi
pkt = b'\x00\x00\x00\xc0\xfeSMB@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00$\x00\x08\x00\x01\x00\x00\x00\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00x\x00\x00\x00\x02\x00\x00\x00\x02\x02\x10\x02"\x02$\x02\x00\x03\x02\x03\x10\x03\x11\x03\x00\x00\x00\x00\x01\x00&\x00\x00\x00\x00\x00\x01\x00 \x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\n\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00'

# Çıktıyı kaydetmek için dosya
output_file = "scan_results.txt"
lock = threading.Lock()  # Thread'lerin aynı anda dosyaya yazmasını önlemek için kilit
vulnerable_count = 0  # Açık bulunan cihaz sayacı

def scan_target(ip):
    global vulnerable_count
    sock = socket.socket(socket.AF_INET)
    sock.settimeout(3)

    try:
        sock.connect((str(ip), 445))
        sock.send(pkt)

        nb, = struct.unpack(">I", sock.recv(4))
        res = sock.recv(nb)

        with lock:
            if res[68:70] != b"\x11\x03" or res[70:72] != b"\x02\x00":
                print(f"{ip} Not vulnerable.")
            else:
                print(f"{ip} Vulnerable!")
                vulnerable_count += 1
                with open(output_file, "a") as f:
                    f.write(f"{ip} is VULNERABLE!\n")
    
    except socket.timeout:
        print(f"{ip} Timeout - No response.")
    except Exception as e:
        print(f"{ip} Error: {e}")
    finally:
        sock.close()

def main():
    if len(sys.argv) != 2:
        print("Kullanım: python script.py <subnet>")
        sys.exit(1)

    subnet = sys.argv[1]
    threads = []

    print(f"Scanning subnet: {subnet}")

    for ip in IPNetwork(subnet):
        thread = threading.Thread(target=scan_target, args=(ip,))
        threads.append(thread)
        thread.start()

        if len(threads) >= 50:  # 50 thread birden çalıştır
            for t in threads:
                t.join()
            threads = []

    for t in threads:
        t.join()

    print(f"\nScan completed. {vulnerable_count} device(s) found vulnerable.")
    print(f"Results saved to {output_file}")

if __name__ == "__main__":
    main()