#!/usr/bin/env python3
import requests

def parameter_pollution_tester(target_url):
    """[Test for parameter pollution vulnerabilities]"""
    payloads = ["param=value1&param=value2", "param=value1&param=value2&other=value"]
    for payload in payloads:
        url = f"{target_url}?{payload}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Potential parameter pollution vulnerability at: {url}")
            else:
                print(f"No vulnerability found at: {url}")
        except requests.exceptions.RequestException as e:
            print(f"Error accessing {url}: {e}")

# User input
target_url = input("\033[91mint4 [Enter the Target URL for Parameter Pollution Testing] > \033[0m")
if target_url.startswith("http://") or target_url.startswith("https://"):
    parameter_pollution_tester(target_url)
else:
    print("Please enter a valid URL starting with http:// or https://")