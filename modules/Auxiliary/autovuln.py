#!/usr/bin/env python3
import requests
import json
import re

class VulnerabilityScanner:
    """[Class for scanning web applications for vulnerabilities]"""

    def __init__(self, target_url):
        """[Initialize with the target URL]"""
        self.target_url = target_url
        self.vulnerabilities = []

    def scan_sql_injection(self):
        """[Check for SQL injection vulnerabilities]"""
        payloads = ["' OR '1'='1", "' OR '1'='2"]
        for payload in payloads:
            response = requests.get(self.target_url + payload)
            if "SQL syntax" in response.text or "mysql" in response.text.lower():
                self.vulnerabilities.append(f"SQL Injection found with payload: {payload}")

    def scan_xss(self):
        """[Check for XSS vulnerabilities]"""
        payloads = ["<script>alert('XSS')</script>", "'><script>alert('XSS')</script>"]
        for payload in payloads:
            response = requests.get(self.target_url + payload)
            if payload in response.text:
                self.vulnerabilities.append(f"XSS found with payload: {payload}")

    def run_scan(self):
        """[Run all vulnerability scans]"""
        self.scan_sql_injection()
        self.scan_xss()

if __name__ == "__main__":
    target_url = input("\033[91mint4 [Enter Target URL for Vulnerability Scanning] > \033[0m")
    scanner = VulnerabilityScanner(target_url)
    scanner.run_scan()
    print(json.dumps(scanner.vulnerabilities, indent=4))