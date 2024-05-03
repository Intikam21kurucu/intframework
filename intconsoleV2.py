#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Gerekli kütüphaneler burada import edilir
from pyfiglet import Figlet
from colorama import Fore, init
import threading
import requests
import time
import sys
import os
import base64
import argparse

# Global değişkenler
spinner = ['/', '-', '\\', '|']
spin_index = 0

# Metni büyütüp küçültmek ve dönen karakterleri göstermek için bir fonksiyon
def run_animation(text, max_size, duration):
    global spin_index  # spin_index'i global olarak kullan
    resize_generator = resize_text(text, max_size)  # Generator nesnesi oluştur

    start_time = time.time()
    while time.time() - start_time < duration:  # Belirtilen süre boyunca döndür
        resized_text = next(resize_generator)
        # Dönen karakteri ve yeniden boyutlandırılmış metni yazdır
        sys.stdout.write(f"{spinner[spin_index]} {resized_text}\r")
        sys.stdout.flush()
        # Dönen karakteri güncelle
        spin_index = (spin_index + 1) % len(spinner)
        # Kısa bir süre beklet
        time.sleep(0.2)

# Metni büyütüp küçültmek için generator fonksiyonu
def resize_text(text, max_size):
    while True:  # Sonsuz döngü ile sürekli değer üret
        for size in range(len(text), max_size + 1):
            yield ' ' * (max_size - size) + text[:size]
        for size in range(max_size, len(text) - 1, -1):
            yield ' ' * (max_size - size) + text[:size]


# Argparse nesnesini oluştur ve otomatik --help işlevselliğini devre dışı bırak
parser = argparse.ArgumentParser(prog='İntikam21', description='Çeşitli komutlar için CLI aracı', add_help=False)

# Özel yardım komutu ekleyin
parser.add_argument('--help', action='store_true', help='Yardım mesajını göster')

# Diğer komut satırı argümanlarını tanımla
parser.add_argument('--linux', action='store_true', help='Linux ile ilgili bilgi göster')
parser.add_argument('intconsole', nargs='?', help='Cyber TOOLS CONSOLE\'u başlat')

# Argümanları ayrıştır
args = parser.parse_args()

# Yardım komutu
if args.help:
    print("İntikam21 kullanılabilir komutlar:")
    print("--help  : Bu yardım mesajını gösterir")
    print("--linux   : Linux ile ilgili bilgi gösterir")
    print("intconsole: Cyber TOOLS CONSOLE'u başlat")

# Linux komutu
elif args.linux:
    print("the linux not updating system! please retrying command : python3 intconsole intconsole / if command not working retry command : ""python3 intconsole"" ")

# intconsole komutu
elif 'intconsole' in args:
    # ASCII sanatı
    ascii_sanat = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⠶⠶⠶⠶⢦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠛⠁⠀⠀⠀⠀⠀⠀⠈⠙⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⣠⡴⠞⠛⠉⠉⣩⣍⠉⠉⠛⠳⢦⣄⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⠀⣴⡿⣧⣀⠀⢀⣠⡴⠋⠙⢷⣄⡀⠀⣀⣼⢿⣦⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⡾⠋⣷⠈⠉⠉⠉⠉⠀⠀⠀⠀⠉⠉⠋⠉⠁⣼⠙⢷⣼⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣇⠀⢻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠀⣸⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣹⣆⠀⢻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡟⠀⣰⣏⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⠞⠋⠁⠙⢷⣄⠙⢷⣀⠀⠀⠀⠀⠀⠀⢀⡴⠋⢀⡾⠋⠈⠙⠻⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠀⠀⠀⠀⠀⠀⠹⢦⡀⠙⠳⠶⢤⡤⠶⠞⠋⢀⡴⠟⠀⠀⠀⠀⠀⠀⠙⠻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣼⠋⠀⠀⢀⣤⣤⣤⣤⣤⣤⣤⣿⣦⣤⣤⣤⣤⣤⣤⣴⣿⣤⣤⣤⣤⣤⣤⣤⡀⠀⠀⠙⣧⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣸⠏⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⢠⣴⠞⠛⠛⠻⢦⡄⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠸⣇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⡟⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⣿⣿⢶⣄⣠⡶⣦⣿⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⢻⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣾⠁⠀⠀⠀⠀⠘⣇⠀⠀⠀⠀⠀⠀⠀⢻⣿⠶⠟⠻⠶⢿⡿⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠈⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢰⡏⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⢾⣄⣹⣦⣀⣀⣴⢟⣠⡶⠀⠀⠀⠀⠀⠀⣼⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⣭⣭⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠘⣧⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⢿⡀⠀⠀⠀⠀⠀⠀⣀⡴⠞⠋⠙⠳⢦⣀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⢰⡏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⢿⣄⣀⠀⠀⢀⣤⣼⣧⣤⣤⣤⣤⣤⣿⣭⣤⣤⣤⣤⣤⣤⣭⣿⣤⣤⣤⣤⣤⣼⣿⣤⣄⠀⠀⣀⣠⡾⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠻⢧⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠼⠟⠛⠛⠉⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
. ⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣷⣷⣶⣿⣿ """	
    print(ascii_sanat)
    # Fonksiyonu 10 saniye boyunca çalıştır
run_animation("İNTİKAM21 CYBER TOOLS CONSOLE STARTING...", 10, 10)

    
 

time.sleep(5)   
      




            
                        
                                    
os.system("clear")





ASCI = """      ⣀⣴⣿⣿⠿⠿⠟⠛⠿⠿⣿⣿⣶⣄⠀⠀⠀
⠀⠀⠀⢀⣾⠟⢀⣾⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣷⡄⠹⣷⡀⠀⠀
⠀⠀⠀⣾⡏⢠⣿⣿⡯⠤⠤⠤⠒⠒⠒⠒⠒⠒⠒⠤⠤⠽⣿⣿⡆⠹⣷⡀⠀
⠀⠀⢸⣟⣠⡿⠿⠟⠒⣒⣒⣉⣉⣉⣉⣉⣉⣉⣉⣉⣒⣒⡛⠻⠿⢤⣹⣇⠀
⠀⠀⣾⡭⢤⣤⣠⡞⠉⠁⢀⣀⣀⠀⠀⠀⠀⢀⣀⣀⠀⠈⢹⣦⣤⡤⠴⣿⠀
⠀⠀⣿⡇⢸⣿⣿⣇⠀⣼⣿⣿⣿⣷⠀⠀⣼⣿⣿⣿⣷⠀⢸⣿⣿⡇⠀⣿⠀
⠀⠀⢻⡇⠸⣿⣿⣿⡄⢿⣿⣿⣿⡿⠀⠀⢿⣿⣿⣿⡿⢀⣿⣿⣿⡇⢸⣿⠀
⠀⠀⠸⣿⡀⢿⣿⣿⣿⣆⠉⠛⠋⠀⢴⣶⠀⠉⠛⠉⣠⣿⣿⣿⡿⠀⣾⠇⠀
⠀⠀⠀⢻⣷⡈⢻⣿⣿⣿⣿⣶⣤⣀⣈⣁⣀⡤⣴⣿⣿⣿⣿⡿⠁⣼⠏⠀⠀
⠀⠀⠀⢀⣽⣷⣄⠙⢿⣿⣿⡟⢲⠧⡦⠼⠤⢷⢺⣿⣿⡿⠋⣠⣾⢿⣄⠀⠀
⣰⠟⠛⠛⠁⣨⡿⢷⣤⣈⠙⢿⡙⠒⠓⠒⠒⠚⡹⠛⢁⣤⣾⠿⣧⡀⠙⠋⠙⣆
⠹⣤⡀⠀⠐⡏⠉⠛⠿⣶⣿⣶⣤⣤⣤⣾⣷⠾⠟⠋⢸⢠⣤
⠀⠀⠳⢤⠾⠃⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠁⠀⠀⠀⠀⠘⠷⠤⠾⠁"""

print(Fore.RED+ASCI)

while True:
# Kullanıcıdan 'help' komutunu girmesini iste
	print(Fore.BLUE + 'başlatmak için help yaz')
	print(Fore.RED + '------------------------------------------------------------')
	print("""5-)Tools * 1000-)commands * 70-)exploits 
""")
	help_input = input("┌──(intikam21-cyber@root[~]\n└─$ ")
	if help_input == "help":
		print("""
		5 Tools:
			1-) DDOS
			2-) SMSBOMBER
			3-DİSCORD
			4-)METASPLOİT
			5-)İNTİKAM21
			6-)iptracker
		
		""")
		print("exploit usage: exp-number")
		print("""
		Exploits:
			1-Exploit Database 
			2-MSFVENOM
			3-MSFCONSOLE
			4-NMAP
			......
		
		""")
	if help_input == "1":
		os.system("python3 DDOS.py")
	if help_input == "3":
		os.system("python3 DİSCORD.py")
	if help_input == "2":
		os.system("Python3 SMSBOMBER.py")
	if help_input == "4":
		os.system("sudo apt-get install metasploit-framework")
		os.system("msfconsole")
	if help_input == "5":
		os.system("""apt update & apt upgrade
sudo apt install git
sudo apt install python3-pyfiglet
sudo apt install python3 
sudo apt install python3-base64
sudo apt install python3-colorama
sudo apt install python3-requests

git clone https://github.com/Intikam21kurucu/Intikam21

cd Intikam21

python3 Intıkam21.py""")
	if help_input == "exp-1":
		print("the exploit is not working ")
	if help_input == "exp-2":
		try:
			os.system("msfconsole")
		except:
			os.system("sudo apt-get install metasploit-framework")
	if help_input == "exp-3":
		try:
			os.system("msfvenom")
		except:
			os.system("sudo apt-get install metasploit-framework")
	if help_input == "exp-4":
		try:
			os.system("pip install nmap")
			os.system("nmap")
		except:
			os.system("sudo apt-get install nmap")
	else:
		print("please restart console")
		os.system("python3 intconsole.V2py")
	if help_input == "exit":
		os.system("exit")
	if help_input == "6":
		os.system("python3 iptracker.py")




















def banner():
	# 'INTIKAM21 CYBER' metnini mavi renkte ve slant fontuyla yazdır
	f = Figlet(font='slant')
	print(Fore.BLUE + f.renderText('INTIKAM21 CYBER') + Fore.RESET)