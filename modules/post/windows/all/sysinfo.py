# -*- coding: utf-8 -*-
# Title: Get system info Windows 

import os
import platform
import subprocess
import argparse


def check_command_availability(command):
    """Check if a command is available on the system."""
    try:
        subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except FileNotFoundError:
        return False


def collect_system_info():
    """Collect basic system information."""
    print("[*] Gathering system information...")
    system_info = {
        "OS": platform.system(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Architecture": platform.architecture()[0],
        "Machine": platform.machine(),
        "Hostname": platform.node(),
        "Processor": platform.processor(),
    }

    return system_info


def list_logged_in_users():
    """List logged-in users using 'query user' or alternative method."""
    print("[*] Checking logged-in users...")
    if check_command_availability("query user"):
        try:
            output = subprocess.check_output("query user", shell=True, text=True)
            return output.strip()
        except subprocess.CalledProcessError as e:
            return f"[-] Error executing 'query user': {e}"
    else:
        return "[-] 'query user' command is not available on this system."


def list_processes():
    """List running processes using 'tasklist' or alternative method."""
    print("[*] Retrieving process list...")
    if check_command_availability("tasklist"):
        try:
            output = subprocess.check_output("tasklist", shell=True, text=True)
            return output.strip()
        except subprocess.CalledProcessError as e:
            return f"[-] Error executing 'tasklist': {e}"
    else:
        return "[-] 'tasklist' command is not available on this system."


def post_exploit_tasks(save_to_file=False):
    """Run post-exploitation tasks and return results."""
    print("[*] Starting post-exploitation tasks...")
    
    system_info = collect_system_info()
    users = list_logged_in_users()
    processes = list_processes()

    results = {
        "SystemInfo": system_info,
        "LoggedInUsers": users,
        "Processes": processes,
    }

    if save_to_file:
        with open("post_exploit_results.txt", "w") as f:
            f.write("[*] System Information\n")
            for key, value in system_info.items():
                f.write(f"{key}: {value}\n")

            f.write("\n[*] Logged-In Users\n")
            f.write(users + "\n")

            f.write("\n[*] Running Processes\n")
            f.write(processes + "\n")

        print("[+] Results saved to 'post_exploit_results.txt'.")

    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Windows Post Exploitation Script")
    parser.add_argument(
        "--save",
        action="store_true",
        help="Save the results to a file (default: output to terminal).",
    )
    args = parser.parse_args()

    print("[*] Windows Post Exploitation Script")
    print("[*] Running on platform:", platform.system())
    
    results = post_exploit_tasks(save_to_file=args.save)

    print("\n[*] SYSTEM INFORMATION")
    for key, value in results["SystemInfo"].items():
        print(f"{key}: {value}")

    print("\n[*] LOGGED-IN USERS")
    print(results["LoggedInUsers"])

    print("\n[*] RUNNING PROCESSES")
    print(results["Processes"])