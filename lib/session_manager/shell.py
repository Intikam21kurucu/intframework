import threading
from .utils import print_info, print_error, print_success

class SessionShell:
    def __init__(self, conn, addr, session_id):
        self.conn = conn
        self.addr = addr
        self.session_id = session_id
        self.prompt = f"{Fore.BLUE}int4-pro{Fore.RESET} {Fore.RED}{module}{Fore.RESET}[{Fore.YELLOW}{session_id}{Fore.RESET}] > " if module is not None else f"{Fore.BLUE}int4-pro{Fore.RESET} [{Fore.RED}{session_id}{Fore.RESET}] > "
        self.dynamic_commands = {}  # dict: command_name -> function(conn)

        self._interact_lock = threading.Lock()  # thread-safe interact

    def load_custom_commands(self, custom_cmds):
        """
        Load custom commands from modules into the shell command registry.
        custom_cmds: list of dicts with 'name' and 'function'
        """
        for cmd in custom_cmds:
            name = cmd.get("name")
            func = cmd.get("function")
            if callable(func) and name:
                self.dynamic_commands[name] = func
                print_info(f"Loaded custom command '{name}' in session #{self.session_id}")

    def unload_command(self, cmd_name):
        """
        Remove a custom command if exists.
        """
        if cmd_name in self.dynamic_commands:
            del self.dynamic_commands[cmd_name]
            print_info(f"Unloaded custom command '{cmd_name}' from session #{self.session_id}")

    def interact(self):
        """
        Interactive shell session loop.
        Thread-safe to prevent concurrency issues.
        """
        with self._interact_lock:
            print_info(f"Starting interaction with session #{self.session_id} ({self.addr[0]}:{self.addr[1]})")
            while True:
                try:
                    cmd = input(self.prompt).strip()
                    if cmd == "":
                        continue
                    if cmd.lower() == "exit":
                        print_info(f"Exiting session #{self.session_id} shell.")
                        break

                    # Check dynamic commands first
                    if cmd in self.dynamic_commands:
                        try:
                            self.dynamic_commands[cmd](self.conn)
                        except Exception as e:
                            print_error(f"Error executing custom command '{cmd}': {e}")
                    else:
                        try:
                            self.conn.sendall(cmd.encode())
                            response = self._recv_all()
                            print(response)
                        except Exception as e:
                            print_error(f"Communication error with session #{self.session_id}: {e}")
                            break
                except (KeyboardInterrupt, EOFError):
                    print_info(f"Session #{self.session_id} shell interrupted by user.")
                    break
                except Exception as e:
                    print_error(f"Unexpected error in session shell: {e}")
                    break

    def _recv_all(self, buffer_size=4096, timeout=1.0):
        """
        Receive all data until timeout or no more data.
        """
        self.conn.settimeout(timeout)
        data = b""
        try:
            while True:
                part = self.conn.recv(buffer_size)
                if not part:
                    break
                data += part
                if len(part) < buffer_size:
                    break
        except socket.timeout:
            pass
        except Exception as e:
            print_error(f"Error receiving data: {e}")
        finally:
            self.conn.settimeout(None)
        return data.decode(errors="ignore")