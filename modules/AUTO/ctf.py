from colorama import *
import colorama
import sys
import os
import time as t
init(autoreset=True)
def logo():
  print("""
  __   _  _  ____  __                  ___  ____  ____ 
 / _\ / )( \(_  _)/  \                / __)(_  _)(  __)
/    \) \/ (  )( (  O )              ( (__   )(   ) _) 
\_/\_/\____/ (__) \__/                \___) (__) (__)  
""")
  print("Ａｕｔｏｃｔｆ | ᴀᴜᴛᴏᴄᴛғ by 𝙞𝙣𝙩𝙛𝙧𝙖𝙢𝙚𝙬𝙤𝙧𝙠")
  print()
  print("")
def portlogo():
	print("""

▗▄▄▄▖▗▖  ▗▖▗▄▄▄▖▗▄▄▄▖▗▄▄▖     ▗▄▄▖  ▗▄▖ ▗▄▄▖▗▄▄▄▖
▐▌   ▐▛▚▖▐▌  █  ▐▌   ▐▌ ▐▌    ▐▌ ▐▌▐▌ ▐▌▐▌ ▐▌ █  
▐▛▀▀▘▐▌ ▝▜▌  █  ▐▛▀▀▘▐▛▀▚▖    ▐▛▀▘ ▐▌ ▐▌▐▛▀▚▖ █  
▐▙▄▄▖▐▌  ▐▌  █  ▐▙▄▄▖▐▌ ▐▌    ▐▌   ▝▚▄▞▘▐▌ ▐▌ █  
	""")
def __user__():
	while True:
		ip = input(f"𝗶𝗻𝘁4 module({Fore.RED}ᴀᴜᴛᴏᴄᴛғ{Fore.RESET}) [Enter İp] >")
		if ip is  None or ip == "" or ip == " ":
			print("please Enter ip!")
			t.sleep(0.2643)
		else:
			break 
	portlogo()
	os.system("nmap {ip}")
	port = input("Enter ports(if not ports exit) >")
	nm = "nmap"
	prt = input("Enter local or remote >")
	if prt == "local":
		nm += " -pn"
	else:
		pass
	os.system(f"{nm} -p {port} -sV -oN VersionScan {ip}")
	s = input("try ftp? [y/n]")
	if s == "y" or "Y":
		os.system("ftp {ip}")
	else:
		pass
	print("completed try use intframework::modules::connector::tcp_connector and run <remote ip>")
	exit()
	
if __name__ == "__main__":
	logo()
	__user__()