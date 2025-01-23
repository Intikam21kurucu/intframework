#!/usr/bin/env python3
import requests

def security_misconfiguration_checker(target_url):
    """[Check for common security misconfigurations]"""
    response = requests.get(target_url)
    if "robots.txt" in response.text:
        print("robots.txt file found, check for sensitive data exposure.")

    # Check for default admin pages
    default_admins = ['/admin', '/admin.php', '/login', '/administrator']
    for admin in default_admins:
        admin_url = target_url + admin
        admin_response = requests.get(admin_url)
        if admin_response.status_code == 200:
            print(f"Default admin page found: {admin_url}")

# User input
target_url = input("\033[91mint4 [Enter the Target URL for Security Misconfiguration Checking] > \033[0m")
security_misconfiguration_checker(target_url)