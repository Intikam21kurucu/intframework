#!/usr/bin/env python3
import requests

def admin_finder(target_url):
    """[Find admin panels on a target website]"""
    admin_paths = [
        "/admin",
        "/admin/login",
        "/administrator",
        "/admin.php",
        "/login.php",
        "/wp-admin",
        "/user/login",
        "/controlpanel",
        "/login",
        "/admin_area",
    ]
    
    found_admins = []
    
    for path in admin_paths:
        url = target_url + path
        response = requests.get(url)

        if response.status_code == 200:
            print(f"Found: {url}")
            found_admins.append(url)
    
    if not found_admins:
        print("No admin panel found.")
    
    return found_admins

# User input
target_url = input("\033[91mint4 [Enter the Target URL] > \033[0m")
admin_finder(target_url)
