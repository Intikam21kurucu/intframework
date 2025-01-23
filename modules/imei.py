#!/usr/bin/env python3
import argparse
import requests

def imei_check(imei):
    url = f"https://imeicheck.com/imei-check/{imei}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return f"Hata: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Hata: {str(e)}"

def main():
    parser = argparse.ArgumentParser(description='IMEI numarası ile sorgulama yapma aracı')
    parser.add_argument('imei', type=str, help='Sorgulanacak IMEI numarası')
    args = parser.parse_args()

    result = imei_check(args.imei)
    print(result)

if __name__ == '__main__':
    main()