#!/usr/bin/env python3
import requests

def owasp_top_ten_scanner(target_url):
    """[Scan for vulnerabilities from OWASP Top Ten]"""
    vulnerabilities = {
        "A1": "Injection",
        "A2": "Broken Authentication",
        "A3": "Sensitive Data Exposure",
        "A4": "XML External Entities (XXE)",
        "A5": "Broken Access Control",
        "A6": "Security Misconfiguration",
        "A7": "Cross-Site Scripting (XSS)",
        "A8": "Insecure Deserialization",
        "A9": "Using Components with Known Vulnerabilities",
        "A10": "Insufficient Logging & Monitoring"
    }

    print("OWASP Top Ten Vulnerabilities:")
    for key, value in vulnerabilities.items():
        print(f"{key}: {value}")

# User input
target_url = input("\033[91mint4 [Enter the Target URL for OWASP Testing] > \033[0m")
owasp_top_ten_scanner(target_url)