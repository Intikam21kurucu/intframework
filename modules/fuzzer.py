#!/usr/bin/env python3
import os
import sys
import socket
import time
from termcolor import colored, cprint

class Fuzzer(object):

    def TCPFuzzer(self):
        os.system('clear')
        CORE_STRING = colored("[tcp_fuzzer]", 'blue')
        host = input(CORE_STRING + " Host> ")  # Changed raw_input to input for Python 3
        buffer_ = 'A' * 2048  # Changed 'x41' to 'A'

        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((host, 443))
                s.settimeout(2)

                print("[!] Sending Buffer Size of: " + colored(str(len(buffer_)), 'blue'))  # Python 3 print format
                s.send(("USER: " + buffer_ + "\r\n").encode())  # Encoding to bytes for Python 3
                time.sleep(2)

                buffer_ = buffer_ + 'A' * 2048  # Changed 'x41' to 'A'

            except socket.error as wn:
                cprint("[+] Service Crashed With Buffer Size Of: " + str(len(buffer_)), 'green')
                break

            except KeyboardInterrupt:
                cprint("[-] Kullanıcı Tarafından Fuzz İşlemi İptal Edildi!", 'red')  # Turkish message
                sys.exit(1)

            except Exception as e:
                print(f"Error: {e}")
                continue

    def FTPFuzzer(self):
        os.system('clear')
        CORE_STRING = colored("[ftp_fuzzer]", 'blue')
        host = input(CORE_STRING + " Host> ")  # Changed raw_input to input for Python 3
        buffer_ = 'A' * 2048  # Changed 'x41' to 'A'

        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((host, 21))
                s.settimeout(2)

                print("[!] Sending Buffer Size of: " + colored(str(len(buffer_)), 'blue'))  # Python 3 print format
                s.send(("USER: " + buffer_ + "\r\n").encode())  # Encoding to bytes for Python 3
                time.sleep(2)

                buffer_ = buffer_ + 'A' * 2048  # Changed 'x41' to 'A'

            except socket.error as wn:
                cprint("[+] Service Crashed With Buffer Size Of: " + str(len(buffer_)), 'green')
                break

            except KeyboardInterrupt:
                cprint("[-] Kullanıcı Tarafından Fuzz İşlemi İptal Edildi!", 'red')  # Turkish message
                sys.exit()

            except Exception as e:
                print(f"Error: {e}")
                continue

    def HTTPFuzzer(self):
        os.system('clear')
        CORE_STRING = colored("[http_fuzzer]", 'blue')
        host = input(CORE_STRING + " Host> ")  # Changed raw_input to input for Python 3
        buffer_ = 'A' * 2048  # Changed 'x41' to 'A'

        HTTP_BASE_SIZE_ = 3333
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((host, 80))
                s.settimeout(2)

                print("[!] Sending Buffer Size of: " + colored(str(len(buffer_)), 'blue'))  # Python 3 print format
                s.send(("USER: " + buffer_ + "\r\n").encode())  # Encoding to bytes for Python 3
                s.send(("\tGET /" + str(HTTP_BASE_SIZE_) + " HTTP/1.1\r\n").encode())  # Encoding to bytes
                s.send(("\tHOST: " + host + "\r\n\r\n").encode())  # Encoding to bytes
                time.sleep(2)

                buffer_ = buffer_ + 'A' * 2048  # Changed 'x41' to 'A'

            except socket.error as wn:
                cprint("[+] Service Crashed With Buffer Size Of: " + str(len(buffer_)), 'green')
                break

            except KeyboardInterrupt:
                cprint("[-] Kullanıcı Tarafından Fuzz İşlemi İptal Edildi!", 'red')  # Turkish message
                sys.exit()

            except Exception as e:
                print(f"Error: {e}")
                continue
Fuzzer = Fuzzer().HTTPFuzzer()