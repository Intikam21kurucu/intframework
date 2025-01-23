#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import json
import re
import urllib.parse

class SocialMediaProfileScraper:
    """[Class for scraping social media profile information]"""

    def __init__(self, username):
        """[Initialize with the username]"""
        self.username = username
        self.base_url = f"https://www.instagram.com/{username}/"

    def scrape_profile(self):
        """[Scrape profile data including followers, following, and posts]"""
        response = requests.get(self.base_url)
        if response.status_code != 200:
            return "Profile not found."
        
        soup = BeautifulSoup(response.text, 'html.parser')
        scripts = soup.find_all('script', type='text/javascript')
        for script in scripts:
            if 'window._sharedData =' in script.text:
                json_data = re.findall(r'window\._sharedData = (.+);</script>', script.text)[0]
                profile_data = json.loads(json_data)
                user_data = profile_data['entry_data']['ProfilePage'][0]['graphql']['user']
                return {
                    "Username": user_data['username'],
                    "Followers": user_data['edge_followed_by']['count'],
                    "Following": user_data['edge_follow']['count'],
                    "Posts": user_data['edge_owner_to_timeline_media']['count'],
                    "Biography": user_data['biography']
                }

if __name__ == "__main__":
    username = input("\033[91mint4 [Enter the Social Media Username] > \033[0m")
    scraper = SocialMediaProfileScraper(username)
    profile_info = scraper.scrape_profile()
    print(json.dumps(profile_info, indent=4))