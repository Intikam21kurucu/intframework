import os
import sys
import socket
import threading
import time

ARCHIVE_DIR = 'recon_archive'
BUFFER_SIZE = 4096  # Buffer size for receiving data
TIMEOUT = 3  # Timeout for socket connections (in seconds)

# Ensure the archive directory exists
if not os.path.exists(ARCHIVE_DIR):
    os.makedirs(ARCHIVE_DIR)

# Thread lock to avoid race conditions when writing files
lock = threading.Lock()

# Function to execute a port scan on the target
def port_scan(target_ip, start_port=1, end_port=1024):
    """Perform a port scan on the target system."""
    open_ports = []
    for port in range(start_port, end_port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(TIMEOUT)
                result = s.connect_ex((target_ip, port))
                if result == 0:
                    open_ports.append(port)
        except socket.error:
            pass
    return open_ports

# Function to fetch the service version running on a port
def get_service_version(target_ip, port):
    """Retrieve the service version on an open port."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(TIMEOUT)
            s.connect((target_ip, port))
            s.send(b'HEAD / HTTP/1.0\r\n\r\n')
            service = s.recv(1024).decode('utf-8')
        return service
    except Exception as e:
        return f"Error: {str(e)}"

# Function to execute a list of reconnaissance commands
def execute_recon_commands(commands, target_ip):
    """Execute reconnaissance commands to gather information about the target."""
    output = ""
    for cmd in commands:
        try:
            print(f"Executing: {cmd}")
            cmd_output = run_recon_command(cmd, target_ip)
            output += f"$ {cmd}\n{cmd_output}\n{'='*40}\n"
        except Exception as e:
            output += f"Error executing command {cmd}: {str(e)}\n"
    return output

# Function to run a single reconnaissance command
def run_recon_command(command, target_ip):
    """Run a single recon command (e.g., port scan, service version retrieval)."""
    if command == "port_scan":
        open_ports = port_scan(target_ip)
        return f"Open ports: {', '.join(map(str, open_ports))}"
    elif command.startswith("service_version"):
        port = int(command.split()[1])
        service_info = get_service_version(target_ip, port)
        return f"Service on port {port}: {service_info}"
    else:
        return f"Unknown command: {command}"

# Function to save output to a file with thread safety
def save_output(filename, data):
    """Save output to a file."""
    with lock:
        try:
            with open(f"{ARCHIVE_DIR}/{filename}", "w") as f:
                f.write(data)
            print(f"Output saved to {ARCHIVE_DIR}/{filename}")
        except Exception as e:
            print(f"Error saving output: {str(e)}")

# Function to handle the recon command
def handle_recon(argv):
    """Handle the recon command input and execute it on the remote target."""
    if len(argv) < 3 or argv[1] in ('-h', '--help'):
        print(f"Usage: {sys.argv[0]} <target_ip> <recon_command1> [<recon_command2> ...] [-o <filename>]")
        return

    target_ip = argv[1]

    write_file = None
    if '-o' in argv:
        write_index = argv.index('-o')
        if len(argv) > write_index + 1:
            write_file = argv[write_index + 1]
        else:
            print("Error: No filename specified for output.")
            return
        argv = argv[:write_index]

    commands = ' '.join(argv[2:])
    output = execute_recon_commands(commands.split(), target_ip)

    if write_file:
        save_output(write_file, output)
    else:
        print(output)

# Command line execution entry point
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: recon.py <target_ip> <recon_command1> [<recon_command2> ...] [-o <filename>]")
        sys.exit(1)

    # Handle reconnaissance execution in a separate thread
    recon_thread = threading.Thread(target=handle_recon, args=(sys.argv,))
    recon_thread.start()
    recon_thread.join()