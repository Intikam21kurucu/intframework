"""
Examples:
        inttable.core.activate("dev") or inttable.core.activate("root") If you don't do this, you won't be able to use the console.
        inttable.exploit.run("intframework/modules/exploits/dropleganger", "dropleganger.py", args=None)
        inttable.console.run("load_plugins (plugin path) ")
        inttable.console.write("exploit") 
"""
import importlib.util
import json
import os

# Banner Function
def banner(hide=False):
    if not hide:
        table = """
⠀⠀⠀⠀⣀⣀⣴⣶⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣠⣶⣆⣀⠀
⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠁
⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠛⢻⣿⡟⠛⠛⠛⠛⠛⠁⠀⠀
⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡟⠻⣿⣶⠄⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣇⣀⣀⣁⣠⣾⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣼⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀inttable⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⠛⠿⠿⠿⠿⠿⠟⠀⠀⠀
    """
        print(table)
    else:
        pass
banner(hide=True)

# Global Variables
rater = None
LHOSTS = None
LPORTS = None

# Write function
def write(packet):
    with open(".int4", "a") as magic:
        magic.write(packet + "\n")

# Load console module
def load_console_module():
    spec = importlib.util.spec_from_file_location("intconsole_module", "intframework/intconsoleV4.py")
    console_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(console_module)
    return console_module

# Run console function
def run_console_function(function_name, *args, **kwargs):
    console_module = load_console_module()
    if hasattr(console_module, function_name):
        function_to_run = getattr(console_module, function_name)
        result = function_to_run(*args, **kwargs)
        return result
    else:
        return f"Fonksiyon '{function_name}' bulunamadı."

# Execute command
def execute_command(command):
    console_module = load_console_module()
    console_module.help_input = command
    console_module.__main__()

# Commands
commands = [
    "load_console_module", "run_console_function", "execute_command", "use", 
    "show_exploits", "run_exploit", "list_plugins", "check", "wifi_scan", "login", 
    "execute_get_input", "run_exploit"
]

# Console Class
class console:
    global rater

    def __init__(self):
        self.prog = "inttable.py"
        self.meta = {
            "author": "@intikam21",
            "most_used": "execute_command",
            "int_commands": self.get_commands(),
            "parser": "no parser!",
            "var": 20
        }

    @staticmethod
    def read_int4():
        json_content = None
        normal_content = None
        try:
            with open(".int4", "r") as file:
                content = file.read()
                try:
                    json_content = json.loads(content)
                except json.JSONDecodeError:
                    normal_content = content
            return json_content, normal_content
        except FileNotFoundError:
            print("Dosya bulunamadı.")
            return None, None

    def get_commands(self):
        return commands

    def interactive(self):
        console_module = load_console_module()
        console_module.__main__()

    def prompt(self, pr):
        console_module = load_console_module()
        console_module.prompt = pr
        run_console_function("get_input")
        console_module.__main__()

    def run(self, packet):
        os.system(f"python3 $INTFRAMEWORK_PATH/remote.py {packet}")

    def read(self):
        with open("intconsoleV4.py") as file:
            return file.read()

# Modules Class
class modules:
    def __init__(self):
        self.prog = "inttable.py"
        self.meta = {
            "author": "@intikam21",
            "most_used": "exploit",
            "parser": "no parser!",
            "var": 5
        }

    def use(self, module):
        execute_command(f"use {module}")

    def show_exploits(self):
        execute_command("show exploits")

    def execute_get_input(self, module):
        run_console_function("get_input", cdn=module)

    def login(self, username, password):
        run_console_function("login", username, password)

    def run_exploit(self):
        execute_command("exploit")

    def wifi_scan(self):
        execute_command("wifi_scan")

    def load_plugins(self, plugin_path):
        execute_command(f"load_plugins {plugin_path}")

    def run_plugins(self, command, *args):
        execute_command(f"run_plugins {command} {args}")

    def list_plugins(self):
        execute_command("list_plugins")

    def check(self, ip):
        run_console_function("check_ip", ip)

# Core Class
class core:
    def activate(self, rate):
        global rater
        if not rate:
            print("enter the rate please!")
        elif rate == "root":
            rater = "root"
            print("user mod activated")
        elif rate == "dev":
            rater = "dev"
            print("developer mode activated!")

    def console_exit(self):
        exit()

    def pass_card(self):
        pass

# Config Class
class config:
    def set(self, value, value2):
        if value == "LHOSTS":
            global LHOSTS
            LHOSTS = value2
            print(f"LHOSTS -> {value2}")
        elif value == "LPORTS":
            global LPORTS
            LPORTS = value2
            print(f"LPORTS -> {value2}")
        else:
            print(f"{value} -> {value2}")

# Exploit Class
class exploit:
    def __init__(self):
        self.prog = "inttable.py"
        self.meta = { 
            "author": "@intSpLoiT Framework",
            "most_used": "run",
            "parser": f"python3 $intmodules_path/exploits/multi/handler/inthandlermodule.py --lhost {LHOSTS} --lport {LPORTS} --output-apk virus --original-apk intframework_virus.apk",
            "var": 4
        }

    def run(self, exp_dir, exploit_name, args=None):
        os.chdir("$intmodules_path/exploits")
        print("running "+exploit_name)
        os.system(f"cd {exp_dir} && python3 {exploit_name} {args if args else ''}")

    def shell(self):
        os.system("cd $intmodules_path/exploits/multi/handler/ && inthandler.py")