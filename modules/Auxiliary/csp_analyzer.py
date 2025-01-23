#!/usr/bin/env python3
import requests

def csp_analyzer(target_url):
    """[Analyze Content Security Policy for weaknesses]"""
    response = requests.get(target_url)
    csp_header = response.headers.get('Content-Security-Policy', None)

    if csp_header:
        print("CSP Header Found:")
        print(csp_header)
    else:
        print("No CSP header found. Potentially insecure.")

# User input
target_url = input("\033[91mint4 [Enter the Target URL for CSP Analysis] > \033[0m")
csp_analyzer(target_url)