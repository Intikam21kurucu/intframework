import argparse
import requests
import bluetooth
import os

def check_vpn_status(ip):
    # Check VPN status using ipinfo.io API
    try:
        vpn_check_url = f"http://ipinfo.io/{ip}/json"
        vpn_response = requests.get(vpn_check_url)
        vpn_data = vpn_response.json()
        
        if 'org' in vpn_data and ('VPN' in vpn_data['org'] or 'Hosting' in vpn_data['org']):
            print(f"{ip} is likely connected to a VPN.")
        else:
            print(f"{ip} is likely not connected to a VPN.")
    except requests.exceptions.RequestException as e:
        print(f"Error during VPN check request: {e}")

def get_device_info(ip):
    # Get device information from HTTP headers
    try:
        url = f"http://{ip}"
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        print("HTTP Headers Retrieved:")
        print(response.headers)

        if 'User-Agent' in response.headers:
            print(f"Browser Info: {response.headers['User-Agent']}")
        if 'X-Device-Name' in response.headers:
            print(f"Device Name: {response.headers['X-Device-Name']}")
        if 'X-Device-Model' in response.headers:
            print(f"Device Model: {response.headers['X-Device-Model']}")
    except requests.exceptions.RequestException as e:
        print(f"Error during HTTP request: {e}")

def scan_bluetooth_devices():
    # Scan for Bluetooth devices nearby
    print("Scanning for Bluetooth devices...")
    devices = bluetooth.discover_devices(lookup_names=True)

    for addr, name in devices:
        print(f"Device Address: {addr}, Device Name: {name}")

def ping_test(ip):
    # Check if the device is reachable by ping
    response = os.system(f"ping -c 1 {ip}")
    
    if response == 0:
        print(f"{ip} is reachable, low probability of VPN usage.")
    else:
        print(f"{ip} is unreachable, VPN or firewall might be in use.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Device Information and VPN Checker Script")
    parser.add_argument("-i", "--ip", type=str, required=True, help="Target IP address")
    parser.add_argument("-v", "--vpn", action="store_true", help="Check if VPN is in use")
    parser.add_argument("-d", "--device", action="store_true", help="Get device information")
    parser.add_argument("-b", "--bluetooth", action="store_true", help="Scan for Bluetooth devices")
    parser.add_argument("-p", "--ping", action="store_true", help="Ping test to check reachability")
    
    args = parser.parse_args()

    print("Starting the script...\n")

    if args.vpn:
        check_vpn_status(args.ip)
    
    if args.device:
        get_device_info(args.ip)

    if args.ping:
        ping_test(args.ip)

    if args.bluetooth:
        scan_bluetooth_devices()

    print("\nScript execution completed.")