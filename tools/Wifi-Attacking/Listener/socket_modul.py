import socket

def start_socket_listener(host='0.0.0.0', port=12345):
    print(f'Starting Socket listener on {host}:{port}')
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))
    
    while True:
        data, addr = sock.recvfrom(1024)  # 1024 byte veri al
        print(f'Received message from {addr}: {data.decode()}')