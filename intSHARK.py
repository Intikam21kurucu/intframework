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

banner = """
⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⢄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⢣⠀⠀⠉⣳⠤⠒⢊⠉⠉⠉⠉⡍⡉⠉⡐⠒⡲⢦⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⠔⠋⠀⠀⠀⡸⡄⠀⠀⠀⠠⣦⣇⡲⣪⣠⠋⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⡔⠁⠀⠀⠀⠀⠰⣃⣷⢆⠠⠒⢈⣵⣯⣿⠷⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⠊⠀⠀⠀⠀⡀⡠⠀⠀⣹⠁⠀⠀⢀⣀⠴⠊⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡰⠁⢀⠠⢄⣂⠥⢼⠀⠀⣠⠧⠒⠲⡊⢿⡆⠀⠀⠀⠀⠀⠀
⠀⠀⣠⠴⠒⡲⣡⡴⠗⠋⠁⠀⠀⢸⠀⡴⠁⠀⠀⠀⠙⡼⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠉⠉⠒⡟⠉⡆⠀⠀⠀⠀⠀⠘⠼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠸⣴⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀       __________________ ______________________ __ 
_________ /__ ___/__ / / /__ |__ __ \__ //_/ __ __ 
\ __/____ \__ /_/ /__ /| |_ /_/ /_ ,<    
_ / / / /_ ____/ /_ __ / _ ___ | _, __/_ /| |   
/_/ /_/\__/ /____/ /_/ /_/ /_/ |_/_/ |_| /_/ |_|  ⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠖⢲⢶⠶⣶⡶⠶⡶⠶⣖⠒⠒⠒⢒⠒⠒⠒⠒⢒⠒⠒⠒⠒⢒⣒⢶⠶⢶⣶⢶⠀⠀⠀"""

os.system("python3 startintshark.py")

ascii = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡤⠤⢴⡒⠒⠛⣟⠉⠉⠉⢹
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠖⠛⠉⠝⣍⣒⣤⣀⠱⠀⠀⠀⠀⠀⡏
⠀⠀⠀⠀⠀⠀⢀⡠⠴⢒⡿⠋⠁⠀⠀⠀⠀⠀⠀⢀⣤⠖⡲⠢⡤⢄⡀⠢⣼
⠀⠀⠀⠀⡠⠖⢉⡠⢴⠞⠀⠀⠀⠀⠀⠀⢀⡠⠊⣁⡌⢩⠝⠓⢳⢽⣴⡧⠟
⠀⠀⡠⠊⠀⠂⠁⣰⠃⠀⡇⠀⠀⠀⠀⠀⡯⣊⣈⣀⠀⠀⡑⠀⣨⠞⠁⠀⠀
⢠⠞⠀⠀⠀⠀⢰⠃⢰⢠⢃⠀⠀⠀⠀⠀⢻⣦⠀⠀⠀⢹⡟⡾⠁⠀⠀⣷⠀
⠛⠒⠒⠒⠦⣠⠇⠀⠐⡂⡪⣂⡀⠀⠀⠀⠈⢿⣽⢤⣀⢰⢮⠇⠀⠀⠀⡇⣇
⠀⠀⠀⠀⠀⢹⡀⡴⠚⠈⠉⠀⠀⠀⠀⠀⠀⠀⠈⣓⣷⣭⠋⠀⠀⠀⠀⡇⢹
⠀⠀⠀⠀⠀⢈⠏⠀⠀⠀⢀⡇⠀⠀⠀⠀⢒⡲⣶⣋⢱⡀⠉⠲⣄⠀⡴⢃⣾
⠀⠀⠀⠀⢠⠏⠀⠀⠀⢀⠎⠀⠀⠀⠀⠀⠈⠐⠈⠢⢉⡳⠤⣀⠈⠳⣗⢁⠇
⠀⠀⠀⢀⠏⠀⠀⠀⣠⠫⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠒⢬⣎⠀
⠀⠀⠀⡜⠀⣀⡠⠔⢧⡀⠀⠁⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⠞⠁⠀⠀
⠀⠀⠀⢗⠉⠁⠀⠀⠀⠈⠓⠢⠤⢤⣀⣀⣀⣀⣀⣠⠤⠤⠒⠉⠀⠀⠀⠀⠀⠀"""

print(banner)

print(Fore.BLUE, "{1}--Information Gathering", Fore.RESET)
print(Fore.RED, "{2}--Password Attacks", Fore.RESET)
print(Fore.RED, "{3}--Penetrastion & Wireless Testing", Fore.RESET)
print(Fore.RED, "{4}--Web Hacking", Fore.RESET)
print(Fore.RED, "{0}--INSTALL & UPDATE")
print(Fore.RED, "{11}-CONTRIBUTORS")
print(Fore.RED, "{99}-Back intframework\n", Fore.RESET)
  
while True :
	inputr = input("┌──(intikam21-cyber@root[intshark]\n└─$")
	if inputr == "1":
		print(ascii)
		print(Fore.RED, """
		{1}--Nmap
		{2}--Nettacker
		{3}--Int-Formations
		{4}--Setoolkit
		{5}--Gasmask
		{6}--Recong
		{7}--RED_HAWK	
		{8}--İnfoSploit
		{9}--GatheTool
		{10}İnfoGRAM	
		""", Fore.BLUE)

		s = input("┌──(intikam21-cyber@root[intshark/information-gathering]\n└─$")		
		print(Fore.RESET)
		if s == "1":
			os.system("pkg install nmap")
			while True:
				s = input("nmap==>")
				os.system(s)
				if s == "exit" or "Exit" or "EXİT" or "EXIT":
					os.system("exit")
		if s == "2":
			os.system("git clone https://github.com/OWASP/Nettacker")
			os.system("cd Nettacker")
			print("example : python nettacker.py -i 127.0.0.1 -m tcp_connect_port_scan -t 1000")
			while True:
				k = input("nettacker==>")
				os.system(k)
				if k == "exit" or "Exit" or "EXİT" or "EXIT":
					os.system("exit")
		if s == "3":
			os.system("""apt update -y && apt upgrade -y
pkg install git
pkg install python
pkg install python3
git clone https://github.com/Intikam21kurucu/int-formations
chmod +x install.sh
./install.sh
""")
		if s == "4":
			os.system("""git clone https://github.com/AnonHackerr/setoolkitinstaller.git
cd setoolkitinstaller
chmod +x setoolkitinstall.sh
./setoolkitinstall.sh""")
		if s == "5":
			os.system("https://github.com/twelvesec/gasmask")
			os.system("cd gasmask")
			print("""usage :python gasmask.py -i censys --html-title "Hacked By" --Limit 10 --html""")
			while True:
				k = input("gasmask==>")
				os.system(k)
				if k == "exit" or "Exit" or "EXİT" or "EXIT":
					os.system(k)	
		if s == "6":
			os.system("""git clone https://github.com/lanmaster53/recon-ng.git
cd recon-ng
pip install -r REQUIREMENTS
./recon-ng
""")
		if s == "7":
			os.system("""git clone https://github.com/Tuhinshubhra/RED_HAWK
cd RED_HAWK
php rhawk.php""")	
		if s == "8":
			os.system("""git clone https://github.com/CybernetiX-S3C/InfoSploit
		cd InfoSploit
		chmod +x install
		./install
		""")
		if s == "9":
			os.system("""git clone https://github.com/AngelSecurityTeam/GatheTOOL

cd GatheTOOL

python3 GatheTool.py""")
		if s == "10":
			os.system("""git clone https://github.com/muneebwanee/InfoGram.git && cd InfoGram""")
			os.system("python3 -m pip install -r requirements.txt")
			print("""$ python3 main.py -u username

$ python3 main.py -h

-p, --post images info highlight
		""")
		while True:
			k = input("""İnfoGRAM===>""")
			os.system(k)
			if k == "exit" or "Exit" or "EXİT" or "EXIT":
				os.system("exit")
		
		if inputr == '2':
			print("""		
{1}--John The Ripper - The #1 Bruteforce Tool 
{2}--BruteX - Multi-protocol brute force tool 
{3}--Hydra - Fast and flexible brute force tool 
{4}--AnonCracker - The #4 Bruteforce Tool
{5}--Ncrack - Brute force tool for network
{6}--python-bruteforce - The Python Bruteforce
{7}--Medusa - Parallel brute force attacks 
{8}--Crunch - The Create Wordlists for Bruteforce
{9}--CeWL - The Create Wordlists for Bruteforce
{10}--Wifite2 - The wifi bruteforce Tool	
			""")
			s = input("""┌──(intikam21-cyber@root[intshark/Bruteforce]\n└─$""")
			if s == "1":
				os.system("""pkg install git
git clone https://github.com/openwall/john.git
cd john/src
./configure
make
				""")
			if s == "2":
				os.system("""pkg install git
git clone https://github.com/1N3/BruteX.git
cd BruteX
chmod +x install.sh
./install.sh""")
			if s == "3":
				os.system("""pkg install git
git clone https://github.com/vanhauser-thc/thc-hydra.git
cd thc-hydra
./configure
make
make install""")
			if s == "4":
				os.system("""
				
				git clone https://github.com/qseCEan53/Anon-Cracker
				cd Anon-Cracker
				pip install -r requirements.txt
				python3 AnonCracker.py				
				""")
			if s == "5":
				os.system("""
					pkg update -y && pkg upgrade -y
					apt update -y && apt upgrade -y
					pkg install wget
					wget https://github.com/nmap/ncrack/archive/refs/tags/v0.7.tar.gz
					tar -xzvf v0.7.tar.gz
					cd ncrack-0.7
					pkg install autoconf 
					pkg install libtool
					pkg install autoconf libtool
					./configure
					make
					make install
			""")
			if s == "6":
					os.system("""
					git clone https://github.com/Antu7/python-bruteForce	
		cd python-bruteForce
		pip install requests
		python3 bruteforce.py	
					
					
					
					""")
			if s == "7":
					os.system("""
					pkg install git
					git clone https://github.com/jmk-foofus/medusa.git
					cd medusa
					./configure
					make
					make install
					""")		
			if s == "8":
					os.system("""
					pkg install git
					git clone https://github.com/crunchsec/crunch.git
					cd crunch
					make
					make install	
					""")	
			if s == "9":
					os.system("""
					pkg install git ruby
					git clone https://github.com/digininja/CeWL.git
					cd CeWL
					gem install bundler
					bundle install		
					""")
			if s == "10":
				os.system("""
				git clone https://github.com/derv82/wifite2.git
				cd wifite2
				chmod +x setup.py
				chmod +x Wifite.py		
				./setup.py install
				./Wifite.py
				""")
		if inputr == "3":
			print("""
			{1}--İntikam21-framework
			{2}--Metasploit-framework
			{3}--Hunner Framework
			{4}--Katana Framework
			{5}--Social Engineer Toolkit (SET)
			{99}-- update intikam21-framework
			{999}-- Back to intframework			
			""")
			s = input("""
			┌──(intikam21-cyber@root)
			║	
			 ──[intshark/penetration-testing]
			║ 		
			└─$
			""")
			if s == "1":
				os.system("""
				pkg update && pkg upgrade
				pkg install python3
				pkg install git
				pip3 install requests
				git clone https://github.com/Intikam21kurucu/intframework
				cd intframework
				chmod +x terbuild.sh
				./terbuild.sh
				""")
			if s == "2":
					os.system("pkg update -y && pkg upgrade -y && apt update -y && apt upgrade -y")
					os.system("pkg install wget -y")
					os.system("wget https://github.com/gushmazuko/metasploit_in_termux/raw/master/metasploit.sh")
					os.system("chmod +x metasploit.sh")
					os.system("./metasploit.sh")
			if s == "3":
				os.system("""
			git clone https://github.com/b3-v3r/Hunner
			cd Hunner
			python hunner.py			
			""")
			if s == "4":
				os.system("""
			git clone https://github.com/PowerScript/KatanaFramework.git
			cd KatanaFramework
			sh dependencies
			python install
			""")
			if s == "5":
				os.system("""
			git clone https://github.com/trustedsec/social-engineer-toolkit/ setoolkit/
			cd setoolkit
			pip3 install -r requirements.txt
			python setup.py
			""")
			if s == "99":
				os.system("""
			exit
			cd ~
			rm -rf intframework
			git clone https://github.com/Intikam21kurucu/intframework
			cd intframework
			chmod +x terbuild.sh
			./terbuild.sh
			""")
			if s == "999":
				os.system("exit")
				os.system("cd intframework")
				os.system("python3 intconsoleV2.py")
		if inputr == "4":
			print("""
			{1}DoSHaCk	
			{2}Nikto
			{3}MHDDOS
			{4}Web2Attack
			""")
			s = input("""
			┌──(intikam21-cyber@root)
			║	
			 ──[intshark/Web-Hacking]
			║ 		
			└─$""")
			if s == "4":
				os.system("""
				git clone https://github.com/santatic/web2attack
				pip install -r requirements.txt
				python w2aconsole""")
			if s == "2":
				os.system("""
				git clone https://github.com/sullo/nikto
				# Main script is in program/
				cd nikto/program
				# Run using the shebang interpreter
				./nikto.pl -h http://www.example.com
				# Run using perl (if you forget to chmod)
				perl nikto.pl -h http://www.example.com
				""")
			if s == "3":
				os.system("apt -y update && apt -y install curl wget libcurl4 libssl-dev python3 python3-pip make cmake automake autoconf m4 build-essential git && git clone https://github.com/MatrixTM/MHDDoS.git && cd MH* && pip3 install -r requirements.txt") or os.system("""
				git clone https://github.com/MatrixTM/MHDDoS.git
				cd MHDDoS
				pip install -r requirements.txt
				""")
			if s == "1":
				os.system("""
				pkg update -y && pkg upgrade -y
				apt update -y && apt upgrade -y
				pkg install python
				pip install queue
				pip install optparse
				pip3 install time
				pip3 install os 
				pip3 install socket
				pip3 install threading
				pip3 install logging
				pip3 install urllib
				pip3 install urllib.request
				pip3 install random
				pkg install git
				git clone https://github.com/Intikam21kurucu/DoShAcK
				cd DoShAcK
				""")
				print("for example:")
				time.sleep(3.70002)
				os.system("python3 DoShAcK.py -s 192.168.1.1 -p 80 -t 135")
	if inputr == "0":
			os.system("""			exit
			cd ~
			rm -rf intframework
			git clone https://github.com/Intikam21kurucu/intframework
			cd intframework
			chmod +x terbuild.sh
			./terbuild.sh
			""")
	if inputr == "99":
			os.system("exit")
			os.system("cd intframework")
			os.system("python3 intconsoleV2.py")
	if inputr == "11":
			os.system("python3 intly.py")			