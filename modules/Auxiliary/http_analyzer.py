#!/usr/bin/env python3
import requests

def http_analyzer(target_url):
    """[Analyze HTTP headers of the target URL]"""
    try:
        response = requests.get(target_url)
        print(f"HTTP Status Code: {response.status_code}")
        print("HTTP Headers:")
        for header, value in response.headers.items():
            print(f"{header}: {value}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# User input
target_url = input("\033[91mint4 [Enter the Target URL] > \033[0m")
http_analyzer(target_url)