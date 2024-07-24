#!/bin/bash

import subprocess
import argparse
import json
import os
import requests
from requests.exceptions import RequestException

# Configuration file path
CONFIG_FILE = 'config.json'
IP_SERVICE_URL = 'https://api.ipify.org?format=json'


def get_public_ip():
    try:
        response = requests.get(IP_SERVICE_URL)
        response.raise_for_status()
        return response.json()['ip']
    except RequestException as e:
        print(f"Error getting public IP: {e}")
        return None

def load_config():
    if not os.path.exists(CONFIG_FILE):
        return {}
    
    with open(CONFIG_FILE, 'r') as file:
        try:
            config = json.load(file)
        except json.JSONDecodeError as e:
            print(f"Error decoding config file: {e}")
            return {}
    
    return config

def save_config(config):
    try:
        with open(CONFIG_FILE, 'w') as file:
            json.dump(config, file, indent=4)
    except IOError as e:
        print(f"Error saving config file: {e}")

def take_photo(ip, port):
    print(f"Taking photo from camera at {ip}:{port}")
    try:
        result = subprocess.run(
            ["ssh", f"user@{ip}", "fswebcam -r 1280x720 --jpeg 85 -D 1 /tmp/webcam.jpg"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        with open("camera_output.txt", "w") as f:
            f.write(result.stdout)
        print(f"Photo taken successfully. Output saved to 'camera_output.txt'.")
    except subprocess.CalledProcessError as e:
        with open("camera_error.txt", "w") as f:
            f.write(e.stderr)
        print(f"Error taking photo: {e}")

def take_screen_photo(ip, port):
    print(f"Taking screen photo from {ip}:{port}")
    try:
        result = subprocess.run(
            ["ssh", f"user@{ip}", "scrot /tmp/screenshot.png"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        with open("screen_output.txt", "w") as f:
            f.write(result.stdout)
        print(f"Screen photo taken successfully. Output saved to 'screen_output.txt'.")
    except subprocess.CalledProcessError as e:
        with open("screen_error.txt", "w") as f:
            f.write(e.stderr)
        print(f"Error taking screen photo: {e}")

def main():
    print("""
	                    ___.-------.___
                _.-' ___.--;--.___ `-._
             .-' _.-'  /  .+.  \  `-._ `-.
           .' .-'      |-|-o-|-|      `-. `.
          (_ <O__      \  `+'  /      __O> _)
            `--._``-..__`._|_.'__..-''_.--'
                  ``--._________.--''
██╗███╗ ██╗████████╗ ██████╗ █████╗ ███╗ ███ ╗
██║████╗ ██║╚══██╔══╝██╔════╝██╔══██╗████ ╗ ████║
██║██╔██╗ ██║ ██║ ██║ ███████║██╔████╔██║
██║██║╚██╗██║ ██║ ██║ ██╔══██║██║╚██╔╝██║
██║██║ ╚████║ ██║ ╚██████╗██║ ██║██║ ╚═╝ ██║
╚═╝╚═╝ ╚═══╝ ╚═╝ ╚═════╝╚═╝ ╚═╝╚═╝ ╚═╝
                                                
	""")
    parser = argparse.ArgumentParser(description='intweb')
    parser.add_argument('-ip', '--ipv4', type=str, help='Specify the IP address')
    parser.add_argument('-p', '--port', type=int, required=True, help='Specify the port number')
    parser.add_argument('-c', '--camera-photo', action='store_true', help='Take a photo from the camera')
    parser.add_argument('-s', '--screen-photo', action='store_true', help='Take a screen photo')
    parser.add_argument('--uip', '--use-public-ip', action='store_true', help='Use the public IP address')

    args = parser.parse_args()

    if args.uip:
        public_ip = get_public_ip()
        if public_ip:
            args.ipv4 = public_ip
        else:
            print("Could not retrieve public IP address.")
            return

    config = load_config()

    if args.ipv4:
        config['ipv4'] = args.ipv4
        save_config(config)

    ip = config.get('ipv4')
    port = args.port

    if not ip:
        print("IP address must be specified either via command line or in the configuration file.")
        return

    if args.camera_photo:
        take_photo(ip, port)
    elif args.screen_photo:
        take_screen_photo(ip, port)
    else:
        print("No action specified. Use -c to take a camera photo or -s to take a screen photo.")

if __name__ == '__main__':
    main()