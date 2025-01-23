import os
import subprocess
import logging
import argparse
import time
import platform
from colorama import init, Fore

# Colorama Initialization
init(autoreset=True)

# Logger Setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def get_os_type():
    """Returns the OS type (Windows, Linux, MacOS, or Android)."""
    os_type = platform.system().lower()
    if "win" in os_type:
        return "windows"
    elif "linux" in os_type:
        return "linux"
    elif "darwin" in os_type:
        return "macos"
    elif "android" in os_type:
        return "android"
    return "unknown"

def execute_file(file_path, interactive=False, hidden=False, work_dir=None, priority=None, user=None, delay=None, verbose=False):
    """
    Executes a file on the target system with advanced options like working directory, priority, user, delay, and verbosity.
    """
    os_type = get_os_type()

    try:
        if not os.path.exists(file_path):
            print(Fore.RED + "[-] File not found.")
            return

        # Prepare the command based on the OS type
        command = file_path

        if os_type == "windows":
            # Windows: If the file is .exe, use start to run
            if file_path.endswith(".exe"):
                command = f"start {file_path}"
            elif file_path.endswith(".bat") or file_path.endswith(".cmd"):
                command = f"cmd /c {file_path}"
            else:
                # Run interactively on Windows
                if interactive:
                    command = f"cmd /K {file_path}"
                else:
                    command = file_path

        elif os_type == "linux" or os_type == "macos" or os_type == "android":
            # Linux, macOS, and Android (Unix-like systems)
            if file_path.endswith(".sh"):
                # For shell scripts
                if hidden:
                    command = f"bash {file_path} > /dev/null 2>&1 &"  # Run in the background
                else:
                    command = f"bash {file_path}"
            elif file_path.endswith(".py"):
                # For Python scripts
                command = f"python3 {file_path}"
            elif file_path.endswith(".c") or file_path.endswith(".cpp"):
                # For C or C++ executables, compile and run (Linux/macOS/Android)
                compiled_file = file_path.replace(".c", "").replace(".cpp", "")  # Remove extension for output
                compile_command = f"gcc {file_path} -o {compiled_file}"
                subprocess.run(compile_command, shell=True)
                command = f"./{compiled_file}"
            elif file_path.endswith(".exe"):
                # For .exe files (Windows executables), handle on Linux/macOS/Android using Wine
                if os_type != "windows":
                    command = f"wine {file_path}"

        if verbose:
            logger.info(Fore.YELLOW + f"[+] Executing command: {command}")

        # If a delay is provided, wait before executing
        if delay:
            logger.info(Fore.YELLOW + f"Waiting for {delay} seconds before execution...")
            time.sleep(delay)

        if work_dir:
            # Change to the working directory before execution
            os.chdir(work_dir)
            logger.info(Fore.YELLOW + f"Changed working directory to {work_dir}")

        # Execute the command
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = process.communicate()

        if verbose:
            if out:
                print(Fore.GREEN + "[+] Output:")
                print(out.decode())
            if err:
                print(Fore.RED + "[-] Error:")
                print(err.decode())

        if process.returncode == 0:
            logger.info(Fore.GREEN + "[+] File executed successfully.")
        else:
            logger.error(Fore.RED + f"[-] Error executing file: {process.returncode}")
    
    except Exception as e:
        logger.error(Fore.RED + f"[-] Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="Execute any file (Python, C, EXE, SH, etc.) with advanced options.")
    parser.add_argument("-f", "--file", required=True, help="File to execute")
    parser.add_argument("-i", "--interactive", action="store_true", help="Run interactively (for Windows only)")
    parser.add_argument("-H", "--hidden", action="store_true", help="Run the file hidden")
    parser.add_argument("-d", "--work_dir", help="Working directory for the file execution")
    parser.add_argument("-p", "--priority", help="Process priority (not used yet)")
    parser.add_argument("-u", "--user", help="User to execute as (root or non-root)")
    parser.add_argument("-t", "--delay", type=int, help="Delay before execution")
    parser.add_argument("-v", "--verbose", action="store_true", help="Show verbose output")

    args = parser.parse_args()

    execute_file(args.file, args.interactive, args.hidden, args.work_dir, args.priority, args.user, args.delay, args.verbose)

if __name__ == "__main__":
    main()