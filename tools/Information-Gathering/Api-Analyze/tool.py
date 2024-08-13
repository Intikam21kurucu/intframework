import requests

def analyze_api(url):
    endpoints = ["/v1/secure", "/v1/admin", "/v1/user"]
    for endpoint in endpoints:
        full_url = f"{url}{endpoint}"
        response = requests.get(full_url)
        print(f"Testing {full_url}: Status Code {response.status_code}")
