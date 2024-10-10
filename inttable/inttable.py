"""
Examples:
	inttable.core.activate("dev") or inttable.core.activate("root") If you don't do this, you won't be able to use the console.
	inttable.exploit.run("intframework/modules/exploits/dropleganger", "dropleganger.py", args=None)
	inttable.console.run("load_plugins (plugin path) ")
	inttable.console.write("exploit") 
"""
import importlib.util
def banner(hide=False):
	if hide == 'False':
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
    
global rater
rater = None
global LHOSTS
LHOSTS = None
global LPORTS
LPORTS = None
def load_console_module():
    spec = importlib.util.spec_from_file_location("intconsole_module", "intframework/intconsoleV4.py")
    console_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(console_module)
    return console_module

def run_console_function(function_name, *args, **kwargs):
    # İntconsoleV4.py modülünü yükle
    console_module = load_console_module()

    # Fonksiyonun var olup olmadığını kontrol et
    if hasattr(console_module, function_name):
        function_to_run = getattr(console_module, function_name)
        result = function_to_run(*args, **kwargs)
        return result
    else:
        return f"Fonksiyon '{function_name}' bulunamadı."

def execute_command(command):
    # İntconsoleV4.py modülünü yükle
    console_module = load_console_module()

    # help_input değişkenine komut atayıp çalıştır
    console_module.help_input = command
    console_module.__main__()


commands = ["load_console_module", "run_console_function", "execute_command", "use", "show_exploits", "run_exploit", "list_plugins", "check", "wifi_scan", "login", "execute_get_input", "run_exploit"]

class console:
	global rater
	if rater == "root" or "dev":
		pass
	else:
		exit()
	def init(self):
		prog = "inttable.py"
		meta = {
		author: "@intikam21",
		most_used: "execute_command",
		"int_commands": self.get_commands(),
		parser: "no parser!",
		var: 20
		}
	def get_commands(self):
		commands = ["load_console_module", "run_console_function", "execute_command", "use", "show_exploits", "run_exploit", "list_plugins", "check", "wifi_scan", "login", "execute_get_input", "run_exploit"]
		return commands
	def write(packet):
		with open(".int4", "a") as magic:
			magic.write(packet + "\n")
	def interactive():
		console_module = load_console_module()
		console_module.__main__()
	def prompt(pr):
		console_module = load_console_module()
		console_module.prompt = pr
		run_console_function(get_input, )
		console_module.__main__()
	def run(packet):
	   console_module = load_console_module()
	   console_module.help_input = packet
	   console_module.__main__()
	def read():
		with open("intconsoleV4.py") as file:
			file.read()
			return file.read
		return os.sys.stdout
class modules:
	def init(self):
		prog = "inttable.py"
		meta = {
		author: "@intikam21",
		most_used: "exploit",
		parser: "no parser!",
		var: 5
		}
	def use(module):
		execute_command(f"use {module}")
	def show_exploits():
		execute_command("show exploits")
	def execute_get_input(module):
		run_console_function(get_input, cdn=module)
	def login(username, password):
		run_console_function(login, username, password)
	def run_exploit():
		execute_command("exploit")
	def wifi_scan():
		execute_command("wifi_scan")
	def load_plugins(plugin_path):
		execute_command(f"load_plugins {plugin_path}")
	def run_plugins(command, *args):
		execute_command("run_plugins {command} {args}")
	def list_plugins():
		execute_command("list_plugins")
	def check(ip):
		run_console_function(check_ip, ip)
class core:
	def activate(rate):
		if not rate:
			print("enter the rate please!")
		if rate == "root":
			rater = "root"
			print("user mod activated")
		if rate == "dev":
			rater = "dev"
			print("developer mode activated!")
	def console_exit():
		exit()
	def pass_card():
		pass
class config:
	"""
	config for a settings example set("LHOSTS", "127.0.0.1")
	"""
	def set(value, value2):
		if value == "LHOSTS":
			LHOSTS = value2
			print(f"LHOSTS -> {value2}")
		if value == "LPORTS":
			LPORTS = value2
			print(f"LPORTS -> {value2}")
		else:
			print(f"{value} -> {value2}")
			
class exploit:
	def init():
		prog = "inttable.py"
		meta = { 
		author: "@intikam21",
		most_used: "run",
		parser: f"python3 $intmodules_path/exploits/multi/handler/inthandlermodule.py --lhost {LHOSTS} --lport {LPORTS} --output-apk virus --original-apk intframework_virus.apk",
		var: 4
		}
	def run(exp_dir, exploit_name, args=None):
		os.chdir("$intmodules_path/exploits")
		print("running "+exploit_name)
		os.system(f"cd {exp_dir} && python3 {exploit_name} {args if args else None}")
	def shell():
		os.system("cd $intmodules_path/exploits/multi/handler/ && inthandler.py")
	