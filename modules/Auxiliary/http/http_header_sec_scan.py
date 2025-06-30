# auxiliary/http_header_sec_scan.py

import requests
from lib.int4.config_manager import option_schema
from lib.utils import print_info, print_success, print_error

class AuxiliaryModule:
    """
    HTTP Header Security Scanner
    Amaç: Hedefteki HTTP cevap header'larında kritik güvenlik başlıklarını kontrol eder.
    """

    def __init__(self):
        self.option_schema = {
            "RHOSTS": {
                "description": "Target host(s), comma separated or single domain/ip",
                "required": True,
                "default": None,
            },
            "PORT": {
                "description": "HTTP port",
                "required": False,
                "default": 80,
            },
            "USE_HTTPS": {
                "description": "Use HTTPS for connections",
                "required": False,
                "default": False,
            },
            "TIMEOUT": {
                "description": "Connection timeout in seconds",
                "required": False,
                "default": 5,
            },
        }

    def run(self):
        targets = self._parse_targets(self.get_option("RHOSTS"))
        port = int(self.get_option("PORT"))
        use_https = bool(self.get_option("USE_HTTPS"))
        timeout = int(self.get_option("TIMEOUT"))

        scheme = "https" if use_https else "http"

        headers_to_check = [
            "Strict-Transport-Security",
            "Content-Security-Policy",
            "X-Content-Type-Options",
            "X-Frame-Options",
            "Referrer-Policy",
            "Feature-Policy",
        ]

        for target in targets:
            url = f"{scheme}://{target}:{port}"
            print_info(f"Scanning {url} for security headers...")

            try:
                response = requests.get(url, timeout=timeout)
                found_headers = {}

                for header in headers_to_check:
                    value = response.headers.get(header)
                    if value:
                        found_headers[header] = value

                if found_headers:
                    print_success(f"Found security headers on {target}:")
                    for h, v in found_headers.items():
                        print(f"  {h}: {v}")
                else:
                    print_error(f"No security headers found on {target}.")

            except requests.RequestException as e:
                print_error(f"Failed to connect to {target}:{port} - {e}")

    # Helper methods for intSpLoiT framework compatibility
    def get_option(self, key):
        # Bu fonksiyon framework'den parametre değerini alır (yerine göre override edilir)
        return self.option_schema[key]["default"]

    def _parse_targets(self, target_str):
        if not target_str:
            return []
        return [t.strip() for t in target_str.split(",") if t.strip()]