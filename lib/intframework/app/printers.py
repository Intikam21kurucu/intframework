#!/usr/bin/python3
from colorama import *

init(autoreset=True)

def print_do(message, color_continue=True):
        print(f"{Fore.GREEN}[+] {message}")
        if color_continue == False:
                print(f"{Fore.GREEN}[+]{Fore.RESET} {message}")
def print_warning(message, color_continue=True):
        print(f"{Fore.RED}[!] {message}")
        if color_continue == False:
                print(f"{Fore.RED}[!]{Fore.RESET} {message}")
def print_sys(message, color_continue=True):
        print(f"{Fore.BLUE}[~] {message}")
        if color_continue == False:
                print(f"{Fore.BLUE}[~]{Fore.RESET} {message}")