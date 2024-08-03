import requests
import argparse
from datetime import datetime

def get_ip_info(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def log_ip_info(ip_info, log_file):
    with open(log_file, 'a') as file:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if ip_info and ip_info.get('status') == 'fail':
            file.write(f"{timestamp} - Error: {ip_info.get('message')}\n")
        elif ip_info:
            log_entry = (
                f"{timestamp} - IP Address: {ip_info.get('query')}, "
                f"City: {ip_info.get('city')}, "
                f"Region: {ip_info.get('regionName')}, "
                f"Country: {ip_info.get('country')}, "
                f"Location: {ip_info.get('lat')}, {ip_info.get('lon')}, "
                f"ISP: {ip_info.get('isp')}\n"
            )
            file.write(log_entry)
        else:
            file.write(f"{timestamp} - IP information could not be retrieved.\n")

def main():
    parser = argparse.ArgumentParser(description="Simple SIEM tool to log IP information.")
    parser.add_argument('ip_address', type=str, help="The IP address to query.")
    parser.add_argument('log_file', type=str, help="The file to write log entries to.")
    
    args = parser.parse_args()
    
    ip_info = get_ip_info(args.ip_address)
    log_ip_info(ip_info, args.log_file)

if __name__ == "__main__":
    main()