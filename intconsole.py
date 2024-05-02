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


# Dönen karakterlerin listesi
dönen_karakterler = ['/', '|', '\\', '-']

# Metni ve dönen karakterleri yazdır
def dönen_animasyon(metin):
    for karakter in dönen_karakterler:
        sys.stdout.write(f'\r{metin} {karakter}')
        sys.stdout.flush()
        time.sleep(0.3)

# Animasyonu belirli bir süre boyunca çalıştır
def animasyonu_çalıştır(süre):
    bitiş_zamanı = time.time() + süre
    while time.time() < bitiş_zamanı:
        dönen_animasyon('Intikam21 Cyber TOOLS CONSOLE Starting')

# Argparse nesnesini oluştur ve otomatik --help işlevselliğini devre dışı bırak
parser = argparse.ArgumentParser(prog='İntikam21', description='Çeşitli komutlar için CLI aracı', add_help=False)

# Özel yardım komutu ekleyin
parser.add_argument('--help', action='store_true', help='Yardım mesajını göster')

# Diğer komut satırı argümanlarını tanımla
parser.add_argument('--linux', action='store_true', help='Linux ile ilgili bilgi göster')
parser.add_argument('intconsole', nargs='?', help='Cyber TOOLS CONSOLE\'u başlat')

# Argümanları ayrıştır
args = parser.parse_args()

# Yardım komutu
if args.help:
    print("İntikam21 kullanılabilir komutlar:")
    print("--help  : Bu yardım mesajını gösterir")
    print("--linux   : Linux ile ilgili bilgi gösterir")
    print("intconsole: Cyber TOOLS CONSOLE'u başlat")

# Linux komutu
elif args.linux:
    print("the linux not updating system! please retrying command : python3 intconsole intconsole / if command not working retry command : ""python3 intconsole"" ")

# intconsole komutu
elif 'intconsole' in args:
    # ASCII sanatı
    ascii_sanat = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⠶⠶⠶⠶⢦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠛⠁⠀⠀⠀⠀⠀⠀⠈⠙⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⣠⡴⠞⠛⠉⠉⣩⣍⠉⠉⠛⠳⢦⣄⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⠀⣴⡿⣧⣀⠀⢀⣠⡴⠋⠙⢷⣄⡀⠀⣀⣼⢿⣦⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⡾⠋⣷⠈⠉⠉⠉⠉⠀⠀⠀⠀⠉⠉⠋⠉⠁⣼⠙⢷⣼⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣇⠀⢻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠀⣸⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣹⣆⠀⢻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡟⠀⣰⣏⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⠞⠋⠁⠙⢷⣄⠙⢷⣀⠀⠀⠀⠀⠀⠀⢀⡴⠋⢀⡾⠋⠈⠙⠻⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠀⠀⠀⠀⠀⠀⠹⢦⡀⠙⠳⠶⢤⡤⠶⠞⠋⢀⡴⠟⠀⠀⠀⠀⠀⠀⠙⠻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣼⠋⠀⠀⢀⣤⣤⣤⣤⣤⣤⣤⣿⣦⣤⣤⣤⣤⣤⣤⣴⣿⣤⣤⣤⣤⣤⣤⣤⡀⠀⠀⠙⣧⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣸⠏⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⢠⣴⠞⠛⠛⠻⢦⡄⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠸⣇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⡟⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⣿⣿⢶⣄⣠⡶⣦⣿⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⢻⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣾⠁⠀⠀⠀⠀⠘⣇⠀⠀⠀⠀⠀⠀⠀⢻⣿⠶⠟⠻⠶⢿⡿⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠈⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢰⡏⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⢾⣄⣹⣦⣀⣀⣴⢟⣠⡶⠀⠀⠀⠀⠀⠀⣼⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⣭⣭⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠘⣧⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⢿⡀⠀⠀⠀⠀⠀⠀⣀⡴⠞⠋⠙⠳⢦⣀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⢰⡏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⢿⣄⣀⠀⠀⢀⣤⣼⣧⣤⣤⣤⣤⣤⣿⣭⣤⣤⣤⣤⣤⣤⣭⣿⣤⣤⣤⣤⣤⣼⣿⣤⣄⠀⠀⣀⣠⡾⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠻⢧⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠼⠟⠛⠛⠉⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
. ⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣷⣷⣶⣿⣿ """	
    print(ascii_sanat)
    # 5 saniye boyunca animasyonu çalıştır
    animasyonu_çalıştır(10)

# Eğer hiçbir argüman verilmezse veya tanımlanmamış bir argüman verilirse, özel yardım mesajını göster
else:
    print("Yardım için '--help' komutunu kullanın.")
    
 

time.sleep(5)   
      




            
                        
                                    
os.system("clear")





ASCI = """                       , ▄ ▄ ▄ ▄ █ █ █ █ █ █ ████ █ █ █ █ ▄ ▄ ▄ ▄ ,

                       ▄ ▄ █ █ █ ██████ █ ▀ █ █ █ █ ▀ ▀ ▀ █ █ ████ ████ █ █ ▄ ▄

                   ▄ ▄ █ █ ██████ ▌ ` └ █ ▌   ▐ █ █ █ ▄ ▄  │ █ █ █ ,  ┌ █ █ █████ █ █ █ ▄

               , ▄ █ █ ███ █ ▀ " ▀ █ ██ ▌     ┌   █ █ █ ▀  « ▓ █ █ █ ∩  ▄ █ ██████ █ ▀ ▀ █ ██ ▄ ,

             ▄ █ █ ██████ U  ╦  ` ▀ █ █ U  ▐ ▄ █ ▄ ▄ █ █ █ ▄ ▄▄▄ █ █ ▄ , , ] █ █ ███ █ `  ╓ ▄  ▐ █ ██ █ ▄

           ▄ █ █ ██ █ ` ▀ █ ██ ▌  ` , ▄ , ▄ █ █ █ █ █ ███ █ ██████████ █ ██████ ▌  └ █ █ ███ █ " ▀ █ █ ▄

         ▄ █ █ █ █ ▀ ▀ ▌   ▀ █ █ █ U ▄ █ █ ██ █ █ █ █ ████████████ ██████ █ █ █ ██ █ ▄ , ▄ █ █ █ ∩  Å ▀▀ █ █ ▄

       ╓ █ █ █ ██ █ ▄    ▄ , ▄ █ █ ██ █ █ ███ █ ██████████████ ██████ █ ██ █ █ █ ███ █ `  , ▄ ▄ █ █ █ █ █ ▄

      ▄ █ Ü  ▀ ▀ █ █ █ █ ▄  , █ █ ██ █ █ ██ █ ████████████████ ███████████ █ █ █ █ █ █ █ █ █ █ ███ █ ▀  ▀ █ █

    ┌ █ █ ██ █ ▄   ` ▀ █ █ █ █ ██ █ █ █ █ ████████████████ ███████████████ ██ █ █ █ █ █ ██ █ ▀    4 U └ █ █ µ

   ┌ █ █ █ █ ▀█ █ █ █ ▄ , ╓ █ █ █ █ █ █ █ ████ █ ▀ █ █ █████ █████████████████ █ ▀ █ █ ███ █ █ █ █ █ █ ▄  ▀ *  ,▄ █ █ █ ▄

  ┌ █ █ █ █   ▀ █ █ █ ████ █ █ █ █ ██ ∩ └ █   ▄ █ ██████████ ██████████████ ▄  ` █  ▐ █ █ █ ██ █ █ █ ▄ ▄▄ █ █ █ █ █ █ U

  █ █ ██ Ü ┌ ▄ µ   ` █ █ █ █ █ █ █ █ ▀ █ U └ ª " ▀ █ █ ███████████ █████████████ █ ▀ " ╜ ╞ ▌ ▀ █ █ █ █ █ █ █ █ ▀ ▀ `    ▀ █

 ▄ █ ████████ █ █ █ █ █ ███ █ █  ╘ ¥ ▀ ª ▓ █ █ █ █ ████ █ █ █ █ █████████████ ███ █ ▓ ª ▀ ╬   █ █ █ █ █ █ ██ U  ▄  ▀ ▄ , █ ▌

┌ █ █ █ ▌ ` " ▀ ▀ ▀ ▀ █ █ ██ ████  └ ▌ ▄ « w █ █ ███████ █ █ █ ▓ ▄ ▄▀ █ █ █ ███████ ███ █ ██ █ w « ▄ ▀  │ █ █ █ █ █ █ █ ▄ ▄ █ █ █ ███ ∩

▐ █ ██ █ █ ▀ `   J █ █ █ █ █ █ █ ▀ ▌  ` , ▄ █ █ █ █ ██ █ █ ███ █ █ ▓ ▓ ▓ ▓ █ █ █ ████ █ ████ █████ █ ▄  ' , ▓ ▀ █ █ ▓███ █ ▀ ▀ ▀ ▀ ▀ " █ ▌

█ █ █ █    ² ╜ ▀ █ █ ██ ▓██ █  └ ╛ `  █ █ ██ ██ █ █ █ █ ██ █ █ █ ███ ▌ ░ ▀ ▀ ▀ ▀ █ █ █ █ ████ ████ ▌  " ╧  , █ █ █ █ █ █ █ ▄ «  ╒ ▄  ╫ █

█ █ ██ █ █ █ █ ▄ ▄ █ █ ██ ▓█ █ ` ▀ ⌡ ▄ * ▐ █ █ █ ██ █ █████ ████ █ █ ░ ▓ █ ██ ▓ ▓ █ ▄ ▄ ▒ █ █ ███████ ▀ * ▄ $ ▀  █ █ █ █ ██ ∩  ▄,  , █ █

█ █ ▀█ ▀ ▀ ▀ ▀ ▀ ▀ █ █ ██ ██ █ █ µ  ,a █ █ █ █ ███████ █ ██ ██ ▓ ▌ ╫ █ █ ███ ██ █ ▓ ▓ ▄ █ █ █ █████ ▌ φ   ┌ █ █ █ ████ █ █ █ ██ ███

█ ▄ ╓ ▓μ╓╓ ▄ ▄ ▄ █ █ ██ ▓█ █  ` h ▀  █ █ ██████████████ █ ▓ ▄ ▓ █ █ ████████ ████ ██ ██ ▌  ▐ ╚ `  █ █ █ █ █████████ █

▀ █ ████████████ ███ ▀ ¥ ▄ ▄ ` │ █ █ █ ███████ ███ ███ █ █ ▓ ▓ ▓ ▓ █ ████ █ █ █ ███████  ╙ ▄ ▄# ▀ █ ▌███████████ ▌

╘ █ ████████████ █ █ █ ▄ , ` ' , Å ▀ █ █ ████████ ████ ████ █ █ █ ████ █ █ ███ █ █ ███ ▀ % , ` , ▄ █ ████████████ ▀

 █ █ ████████████ █ █ █ " ▀ ▀ ▀ ▐ █ █ █████████████ █████████████ █ █ █ █ █ █ █ ▄  ▀ Å ▀ ▐ █ █ █ █ █████████ █

 └ ▓ ▓▓▓▓▓▓█ █ █ ▓ ▓▓ █ █ █ █ ▄ ▄ ▄ &   █ ██████ ███████ ██████████████ █████  │ ▌ ▄ ▄ ▄ █ ██ █ ▓ ▓█ ▀█▓▓▓▓▓ ∩

  ▐ ▓ ▓▓▓▓ █ ▀ ⁿ  ▀ ▓ ▓▓ █ █ █ █ ,    ▄  ▐ █ ███████ ███████ ████████████ █ █ ▀  ▄  `  ╓ █ █ █ █ ▓ ▓█ ▓  `▀ █ ▓▓ ▀

   ▀ ▓ ▓ ▌   , æ ▄ , ▀ █ ▓▓ █ █ █ █ ▌ " " ┘  ▄ █ ███████████████ █████████████ ▄  ª ▀ " █ █ █ █ ▓ ▓ ▓ █ U ,    ` ▀ ▀

    ▀ █ ▓ ▓ █ █ ▀ "   └ █ ▓ ▓ ▓ █ █ █ █ █ █ ███ █ █ ██████████ ██████████████ █ ▀ █ █ █ █ █ █ █ █ ▓ ▓▓ ▀  g █ ▓█ █ ▓ ▀

     ╙ █ ▓ █ ,  ≤ , ▀ ▄ ▄ █ █ ▓ ▓ █ █ █ █ █ █ ███████████████ ███████████████ ██ █ █ █ █ ▓ ▓█ █▓ ▄  └ ▀ ▀  ▄ ▀

      ` ▀ ▓ █ ▄ ╓ ▓ ▀ "  ,  ▀ ▓ ▓▓ ▓ █ █ █ █ █ █ ███████████████ ███████████ █ ██ █ █ ▓ ▓▓ ▌ `  ` ╙ ▀ ▄ ▄ ▄ ▓

        ╙ █ ▓█ ▄ bir ,╙  ╓ ▓ ▀ " █ ▓ ▓▓ ▓ █ █ █ ███ █ █ ███████████ █████ █ █ ██ █ █ █ ▓ ▓ ▓█ ▀ └ ▓ U  *  , , ▓ ▀"""

print(Fore.WHITE+ASCI)


# 'INTIKAM21 CYBER' metnini mavi renkte ve slant fontuyla yazdır
f = Figlet(font='slant')
print(Fore.BLUE + f.renderText('INTIKAM21 CYBER') + Fore.RESET)
while True:
# Kullanıcıdan 'help' komutunu girmesini iste
	print(Fore.BLUE + 'başlatmak için help yaz')
	print("""5-)Tools * 1000-)commands * 70-)exploits 
""")
	help_input = input("┌──(intikam21-cyber@root[~]\n└─$ ")
	if help_input == "help":
		print("""
		5 Tools:
			1-) DDOS
			2-) SMSBOMBER
			3-DİSCORD
			4-)METASPLOİT
			5-)İNTİKAM21
		
		""")
		print("exploit usage: exp-number")
		print("""
		Exploits:
			1-Exploit Database 
			2-MSFVENOM
			3-MSFCONSOLE
			4-NMAP
			......
		
		""")
	if help_input == "1":
		os.system("python3 DDOS.py")
	if help_input == "3":
		os.system("python3 DİSCORD.py")
	if help_input == "2":
		os.system("Python3 SMSBOMBER.py")
	if help_input == "4":
		os.system("sudo apt-get install metasploit-framework")
		os.system("msfconsole")
	if help_input == "5":
		os.system("""apt update & apt upgrade
sudo apt install git
sudo apt install python3-pyfiglet
sudo apt install python3 
sudo apt install python3-base64
sudo apt install python3-colorama
sudo apt install python3-requests

git clone https://github.com/Intikam21kurucu/Intikam21

cd Intikam21

python3 Intıkam21.py""")
	if help_input == "exp-1":
		print("the exploit is not working ")
	if help_input == "exp-2":
		try:
			os.system("msfconsole")
		except:
			os.system("sudo apt-get install metasploit-framework")
	if help_input == "exp-3":
		try:
			os.system("msfvenom")
		except:
			os.system("sudo apt-get install metasploit-framework")
	if help_input == "exp-4":
		try:
			os.system("pip install nmap")
			os.system("nmap")
		except:
			os.system("sudo apt-get install nmap")
	else:
		print("please restart console")
		os.system("python3 intconsole.V2py")