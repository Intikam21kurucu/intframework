import os
import subprocess
import logging
import argparse
import time
from colorama import init, Fore

# Colorama Initialization
init(autoreset=True)

# Logger Setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def execute_file(file_path, interactive=False, hidden=False, work_dir=None, priority=None, user=None, delay=None, verbose=False):
    """
    Executes a file on the target system with advanced options like working directory, priority, user, delay and verbosity.
    """
    try:
        if not os.path.exists(file_path):
            print(Fore.RED + "[-] File not found.")
            return

        # Prepare the command
        command = file_path
        if interactive:
            command = f"{file_path} /K"  # For interactive mode (e.g., cmd.exe will keep open)
            if verbose:
                print(Fore.YELLOW + f"[*] Running interactively: {file_path}")

        if hidden:
            # Hide the window using 'start /min' for Windows executables
            command = f"start /min {file_path}"
            if verbose:
                print(Fore.YELLOW + f"[*] Running hidden: {file_path}")

        if work_dir:
            command = f"cd {work_dir} && {command}"
            if verbose:
                print(Fore.YELLOW + f"[*] Working directory set to: {work_dir}")

        if delay:
            if verbose:
                print(Fore.YELLOW + f"[*] Waiting for {delay} seconds before execution...")
            time.sleep(delay)

        if priority:
            priority_command = {
                'low': 'start /low',
                'normal': 'start',
                'high': 'start /high'
            }.get(priority.lower(), 'start')
            command = f"{priority_command} {command}"
            if verbose:
                print(Fore.YELLOW + f"[*] Running with {priority} priority.")

        if user:
            # Windows run as another user (requires credentials and may depend on system configuration)
            command = f"runas /user:{user} {command}"
            if verbose:
                print(Fore.YELLOW + f"[*] Running as user: {user}")

        # Execute the command
        if verbose:
            print(Fore.CYAN + f"[*] Executing command: {command}")

        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        # Displaying output
        if stdout:
            print(Fore.GREEN + f"[+] Output: {stdout.decode('utf-8')}")
        if stderr:
            print(Fore.RED + f"[-] Error: {stderr.decode('utf-8')}")

        if verbose:
            print(Fore.GREEN + f"[+] File executed successfully: {file_path}")

    except Exception as e:
        print(Fore.RED + f"[-] Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="Advanced Execute Command with Multiple Options")

    # Arguments for execution options
    parser.add_argument('-f', '--file', type=str, required=True, help="Path to the file to execute")
    parser.add_argument('-i', '--interactive', action='store_true', help="Run the file interactively")
    parser.add_argument('-H', '--hidden', action='store_true', help="Run the file hidden (minimized window)")
    parser.add_argument('-d', '--dir', type=str, help="Set working directory before executing the file")
    parser.add_argument('-p', '--priority', choices=['low', 'normal', 'high'], help="Set execution priority")
    parser.add_argument('-u', '--user', type=str, help="Run the file as a specific user (requires credentials)")
    parser.add_argument('-t', '--time', type=int, help="Delay execution by a certain number of seconds")
    parser.add_argument('-v', '--verbose', action='store_true', help="Enable verbose output to show detailed command execution")

    args = parser.parse_args()

    # Execute the file with provided options
    execute_file(args.file, interactive=args.interactive, hidden=args.hidden, work_dir=args.dir, priority=args.priority, user=args.user, delay=args.time, verbose=args.verbose)

if __name__ == "__main__":
    main()