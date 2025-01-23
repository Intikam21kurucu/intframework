#!/usr/bin/env python3
import argparse
import shodan

def search_by_query(api_key, query):
    api = shodan.Shodan(api_key)
    try:
        results = api.search(query)
        print(f"Sonuç Sayısı: {results['total']}")
        for result in results['matches']:
            print(f"IP: {result['ip_str']}")
            print(f"Port: {result.get('port', 'N/A')}")
            print(f"Ülke: {result.get('location', {}).get('country_name', 'N/A')}")
            print(f"İçerik: {result.get('data', 'N/A')}")
            print('-' * 40)
    except shodan.APIError as e:
        print(f"API Hatası: {e}")

def search_by_ip(api_key, ip):
    api = shodan.Shodan(api_key)
    try:
        result = api.host(ip)
        print(f"IP: {result['ip_str']}")
        print(f"Ülke: {result.get('location', {}).get('country_name', 'N/A')}")
        print(f"Şehir: {result.get('location', {}).get('city', 'N/A')}")
        print(f"İşletim Sistemi: {result.get('os', 'N/A')}")
        print(f"Portlar: {', '.join(map(str, result.get('ports', [])))}")
        print('-' * 40)
    except shodan.APIError as e:
        print(f"API Hatası: {e}")

def search_by_email_or_phone(api_key, email=None, phone=None):
    # Shodan üzerinde bu tür doğrudan aramalar yapılamaz. Yine de, bu işlevi genel sorgulara adapte edebilirsiniz.
    # Burada örnek bir arama yapıyoruz, Shodan üzerinde email veya telefon numarası bilgisi bulamayabilirsiniz.
    query = f"{email or phone}"
    search_by_query(api_key, query)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Shodan arama aracı")
    parser.add_argument('api_key', type=str, help="Shodan API anahtarınız")
    parser.add_argument('--query', type=str, help="Arama sorgusu")
    parser.add_argument('--ip', type=str, help="IP adresi ile arama")
    
    args = parser.parse_args()
    
    if args.query:
        search_by_query(args.api_key, args.query)
    elif args.ip:
        search_by_ip(args.api_key, args.ip)