import requests

def get_geo_info(ip):
    response = requests.get(f"http://ipinfo.io/{ip}/json")
    data = response.json()
    print(f"IP: {ip}")
    print(f"City: {data.get('city')}")
    print(f"Region: {data.get('region')}")
    print(f"Country: {data.get('country')}")
    print(f"Location: {data.get('loc')}")