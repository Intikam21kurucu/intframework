#!/usr/bin/env python3
import dns.resolver
import requests
import json
import concurrent.futures

class AdvancedDNSEnumerator:
    """[Class for advanced DNS enumeration]"""

    def __init__(self, target_domain):
        """[Initialize with the target domain]"""
        self.target_domain = target_domain
        self.dns_records = {}

    def fetch_dns_record(self, record_type):
        """[Fetch a specific DNS record type]"""
        try:
            answers = dns.resolver.resolve(self.target_domain, record_type)
            self.dns_records[record_type] = [str(answer) for answer in answers]
        except Exception as e:
            self.dns_records[record_type] = f"Error: {str(e)}"

    def enumerate_dns(self):
        """[Enumerate various DNS records]"""
        record_types = ['A', 'AAAA', 'CNAME', 'MX', 'TXT']
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(self.fetch_dns_record, record_types)

if __name__ == "__main__":
    target_domain = input("\033[91mint4 [Enter Target Domain for DNS Enumeration] > \033[0m")
    enumerator = AdvancedDNSEnumerator(target_domain)
    enumerator.enumerate_dns()
    print(json.dumps(enumerator.dns_records, indent=4))
