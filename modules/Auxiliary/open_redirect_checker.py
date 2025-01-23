#!/usr/bin/env python3
import requests

def open_redirect_checker(target_url):
    """[Check for open redirect vulnerabilities]"""
    payloads = ["http://evil.com", "https://malicious.com"]
    vulnerable_urls = []

    for payload in payloads:
        url = f"{target_url}?redirect={payload}"
        response = requests.get(url)
        
        if response.url != target_url:
            print(f"Open Redirect Vulnerability Found: {url}")
            vulnerable_urls.append(url)

    if not vulnerable_urls:
        print("No open redirect vulnerabilities found.")
    
    return vulnerable_urls

# User input
target_url = input("\033[91mint4 [Enter the Target URL] > \033[0m")
open_redirect_checker(target_url)