import requests
import os
import platform
import sys

def collect_data():
    # Sistem bilgilerini toplama
    system_info = {
        "os_name": os.name,
        "platform": platform.system(),
        "platform_release": platform.release(),
        "user": os.getenv("USER") or os.getenv("USERNAME"),
    }
    return system_info

def send_data(url, data):
    try:
        response = requests.post(url, json=data)
        print(f"Data gönderildi. Durum kodu: {response.status_code}")
    except Exception as e:
        pass  # Hataları sessizce geç

if __name__ == "__main__":
    # Komut satırından argüman kontrolü
    if len(sys.argv) < 2:
        print("Kullanım: python data_collect.py <bizim serverimizin url si>")
        sys.exit(1)
    
    # Hedef URL'yi sys.argv[1]'den al
    target_url = sys.argv[1]

    # Veri toplama ve gönderme
    data = collect_data()
    send_data(target_url, data)