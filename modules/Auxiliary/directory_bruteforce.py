#!/usr/bin/env python3 
import requests

def directory_bruteforce(target_url, wordlist):
    """[Bruteforce directories on a target website]"""
    found_dirs = []

    with open(wordlist, 'r') as f:
        directories = f.readlines()

    for directory in directories:
        dir_path = directory.strip()
        url = target_url + "/" + dir_path
        response = requests.get(url)
        
        if response.status_code == 200:
            print(f"Found Directory: {url}")
            found_dirs.append(url)

    if not found_dirs:
        print("No directories found.")
    
    return found_dirs

# User input
target_url = input("\033[91mint4 [Enter the Target URL] > \033[0m")
wordlist_path = input("\033[91mint4 [Enter the Path to the Wordlist] > \033[0m")
directory_bruteforce(target_url, wordlist_path)