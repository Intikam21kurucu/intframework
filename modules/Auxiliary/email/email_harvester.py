#!/usr/bin/env python3 
import requests
import re
import csv
from urllib.parse import urlparse

class EmailHarvester:
    """[Class for harvesting email addresses from a given URL]"""

    def __init__(self, target_url):
        """[Initialize with the target URL]"""
        self.target_url = target_url
        self.emails = []

    def fetch_content(self):
        """[Fetch the content from the target URL]"""
        try:
            print(f"Accessing {self.target_url}...")
            response = requests.get(self.target_url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.text
        except requests.RequestException as e:
            print(f"Error accessing {self.target_url}: {e}")
            return None

    def extract_emails(self, content):
        """[Extract email addresses from the HTML content]"""
        if content:
            self.emails = list(set(re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+', content)))  # Remove duplicates
            if self.emails:
                print(f"Found {len(self.emails)} unique email addresses.")
            else:
                print("No email addresses found.")
        else:
            print("No content to extract emails from.")

    def save_to_csv(self):
        """[Save the harvested emails to a CSV file]"""
        if self.emails:
            with open("harvested_emails.csv", "w", newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["Email Addresses"])  # Header
                for email in self.emails:
                    writer.writerow([email])
            print("Email addresses saved to harvested_emails.csv")
        else:
            print("No emails to save.")

    def run(self):
        """[Execute the email harvesting process]"""
        content = self.fetch_content()
        self.extract_emails(content)
        self.save_to_csv()

def is_valid_url(url):
    """[Validate the URL format]"""
    parsed_url = urlparse(url)
    return all([parsed_url.scheme, parsed_url.netloc])

if __name__ == "__main__":
    target_url = input("\033[91mint4 [Enter the Target URL to Harvest Emails] > \033[0m")
    if not is_valid_url(target_url):
        print("Invalid URL format. Please enter a valid URL including 'http://' or 'https://'.")
    else:
        harvester = EmailHarvester(target_url)
        harvester.run()