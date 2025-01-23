import socket
import sys

def show_help():
    """Display the help menu."""
    help_text = """
TCP Connector Usage:
    python tcp_connector.py <website>

Description:
    - <website>: The target website's IP address or domain name (e.g., example.com).
    - You will be prompted to enter your username and password during execution.

Features:
    - Establish a TCP connection to the specified target.
    - Send a username and password for authentication.
    - Enter interactive command mode after authentication.
    
Example Usage:
    python tcp_connector.py example.com
"""
    print(help_text)

def interactive_shell(client_socket):
    """Interactive shell for sending commands."""
    print("[Command Mode] You can now send commands to the target system. Type 'exit' to quit.")
    while True:
        try:
            command = input("Enter command > ")
            if command.lower() == "exit":
                print("[Disconnecting] Exiting...")
                break
            client_socket.send(command.encode())
            response = client_socket.recv(4096).decode()
            print(f"[Response] {response}")
        except Exception as e:
            print(f"[Error] {e}")
            break

def tcp_connect(website, port, username, password):
    """Establish a TCP connection, send credentials, and start command mode."""
    try:
        print(f"[Connecting] Connecting to {website}:{port}...")
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((website, port))
        print(f"[Connected] Successfully connected to {website}:{port}.")

        # Send username and password
        auth_data = f"{username} > {password}"
        client_socket.send(auth_data.encode())
        print("[Sent] Username and password sent to the server.")

        # Receive server response
        response = client_socket.recv(1024).decode()
        print(f"[Server Response] {response}")

        # Start interactive shell
        interactive_shell(client_socket)

        client_socket.close()
        print("[Disconnected] Connection closed.")
    except Exception as e:
        print(f"[Error] {e}")

def main():
    """Main function of the application."""
    if len(sys.argv) != 2 or sys.argv[1] in ['--help', '-h']:
        show_help()
        sys.exit()

    website = sys.argv[1]
    port = 80  # TCP port (default 80)
    
    # Prompt user for username and password
    username = input("Enter username > ")
    password = input("Enter password > ")
    
    # Start TCP connection
    tcp_connect(website, port, username, password)

if __name__ == "__main__":
    main()