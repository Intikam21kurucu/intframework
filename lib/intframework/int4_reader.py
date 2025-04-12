import os
import importlib.util
import time
import math
from datetime import datetime
import subprocess
import requests

# Değişkenleri saklamak için bir dictionary
variables = {}

# Modül yükleme fonksiyonu
def load_module(module_name):
    try:
        if module_name.endswith(".py"):
            spec = importlib.util.spec_from_file_location("module", module_name)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
        else:
            raise ImportError("Sadece .py uzantılı dosyalar yüklenebilir.")
    except Exception as e:
        print(f"Modül yüklenirken hata: {e}")

# print fonksiyonu (Python'daki print işlevi)
def int4_print(message):
    try:
        print(message)
    except Exception as e:
        print(f"Print hatası: {e}")

# WiFi ağlarını tarama
def scan_wifi():
    try:
        print("WiFi ağları taranıyor...")
        result = subprocess.run(['nmcli', 'dev', 'wifi'], capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print(f"WiFi tarama hatası: {e}")

# WiFi ağına bağlanma
def connect_wifi(ssid, password):
    try:
        print(f"{ssid} ağına bağlanıyor...")
        subprocess.run(['nmcli', 'dev', 'wifi', 'connect', ssid, 'password', password], check=True)
        print(f"{ssid} ağına başarıyla bağlanıldı.")
    except Exception as e:
        print(f"Bağlantı hatası: {e}")

# HTTP GET isteği
def http_get(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"GET isteği başarılı! Yanıt: {response.text}")
        else:
            print(f"GET isteği başarısız! Hata Kodu: {response.status_code}")
    except Exception as e:
        print(f"GET isteği hatası: {e}")

# HTTP POST isteği
def http_post(url, data):
    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print(f"POST isteği başarılı! Yanıt: {response.text}")
        else:
            print(f"POST isteği başarısız! Hata Kodu: {response.status_code}")
    except Exception as e:
        print(f"POST isteği hatası: {e}")

# JSON verisi işleme
def handle_json(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(f"JSON verisi: {data}")
        else:
            print(f"JSON isteği başarısız! Hata Kodu: {response.status_code}")
    except Exception as e:
        print(f"JSON işleme hatası: {e}")

# Web sayfası çekme
def fetch_webpage(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Web sayfası içeriği: {response.text[:200]}...")  # İlk 200 karakteri yazdırıyoruz
        else:
            print(f"Web sayfası çekme hatası! Hata Kodu: {response.status_code}")
    except Exception as e:
        print(f"Web sayfası hatası: {e}")

# Değişken ataması ve hesaplama
def assign_variable(variable_name, value):
    try:
        # Aritmetik ifadeleri değerlendirme
        if isinstance(value, str) and '+' in value:
            value = sum(map(int, value.split('+')))
        elif isinstance(value, str) and '-' in value:
            value = sum(map(int, value.split('-')))
        variables[variable_name] = value
        print(f"{variable_name} değişkenine {value} değeri atandı.")
    except Exception as e:
        print(f"Değişken atama hatası: {e}")

# each fonksiyonu (Bir iterable üzerinde işlem yapmak)
def each(iterable, function):
    try:
        for item in iterable:
            function(item)
    except Exception as e:
        print(f"Each döngüsü hatası: {e}")

# conditional fonksiyonu (Koşul yapısı)
def conditional(statement, true_block, false_block):
    try:
        if statement:
            block(true_block)
        else:
            block(false_block)
    except Exception as e:
        print(f"Koşul hatası: {e}")

# Fonksiyonlar ve işlemler
def test(module_name):
    try:
        __import__(module_name)
        print(f"{module_name} başarıyla yüklü.")
    except ImportError:
        print(f"{module_name} eksik.")

def wait(seconds):
    try:
        time.sleep(int(seconds))
    except ValueError:
        print("Hatalı bekleme süresi.")

def block(function, *args):
    try:
        return function(*args)
    except Exception as e:
        print(f"Block hatası: {e}")

# switch fonksiyonu (Koşul yapıları için)
def switch(value, *cases):
    for case in cases:
        if case[0] == value:
            return case[1]()
    return None

# assert fonksiyonu (Test ve doğrulama)
def assert_equal(expected, actual):
    if expected != actual:
        raise AssertionError(f"Beklenen: {expected}, Gerçek: {actual}")

# int4 okuyucu (Ruby diline özgü kodlar)
def int4_reader(file_path):
    if not os.path.exists(file_path):
        print("Dosya bulunamadı.")
        return

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith("#"):  # Yorum satırlarını atla
                continue

            try:
                if line.startswith("Load"):
                    module_name = line.split("Load")[-1].strip()
                    load_module(module_name)

                elif line.startswith("print"):
                    message = line.split("print", 1)[-1].strip()
                    int4_print(message)

                elif line.startswith("def"):
                    parts = line.split(":", 1)
                    function_name = parts[0].replace("def", "").strip()
                    function_body = parts[1].strip()
                    define_function(function_name, function_body)

                elif line.startswith("test"):
                    module_name = line.split("test")[-1].strip()
                    test(module_name)

                elif line.startswith("wait"):
                    seconds = line.split("wait")[-1].strip()
                    wait(seconds)

                elif line.startswith("scan_wifi"):
                    scan_wifi()

                elif line.startswith("connect_wifi"):
                    params = line.split("connect_wifi")[-1].strip()
                    ssid, password = params.split(",")
                    connect_wifi(ssid.strip(), password.strip())

                elif line.startswith("disconnect_wifi"):
                    disconnect_wifi()

                elif line.startswith("get_connected_wifi"):
                    get_connected_wifi()

                elif line.startswith("http_get"):
                    url = line.split("http_get")[-1].strip()
                    http_get(url)

                elif line.startswith("http_post"):
                    params = line.split("http_post")[-1].strip()
                    url, data = params.split(",")
                    http_post(url.strip(), data.strip())

                elif line.startswith("handle_json"):
                    url = line.split("handle_json")[-1].strip()
                    handle_json(url)

                elif line.startswith("fetch_webpage"):
                    url = line.split("fetch_webpage")[-1].strip()
                    fetch_webpage(url)

                elif line.startswith("each"):
                    params = line.split("each")[-1].strip()
                    iterable, func = params.split(",")
                    iterable = eval(iterable)  # iterable string olarak alınır ve eval ile işlenir
                    each(iterable, globals()[func.strip()])

                elif line.startswith("conditional"):
                    params = line.split("conditional")[-1].strip()
                    statement, true_block, false_block = params.split(",")
                    conditional(eval(statement.strip()), globals()[true_block.strip()], globals()[false_block.strip()])

                elif "=" in line:
                    # Değişken atama
                    variable_name, value = line.split("=", 1)
                    variable_name = variable_name.strip()
                    value = value.strip()
                    if value.isdigit():
                        assign_variable(variable_name, int(value))
                    else:
                        assign_variable(variable_name, value)

                else:
                    os.system(line)
            except Exception as e:
                print(f"Hata: {e}")
                pass_card()

# pass_card (hata yakalama ve geçiş komutu)
def pass_card():
    pass

# Fonksiyon çalıştırma örneği
if __name__ == "__main__":
    pass
    #try:
        #int4_reader("ornek.int4")