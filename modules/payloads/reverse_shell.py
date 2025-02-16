#!/usr/bin/env python3

import sys
import os
from colorama import *

init(autoreset=True)

def print_do(message, color_continue=True):
        print(f"{Fore.GREEN}[+] {message}")
        if color_continue == False:
                print(f"{Fore.GREEN}[+]{Fore.RESET} {message}")
def print_warning(message, color_continue=True):
        print(f"{Fore.RED}[!] {message}")
        if color_continue == False:
                print(f"{Fore.RED}[!]{Fore.RESET} {message}")
def print_sys(message, color_continue=True):
        print(f"{Fore.BLUE}[~] {message}")
        if color_continue == False:
                print(f"{Fore.BLUE}[~]{Fore.RESET} {message}")
port = sys.argv[2]
host = sys.argv[1]

if port:
        print("""

 ____  ____  _  _  ____  ____  ____  ____        ____  _  _  ____  __    __   
(  _ \(  __)/ )( \(  __)(  _ \/ ___)(  __)      / ___)/ )( \(  __)(  )  (  )  
 )   / ) _) \ \/ / ) _)  )   /\___ \ ) _)  ____ \___ \) __ ( ) _) / (_/\/ (_/\
(__\_)(____) \__/ (____)(__\_)(____/(____)(____)(____/\_)(_/(____)\____/\____/
           by intframework
        """)
        print_do("starting netcat")
        try:
                print_sys(f"listening on {host}:{port}")
                os.system(f"nc -lvnp {port}")
        except:
                print_warning("Error please check netcat is installed and try again.")
