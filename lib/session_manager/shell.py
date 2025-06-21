from .utils import print_info, print_error
from colorama import Fore

class SessionShell:
    def __init__(self, conn, addr, session_id, module=None):
        self.conn = conn
        self.addr = addr
        self.session_id = session_id
        self.prompt = f"{Fore.BLUE}int4-pro{Fore.RESET} {Fore.RED}{module}{Fore.RESET}[{Fore.YELLOW}{session_id}{Fore.RESET}] > " if module is not None else f"{Fore.BLUE}int4-pro{Fore.RESET} [{Fore.RED}{session_id}{Fore.RESET}] > "
        self.dynamic_commands = {}  # key: command, value: function

    def load_custom_commands(self, custom_cmds):
        for cmd in custom_cmds:
            self.dynamic_commands[cmd["name"]] = cmd["function"]

    def interact(self):
        while True:
            try:
                cmd = input(self.prompt).strip()
                if cmd == "exit":
                    break
                elif cmd in self.dynamic_commands:
                    self.dynamic_commands[cmd](self.conn)
                else:
                    self.conn.sendall(cmd.encode())
                    result = self.conn.recv(4096).decode()
                    print(result)
            except Exception:
                print_error("Session disconnected")
                break