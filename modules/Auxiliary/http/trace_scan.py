# modules/auxiliary/http/trace_scan.py

# Author: intAIv3
# Title: HTTP TRACE Vulnerability Scanner
# Description:
# Test:

import requests
import time
from lib.utils import print_info, print_success, print_error

option_schema = {
    "RHOSTS": {
        "description": "Target hosts, comma separated",
        "required": True,
        "default": None,
    },
    "PORT": {
        "description": "Target port",
        "required": False,
        "default": 80,
    },
    "HTTPS": {
        "description": "Use HTTPS",
        "required": False,
        "default": False,
    },
    "TIMEOUT": {
        "description": "Request timeout in seconds",
        "required": False,
        "default": 5,
    },
    "RETRIES": {
        "description": "Number of retries for failed requests",
        "required": False,
        "default": 2,
    },
    "DELAY": {
        "description": "Delay between requests (seconds)",
        "required": False,
        "default": 1,
    },
}

class AuxiliaryModule:

    def __init__(self):
        pass

    def get_option(self, key):
        # Placeholder: framework tarafından override edilerek gerçek parametre dönecek
        return option_schema[key]["default"]

    def _parse_targets(self, target_string):
        if not target_string:
            return []
        return [t.strip() for t in target_string.split(",") if t.strip()]

    def _send_trace_request(self, url, timeout):
        try:
            response = requests.request("TRACE", url, timeout=timeout)
            return response
        except requests.RequestException:
            return None

    def run(self):
        targets = self._parse_targets(self.get_option("RHOSTS"))
        port = int(self.get_option("PORT"))
        use_https = bool(self.get_option("HTTPS"))
        timeout = int(self.get_option("TIMEOUT"))
        retries = int(self.get_option("RETRIES"))
        delay = float(self.get_option("DELAY"))
        scheme = "https" if use_https else "http"

        if not targets:
            print_error("No targets specified in RHOSTS option.")
            return

        print_info(f"Starting HTTP TRACE vulnerability scan on {len(targets)} target(s)...")

        for target in targets:
            url = f"{scheme}://{target}:{port}"
            attempt = 0
            response = None

            while attempt <= retries:
                print_info(f"Sending TRACE request to {url} (Attempt {attempt + 1}/{retries + 1})")
                response = self._send_trace_request(url, timeout)
                if response:
                    break
                else:
                    print_error(f"Request failed for {url}, retrying...")
                    attempt += 1
                    time.sleep(delay)

            if not response:
                print_error(f"All attempts failed for {url}. Skipping.")
                continue

            status = response.status_code
            if status == 200:
                print_success(f"[VULNERABLE] TRACE method enabled on {target}")
            elif status == 405:
                print_info(f"TRACE method disabled (405 Method Not Allowed) on {target}")
            else:
                print_info(f"Received HTTP {status} from {target}")

            time.sleep(delay)

        print_info("HTTP TRACE vulnerability scan completed.")