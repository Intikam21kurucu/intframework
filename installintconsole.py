#!/usr/bin/env/python3


import os
import sys
import time



def loading(text):
    for i in range(10):
        sys.stdout.write("\r" + "[+] " + text + "." * i)
        time.sleep(0.1)
        sys.stdout.flush()
    print("\033[92m" + "\r" + "[+] " + text + "....................OK!\033[0m")

def prompt():
    input("Press ENTER to continue. ")

def start_exploit():
    loading("Accessing Backdoor.........")
    loading("Crafting İntconsole...........")
    loading("Sending İntconsole............")

user_input = input("Do you using termux?[Y/n]")

if user_input == "y" or "Y":
	start_exploit()	
	loading("İnstalling İntconsole...........")
	os.system("apt-get install python3")
	os.system("apt-get install python3-pip")
	os.system("pip3 install --upgrade")
	os.system("pip3 install pyfiglet")
	os.system("pip3 install colorama")
	os.system("pip3 install Fore")
	os.system("pip3 install init")
	os.system("pip3 install threading")
	os.system("pip3 install requests")
	os.system("pip3 install time")
	os.system("pip3 install sys")
	os.system("pip3 install os")
	os.system("pip3 install base64")
	os.system("pip3 install time")
	os.system("pip3 install argparse")
	os.system("chmod +x intconsole.js")
	os.system("cd ~")
	os.system("source .bashrc")
	os.system("alias intconsole='python3 /data/data/com.termux/files/home/intconsoleV2.py' ")
	



	loading("İntconsole Downloading..........")
	print("""
	installed intconsole 
	using = intconsole 
	else : please command using=='run intconsole'		
	""")
	k = input("Do you command is working[Y/n]")
	
	
	if k == "y" or k == "Y":
		os.system("cd ~")
		os.system("nano .bashrc")
		os.system("source .bashrc")
		os.system("alias intconsole='python3 /data/data/com.termux/files/home/intconsoleV2.py' ")
  os.system("source .bashrc")
	if k == "n" or k == "N":
		print("type intconsole to start please")


if user_input == "n" or input == "N":
	start_exploit()	
	loading("İnstalling İntconsole...........")
	os.system("sudo apt-get install python3")
	os.system("sudo apt-get install python3-pip")
	os.system("sudo pip3 install --upgrade")
	os.system("sudo apt install python3-pyfiglet")
	os.system("sudo apt install python3-colorama")
	os.system("sudo apt install python3-Fore")
	os.system("sudo apt install python3-init")
	os.system("sudo install python3-threading")
	os.system("sudo apt install requests")
	os.system("sudo apt install python3-time")
	os.system("sudo apt install python3-sys")
	os.system("sudo apt install python3-os")
	os.system("sudo apt install python3-base64")
	os.system("sudo apt install python3-time")
	os.system("sudo apt install python3-argparse")
	os.system("sudo chmod +x intconsole.js")
	os.system("cd ~")
	os.system("nano .bashrc")
	os.system("echo \"alias intconsole='python3 /path/to/intconsoleV2.py'\" >> ~/.bashrc") or os.system("sudo mv intconsoleV2.py /usr/local/bin/intconsole")
os.system("source ~/.bashrc")
	loading("İntconsole Downloading..........")
	print("""
	installed intconsole 
	using = intconsole 
	else : please command using=='run intconsole'		
	""")
	k = input("Do you command is working[Y/n]")
	
	
	if k == "y" or k == "Y":
	   	os.system("cd ~")
	   	os.system("nano .bashrc")
	   	os.system("source ~/.bashrc")
	   	os.system("echo \"alias intconsole='python3 /usr/bin/intframework/intconsoleV2.py'\" >> ~/.bashrc")
	elif k == "n" or k == "N":
		print("type intconsole to start please")	