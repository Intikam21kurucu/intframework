#!/usr/bin/env python3
import requests

def header_analyzer(target_url):
    """[Analyze HTTP headers for security misconfigurations]"""
    try:
        response = requests.get(target_url)
        security_headers = [
            "Strict-Transport-Security",
            "Content-Security-Policy",
            "X-Content-Type-Options",
            "X-Frame-Options",
            "X-XSS-Protection"
        ]
        
        print("Security Headers:")
        for header in security_headers:
            if header in response.headers:
                print(f"{header}: {response.headers[header]}")
            else:
                print(f"{header}: Not Found")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# User input
target_url = input("\033[91mint4 [Enter the Target URL] > \033[0m")
if target_url.startswith("http://") or target_url.startswith("https://"):
    header_analyzer(target_url)
else:
    print("Please enter a valid URL starting with http:// or https://")