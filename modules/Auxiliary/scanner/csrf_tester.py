#!/usr/bin/env python3

import requests

def csrf_vulnerability_tester(target_url):
    """[Test for CSRF vulnerabilities by sending a fake request]"""
    payload = {'data': 'test'}
    try:
        response = requests.post(target_url, data=payload)
        if response.status_code == 200:
            print(f"CSRF vulnerability potential at: {target_url}")
        else:
            print(f"No CSRF vulnerability found at: {target_url}")
    except requests.exceptions.RequestException as e:
        print(f"Error accessing {target_url}: {e}")

# User input
target_url = input("\033[91mint4 [Enter the Target URL] > \033[0m")
if target_url.startswith("http://") or target_url.startswith("https://"):
    csrf_vulnerability_tester(target_url)
else:
    print("Please enter a valid URL starting with http:// or https://")