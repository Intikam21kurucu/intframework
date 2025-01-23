#!/usr/bin/env python3
import requests

class WebFormScanner:
    """[Class for scanning web forms for vulnerabilities]"""

    def __init__(self, target_url):
        """[Initialize with the target URL]"""
        self.target_url = target_url

    def scan_form(self):
        """[Scan the web form for common vulnerabilities]"""
        payloads = ["<script>alert(1)</script>", "' OR '1'='1' --"]
        for payload in payloads:
            response = requests.post(self.target_url, data={'input': payload})
            if "error" not in response.text.lower():
                print(f"Potential vulnerability found with payload: {payload}")

if __name__ == "__main__":
    target_url = input("\033[91mint4 [Enter the Target Form URL] > \033[0m")
    scanner = WebFormScanner(target_url)
    scanner.scan_form()