#!/usr/bin/env python3
import requests
import re

def robots_txt_scanner(target_url):
    """[Scan for sensitive information in robots.txt and analyze directives]"""
    robots_url = f"{target_url}/robots.txt"
    
    try:
        response = requests.get(robots_url)
        
        if response.status_code == 200:
            print("Contents of robots.txt:")
            print(response.text)
            analyze_robots_directives(response.text)
        else:
            print("robots.txt not found.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def analyze_robots_directives(robots_content):
    """[Analyze the directives in the robots.txt for potential vulnerabilities]"""
    disallowed_paths = re.findall(r'Disallow:\s*(.*)', robots_content, re.IGNORECASE)

    if disallowed_paths:
        print("\nPotentially Disallowed Paths:")
        for path in disallowed_paths:
            if path:
                print(f"Disallowed Path: {path.strip()}")
                print(f"Try accessing: {path.strip()} at [Target URL + {path.strip()}]")
    else:
        print("No disallowed paths found in robots.txt.")

# User input
target_url = input("\033[91mint4 [Enter the Target URL] > \033[0m")
if target_url.startswith("http://") or target_url.startswith("https://"):
    robots_txt_scanner(target_url)
else:
    print("Please enter a valid URL starting with http:// or https://")