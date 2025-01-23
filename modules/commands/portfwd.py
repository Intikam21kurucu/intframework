import socket
import threading
import argparse

def forward_data(src_socket, dst_socket):
    """Forward data between source and destination sockets."""
    try:
        while True:
            data = src_socket.recv(4096)
            if not data:
                break
            dst_socket.sendall(data)
    except Exception as e:
        print(f"Error during data forwarding: {e}")

def start_port_forwarding(local_port, remote_host, remote_port):
    """Start port forwarding manually using socket operations."""
    # Create a server socket to listen for incoming connections
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind(('0.0.0.0', local_port))
        server_socket.listen(5)
        print(f"Listening on port {local_port}...")

        while True:
            try:
                client_socket, addr = server_socket.accept()
                print(f"Accepted connection from {addr}")

                # Connect to the remote host
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as remote_socket:
                    remote_socket.connect((remote_host, remote_port))
                    print(f"Connected to remote host {remote_host}:{remote_port}")

                    # Start forwarding data between the client and remote socket
                    threading.Thread(target=forward_data, args=(client_socket, remote_socket)).start()
                    threading.Thread(target=forward_data, args=(remote_socket, client_socket)).start()
            except Exception as e:
                print(f"Error during connection handling: {e}")

def main():
    parser = argparse.ArgumentParser(description="Port forwarding and attack redirection script.")
    parser.add_argument('-l', '--local-port', type=int, required=True, help="Local port to listen on for incoming connections.")
    parser.add_argument('-r', '--remote-host', type=str, required=True, help="Remote host IP to connect to.")
    parser.add_argument('-rp', '--remote-port', type=int, required=True, help="Remote port to connect to.")
    parser.add_argument('--redirect', type=str, help="IP to redirect incoming attacks to.")
    parser.add_argument('--listen-port', type=int, help="Port for a service to run while redirecting attacks.")

    args = parser.parse_args()

    start_port_forwarding(args.local_port, args.remote_host, args.remote_port)

if __name__ == "__main__":
    main()