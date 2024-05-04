#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pyfiglet import Figlet
from colorama import Fore, init
import threading
import requests
import time
import sys
import os
import base64
import time as t
import argparse
import sys




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
    # 5 saniye boyunca animasyonu çalıştır
    os.system("python3 startoolkit.py")

     

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
# Kullanıcıdan 'help' komutunu girmesini iste
print(Fore.BLUE + 'başlatmak için help yaz')
	


while True:
	
	
	print(Fore.RED+ASCI)
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
			7-)youtube-hack
			8-)Send email
			9-)OSINT Framework
	SPECİAL:	
			----------------------------------------------
			| [10]android-pin-bruteforce |
			-----------------------------------------------
		""")
		print("exploit usage: exp-number")
		print("""
		Exploits:
			[1]-Exploit Database 
			[2]-MSFVENOM
			[3]-MSFCONSOLE
			[4]-NMAP
			[5]-TRAİTOR
			[6]-facebook-id-collector			
			
			SPECİAL:
			---------------------------------------------
		   |. [7]-youtube -------- exploit    |
		   |	[8]-phonesploit	  			|
		   |	[9]-camera exploit			 |
		   |	 [10]-camexp2				   |
			---------------------------------------------	
			
			
			[11] EMAIL FINDER
			[12]-error!
			[13]-error!
			[14]-error!
			[15]-error!
			
			we are working...
		
		""")
		
		print("command help for using : com-help")
	
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
	if help_input == "exit":
		os.system("exit")
	if help_input == "6":
		os.system("python3 iptracker.py")
	if help_input == "exp-5":
		os.system("""git clone https://github.com/liamg/traitor
		cd traitor
		traitor -p -e docker:writable-socket			
		""")
	if help_input == "exit":
		print("exiting console...")
		time.sleep(2)
		os.system("exit")
	if help_input == "exp-6":
		os.system("python2 id-collector.py")
	if help_input == "exp-7":
		os.system("python3 specialintikam21youtube.py")

	if help_input == "exp-8":
		os.system("python phonesploit.py")
	
	if help_input == "exp-9":
		os.system("python expcamera.py")
	if help_input == "exp-10":
		s = input ("Do yo want to continue [y/n]")
		if s == "y":
			os.system("python3 camexp2.py")
		if s == "n":
			print("restarting...")
			time.sleep(3)
			os.system("python3 intconsoleV2.py")

	if help_input == "7": 
		os.system("""
		git clone https://github.com/in4osecurity/Youtube-Hack
		cd Youtube-Hack
		bash kurulum.sh		
		""")
	if help_input == "8":
		os.system("python3 sendemail.py")
	if help_input == "9":
		os.system("Python3 OSINT.py")
	if help_input == "exp-11":
		os.system("python3 emailfinder.py")
	if help_input == "10":
		s = input("do you want to continue? [y/n]")
		if s == "y":
			os.system("""			
			git clone https://github.com/urbanadventurer/Android-PIN-Bruteforce
			cd Android-PIN-Bruteforce
			./android-pin-bruteforce crack --length 6				""")
		if s == "n":
			print("restarting...")
			time.sleep(3)
			os.system("python3 intconsoleV2.py")
	if help_input == "11":
		os.system("""
		
		git clone https://github.com/Antu7/python-bruteForce	
		cd python-bruteForce
		pip install requests
		python3 bruteforce.py		
		""")