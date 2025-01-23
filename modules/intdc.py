#!/usr/bin/env python3
# Modules importation
from pyfiglet import Figlet
import os
import base64
import argparse
try:
    from colorama import Fore, init
except:
    os.system("py -m pip install colorama")
    from colorama import Fore, init
init()

f = Figlet(font='slant')
print(f.renderText('intDC'))

H = '\033[95m'
B = '\033[94m'
G = '\033[92m'
W = '\033[93m'
F = '\033[91m'
E = '\033[0m'
U = '\033[4m'
O = '\033[33m'
def search(userid):
	encodedBytes = base64.b64encode(userid.encode("utf-8"))
	encodedStr = str(encodedBytes, "utf-8")
	print(f'\n {encodedStr}')
	os.system('figlet pause>nul')  # Pause command in Batch (press any key to exit the code)
def __user__():
	parser = argparse.ArgumentParser(description='intdiscord')
	parser.add_argument("userid", help="target id")
	args = parser.parse_args()
	if args.userid:
		search(args.userid)
	else:
		print("usage: intdc <Token>")
	
	
if __name__ == "__main__":
	__user__()