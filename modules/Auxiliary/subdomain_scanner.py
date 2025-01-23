#!/usr/bin/env python3
import requests

def subdomain_scanner(target_domain, subdomains_file):
    """[Scan for subdomains of a target domain]"""
    found_subdomains = []

    with open(subdomains_file, 'r') as f:
        subdomains = f.readlines()

    for subdomain in subdomains:
        subdomain = subdomain.strip()
        url = f"http://{subdomain}.{target_domain}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Found Subdomain: {url}")
                found_subdomains.append(url)
        except requests.exceptions.RequestException:
            continue

    if not found_subdomains:
        print("No subdomains found.")
    
    return found_subdomains

# User input
target_domain = input("\033[91mint4 [Enter the Target Domain] > \033[0m")
subdomains_file = input("\033[91mint4 [Enter the Path to the Subdomains File] > \033[0m")
subdomain_scanner(target_domain, subdomains_file)