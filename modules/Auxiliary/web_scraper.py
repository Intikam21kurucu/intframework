#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import threading
import json
import os
import hashlib

class WebScraper:
    """[Class for scraping web pages with caching]"""

    def __init__(self, urls):
        """[Initialize with a list of URLs]"""
        self.urls = urls
        self.results = {}
        self.lock = threading.Lock()
        self.cache_dir = 'cache/'

        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)

    def fetch_url(self, url):
        """[Fetch and cache a URL]"""
        cache_file = self.get_cache_file(url)
        if os.path.exists(cache_file):
            with open(cache_file, 'r') as file:
                self.lock.acquire()
                self.results[url] = json.load(file)
                self.lock.release()
            return

        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.title.string if soup.title else 'No Title'
            data = {
                'url': url,
                'title': title,
                'status': response.status_code,
            }
            with open(cache_file, 'w') as file:
                json.dump(data, file)
            self.lock.acquire()
            self.results[url] = data
            self.lock.release()

    def get_cache_file(self, url):
        """[Generate a cache filename based on the URL]"""
        url_hash = hashlib.md5(url.encode()).hexdigest()
        return os.path.join(self.cache_dir, f'{url_hash}.json')

    def scrape(self):
        """[Start the scraping process]"""
        threads = []
        for url in self.urls:
            thread = threading.Thread(target=self.fetch_url, args=(url,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

if __name__ == "__main__":
    urls = [
        input("\033[91mint4 [Enter URL to Scrape] > \033[0m"),
        # Daha fazla URL eklenebilir
    ]
    scraper = WebScraper(urls)
    scraper.scrape()
    print(json.dumps(scraper.results, indent=4))