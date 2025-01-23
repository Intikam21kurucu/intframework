#!/usr/bin/env python3
import argparse
import os
import platform
import getpass
import socket
import hashlib
from cryptography.fernet import Fernet

# Şifreleme anahtarı (bu genellikle güvenli bir yerde saklanmalıdır)
KEY = b + f'{args.secret}' # Anahtarınızı buraya yerleştirin
cipher_suite = Fernet(KEY)

def get_system_info():
    system_info = {
        'OS': platform.system(),
        'Release': platform.release(),
        'Version': platform.version(),
        'Architecture': platform.architecture()[0],
        'Machine': platform.machine(),
        'Processor': platform.processor()
    }
    return system_info

def list_files(directory):
    try:
        files = os.listdir(directory)
        return files
    except Exception as e:
        return str(e)

def get_user_info():
    user_info = {
        'Username': getpass.getuser(),
        'Home Directory': os.path.expanduser("~")
    }
    return user_info

def get_network_info():
    network_info = {
        'Hostname': socket.gethostname(),
        'IP Address': socket.gethostbyname(socket.gethostname())
    }
    return network_info

def encrypt_message(message):
    encrypted = cipher_suite.encrypt(message.encode())
    return encrypted.decode()

def decrypt_message(encrypted_message):
    decrypted = cipher_suite.decrypt(encrypted_message.encode())
    return decrypted.decode()

def main():
    parser = argparse.ArgumentParser(prog="intsecret", description='intsecret')
    parser.add_argument('command', choices=['info', 'list', 'user', 'network', 'encrypt', 'decrypt'], help='Komut seçimi')
    parser.add_argument('--directory', type=str, help='Listeleme için dizin')
    parser.add_argument('--message', type=str, help='Şifrelemek veya deşifre etmek için mesaj')
    parser.add_argument("-s","--secret-key", help="your secret key here", dest="secret")

    args = parser.parse_args()

    if args.command == 'info':
        info = get_system_info()
        for key, value in info.items():
            print(f'{key}: {value}')
    elif args.command == 'list':
        if args.directory:
            files = list_files(args.directory)
            if isinstance(files, list):
                for file in files:
                    print(file)
            else:
                print(f'Hata: {files}')
        else:
            print('Dizin belirtmeniz gerekiyor.')
    elif args.command == 'user':
        info = get_user_info()
        for key, value in info.items():
            print(f'{key}: {value}')
    elif args.command == 'network':
        info = get_network_info()
        for key, value in info.items():
            print(f'{key}: {value}')
    elif args.command == 'encrypt':
        if args.message:
            encrypted = encrypt_message(args.message)
            print(f'Encrypted: {encrypted}')
        else:
            print('Mesaj belirtmeniz gerekiyor.')
    elif args.command == 'decrypt':
        if args.message:
            decrypted = decrypt_message(args.message)
            print(f'Decrypted: {decrypted}')
        else:
            print('Şifreli mesaj belirtmeniz gerekiyor.')

if __name__ == '__main__':
    main()