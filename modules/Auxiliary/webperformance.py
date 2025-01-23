#!/usr/bin/env python3
import requests
import time

class WebsitePerformanceAnalyzer:
    """[Class for analyzing the performance of a target website]"""

    def __init__(self, target_url):
        """[Initialize with the target URL]"""
        self.target_url = target_url

    def analyze_performance(self):
        """[Measure response time and check status code]"""
        start_time = time.time()
        response = requests.get(self.target_url)
        response_time = time.time() - start_time
        return response.status_code, response_time

if __name__ == "__main__":
    target_url = input("\033[91mint4 [Enter the Target URL for Performance Analysis] > \033[0m")
    analyzer = WebsitePerformanceAnalyzer(target_url)
    status_code, response_time = analyzer.analyze_performance()
    print(f"Status Code: {status_code}, Response Time: {response_time:.2f} seconds")