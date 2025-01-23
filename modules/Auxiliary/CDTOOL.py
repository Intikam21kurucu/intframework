#!/usr/bin/env python3
import requests

class ContentDiscoveryTool:
    """[Class for discovering hidden files and directories]"""

    def __init__(self, target_url, wordlist):
        """[Initialize with target URL and wordlist]"""
        self.target_url = target_url
        self.wordlist = wordlist

    def discover_content(self):
        """[Discover content based on the wordlist]"""
        found_paths = []
        with open(self.wordlist, 'r') as file:
            for line in file:
                path = line.strip()
                url = f"{self.target_url}/{path}"
                response = requests.get(url)
                if response.status_code == 200:
                    found_paths.append(url)
        return found_paths

if __name__ == "__main__":
    target_url = input("\033[91mint4 [Enter the Target URL for Content Discovery] > \033[0m")
    wordlist = input("\033[91mint4 [Enter the Wordlist Path] > \033[0m")
    tool = ContentDiscoveryTool(target_url, wordlist)
    discovered_content = tool.discover_content()
    print(f"Found Content: {discovered_content}")
