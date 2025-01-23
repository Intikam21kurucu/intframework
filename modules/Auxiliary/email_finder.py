#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

class EmailFinder:
    """[Class for finding emails on a target website]"""

    def __init__(self, target_url):
        """[Initialize with the target URL]"""
        self.target_url = target_url

    def find_emails(self):
        """[Scrape the website for email addresses]"""
        response = requests.get(self.target_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        emails = set()
        for mailto in soup.select('a[href^=mailto]'):
            emails.add(mailto.get('href').replace('mailto:', ''))
        return emails

if __name__ == "__main__":
    target_url = input("\033[91mint4 [Enter the Target URL to Find Emails] > \033[0m")
    finder = EmailFinder(target_url)
    emails = finder.find_emails()
    print(f"Found Emails: {emails}")