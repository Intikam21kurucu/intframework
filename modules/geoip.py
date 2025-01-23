#!/usr/bin/env python3
import os
import sys
import time
import socket
import urllib.request
from termcolor import colored, cprint

def geolocate():
    CORE_STRING = colored("[intbase]", 'red')

    ip_addr = input(CORE_STRING + " int4 (IP Address) > ")
    REVERSE_SOCKET_DNS = socket.getfqdn(ip_addr)

    try:
        # Using urllib to make the API request
        geoip = urllib.request.urlopen('http://api.hackertarget.com/geoip/?q=' + ip_addr).read().decode('utf-8')
        
        cprint("[*] Authenticating API...", 'blue')
        time.sleep(1)
        cprint("[!] Gathering Information...", 'blue')
        time.sleep(1)
        print("\tIP Information:\n\n")
        print(geoip)
        
    except Exception as e:
        cprint(f"Error: {str(e)}", 'red')

geolocate()