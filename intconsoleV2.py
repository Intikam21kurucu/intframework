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
import platform

# intconsole komutu
    # ASCII sanatı
ascii_sanat = """⠀⠀⠀⠀⠀⠀⠀⠀⠀. 
            ⢀⣠⣤⠶⠶⠶⠶⢦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠛⠁⠀⠀⠀⠀⠀⠀⠈⠙⢷⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠸
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⣠⡴⠞⠛⠉⠉⣩⣍⠉⠉⠛⠳⢦⣄⠀⠀⠀⠀⣿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⠀⣴⡿⣧⣀⠀⢀⣠⡴⠋⠙⢷⣄⡀⠀⣀⣼⢿⣦⠀⠀⣿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⡾⠋⣷⠈⠉⠉⠉⠉⠀⠀⠀⠀⠉⠉⠋⠉⠁⣼⠙⢷⣼⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣇⠀⢻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠀⣸⡟⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣹⣆⠀⢻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡟⠀⣰⣏⣀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⠞⠋⠁⠙⢷⣄⠙⢷⣀⠀⠀⠀⠀⠀⠀⢀⡴⠋⢀⡾⠋⠈⠙⠻⢦
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠀⠀⠀⠀⠀⠀⠹⢦⡀⠙⠳⠶⢤⡤⠶⠞⠋⢀⡴⠟⠀⠀⠀⠀⠀⠀⣆
⠀⠀⠀⠀⠀⠀⠀⠀⣼⠋⠀⠀⢀⣤⣤⣤⣤⣤⣤⣤⣿⣦⣤⣤⣤⣤⣤⣤⣴⣿⣤⣤⣤⣤⣤⣤⣤⡀⠀⠀⠙⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠏⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⢠⣴⠞⠛⠛⠻⢦⡄⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠸⣇⠀⠀⠀⠀⠀⠀⠀⠀
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

     

time.sleep(1)   
      




            
                        
                                    
os.system("clear")





ASCI = """     
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⠶⠾⠿⠛⠛⠻⠿⠶⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⣾⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣆⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⠇⡤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡈⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⡆⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠁⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠸⣧⢸⡆⢀⣀⣀⣤⡀⠀⠀⢀⣤⣀⣀⡀⠀⡟⣸⡟⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠹⣿⠁⣿⣿⣿⣿⡟⠀⠀⠸⣿⣿⣿⣿⠆⣿⠟⠀⠀⠀⣀⠀
⠀⢰⡟⢿⣆⠀⠀⣿⠀⠙⢿⣿⠟⠀⣠⣄⠀⠹⣿⣿⠟⠀⢹⠀⠀⣠⡿⢻⠀
⣠⡾⠃⠈⠻⢷⣦⣽⣄⡀⠀⠀⠀⢸⣿⣿⣧⠀⠀⠀⢀⣠⣿⣤⡶⠟⠁⠘⢿⣆
⠻⠷⠶⠶⣶⣤⣈⠙⠻⣿⣷⣦⠀⠸⠋⠙⠟⠀⣠⣾⣿⠟⠋⣁⣠⣴⠶⠶⠟
⠀⠀⠀⠀⠀⠉⠛⠿⣶⣼⠿⣿⣲⡤⡤⡤⢤⢰⣿⡏⣿⣶⠿⠛⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣠⣴⣿⡄⠻⣹⡟⡟⡟⣻⣻⠽⠁⣿⣦⣄⡀⠀⠀⠀⠀⠀
⠀⠀⣶⠾⠶⠾⠟⠋⣁⣼⣷⡀⠀⠉⠉⠉⠉⠀⢀⣼⣧⣀⠉⠛⠷⠶⠿⣶⠀
⠀⠀⠙⣷⡄⢀⣴⠿⠛⠁⠀⠙⠳⠶⠤⠴⠶⠞⠋⠀⠈⠙⠻⣶⡄⠀⣾⠟⠀
⠀⠀⠀⢸⣷⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣶⡿⠀⠀⠀
-----------------------------------------------------------

___ _   _ _____ ___ _  __    _    __  __ ____  _ _ ____
|_ _| \ | |_   _|_ _| |/ /   / \  |  \/  |___ \/ ( ) ___|
 | ||  \| | | |  | || ' /   / _ \ | |\/| | __) | |/\___ \
 | || |\  | | |  | || . \  / ___ \| |  | |/ __/| |  ___) |
|___|_| \_| |_| |___|_|\_\/_/   \_\_|  |_|_____|_| |____/

 ____  _____ ____  _  _______ ___  ____
|  _ \| ____/ ___|| |/ /_   _/ _ \|  _ \
| | | |  _| \___ \| ' /  | || | | | |_) |
| |_| | |___ ___) | . \  | || |_| |  __/
|____/|_____|____/|_|\_\ |_| \___/|_|
             """
# Kullanıcıdan 'help' komutunu girmesini iste

print(Fore.RED+ASCI)

print(Fore.RED + '------------------------------------------------------------' + Fore.RESET)

print(Fore.BLUE + 'başlatmak için help yaz')
print("""=[ İntikam21-Framework console v2.7.30-dev-bbf096e                  ]
+ -- --=[ 2433 exploits - 1248 auxiliary - 500 post       ]
+ -- --=[ 1465 payloads - 50 encoders - 11 nops           ]
+ -- --=[ 1 evasion ]
+ -- --=[ 103 Tools]
""")

print(Fore.RED + '------------------------------------------------------------' + Fore.RESET)
	
while True:
	help_input = input(Fore.RED+'┌──(intikam21-cyber@root[~]\n└─$ ')
	print(Fore.RESET)
	if help_input == "help":
		print(Fore.RED + """
		103 Tools:
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
		[11] bruteforce 
		[12]update
		+90 tools: [13]
		[14]social hack
				""" + Fore.RESET)
		print("exploit usage: exp-number")
		print(Fore.RED + """
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
			[12]-others command: msfconsole
			[13]-others command: msfconsole
			[14]-others command: msfconsole
			[15]-others command: msfconsole
			
			we are working...
		
		""" + Fore.RESET)
		
		
		print("command help for using : com-help")
	
	if help_input == "1":
		os.system("python3 DDOS.py")
	if help_input == "3":
		os.system("python3 DİSCORD.py")
	if help_input == "2":
		os.system("python3 SMSBOMBER.py")
	if help_input == "4":
		time.sleep(1)
		print("termux [y] kali [n]")
		k = input("Do you using [termux/kali] ?")
		if k == "y" or "Y" or "termux" or "Termux" or "TERMUX":
			os.system("pkg update -y && pkg upgrade -y && apt update -y && apt upgrade -y")
			os.system("pkg install wget -y")
			os.system("wget https://github.com/gushmazuko/metasploit_in_termux/raw/master/metasploit.sh")
			os.system("chmod +x metasploit.sh")
			os.system("./metasploit.sh")
		if k == "n" or "N" or "kali" or "Kali" or "KALİ":
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
		print("Bye bye / yine bekleriz ")
		os.system("exit")
		break
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
		os.system("""
git clone https://github.com/AzeemIdrisi/PhoneSploit-Pro.git
cd PhoneSploit-Pro/
pip install -r requirements.txt
python3 phonesploitpro.py""")
	
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
		os.system("python3 OSINT.py")
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
		
	if help_input == "12":
	    time.sleep(1)
	    print("Termux=n kali=y")
	    k = input("Are you using [termux/kali]? ")
	    if k == "y" or "Y" or "kali" or "Kali" or "KALİ" or "KAli" or "kAli" or "kALİ" or "kalı" or "KALI" or "kalı":
	        os.system("""
cd ~
rm -rf intframework 
git clone https://github.com/Intikam21kurucu/intframework
cd intframework
chmod +x start_kali.sh
./start_kali.sh
""")
	    elif k == "n" or k == "N" or k == "termux" or k == "Termux" or k == "TERMUX" or k == "TermuX" or k == "tERMUX" or k == "tErmux" or k == "tERmux" or k == "terMux" or k == "tErMUX":
	        os.system("""
cd ~
rm -rf intframework
git clone https://github.com/Intikam21kurucu/intframework
cd intframework
chmod +x terbuild.sh
./terbuild.sh
	""")
	if help_input == "13":
		os.system("python3 +90wifitools.py")
	if help_input == "neofetch" or "Neofetch" or "NEOFETCH":
		print("""
+----------------+
   |.---------------.|
   || ||
   || ||
   || ||
   || ||
   |+------------+|
   +-..-----------..-+
   --------------------.
  / /============\ \
 / /===============\ \
/____________________\
\____________________/

"""
	  f"SYSTEM: INTIKAM21'S DESKTOP"
      f"Sürüm: {platform.release()}, "
      f"Makine: {platform.machine()}, "
      f"İşlemci: {platform.processor()}, "
      f"Python Sürümü: {platform.python_version()}")
	if help_input == "14":
		os.system("python3 socialhack.py")
	if help_input != "14" or "13" or "12" or "11" or "10" or "9" or "8" or "7" or "6" or "5" or "4" or "3" or "2" or "1" or "exp-11" or "exp-10" or "exp-9" or "exp-8" or "exp-7" or "exp-6" or "exp-5" or "exp-4" or "exp-3" or "exp-2" or "exp-1":
		os.system(help_input)