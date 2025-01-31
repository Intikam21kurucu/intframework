#!/usr/bin/env python3 
import requests

def cache_poisoning_tester(target_url):
    """[Test for cache poisoning vulnerabilities]"""
    payload = {'header': 'Cache-Control: no-cache'}
    response = requests.get(target_url, headers=payload)
    if "cached" in response.text:
        print("Cache poisoning vulnerability found.")

# User input
target_url = input("\033[91mint4 [Enter the Target URL for Cache Poisoning Testing] > \033[0m")
cache_poisoning_tester(target_url)