import requests

def get_robots_txt(url):
    response = requests.get(url + "/robots.txt")
    print(f"Robots.txt for {url}:")
    print(response.text)