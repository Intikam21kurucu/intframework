#!/usr/bin/env python3
import requests

class ReverseIPLookupTool:
    """[Class for performing reverse IP lookup]"""

    def __init__(self, target_ip):
        """[Initialize with the target IP]"""
        self.target_ip = target_ip

    def reverse_lookup(self):
        """[Perform reverse IP lookup to find hosted domains]"""
        response = requests.get(f"https://api.hackertarget.com/reverseiplookup/?q={self.target_ip}")
        return response.text

if __name__ == "__main__":
    target_ip = input("\033[91mint4 [Enter the Target IP for Reverse Lookup] > \033[0m")
    lookup_tool = ReverseIPLookupTool(target_ip)
    domains = lookup_tool.reverse_lookup()
    print(f"Hosted Domains:\n{domains}")