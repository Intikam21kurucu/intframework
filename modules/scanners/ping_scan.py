import subprocess
import argparse

def ping(host):
    result = subprocess.run(['ping', '-c', '1', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.returncode == 0

def scan_subnet(subnet, wordlist):
    print(f"Scanning subnet {subnet}...")
    with open(wordlist, 'r') as file:
        for line in file:
            ip = line.strip()
            if ping(ip):
                print(f"{ip} is up")

def main():
    parser = argparse.ArgumentParser(description='Ping scanner for a given subnet.')
    parser.add_argument('subnet', type=str, help='The subnet to scan.')
    parser.add_argument('wordlist', type=str, help='Path to the wordlist file with IP addresses.')
    args = parser.parse_args()
    
    scan_subnet(args.subnet, args.wordlist)

if __name__ == '__main__':
    main()