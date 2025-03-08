#!/usr/bin/env python3
# Title: WiFi SSID or MAC address lookup tool.
import os
import re
import json
import argparse
import requests
from datetime import date
from base64 import b64encode
from terminaltables import SingleTable
from dateutil.relativedelta import relativedelta
from pygments import highlight, lexers, formatters

# Terminal renkleri
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"

class GeoWifi:
    def __init__(self, ssid=None, mac=None, country="PH", last_update=6, debug=False):
        self.ssid = ssid
        self.mac = mac
        self.country = country
        self.last_update = last_update
        self.debug = debug

        self.api_name = os.getenv('WIGLE_API_NAME')
        self.api_key = os.getenv('WIGLE_API_TOKEN')
        self.auth_headers = {
            'Authorization': 'Basic ' + b64encode(f"{self.api_name}:{self.api_key}".encode()).decode(),
            'Accept': 'application/json'
        }

    def run(self):
        print(f"\n{YELLOW}[+] Searching for target...{RESET}")

        if not self.api_name or not self.api_key:
            print(f"{RED}[-] API credentials are missing!{RESET}")
            return
        
        if self.ssid:
            url = self._request_wifi_bssid(self.ssid)
        elif self.mac:
            url = self._request_wifi_mac(self.mac)
        else:
            print(f"{RED}[-] Please provide --ssid or --mac for searching!{RESET}")
            return

        response = requests.get(url, headers=self.auth_headers)

        if response.status_code == 429:
            print(f"{RED}[-] Too many requests! Try again later.{RESET}")
            return 

        data = response.json()

        if self.debug:
            self._debug(data)
            return

        if data["resultCount"] <= 0:
            print(f"{RED}[-] No results found.{RESET}")
            return

        self._print_results(data)

    def _last_x_months(self):
        return (date.today() + relativedelta(months=-self.last_update)).strftime("%Y%m%d") + "000000"

    def _request_wifi_bssid(self, ssid):
        return f"https://api.wigle.net/api/v2/network/search?ssid={ssid}&country={self.country}&lastupdt={self._last_x_months()}"

    def _request_wifi_mac(self, mac):
        return f"https://api.wigle.net/api/v2/network/search?netid={mac}&country={self.country}&lastupdt={self._last_x_months()}"

    def _print_results(self, data):
        print(f"\n{GREEN}[✓] Target found!{RESET}\n")
        table_data = [(f"{BOLD}Update{RESET}", f"{BOLD}MAC{RESET}", f"{BOLD}Encryption{RESET}", f"{BOLD}Channel{RESET}", f"{BOLD}Location{RESET}", f"{BOLD}Coordinates{RESET}")]
        
        for entry in data["results"]:
            table_data.append((
                f"{CYAN}{entry['lastupdt']}{RESET}",
                f"{RED}{entry['netid']}{RESET}",
                f"{YELLOW}{entry['encryption']}{RESET}",
                f"{GREEN}{entry['channel']}{RESET}",
                f"{entry['road']} {entry['city']}, {entry['region']}, {entry['country']}",
                f"{CYAN}{entry['trilat']} , {entry['trilong']}{RESET}"
            ))

        print(SingleTable(table_data, " Search Results ").table)
        print(f"\n{GREEN}[✓] Scan completed.{RESET}")

    def _debug(self, data):
        print(f"\n{YELLOW}[DEBUG] Raw API Response:{RESET}\n")
        raw_json = json.dumps(data, indent=4, sort_keys=True)
        print(highlight(raw_json, lexers.JsonLexer(), formatters.TerminalFormatter()))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="WiFi SSID or MAC address lookup tool.")
    parser.add_argument("--ssid", help="Target SSID", type=str)
    parser.add_argument("--mac", help="Target MAC address", type=str)
    parser.add_argument("--country", help="Country code (Default: PH)", type=str, default="PH")
    parser.add_argument("--last-update", help="How many months back to search (Default: 6)", type=int, default=6)
    parser.add_argument("--debug", help="Show raw API JSON response", action="store_true")

    args = parser.parse_args()

    geo = GeoWifi(ssid=args.ssid, mac=args.mac, country=args.country, last_update=args.last_update, debug=args.debug)
    geo.run()