#!/usr/bin/env python3
import requests

def session_fixation_tester(target_url):
    """[Test for session fixation vulnerabilities]"""
    session_cookie = {'sessionid': 'malicious-session-id'}
    
    # Sending request with a malicious session ID
    response = requests.get(target_url, cookies=session_cookie)
    
    if "Welcome back" in response.text:  # Adjust based on expected response
        print("Session fixation vulnerability found!")

# User input
target_url = input("\033[91mint4 [Enter the Target URL for Session Fixation Testing] > \033[0m")
session_fixation_tester(target_url)