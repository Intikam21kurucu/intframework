#!/usr/bin/env python3
import requests

def security_misconfiguration_scanner(target_url):
    """[Scan for common security misconfigurations]"""
    response = requests.get(target_url)
    misconfigurations = [
        "development",
        "debug",
        "config"
    ]

    for misconfiguration in misconfigurations:
        if misconfiguration in response.text.lower():
            print(f"Potential security misconfiguration found: {misconfiguration}")

# User input
target_url = input("\033[91mint4 [Enter the Target URL for Security Misconfiguration Checking] > \033[0m")
security_misconfiguration_scanner(target_url)