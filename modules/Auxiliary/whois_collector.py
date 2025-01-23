#!/usr/bin/env python3
import whois

class WhoisInfoCollector:
    """[Class for collecting Whois information about a domain]"""

    def __init__(self, target_domain):
        """[Initialize with the target domain]"""
        self.target_domain = target_domain

    def collect_info(self):
        """[Collect Whois information]"""
        domain_info = whois.whois(self.target_domain)
        return domain_info

if __name__ == "__main__":
    target_domain = input("\033[91mint4 [Enter the Target Domain for Whois Lookup] > \033[0m")
    collector = WhoisInfoCollector(target_domain)
    info = collector.collect_info()
    print(f"Whois Information:\n{info}")