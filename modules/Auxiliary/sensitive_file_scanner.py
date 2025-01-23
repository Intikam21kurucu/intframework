#!/usr/bin/env python3
import requests

def sensitive_file_scanner(target_url):
    """[Scan for sensitive files and directories]"""
    sensitive_files = [
        "/.env", "/config.php", "/backup.zip", "/admin/config.php", 
        "/db_backup.sql", "/wp-config.php"
    ]
    
    for file in sensitive_files:
        url = f"{target_url}{file}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Sensitive file found at: {url}")
            else:
                print(f"No sensitive file at: {url}")
        except requests.exceptions.RequestException as e:
            print(f"Error accessing {url}: {e}")

# User input
target_url = input("\033[91mint4 [Enter the Target URL] > \033[0m")
if target_url.startswith("http://") or target_url.startswith("https://"):
    sensitive_file_scanner(target_url)
else:
    print("Please enter a valid URL starting with http:// or https://")