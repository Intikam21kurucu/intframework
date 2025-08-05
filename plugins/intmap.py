import requests
import socket
import json
import ipaddress

class Plugin:
    def __init__(self):
        self.name = "intmap"
        self.commands = {
            "intmap": {
                "func": self.cmd_intmap,
                "desc": "Fetches detailed geolocation and network intelligence for an IP address or hostname.",
                "usage": "intmap <ip_address_or_hostname>"
            }
        }

    def resolve_hostname(self, hostname):
        try:
            return socket.gethostbyname(hostname)
        except Exception:
            return None

    def reverse_dns(self, ip):
        try:
            return socket.gethostbyaddr(ip)[0]
        except Exception:
            return "N/A"

    def is_valid_ip(self, ip):
        try:
            ipaddress.ip_address(ip)
            return True
        except ValueError:
            return False

    def is_private_ip(self, ip):
        try:
            return ipaddress.ip_address(ip).is_private
        except:
            return False

    def get_ip_version(self, ip):
        try:
            return f"IPv{ipaddress.ip_address(ip).version}"
        except:
            return "Unknown"

    def get_cidr_info(self, ip):
        try:
            r = requests.get(f"https://rdap.arin.net/registry/ip/{ip}", timeout=5)
            if r.status_code == 200:
                data = r.json()
                return data.get("cidr", "N/A")
        except:
            pass
        return "N/A"

    def get_ip_info(self, ip_or_host):
        ip = ip_or_host
        if not self.is_valid_ip(ip_or_host):
            resolved = self.resolve_hostname(ip_or_host)
            if resolved is None:
                return {"status": "fail", "message": f"Unable to resolve hostname: {ip_or_host}"}
            ip = resolved

        url = (
            f"http://ip-api.com/json/{ip}"
            "?fields=status,message,continent,continentCode,country,countryCode,region,regionName,"
            "city,district,zip,lat,lon,timezone,isp,org,as,reverse,mobile,proxy,hosting,query"
        )

        try:
            resp = requests.get(url, timeout=10)
            if resp.status_code == 200:
                data = resp.json()
                if data.get("status") == "success":
                    data["ip_version"] = self.get_ip_version(data.get("query"))
                    data["is_private"] = self.is_private_ip(data.get("query"))
                    data["resolved_ptr"] = self.reverse_dns(data.get("query"))
                    data["cidr_block"] = self.get_cidr_info(data.get("query"))
                return data
            else:
                return {"status": "fail", "message": f"HTTP error: {resp.status_code}"}
        except requests.RequestException as e:
            return {"status": "fail", "message": f"Request error: {str(e)}"}

    def format_output(self, data):
        if data.get("status") != "success":
            return f"[!] Error: {data.get('message', 'Unknown error')}"

        as_info = data.get("as", "N/A")
        if as_info != "N/A" and as_info.startswith("AS"):
            as_split = as_info.split(" ", 2)
            as_number = as_split[0]
            as_isp = as_split[1] if len(as_split) > 1 else "N/A"
        else:
            as_number = as_info
            as_isp = "N/A"

        lat, lon = data.get("lat"), data.get("lon")

        lines = [
            f"{'='*60}",
            f"📡 IP Address Intelligence Report",
            f"{'='*60}",
            f"Target IP       : {data.get('query')}",
            f"IP Version      : {data.get('ip_version')}",
            f"Private IP      : {'Yes' if data.get('is_private') else 'No'}",
            f"CIDR Block      : {data.get('cidr_block')}",
            f"PTR Record      : {data.get('resolved_ptr')}",
            f"Reverse DNS     : {data.get('reverse', 'N/A')}",
            f"{'-'*60}",
            f"📍 Geolocation",
            f"{'-'*60}",
            f"Continent       : {data.get('continent')} ({data.get('continentCode')})",
            f"Country         : {data.get('country')} ({data.get('countryCode')})",
            f"Region          : {data.get('regionName')} ({data.get('region')})",
            f"City            : {data.get('city')}",
            f"District        : {data.get('district')}",
            f"ZIP Code        : {data.get('zip')}",
            f"Coordinates     : {lat}, {lon}",
            f"Timezone        : {data.get('timezone')}",
            f"{'-'*60}",
            f"🛰️ Network Info",
            f"{'-'*60}",
            f"ISP             : {data.get('isp')}",
            f"Organization    : {data.get('org')}",
            f"AS Number       : {as_number}",
            f"AS ISP          : {as_isp}",
            f"Mobile Network  : {'Yes' if data.get('mobile') else 'No'}",
            f"Proxy/VPN       : {'Yes' if data.get('proxy') else 'No'}",
            f"Hosting Service : {'Yes' if data.get('hosting') else 'No'}",
            f"{'-'*60}",
            f"🌐 Map Links",
            f"{'-'*60}",
            f"Google Maps     : https://www.google.com/maps/search/?api=1&query={lat},{lon}",
            f"Bing Maps       : https://www.bing.com/maps?cp={lat}~{lon}&lvl=15",
            f"OpenStreetMap   : https://www.openstreetmap.org/?mlat={lat}&mlon={lon}#map=15/{lat}/{lon}",
            f"{'='*60}"
        ]
        return "\n".join(lines)

    def cmd_intmap(self, args):
        if not args or len(args) == 0:
            return "[!] Usage: intmap <ip_address_or_hostname>"
        target = args[0]
        data = self.get_ip_info(target)
        return self.format_output(data)