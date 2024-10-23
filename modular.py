import importlib
import inspect
import os
from colorama import Fore, Style

def inputer(modulepth=None):
    global prompt
    module = modulepth if modulepth else None
    prompt = (
        f"int4 module({Fore.RED + Style.BRIGHT}{module}{Style.RESET_ALL}) > " if module else
        f"int4 ({Fore.RED}modular{Style.RESET_ALL}) > "
    )

def list_module_files(directory='modules'):  # Değişiklik burada
    try:
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f.endswith('.py')]
        files = [os.path.splitext(f)[0] for f in files]
        return files
    except FileNotFoundError:
        print(f"Directory not found: {directory}")
        return []

class IntFrameworkConsole:
    def __init__(self):
        self.module = None
        self.module_name = None
        self.module_args = {}
        self.prompt = "int4 > "

    def use_module(self, module_name):
        """Modülü seçer ama çalıştırmaz."""
        try:
            self.module = importlib.import_module(f"modules.{module_name}")
            self.module_name = module_name
            self.module_args = self._get_module_args()
            inputer(module_name)
            self._print_status(f"Module selected: {module_name}")
        except ModuleNotFoundError:
            self._print_error(f"Module not found: {module_name}")

    def run_module(self):
        """Modülü çalıştırır."""
        if not self.module:
            self._print_error("You must select a module first.")
            return

        # Komut satırı argümanlarını oluştur
        args = ' '.join(f"--{arg} {value}" for arg, value in self.module_args.items() if value is not None)
        os.system(f"python3 modules/{self.module_name}.py {args}")  # Modül ismini burada kullanıyoruz.

    def _get_module_args(self):
        """Modül içindeki fonksiyonların parametrelerini alır."""
        if self.module:
            for name, obj in inspect.getmembers(self.module):
                if inspect.isfunction(obj):
                    sig = inspect.signature(obj)
                    return {param: None for param in sig.parameters}
        return {}

    def set_arg(self, arg, value):
        """Modül parametresi ayarla."""
        if arg in self.module_args:
            self.module_args[arg] = value
            self._print_status(f"{arg} = {value}")
        else:
            self._print_error(f"Invalid argument: {arg}")

    def reset_module(self):
        """Modül seçimlerini sıfırlar."""
        self.module = None
        self.module_args = {}
        inputer()
        self._print_status("Module reset. Returning to main console.")

    def help(self):
        """Kullanılabilir komutları listeler."""
        self._print_status("Available Commands:")
        print("""
    use [module]         : Select a module (but do not run)
    set [arg] [value]    : Set a module argument
    run                 : Execute the selected module
    reset               : Reset the current module
    exit                : Exit the console
    help                : Display available commands
    modules             : List available modules
    show options        : Show module options
    info [module]       : Display information about a module
    history             : Show command history
    back                : Return to main console
    check               : Check the status of the selected module
    version             : Show framework version
""")

    def show_options(self):
        """Modül seçeneklerini gösterir."""
        if self.module_args:
            self._print_status(f"Available options for module: {self.module_name}")
            for arg, value in self.module_args.items():
                print(f"{arg}: {value}")
        else:
            self._print_error("No module selected.")

    def start_console(self):
        inputer()
        command_history = []
        while True:
            user_input = input(prompt)
            args = user_input.split()
            command_history.append(user_input)

            if not args:
                continue

            command = args[0].lower()

            if command == 'use':
                if len(args) > 1:
                    self.use_module(args[1])
                else:
                    self._print_error("Please specify a module name.")
            elif command == 'set':
                if len(args) > 2:
                    self.set_arg(args[1], args[2])
                else:
                    self._print_error("Please specify an argument and value.")
            elif command == 'run':
                self.run_module()
            elif command == 'reset':
                self.reset_module()
            elif command == 'help':
                self.help()
            elif command == 'modules':
                module_files = list_module_files()
                print("Modules:  ")
                for file in module_files:
                    print(f"  - {file}")
            elif command == 'show' and len(args) > 1 and args[1] == 'options':
                self.show_options()
            elif command == 'exit':
                self._print_status("Exiting Intikam21 Framework")
                break
            else:
                self._print_error("Invalid command. Type 'help' for available commands.")

    def _print_status(self, message):
        print(f"{Fore.BLUE}[*] {message}{Style.RESET_ALL}")

    def _print_error(self, message):
        print(f"{Fore.RED}[-] {message}{Style.RESET_ALL}")

    def _print_good(self, message):
        print(f"{Fore.GREEN}[+] {message}{Style.RESET_ALL}")

# Konsol başlatma
if __name__ == "__main__":
    console = IntFrameworkConsole()
    console.start_console()