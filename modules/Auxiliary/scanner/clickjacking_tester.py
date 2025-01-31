#!/usr/bin/env python3
import requests

def clickjacking_tester(target_url):
    """[Check if the target URL is vulnerable to clickjacking]"""
    response = requests.get(target_url)
    if "X-Frame-Options" not in response.headers:
        print(f"{target_url} is vulnerable to clickjacking.")
    else:
        print(f"{target_url} is protected against clickjacking.")

# User input
target_url = input("\033[91mint4 [Enter the Target URL for Clickjacking Testing] > \033[0m")
clickjacking_tester(target_url)