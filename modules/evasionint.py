#!/usr/bin/env python3
import argparse
import base64
import random
import time
import os
import requests
import cryptography.fernet
import zlib
import io
import ctypes
import psutil
import socket
import ssl
import sys

# Evasion Teknikleri
def technique_1():
    print("Technique 1: Basic Obfuscation")
    if args.code:
        code = args.code
        exec(''.join([chr(int(''.join(c), 16)) for c in zip(code.split())]))
    else:
        print("No code provided.")

def technique_2():
    print("Technique 2: Polymorphic Coding")
    if args.code:
        code = args.code
        polymorphic_payload = ''.join([chr(ord(char) + random.randint(1, 10)) for char in code])
        print(polymorphic_payload)
    else:
        print("No code provided.")

def technique_3():
    print("Technique 3: Metamorphic Coding")
    if args.code:
        code = args.code
        code_variants = [
            code,
            code.lower(),
            code.replace('World', 'Universe')
        ]
        exec(random.choice(code_variants))
    else:
        print("No code provided.")

def technique_4():
    print("Technique 4: Traffic Encryption")
    if args.code:
        data = args.code
        encoded_data = base64.b64encode(data.encode())
        print(encoded_data)
        decoded_data = base64.b64decode(encoded_data).decode()
        print(decoded_data)
    else:
        print("No code provided.")

def technique_5():
    print("Technique 5: Anti-Debugging")
    import sys
    if hasattr(sys, 'gettrace') and sys.gettrace() is not None:
        print("Debugging detected!")
        sys.exit()
    print("No debugging detected, proceeding with execution.")

def technique_pe():
    print("Technique PE: Simulating PE Execution")
    if args.use:
        command = args.use
        pe_header = b'\x4D\x5A'  # MZ header for PE file simulation
        pe_body = command.encode()
        pe_file = io.BytesIO(pe_header + pe_body)
        print("Simulated PE file content:")
        print(pe_file.getvalue())
    else:
        print("No command provided for PE simulation.")

def trafic_encryption():
    if args.code:
        data = args.code
        encoded_data = base64.b64encode(data.encode())
        decoded_data = base64.b64decode(encoded_data).decode()
        exec(decoded_data)
    else:
        print("No code provided.")

def antidebug():
    import sys
    if hasattr(sys, 'gettrace') and sys.gettrace() is not None:
        print("Debugging detected!")
        sys.exit()
    print("No debugging detected, proceeding with execution.")

def execution():
    if args.code:
        exec(args.code)
    else:
        print("No code provided.")

def string_encoding():
    if args.code:
        code = args.code
        encoded_code = base64.b64encode(code.encode()).decode()
        decoded_code = base64.b64decode(encoded_code.encode()).decode()
        exec(decoded_code)
    else:
        print("No code provided.")

def execute_code(code):
    exec(code)
    if args.code:
        code = args.code
        execute_code(code)

def encrypted_payloads():
    from cryptography.fernet import Fernet
    if args.code:
        key = Fernet.generate_key()
        cipher_suite = Fernet(key)
        cipher_text = cipher_suite.encrypt(args.code.encode())
        plain_text = cipher_suite.decrypt(cipher_text).decode()
        exec(plain_text)
    else:
        print("No code provided.")

def string_manipulation():
    code = "".join(["p", "r", "i", "n", "t", "(", "'", "H", "e", "l", "l", "o", ",", " ", "W", "o", "r", "l", "d", "!", "'", ")"])
    exec(code)

def memory_of_code():
    import ctypes
    def run_code():
        if args.code:
            code = args.code
            ctypes.cdll.LoadLibrary(None).mprotect(ctypes.c_void_p(id(code)), len(code), 7)
            exec(ctypes.CFUNCTYPE(None)(ctypes.addressof(code)))
        else:
            print("No code provided.")
    run_code()

def cryptographic_padding():
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
    from cryptography.hazmat.backends import default_backend
    import base64
    def encrypt_code(code, key):
        cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
        encryptor = cipher.encryptor()
        padded_code = code + ' ' * (16 - len(code) % 16)
        encrypted_code = encryptor.update(padded_code.encode()) + encryptor.finalize()
        return base64.b64encode(encrypted_code).decode()
    
    def decrypt_code(encrypted_code, key):
        cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
        decryptor = cipher.decryptor()
        encrypted_code = base64.b64decode(encrypted_code.encode())
        decrypted_code = decryptor.update(encrypted_code) + decryptor.finalize()
        return decrypted_code.decode().strip()
    
    if args.code:
        key = b'0123456789abcdef'  # Must be 16 bytes
        encrypted_code = encrypt_code(args.code, key)
        exec(decrypt_code(encrypted_code, key))
    else:
        print("No code provided.")

def hidden_import():
    import importlib
    module = importlib.import_module('builtins')
    if args.code:
        exec(module.__builtins__['eval'](args.code))
    else:
        print("No code provided.")

def generate_function():
    if args.code:
        code = args.code
        random_suffix = random.randint(1, 100)
        exec(f"def dynamic_func_{random_suffix}(): {code}")
    else:
        print("No code provided.")

def data_obfuscation():
    import base64
    def obfuscate_data(data):
        return base64.b64encode(data.encode()).decode()
    
    def deobfuscate_data(obfuscated_data):
        return base64.b64decode(obfuscated_data.encode()).decode()
    
    if args.code:
        data = args.code
        obfuscated_data = obfuscate_data(data)
        print(f"Obfuscated Data: {obfuscated_data}")
        deobfuscated_data = deobfuscate_data(obfuscated_data)
        print(f"Deobfuscated Data: {deobfuscated_data}")
    else:
        print("No code provided.")

# Evasion Teknikleri listesini tanımla
techniques = {
    'evasion/basic/obfuscation/': technique_1,
    'evasion/basic/polymorphic/': technique_2,
    'evasion/good/metamorphic/': technique_3,
    'evasion/super/hidden_import/': hidden_import,
    'evasion/super/traffic/encryption/': technique_4,
    'evasion/basic/debugging/': technique_5,
    'evasion/intsuper/cryptographic_padding/': cryptographic_padding,
    'evasion/super/anti/debugging/': antidebug,
    'evasion/good/generate_function/': generate_function,
    'evasion/intsuper/memory_of_code/': memory_of_code,
    'evasion/good/traffic_encryption/': trafic_encryption,
    'evasion/good/string_encoding/': string_encoding,
    'evasion/basic/execute/': execution,
    'evasion/super/manipulation/': string_manipulation,
    'evasion/intsuper/data_obfuscation/': data_obfuscation,
}

def search_techniques():
    for key, func in techniques.items():
        print(f"Technique {key}:")
        func()
        print("\n")

def use_technique(technique_id):
    if technique_id in techniques:
        techniques[technique_id]()
    else:
        print("Invalid technique ID.")

def use_pe_technique():
    technique_pe()

def send_data(lhost, lport):
    print(f"Sending data to {lhost}:{lport}")
    response = requests.post(f'http://{lhost}:{lport}', data={'message': 'Hello, World!'})
    print(response.text)

def main():
    parser = argparse.ArgumentParser(description='Evasion Techniques Tool')
    parser.add_argument('-s', '--search', action='store_true', help='Search for all techniques')
    parser.add_argument('-u', '--use', type=str, help='Use a specific technique by ID')
    parser.add_argument('-pe', action='store_true', help='Simulate PE technique with user command')
    parser.add_argument('-l', '--lhost', type=str, help='Local host to send data')
    parser.add_argument('-p', '--lport', type=int, help='Local port to send data')
    parser.add_argument('-c', '--code', type=str, help='Code to use in evasion techniques')
    
    global args
    args = parser.parse_args()

    if args.search:
        search_techniques()
    elif args.use:
        use_technique(args.use)
    elif args.pe:
        use_pe_technique()
    elif args.lhost and args.lport:
        send_data(args.lhost, args.lport)
    else:
        print("No valid option provided. Use -h for help.")

if __name__ == '__main__':
    main()