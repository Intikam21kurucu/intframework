

import os
import sys
import json
import uuid
import time
import socket
import random
import hashlib
import platform
import datetime
import shutil
from pathlib import Path

# === Terminal Styles and Colors === #
class Style:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'

# === Terminal Output Functions === #
def print_info(text: str, prefix: str = "[INFO]", newline: bool = True):
    output = f"{Style.BLUE}{prefix}{Style.RESET} {text}"
    print(output if newline else output, end='')

def print_success(text: str, prefix: str = "[ OK ]", newline: bool = True):
    output = f"{Style.GREEN}{prefix}{Style.RESET} {text}"
    print(output if newline else output, end='')

def print_warning(text: str, prefix: str = "[WARN]", newline: bool = True):
    output = f"{Style.YELLOW}{prefix}{Style.RESET} {text}"
    print(output if newline else output, end='')

def print_error(text: str, prefix: str = "[FAIL]", exit_after: bool = False):
    print(f"{Style.RED}{prefix}{Style.RESET} {text}")
    if exit_after:
        sys.exit(1)

def print_debug(text: str, enable: bool = False):
    if enable:
        print(f"{Style.MAGENTA}[DEBUG]{Style.RESET} {text}")

def print_banner(title: str, color: str = Style.CYAN, padding: int = 4):
    border = "=" * (len(title) + (padding * 2))
    print(f"{color}{border}\n{' ' * padding}{title}{' ' * padding}\n{border}{Style.RESET}")

# === IP and Port Validations === #
def is_valid_ip(ip: str, allow_local: bool = True) -> bool:
    try:
        socket.inet_aton(ip)
        if not allow_local and ip.startswith("127."):
            return False
        return True
    except socket.error:
        return False

def is_valid_port(port: int, reserved_check: bool = True) -> bool:
    if not isinstance(port, int):
        try:
            port = int(port)
        except:
            return False
    if reserved_check and port < 1024:
        return False
    return 1 <= port <= 65535

# === System Information === #
def get_os_info(short: bool = False) -> str:
    if short:
        return platform.system()
    return f"{platform.system()} {platform.release()} ({platform.machine()})"

def get_python_version(full: bool = False) -> str:
    return sys.version if full else sys.version.split()[0]

# === UUID / Random Generators === #
def generate_uuid(version: int = 4) -> str:
    if version == 1:
        return str(uuid.uuid1())
    return str(uuid.uuid4())

def generate_session_id(prefix: str = "") -> str:
    sid = datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S%f")
    return f"{prefix}{sid}" if prefix else sid

def random_string(length: int = 12, charset: str = None) -> str:
    if charset is None:
        charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choices(charset, k=length))

# === File & Directory Functions === #
def file_exists(path: str, readable: bool = False) -> bool:
    if not os.path.isfile(path):
        return False
    return os.access(path, os.R_OK) if readable else True

def dir_exists(path: str, writable: bool = False) -> bool:
    if not os.path.isdir(path):
        return False
    return os.access(path, os.W_OK) if writable else True

def ensure_directory(path: str, verbose: bool = False):
    try:
        Path(path).mkdir(parents=True, exist_ok=True)
        if verbose:
            print_success(f"Directory created: {path}")
    except Exception as e:
        print_error(f"Failed to create directory: {e}")

def read_file(path: str, strip: bool = False, default: str = "") -> str:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
            return content.strip() if strip else content
    except Exception as e:
        print_error(f"Failed to read file: {e}")
        return default

def write_file(path: str, data: str, overwrite: bool = True, silent: bool = False):
    try:
        mode = 'w' if overwrite else 'a'
        with open(path, mode, encoding='utf-8') as f:
            f.write(data)
    except Exception as e:
        if not silent:
            print_error(f"Failed to write file: {e}")

# === JSON Functions === #
def save_json(data: dict, path: str, indent: int = 4):
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=indent)
    except Exception as e:
        print_error(f"Failed to save JSON: {e}")

def load_json(path: str, default: dict = {}) -> dict:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print_error(f"Failed to load JSON: {e}")
        return default

# === Hash Functions === #
def hash_file(path: str, algo: str = 'sha256', return_bytes: bool = False) -> str:
    try:
        h = hashlib.new(algo)
        with open(path, 'rb') as f:
            for chunk in iter(lambda: f.read(8192), b''):
                h.update(chunk)
        return h.digest() if return_bytes else h.hexdigest()
    except Exception as e:
        print_error(f"Failed to compute hash: {e}")
        return b'' if return_bytes else ""

# === Command Availability Checker === #
def is_command_available(command: str, platform_check: bool = False) -> bool:
    if platform_check and os.name == "nt":
        return False
    return shutil.which(command) is not None

# === Time & Terminal === #
def get_timestamp(fmt: str = "%Y-%m-%d %H:%M:%S") -> str:
    return datetime.datetime.now().strftime(fmt)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def sleep(sec: float, interrupt_msg: str = "Interrupted by user."):
    try:
        time.sleep(sec)
    except KeyboardInterrupt:
        print_warning(interrupt_msg)