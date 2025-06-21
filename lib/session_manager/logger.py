import time

def log(event, addr=None):
    timestamp = time.strftime("[%Y-%m-%d %H:%M:%S]")
    with open("lib/session_manager/session.log", "a") as log_file:
        entry = f"{timestamp} {event}"
        if addr:
            entry += f" from {addr[0]}:{addr[1]}"
        log_file.write(entry + "\n")