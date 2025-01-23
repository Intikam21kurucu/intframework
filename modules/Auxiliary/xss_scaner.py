#!/usr/bin/env python3 
import requests

def xss_tester(target_url):
    """[Test for XSS vulnerabilities using common payloads]"""
    xss_payloads = ["<script>alert('XSS')</script>", "';alert(1);//", "<img src=x onerror=alert(1)>"]
    
    for payload in xss_payloads:
        url = f"{target_url}?input={payload}"
        try:
            response = requests.get(url)
            if payload in response.text:
                print(f"Possible XSS vulnerability found at: {url}")
            else:
                print(f"No vulnerability found with payload at: {url}")
        except requests.exceptions.RequestException as e:
            print(f"Error accessing {url}: {e}")

# User input
target_url = input("\033[91mint4 [Enter the Target URL] > \033[0m")
if target_url.startswith("http://") or target_url.startswith("https://"):
    xss_tester(target_url)
else:
    print("Please enter a valid URL starting with http:// or https://")