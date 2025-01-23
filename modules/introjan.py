#!/usr/bin/env python3
import argparse
import subprocess
import webbrowser
import socket
import paramiko

def execute_local_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Output: {result.stdout.decode()}")
        print(f"Error: {result.stderr.decode()}")
    except subprocess.CalledProcessError as e:
        print(f"Command execution error: {e}")

def open_video_url(url):
    try:
        webbrowser.open(url)
        print(f"Opened URL: {url}")
    except Exception as e:
        print(f"URL opening error: {e}")

def connect_via_tcp(ip, port, message):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip, port))
            s.sendall(message.encode())
            data = s.recv(1024)
            print(f"Received: {data.decode()}")
    except Exception as e:
        print(f"TCP connection error: {e}")

def execute_remote_command_ssh(ip, username, password, command):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, username=username, password=password)
        stdin, stdout, stderr = ssh.exec_command(command)
        print(f"Output: {stdout.read().decode()}")
        print(f"Error: {stderr.read().decode()}")
        ssh.close()
    except Exception as e:
        print(f"SSH execution error: {e}")

def transfer_file_sftp(ip, username, password, local_file, remote_file):
    try:
        transport = paramiko.Transport((ip, 22))
        transport.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(transport)
        sftp.put(local_file, remote_file)
        print(f"Transferred: {local_file} to {remote_file}")
        sftp.close()
        transport.close()
    except Exception as e:
        print(f"SFTP transfer error: {e}")

def download_file_sftp(ip, username, password, remote_file, local_file):
    try:
        transport = paramiko.Transport((ip, 22))
        transport.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(transport)
        sftp.get(remote_file, local_file)
        print(f"Downloaded: {remote_file} to {local_file}")
        sftp.close()
        transport.close()
    except Exception as e:
        print(f"SFTP download error: {e}")

def print_ascii_art():
    ascii_art = """
    ⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⢱⠐⠄⠙⠽⡲⣤⡀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⡾⠃⠀⠀⢀⠈⠻⣿⣿⣶⡶⢃⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⡼⣧⣀⣠⡴⠀⢂⠀⠙⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⢸⣅⣩⠟⠁⢰⠀⠸⡄⠀⠐⢻⣿⣿⡿⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠙⠁⠀⠀⢀⠀⠀⡇⠀⠀⠄⠻⠿⢷⣋⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⣸⠀⢠⠇⢀⡜⠀⠀⠐⡄⠀⠀⠈⠈⠐⢤⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⢠⡏⠀⢈⡴⠋⠀⠀⠀⠀⡗⠀⠀⠀⠀⠀⠀⢻⣿⣶⣦⣄⠀
    ⠀⠀⠀⠀⡾⠀⡄⡎⠀⠀⠀⠀⠀⡰⠃⠀⠀⠀⠀⡠⠀⢀⡇⠙⣿⣿⡷
    ⠀⠀⠀⡠⠣⠀⠇⡄⠀⠀⠀⢠⠔⠁⠀⠀⠀⣠⠞⠀⢀⡜⣠⣾⢿⠟⠀
    ⠀⢀⡴⠁⣀⠤⠊⠘⡆⠀⣠⠣⢤⠤⠴⢲⠋⠙⠀⣰⠋⠘⡝⠁⠘⠄⠀
    ⠀⣰⡿⠖⠉⠀⠀⢀⠊⡀⠚⠁⠀⠈⠀⡰⠁⠀⡆⡜⠁⠀⠀⠁⠀⠀   ⢀⡿⠁⠀⠀⠀⢰⣿⠏⠀⠀⠀⠀⡀⢰⠁⢀⣼⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⣾⡇⠀⠀⠀⠀⠀⢻⣧⣶⡄⠀⠀⣇⠎⣠⡾⠛⠀⠀⠀⠀⠀⠀⠀⠀    ⣿⣷⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⣼⢏⣴⠟⠁⠀From İntikam21⠀
    ⠙⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣾⡇⠀⠀⠀    Framework   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠏⠀⠉⠀                  To⠀You⠀⠀
    """
    print(ascii_art)

def main():
    print_ascii_art()
    
    parser = argparse.ArgumentParser(description="introjan")
    
    parser.add_argument('-k', '--kablo', action='store_true', help='Use cable connection')
    parser.add_argument('-r', '--remote', type=str, choices=["lxde", "cmd"], required=True, help='Remote operation type: cmd or lxde')
    parser.add_argument('-d', '--dir', type=str, required=True, help='Directory to show on computer')
    parser.add_argument('-g', '--video-url', type=str, help='Video URL to play locally')
    parser.add_argument('-c', '--cmd', type=str, help='Command to execute (for cmd remote only)')
    parser.add_argument('--ipv4', type=str, help='IPv4 address')
    parser.add_argument('-p', '--port', type=int, help='Port number (required if -k is used)')
    parser.add_argument('-s', '--send-message', type=str, metavar='MESSAGE', help='Message to send via TCP socket')
    parser.add_argument('--ssh-user', type=str, help='SSH username')
    parser.add_argument('--ssh-pass', type=str, help='SSH password')
    parser.add_argument('--remote-cmd', type=str, help='Remote command to execute via SSH')
    parser.add_argument('--local-file', type=str, help='Local file to transfer via SFTP')
    parser.add_argument('--remote-file', type=str, help='Remote file path for SFTP transfer')
    parser.add_argument('--download-file', type=str, help='Remote file to download via SFTP')
    parser.add_argument('--local-download-path', type=str, help='Local path for downloaded file via SFTP')

    args = parser.parse_args()

    if args.send_message:
        if not args.ipv4 or not args.port:
            parser.error("IPv4 address and port number are required to send a message.")
        connect_via_tcp(args.ipv4, args.port, args.send_message)

    if args.kablo:
        if not args.port:
            parser.error("Port number is required with -k option.")
        if args.remote == "lxde" and args.video_url:
            open_video_url(args.video_url)
        elif args.remote == "cmd" and args.cmd:
            execute_local_command(args.cmd)
        else:
            parser.error("Specify a valid action for the given options.")
    else:
        if not args.ipv4:
            parser.error("IPv4 address is required.")
        if args.remote == "lxde" and args.video_url:
            open_video_url(args.video_url)
        elif args.remote == "cmd" and args.cmd:
            execute_local_command(args.cmd)
        elif args.remote_cmd and args.ssh_user and args.ssh_pass:
            execute_remote_command_ssh(args.ipv4, args.ssh_user, args.ssh_pass, args.remote_cmd)
        elif args.local_file and args.remote_file and args.ssh_user and args.ssh_pass:
            transfer_file_sftp(args.ipv4, args.ssh_user, args.ssh_pass, args.local_file, args.remote_file)
        elif args.download_file and args.local_download_path and args.ssh_user and args.ssh_pass:
            download_file_sftp(args.ipv4, args.ssh_user, args.ssh_pass, args.download_file, args.local_download_path)
        else:
            parser.error("Specify a valid action for the given options.")

if __name__ == "__main__":
    main()