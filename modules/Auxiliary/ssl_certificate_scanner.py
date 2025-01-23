#!/usr/bin/env python3
import ssl
import socket

def ssl_certificate_checker(domain):
    """[Check the SSL certificate of a target domain]"""
    context = ssl.create_default_context()
    with socket.create_connection((domain, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=domain) as ssock:
            cert = ssock.getpeercert()
            print("SSL Certificate Information:")
            for key, value in cert.items():
                print(f"{key}: {value}")

# User input
domain = input("\033[91mint4 [Enter the Target Domain] > \033[0m")
ssl_certificate_checker(domain)