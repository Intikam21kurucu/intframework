#!/usr/bin/env python3
import requests

def web_app_fingerprinter(target_url):
    """[Fingerprint the web application by analyzing response headers]"""
    response = requests.get(target_url)
    server = response.headers.get('Server')
    x_powered_by = response.headers.get('X-Powered-By')

    if server:
        print(f"Web server: {server}")
    if x_powered_by:
        print(f"Powered by: {x_powered_by}")

# User input
target_url = input("\033[91mint4 [Enter the Target URL for Web Application Fingerprinting] > \033[0m")
web_app_fingerprinter(target_url)