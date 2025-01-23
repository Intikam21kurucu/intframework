#!/usr/bin/env python3
import requests

def csp_checker(target_url):
    """[Check if the target URL has a Content Security Policy]"""
    response = requests.get(target_url)
    csp_header = response.headers.get('Content-Security-Policy')

    if csp_header:
        print(f"CSP header found: {csp_header}")
    else:
        print("No Content Security Policy found, vulnerable to various attacks.")

# User input
target_url = input("\033[91mint4 [Enter the Target URL for CSP Checking] > \033[0m")
csp_checker(target_url)