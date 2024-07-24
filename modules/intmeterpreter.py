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
import argparse
import os
import shutil

# Create payloads directory if it doesn't exist
if not os.path.exists("payloads"):
    os.makedirs("payloads")

def create_payload(payload_name):
    payload_path = f"payloads/{payload_name}"
    if os.path.exists(payload_path):
        print(f"Payload '{payload_name}' already exists.")
    else:
        os.makedirs(payload_path)
        print(f"Payload '{payload_name}' created.")

def add_code_to_payload(payload_name, command_name, code_file):
    payload_path = f"payloads/{payload_name}"
    if os.path.exists(payload_path):
        if os.path.isfile(code_file):
            command_path = os.path.join(payload_path, f"{command_name}.py")
            shutil.copy(code_file, command_path)
            print(f"Command '{command_name}.py' added to payload '{payload_name}'.")
        else:
            print(f"Code file '{code_file}' not found.")
    else:
        print(f"Payload '{payload_name}' not found.")

def show_payload(payload_name):
    payload_path = f"payloads/{payload_name}"
    if os.path.exists(payload_path):
        commands = os.listdir(payload_path)
        if commands:
            print(f"Commands in payload '{payload_name}':")
            for command in commands:
                print(f"- {command}")
        else:
            print(f"No command files in payload '{payload_name}'.")
    else:
        print(f"Payload '{payload_name}' not found.")

def check_network():
    import socket
    try:
        # Attempt to connect to Google's DNS server
        socket.create_connection(("8.8.8.8", 53))
        return True
    except OSError:
        return False

def main():
    parser = argparse.ArgumentParser(description="Intmeterpreter tool")

    subparsers = parser.add_subparsers(dest='command')

    # Command to create a payload
    create_parser = subparsers.add_parser('-p', help="Create payload")
    create_parser.add_argument('payload_name', help="Payload name")

    # Command to add code to a payload
    code_parser = subparsers.add_parser('-c', help="Add code to payload")
    code_parser.add_argument('payload_name', help="Payload name")
    code_parser.add_argument('command_name', help="Command name")
    code_parser.add_argument('code_file', help="Code file to be added")
    parser.add_argument("start", nargs='?', help="meterpreter Starter")
    # Command to show payload contents
    show_parser = subparsers.add_parser('-pe', help="Show payload contents")
    show_parser.add_argument('payload_name', help="Payload name")

    args = parser.parse_args()

    if check_network():
        print("Network connection is available.")
    else:
        print("No network connection.")
    if args.start:
    	os.system("pyhon3 meterpreter_user.py")
    if args.command == '-p':
        create_payload(args.payload_name)
    elif args.command == '-c':
        add_code_to_payload(args.payload_name, args.command_name, args.code_file)
    elif args.command == '-pe':
        show_payload(args.payload_name)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()

