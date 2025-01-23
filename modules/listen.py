#!/usr/bin/env python3
import socket
import sys

HOST = '' 
PORT = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((HOST, PORT))
    
except socket.error as msg:
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
	
print('Socket bind complete')

s.listen(1)

conn, addr = s.accept()

print('Connected with ' + addr[0] + ':' + str(addr[1]))