import readline
import os
import json
import time
from colorama import Fore, Style, init
init(autoreset=True)

class HistoryManager:
    def __init__(self, history_file=None, json_log_file=None, history_limit=1000):
        self.history_file = history_file or os.path.expanduser("~/.intframework_history")
        self.json_log_file = json_log_file or os.path.expanduser("~/.inthistory.json")
        self.history_limit = history_limit
        self.load_history()

    def load_history(self):
        try:
            readline.read_history_file(self.history_file)
        except FileNotFoundError:
            open(self.history_file, "a").close()
        readline.set_history_length(self.history_limit)
        readline.set_completer(self.autocomplete)
        readline.parse_and_bind("tab: complete")

    def autocomplete(self, text, state):
        # Buraya Shell’in komut listesini dışardan verirsiniz
        if not hasattr(self, "commands"):
            return None
        matches = [cmd for cmd in self.commands if cmd.startswith(text)]
        return matches[state] if state < len(matches) else None

    def set_commands(self, commands):
        self.commands = commands

    def log_command(self, cmd):
        entry = {
            "command": cmd,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        try:
            with open(self.json_log_file, "a", encoding="utf-8") as f:
                f.write(json.dumps(entry) + "\n")
        except:
            pass

    def save_history(self):
        try:
            readline.write_history_file(self.history_file)
        except:
            pass

    def get_history(self):
        return [readline.get_history_item(i+1) for i in range(readline.get_current_history_length())]

    def run_history_command(self, index):
        try:
            cmd = readline.get_history_item(index)
            return cmd
        except:
            return None

    def clear_screen(self):
        os.system("clear" if os.name != "nt" else "cls")

    def format_colored(self, command):
        base = command.strip().split()[0] if command.strip() else ""
        if base == "exploit":
            return Fore.RED + command + Style.RESET_ALL
        elif base == "payload":
            return Fore.YELLOW + command + Style.RESET_ALL
        elif base in ["scan", "osint", "whois"]:
            return Fore.CYAN + command + Style.RESET_ALL
        return command

# Shell içerisinde örnek kullanım:

class ExampleShell:
    def __init__(self):
        self.history = HistoryManager()
        # Shell komut listesi
        self.commands = [
            "exploit", "payload", "scan", "osint", "whois",
            "set", "show", "clear", "exit", "history", "help"
        ]
        self.history.set_commands(self.commands)

    def input_loop(self):
        print(Fore.GREEN + "[*] Shell başlatıldı.")
        while True:
            try:
                cmd = input("> ").strip()
                if not cmd:
                    continue
                readline.add_history(cmd)
                self.history.log_command(cmd)
                if cmd == "exit":
                    print(Fore.MAGENTA + "[*] Shell kapatılıyor.")
                    self.history.save_history()
                    break
                elif cmd == "clear":
                    self.history.clear_screen()
                elif cmd == "history":
                    for i, c in enumerate(self.history.get_history(), start=1):
                        print(f"{i}: {c}")
                elif cmd.startswith("!"):
                    try:
                        idx = int(cmd[1:])
                        recalled_cmd = self.history.run_history_command(idx)
                        if recalled_cmd:
                            print(Fore.BLUE + f"[!] Tekrar çalıştırılıyor: {recalled_cmd}")
                            # Burada recursive veya direkt execute çağrılır
                            # self.execute(recalled_cmd) gibi
                        else:
                            print(Fore.RED + "[!] Geçersiz komut geçmişi indeksi.")
                    except:
                        print(Fore.RED + "[!] Geçersiz komut geçmişi formatı.")
                else:
                    print("->", self.history.format_colored(cmd))
                    # Burada komut işleme fonksiyonunu çağırabilirsiniz
            except (EOFError, KeyboardInterrupt):
                print(Fore.MAGENTA + "\n[*] Shell kapatıldı.")
                self.history.save_history()
                break

# Kullanım

if __name__ == "__main__":
    shell = ExampleShell()
    shell.input_loop()