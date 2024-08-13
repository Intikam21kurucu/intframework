import ssl
import socket
from datetime import datetime

def get_ssl_cert_info(hostname):
    port = 443
    context = ssl.create_default_context()
    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()
            print(f"Certificate for: {hostname}")
            print(f"Issuer: {cert['issuer']}")
            print(f"Subject: {cert['subject']}")
            print(f"Expiry Date: {cert['notAfter']}")
            print(f"Start Date: {cert['notBefore']}")
