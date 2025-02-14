import yaml
import importlib.util
import os
import glob
import json
from colorama import Fore, Style

INTFRAMEWORK_PATH = os.getenv("INTFRAMEWORK_PATH", "")

COMMANDS_JSON = "commands.json"

# ✅ YAML files -> JSON conversion
def load_and_save_configs():
    r = {}

    for yaml_file in glob.glob("plugins/*.yaml"):
        with open(yaml_file, "r", encoding="utf-8") as f:
            try:
                config = yaml.safe_load(f)
                if isinstance(config, dict) and "command_name" in config:
                    r[config["command_name"]] = config
            except yaml.YAMLError as e:
                print(f"{Fore.RED}✖ YAML Error ({yaml_file}): {e}{Style.RESET_ALL}")

    with open(COMMANDS_JSON, "w", encoding="utf-8") as json_file:
        json.dump(r, json_file, indent=4, ensure_ascii=False)

    print(f"{Fore.GREEN}✔ YAML files successfully converted to JSON!{Style.RESET_ALL}")
    return r

# ✅ Load user's library from __user__.lib
def load_user_lib(lib_path):
    if not os.path.exists(lib_path):
        print(f"{Fore.RED}✖ User library not found: {lib_path}{Style.RESET_ALL}")
        return None
    
    module_name = os.path.splitext(os.path.basename(lib_path))[0]
    
    spec = importlib.util.spec_from_file_location(module_name, lib_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    print(f"{Fore.CYAN}ℹ User library loaded: {lib_path}{Style.RESET_ALL}")
    return module

# ✅ Check if a command requires a parser
def get_parser(command_name):
    if not os.path.exists(COMMANDS_JSON):
        return False

    with open(COMMANDS_JSON, "r", encoding="utf-8") as json_file:
        commands = json.load(json_file)

    return commands.get(command_name, {}).get("com_parser", False)

# ✅ Execute payload from user-defined command
def execute_payload(command_name, *args):
    if not os.path.exists(COMMANDS_JSON):
        print(f"{Fore.RED}✖ Command JSON file not found. Run the script first!{Style.RESET_ALL}")
        return

    with open(COMMANDS_JSON, "r", encoding="utf-8") as json_file:
        commands = json.load(json_file)

    if command_name not in commands:
        print(f"{Fore.RED}✖ Command '{command_name}' not found!{Style.RESET_ALL}")
        return

    config = commands[command_name]
    lib_path = config.get("user_lib_path", "__user__.lib")

    # Replace $INTFRAMEWORK_PATH if used
    if "$INTFRAMEWORK_PATH" in lib_path:
        lib_path = lib_path.replace("$INTFRAMEWORK_PATH", INTFRAMEWORK_PATH)

    if not os.path.exists(lib_path):
        print(f"{Fore.RED}✖ User library file not found: {lib_path}{Style.RESET_ALL}")
        return

    user_lib = load_user_lib(lib_path)
    if not user_lib:
        return

    method_name = config.get("payload_method")
    params = config.get("payload_params", {})

    if not method_name:
        print(f"{Fore.YELLOW}⚠ No method specified in {lib_path}.{Style.RESET_ALL}")
        return

    # ✅ If com_parser is True, store arguments inside parser
    if config.get("com_parser", False):
        params["parser"] = list(args)

    # Call the method
    if hasattr(user_lib, method_name):
        method = getattr(user_lib, method_name)
        if callable(method):
            try:
                print(f"{Fore.BLUE}🚀 Executing '{command_name}'...{Style.RESET_ALL}")
                result = method(**params)
                print(f"{Fore.GREEN}✔ Execution completed: {result}{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}✖ Payload execution failed: {e}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}✖ '{method_name}' is not a callable function!{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}✖ Method '{method_name}' not found in {lib_path}!{Style.RESET_ALL}")

# ✅ Main function
def main():
    print(f"{Fore.BLUE}ℹ Converting YAML files to JSON...{Style.RESET_ALL}")
    load_and_save_configs()

if __name__ == "__main__":
    main()