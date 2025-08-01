import socket
import threading
from typing import Optional, List, Dict
from .config import CONFIG
from .handler import handle_new_connection, SessionThread
from .registry import (
    increment_session_id,
    list_sessions,
    register_session,
    get_session,
    remove_session,
)
from .utils import print_info, print_success, print_error
from .logger import log
from .shell import SessionShell


class SessionManager:
    """
    Robust, modular, and professional session manager that handles:
    - TCP listener (for reverse shells),
    - Active session creation,
    - Session listing and metadata,
    - Command dispatching,
    - Group command execution,
    - Session persistence and restoration,
    - Clean shutdown.
    
    Fully integrates with existing lib/session_manager components.
    """

    def __init__(self):
        self.listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.active = False
        self.listener_thread: Optional[threading.Thread] = None

    def start_listener(self, lhost: Optional[str] = None, lport: Optional[int] = None) -> None:
        """
        Start a TCP listener to accept incoming connections.
        """
        host = lhost or CONFIG["LHOST"]
        port = lport or CONFIG["LPORT"]
        try:
            self.listener.bind((host, port))
            self.listener.listen()
            self.active = True
            print_success(f"Listening on {host}:{port}")
            self.listener_thread = threading.Thread(target=self._accept_loop, daemon=True)
            self.listener_thread.start()
        except Exception as e:
            print_error(f"Failed to start listener: {e}")

    def _accept_loop(self) -> None:
        """
        Listener loop accepting incoming connections and registering sessions.

        Yeni bağlantı kabul edilirken:
        - IP ve port kontrol edilir,
        - Aynı IP:port için aktif session varsa bağlantı reddedilir,
        - Yeni session için ID oluşturulur,
        - Yeni session kaydedilir ve loglanır,
        - Hatalar detaylı loglanır.
        """
        while self.active:
            try:
                conn, addr = self.listener.accept()
                ip, port = addr

                # Aktif sessionlarda aynı IP ve port var mı kontrolü
                existing_sessions = [
                    (sid, sess) for sid, sess in list_sessions().items()
                    if sess.addr == addr and sess.is_alive()
                ]

                if existing_sessions:
                    sid, sess = existing_sessions[0]
                    print_info(f"[!] Active session already exists for {ip}:{port} with ID #{sid}. Rejecting duplicate connection.")
                    try:
                        conn.shutdown(socket.SHUT_RDWR)
                    except Exception:
                        pass
                    conn.close()
                    log(f"Rejected duplicate connection from {ip}:{port} for existing session #{sid}")
                    continue

                # Yeni session ID oluştur
                session_id = increment_session_id()

                # Yeni session'u handle et
                handle_new_connection(conn, addr, session_id, module_commands=[])

                print_success(f"New session #{session_id} opened from {ip}:{port}")
                log(f"New session #{session_id} opened from {ip}:{port}")

            except Exception as e:
                print_error(f"[!] Error accepting connections: {e}")
                log(f"Error accepting connection: {e}")

    def create_session(
        self,
        session_type: str,
        host: str,
        description: str = "",
        data: str = "",
        module_commands: Optional[List[Dict]] = None,
    ) -> int:
        """
        Actively create and register a new session by connecting to the target host.

        Args:
            session_type (str): Session type label (e.g. reverse_tcp).
            host (str): Target IP or hostname.
            description (str, optional): Human-readable description.
            data (str, optional): Additional session metadata.
            module_commands (list, optional): Custom commands injected into shell.

        Returns:
            int: New session ID on success, -1 on failure.
        """
        module_commands = module_commands or []
        try:
            session_id = increment_session_id()
            conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            conn.settimeout(CONFIG["TIMEOUT"])
            conn.connect((host, CONFIG["LPORT"]))

            shell = SessionShell(conn, (host, CONFIG["LPORT"]), session_id)
            shell.load_custom_commands(module_commands)

            session_thread = SessionThread(conn, (host, CONFIG["LPORT"]), session_id, module_commands)
            session_thread.shell = shell
            session_thread.type = session_type
            session_thread.description = description
            session_thread.data = data

            register_session(session_id, session_thread)
            session_thread.start()

            log(f"Session {session_id} actively created to {host}")
            print_success(f"Session #{session_id} successfully created to {host}")
            return session_id
        except Exception as e:
            print_error(f"Failed to create session: {e}")
            return -1

    def list_sessions(self) -> None:
        """
        Display active sessions and metadata in a formatted table.
        """
        sessions = list_sessions()
        print_info("Active sessions:")
        print(f"{'ID':<4} | {'Address':<17} | {'Status':<7} | {'Type':<12} | Description")
        print("-" * 60)
        for sid, session in sessions.items():
            ip = session.addr[0]
            status = "ALIVE" if session.is_alive() else "DEAD"
            session_type = getattr(session, "type", "unknown")
            description = getattr(session, "description", "-")
            print(f"{sid:<4} | {ip:<17} | {status:<7} | {session_type:<12} | {description}")

    def interact(self, session_id: int) -> None:
        """
        Enter interactive shell with the given session.
        """
        session = get_session(session_id)
        if session and session.is_alive():
            session.shell.interact()
        else:
            print_error(f"Session {session_id} is not active or does not exist.")

    def send_command(self, session_id: int, command: str) -> Optional[str]:
        """
        Send a command to the session and return its output.

        Returns:
            str or None: Command output or None if failed.
        """
        session = get_session(session_id)
        if session and session.is_alive():
            try:
                session.conn.sendall(command.encode())
                response = session.conn.recv(CONFIG["BUFFER_SIZE"]).decode(errors="ignore")
                return response
            except Exception as e:
                print_error(f"Failed to send command to session {session_id}: {e}")
        else:
            print_error(f"Session {session_id} is not available.")
        return None

    def kill_session(self, session_id: int) -> None:
        """
        Close and remove the session cleanly.
        """
        session = get_session(session_id)
        if session:
            try:
                session.conn.close()
                remove_session(session_id)
                print_success(f"Session {session_id} terminated.")
            except Exception as e:
                print_error(f"Failed to terminate session {session_id}: {e}")
        else:
            print_error(f"Session {session_id} not found.")

    def session_group_exec(self, command: str) -> Dict[int, Optional[str]]:
        """
        Execute a command on all active sessions.

        Returns:
            dict: Mapping of session_id to command output.
        """
        results = {}
        for sid, session in list_sessions().items():
            if session.is_alive():
                results[sid] = self.send_command(sid, command)
        return results

    def save_sessions(self) -> None:
        """
        Persist sessions' metadata (not full connection) to JSON file.
        """
        import json

        data = {}
        for sid, session in list_sessions().items():
            data[sid] = {
                "host": session.addr[0],
                "port": session.addr[1],
                "type": getattr(session, "type", "unknown"),
                "description": getattr(session, "description", ""),
                "alive": session.is_alive(),
            }
        try:
            with open("lib/session_manager/session_db.json", "w") as f:
                json.dump(data, f, indent=4)
            print_success("Sessions saved successfully.")
        except Exception as e:
            print_error(f"Failed to save sessions: {e}")

    def load_sessions(self) -> None:
        """
        Load and display saved session metadata.
        """
        import json

        try:
            with open("lib/session_manager/session_db.json", "r") as f:
                data = json.load(f)
                print_info("Saved sessions:")
                for sid, info in data.items():
                    print(f"Session {sid}: {info['host']}:{info['port']} [{info['type']}] - {info['description']}")
        except Exception as e:
            print_error(f"Failed to load session data: {e}")

    def stop_listener(self) -> None:
        """
        Stop listener and release socket resources.
        """
        self.active = False
        try:
            self.listener.close()
            print_success("Listener stopped.")
        except Exception as e:
            print_error(f"Error stopping listener: {e}")
