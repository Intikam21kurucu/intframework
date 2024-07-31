import dns.resolver
import argparse

def scan_dns(domain):
    print(f"Scanning DNS records for {domain}...")
    
    try:
        # A Records
        a_records = dns.resolver.resolve(domain, 'A')
        print("A Records:")
        for rdata in a_records:
            print(f"IP Address: {rdata.address}")
    except dns.resolver.NoAnswer:
        print("No A records found.")

    try:
        # MX Records
        mx_records = dns.resolver.resolve(domain, 'MX')
        print("MX Records:")
        for rdata in mx_records:
            print(f"MX Record: {rdata.exchange} Preference: {rdata.preference}")
    except dns.resolver.NoAnswer:
        print("No MX records found.")

def main():
    parser = argparse.ArgumentParser(description='Scan DNS records for a given domain.')
    parser.add_argument('domain', type=str, help='The domain to scan.')
    args = parser.parse_args()
    
    scan_dns(args.domain)

if __name__ == '__main__':
    main()