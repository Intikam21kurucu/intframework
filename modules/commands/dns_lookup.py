#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pyfiglet import Figlet
from colorama import Fore, init
import threading
import requests
import time
import sys
import os
import base64
import time as t
import argparse
import sys
import platform
import getpass
import subprocess
import socket
from netaddr import IPNetwork, IPAddress
import argparse
import socket
import threading
import time
import sys
import random
import urllib.request
from queue import Queue

def dns_lookup_a(domain, port=None):
    try:
        ip_address = socket.gethostbyname(domain)
        if port:
            ip_address = f"{ip_address}:{port}"
        print(f"{domain}:{port} için A kaydı: {ip_address}")
    except socket.gaierror as e:
        print(f"{domain}:{port} için A kaydı bulunamadı: {e}")

def dns_lookup_mx(domain, port=None):
    try:
        answers = socket.getaddrinfo(domain, port, socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
        mx_records = [answer for answer in answers if answer[1] == socket.SOCK_STREAM]
        if mx_records:
            for mx_record in mx_records:
                print(f"{domain}:{port} için MX kaydı: {mx_record}")
        else:
            print(f"{domain}:{port} için MX kaydı bulunamadı.")
    except socket.gaierror as e:
        print(f"{domain}:{port} için MX kaydı sorgulaması başarısız oldu: {e}")

def dns_lookup_ns(domain, port=None):
    try:
        answers = socket.getaddrinfo(domain, port, socket.AF_INET, socket.SOCK_STREAM)
        ns_records = [answer for answer in answers if answer[1] == socket.SOCK_STREAM]
        if ns_records:
            for ns_record in ns_records:
                print(f"{domain}:{port} için NS kaydı: {ns_record}")
        else:
            print(f"{domain}:{port} için NS kaydı bulunamadı.")
    except socket.gaierror as e:
        print(f"{domain}:{port} için NS kaydı sorgulaması başarısız oldu: {e}")

def dns_lookup_txt(domain, port=None):
    try:
        answers = socket.getaddrinfo(domain, port, socket.AF_INET, socket.SOCK_STREAM)
        txt_records = [answer for answer in answers if answer[1] == socket.SOCK_STREAM]
        if txt_records:
            for txt_record in txt_records:
                print(f"{domain}:{port} için TXT kaydı: {txt_record}")
        else:
            print(f"{domain}:{port} için TXT kaydı bulunamadı.")
    except socket.gaierror as e:
        print(f"{domain}:{port} için TXT kaydı sorgulaması başarısız oldu: {e}")

def reverse_dns_lookup(ip, port=None):
    try:
        hostnames = socket.gethostbyaddr(ip)
        if port:
            ip = f"{ip}:{port}"
        print(f"{ip} için ters DNS çözümlemesi: {hostnames}")
    except socket.herror as e:
        print(f"{ip} için ters DNS çözümlemesi başarısız oldu: {e}")

def ip_check(ip_address):
    ip = IPAddress(ip_address)
    if ip in IPNetwork('192.168.1.0/24'):
        print(f"{ip_address} yerel ağda bulunuyor.")
    else:
        print(f"{ip_address} yerel ağda bulunmuyor.")

def main():
    input_str = input("Bir IP adresi veya domain adı (opsiyonel olarak port ile birlikte) girin: ")
    domain, port = parse_input(input_str)
    
    try:
        socket.inet_aton(domain)
        is_ip = True
    except socket.error:
        is_ip = False
    
    if is_ip:
        reverse_dns_lookup(domain, port)
    else:
        dns_lookup_a(domain, port)
        dns_lookup_mx(domain, port)
        dns_lookup_ns(domain, port)
        dns_lookup_txt(domain, port)