#!/usr/bin/env python3
import requests
import threading
import argparse
import time
import random
import os
from queue import Queue

class DirScanner:
    def __init__(self, target_url, wordlist, threads, output_file, proxies, user_agents, timeout, retries, status_filter):
        self.target_url = target_url.rstrip("/")
        self.wordlist = wordlist
        self.threads = threads
        self.output_file = output_file
        self.proxies = proxies
        self.timeout = timeout
        self.retries = retries
        self.queue = Queue()
        self.user_agents = user_agents.split(",")
        self.status_filter = [int(x) for x in status_filter.split(",")] if status_filter else []
        self.results = []

    def load_wordlist(self):
        """Load directories from the wordlist file into the queue."""
        with open(self.wordlist, "r") as file:
            for line in file:
                self.queue.put(line.strip())

    def request_with_retries(self, url, headers):
        """Send request with retry logic."""
        for _ in range(self.retries):
            try:
                response = requests.get(url, headers=headers, proxies=self.proxies, timeout=self.timeout)
                return response
            except requests.exceptions.RequestException:
                time.sleep(1)
        return None

    def scan_directory(self):
        """Scan directories from the queue."""
        while not self.queue.empty():
            directory = self.queue.get()
            url = f"{self.target_url}/{directory}"
            headers = {"User-Agent": random.choice(self.user_agents)}

            response = self.request_with_retries(url, headers)
            if response:
                status_code = response.status_code
                if not self.status_filter or status_code in self.status_filter:
                    color = "\033[92m" if status_code == 200 else "\033[93m" if status_code == 403 else "\033[91m"
                    result = f"{color}[{status_code}] Found: {url} - {headers['User-Agent']}\033[0m"
                    print(result)
                    self.results.append(f"[{status_code}] {url}")

    def save_results(self):
        """Save results to a file if specified."""
        if self.output_file and self.results:
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            output_path = f"{self.output_file}-{timestamp}.txt"
            with open(output_path, "w") as file:
                file.write("\n".join(self.results))
            print(f"\n\033[94m[*] Results saved to {output_path}\033[0m")

    def run(self):
        """Start scanning with multithreading."""
        print(f"\n\033[96m[*] Starting scan on {self.target_url}...\033[0m")
        print(f"   📌 Threads: {self.threads}")
        print(f"   📌 User-Agents: {len(self.user_agents)} available")
        print(f"   📌 Wordlist: {self.wordlist}")
        print(f"   📌 Proxy: {'Enabled' if self.proxies else 'Disabled'}")
        print(f"   📌 Timeout: {self.timeout} sec")
        print(f"   📌 Retries: {self.retries}")
        print(f"   📌 Status Code Filter: {self.status_filter if self.status_filter else 'All'}\n")
        
        start_time = time.time()
        self.load_wordlist()
        
        threads = []
        for _ in range(self.threads):
            t = threading.Thread(target=self.scan_directory)
            t.start()
            threads.append(t)

        for t in threads:
            t.join()
        
        self.save_results()
        elapsed_time = time.time() - start_time
        print(f"\n\033[96m[*] Scan completed in {elapsed_time:.2f} seconds.\033[0m")

# Argument parser
def parse_args():
    parser = argparse.ArgumentParser(description="Advanced DirScanner with User-Agent Rotation & Status Filtering")
    parser.add_argument("-u", "--url", required=True, help="Target URL")
    
    default_wordlist = os.path.join(os.path.dirname(__file__), "data/defaultdir.txt")
    parser.add_argument("-w", "--wordlist", default=default_wordlist, help=f"Path to wordlist file (default: {default_wordlist})")

    parser.add_argument("-t", "--threads", type=int, default=10, help="Number of threads (default: 10)")
    parser.add_argument("-o", "--output", help="Save results to a file (timestamp added)")
    parser.add_argument("-p", "--proxy", help="Proxy (e.g., http://127.0.0.1:8080)")
    
    default_ua = "Mozilla/5.0,Googlebot/2.1,Opera/9.80"
    parser.add_argument("-ua", "--user-agents", default=default_ua, help=f"Comma-separated list of User-Agents (default: {default_ua})")

    parser.add_argument("--timeout", type=int, default=5, help="Request timeout in seconds (default: 5)")
    parser.add_argument("--retries", type=int, default=3, help="Number of retries if request fails (default: 3)")
    parser.add_argument("--status", help="Comma-separated list of status codes to display (e.g., 200,403,500)")

    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    
    proxies = {"http": args.proxy, "https": args.proxy} if args.proxy else None
    
    scanner = DirScanner(
        target_url=args.url,
        wordlist=args.wordlist,
        threads=args.threads,
        output_file=args.output,
        proxies=proxies,
        user_agents=args.user_agents,
        timeout=args.timeout,
        retries=args.retries,
        status_filter=args.status
    )
    
    scanner.run()