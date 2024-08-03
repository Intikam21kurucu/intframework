import requests
import argparse

def get_ip_info(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def print_ip_info(ip_info):
    if ip_info and ip_info.get('status') == 'fail':
        print(f"Error: {ip_info.get('message')}")
    elif ip_info:
        print(f"IP Address: {ip_info.get('query')}")
        print(f"City: {ip_info.get('city')}")
        print(f"Region: {ip_info.get('regionName')}")
        print(f"Country: {ip_info.get('country')}")
        print(f"Location: {ip_info.get('lat')}, {ip_info.get('lon')}")
        print(f"ISP: {ip_info.get('isp')}")
        
        # Create Google Maps URL
        maps_url = f"https://www.google.com/maps?q={ip_info.get('lat')},{ip_info.get('lon')}"
        print(f"Google Maps URL: {maps_url}")
    else:
        print("IP information could not be retrieved.")

def main():
    parser = argparse.ArgumentParser(description="Get IP information and display location on Google Maps.")
    parser.add_argument('ip_address', type=str, help="The IP address to query.")
    
    args = parser.parse_args()
    
    ip_info = get_ip_info(args.ip_address)
    print_ip_info(ip_info)

if __name__ == "__main__":
    main()