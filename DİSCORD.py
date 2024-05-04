# Modules importation
from pyfiglet import Figlet
import os
import base64
try:
    from colorama import Fore, init
except:
    os.system("py -m pip install colorama")
    from colorama import Fore, init
init()

f = Figlet(font='slant')
print(f.renderText('ARES DİSCORD SIKICI'))

H = '\033[95m'
B = '\033[94m'
G = '\033[92m'
W = '\033[93m'
F = '\033[91m'
E = '\033[0m'
U = '\033[4m'
O = '\033[33m'



userid = input(" [INPUT] USER ID : ")
encodedBytes = base64.b64encode(userid.encode("utf-8"))
encodedStr = str(encodedBytes, "utf-8")
print(f'\n [LOGS] TOKEN FIRST PART : {encodedStr}')
os.system('figlet pause>nul')  # Pause command in Batch (press any key to exit the code) a 