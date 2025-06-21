import threading
from .shell import SessionShell
from .registry import register_session
from .logger import log
from .utils import print_success

class SessionThread(threading.Thread):
    def __init__(self, conn, addr, session_id, module_commands=[]):
        super().__init__()
        self.conn = conn
        self.addr = addr
        self.session_id = session_id
        self.shell = SessionShell(conn, addr, session_id)
        self.shell.load_custom_commands(module_commands)
        self.alive = True

    def run(self):
        try:
            self.shell.interact()
        except Exception:
            pass
        finally:
            self.conn.close()
            self.alive = False

def handle_new_connection(conn, addr, session_id, module_commands=[]):
    session = SessionThread(conn, addr, session_id, module_commands)
    register_session(session_id, session)
    session.start()
    log("New session opened", addr)
    print_success(f"Session #{session_id} from {addr[0]}:{addr[1]}")