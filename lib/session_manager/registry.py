sessions = {}
session_counter = 0
session_names = {}  # session_id: name mapping

def set_session_name(session_id, name):
    if session_id in sessions:
        session_names[session_id] = name
        return True
    return False

def get_session_name(session_id):
    return session_names.get(session_id, "")
    
def increment_session_id():
    global session_counter
    session_counter += 1
    return session_counter

def register_session(session_id, session_thread):
    sessions[session_id] = session_thread

def get_session(session_id):
    return sessions.get(session_id)

def list_sessions():
    return sessions

def remove_session(session_id):
    if session_id in sessions:
        del sessions[session_id]