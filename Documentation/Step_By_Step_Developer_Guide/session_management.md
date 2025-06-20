# 🖥️ intSpLoiT Session Manager Detailed Usage & Developer Guide

This guide covers the comprehensive use and internal workings of the `SessionManager` class found in `lib/session_manager/manager.py`. It is intended for framework developers and advanced users who want to understand or extend session management capabilities.

---

## Overview

The `SessionManager` class manages all network sessions (remote connections) established to the intSpLoiT framework. It listens on a configured IP and port, accepts incoming connections, assigns unique session IDs, manages session metadata, and allows interaction with active sessions.

---

## 1. Initialization and Listener Setup

### Constructor

```python
def __init__(self):
    self.listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    self.active = False
```

Creates a TCP socket listener.

Sets SO_REUSEADDR to allow rebinding quickly after restart.

Initializes the active flag to track listener state.



---

## 2. Starting the Listener

```
def start_listener(self):
    self.listener.bind((CONFIG["LHOST"], CONFIG["LPORT"]))
    self.listener.listen()
    self.active = True
    print_success(f"Listening on {CONFIG['LHOST']}:{CONFIG['LPORT']}")
    threading.Thread(target=self.accept_loop).start()
```
Binds the socket to LHOST and LPORT from config.

Starts listening for incoming TCP connections.

Sets active = True.

Spawns a background thread to run accept_loop().



---

## 3. Accepting Incoming Connections

### Accept Loop

```
def accept_loop(self):
    from .registry import increment_session_id
    while self.active:
        conn, addr = self.listener.accept()
        session_id = increment_session_id()
        handle_new_connection(conn, addr, session_id)
```

Runs continuously while active is True.

Blocks on accept() to wait for new client connections.

Generates a unique session_id.

Calls handle_new_connection() to wrap the connection into a session object and store it in the registry.



---

## 4. Session Registry and Management

The session registry (in registry.py) stores active sessions keyed by session_id.

Each session object contains:

Connection socket (conn)

Address tuple (addr)

Status flag (alive)

Shell object for interactive control

Optional session name



### Listing Sessions

```
def list_sessions(self):
    print_info("Active sessions:")
    for sid, session in list_sessions().items():
        status = "ALIVE" if session.alive else "DEAD"
        print(f"#{sid} -> {session.addr[0]}:{session.addr[1]} :: {status}")
```

Prints all sessions with status.

Useful for monitoring current active connections.



---

## 5. Session Interaction

### Interact Method

```
def interact(self, session_id):
    session = get_session(session_id)
    if session and session.alive:
        session.shell.interact()
    else:
        print_error(f"Session {session_id} is not active.")

```

Retrieves the session by ID.

Opens an interactive shell session.

Fails gracefully if session is inactive.


### Sending Commands

```
def send_command(self, session_id, command):
    session = get_session(session_id)
    if session and session.alive:
        session.conn.sendall(command.encode())
        response = session.conn.recv(CONFIG["BUFFER_SIZE"]).decode()
        return response
    return None
```

Sends a raw command string to the remote session.

Receives up to BUFFER_SIZE bytes as response.

Returns the decoded response string or None.



---

## 6. Advanced Management Features

### Renaming Sessions

```
def rename_session(self, session_id, new_name):
    if set_session_name(session_id, new_name):
        print(f"[+] Session {session_id} renamed to '{new_name}'")
    else:
        print(f"[!] Session {session_id} not found")
```

Assigns human-readable names to sessions.

Improves usability in multi-session scenarios.


### Setting Response Timeout

```
def set_timeout(self, seconds):
    try:
        seconds = int(seconds)
        CONFIG["TIMEOUT"] = seconds
        print(f"[+] Response timeout set to {seconds} seconds.")
    except Exception:
        print("[!] Invalid timeout value.")
```

Adjusts socket timeout globally via configuration.

Important for network stability and responsiveness.


### Searching Sessions

```
def search_sessions(self, filter_str):
    results = []
    for sid, sess in list_sessions().items():
        if filter_str in sess.addr[0]:
            results.append((sid, sess))
    if results:
        print("[*] Search Results:")
        for sid, sess in results:
            print(f"#{sid} {sess.addr[0]}:{sess.addr[1]}")
    else:
        print("[!] No sessions matched the filter.")
```

Filters sessions by IP or custom attribute substring.

Useful for locating targets in large session lists.



---

## 7. Stopping the Listener

### To stop accepting new sessions:
```
manager.active = False
manager.listener.close()
```

Set active to False to break out of the accept loop.

Close the listener socket to release the port.



---

## 8. Extending SessionManager

You can extend the class to add:

Session timeout handling and automatic cleanup.

Advanced session filtering (e.g., by platform, name, activity).

Encrypted communication channels (TLS/SSL).

Persistent session storage to disk or database.

Custom session event hooks (on connect, on disconnect).



---

## 9. Best Practices and Tips

Always verify session.alive before interacting or sending commands.

Clean up dead sessions to free resources.

Use session renaming for clarity in engagements.

Adjust CONFIG["TIMEOUT"] based on network conditions.

Review and handle exceptions inside session handlers to avoid thread crashes.



---

## 10. Summary of Key Methods

### Method	Description

> start_listener()	Start listening and accept new sessions.
> accept_loop()	Internal loop for accepting connections.
> list_sessions()	Print active sessions and their status.
> interact(session_id)	Open an interactive shell for a session.
> send_command(session_id, cmd)	Send a single command and get the response.
> rename_session(session_id, name)	Rename a session for clarity.
> set_timeout(seconds)	Set global socket response timeout.
> search_sessions(filter_str)	Search sessions by filter string.
> active (attribute)	Control listener state (True/False).



---

For detailed implementation, refer to lib/session_manager/manager.py, registry.py, handler.py, and config.py.

End of Session Manager Guide.