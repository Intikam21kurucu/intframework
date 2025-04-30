# -*- coding: utf-8 -*-
from lib.int4.session_manager import SessionManager

# Instantiate the SessionManager
session_manager = SessionManager()

def session_command(help_input):
    """
    Handle session-related commands similar to metasploit's 'session' command.
    
    :param help_input: The user's command input string
    """
    if help_input.startswith("session"):
        d = help_input[8:].strip()

        if d == "-l":
            # List all sessions
            sessions = session_manager.list_sessions()
            if not sessions:
                print("No active sessions.")
            else:
                for session_id in sessions:
                    print(f"Session ID: {session_id}")
                    session_modules = session_manager.list_modules_in_session(session_id)
                    if session_modules:
                        print(f"Modules: {', '.join(session_modules)}")
                    else:
                        print("No modules in this session.")

        elif d.startswith("-i"):
            # Interact with a specific session
            session_id = d[3:].strip()
            if session_manager.has_session(session_id):
                # Switching to the session
                session_manager.switch_session(session_id)
                print(f"Session {session_id} is now active.")
            else:
                print(f"Session {session_id} does not exist.")

        elif d.startswith("-k"):
            # Kill a specific session
            session_id = d[3:].strip()
            if session_manager.has_session(session_id):
                session_manager.remove_session(session_id)
                print(f"Session {session_id} has been terminated.")
            else:
                print(f"Session {session_id} does not exist.")

        elif d == "-h":
            # Show help message
            print("""
            Session Command Options:
            - session -l          : List all active sessions.
            - session -i <ID>     : Interact with a specific session by ID.
            - session -k <ID>     : Kill (terminate) a session by ID.
            - session -h          : Show this help message.
            """)

        else:
            print("Invalid session command. Use 'session -h' for help.")

# Example usage of the session command
# help_input = "session -l"  # Example: List all sessions
# session_command(help_input)

# To interact with a session, use "session -i <session_id>"
# To kill a session, use "session -k <session_id>"
# To get help, use "session -h"