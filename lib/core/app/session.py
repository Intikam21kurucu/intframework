import time

class Session:
    def __init__(self, session_id, exploit, payload, target_ip, target_port, user, arch, platform):
        self.session_id = session_id
        self.exploit = exploit
        self.payload = payload
        self.target_ip = target_ip
        self.target_port = target_port
        self.user = user
        self.arch = arch
        self.platform = platform
        self.start_time = time.strftime("%Y-%m-%d %H:%M:%S")
        self.active = True
        self.log_session()

    def log_session(self):
        with open("session.int4", "a") as log_file:
            log_file.write(f"Session {self.session_id} started: {self.get_info()}\n")

    def get_info(self):
        return {
            "Session ID": self.session_id,
            "Exploit": self.exploit,
            "Payload": self.payload,
            "Target IP": self.target_ip,
            "Target Port": self.target_port,
            "User": self.user,
            "Arch": self.arch,
            "Platform": self.platform,
            "Start Time": self.start_time,
            "Status": "Active" if self.active else "Closed"
        }

    def close(self):
        self.active = False
        with open("session.int4", "a") as log_file:
            log_file.write(f"Session {self.session_id} closed.\n")


class SessionManager:
    def __init__(self):
        self.sessions = {}
        self.next_id = 1
        self.current_session = None

    def create_session(self, exploit, payload, target_ip, target_port, user, arch, platform):
        session = Session(self.next_id, exploit, payload, target_ip, target_port, user, arch, platform)
        self.sessions[self.next_id] = session
        self.next_id += 1
        return session

    def list_sessions(self):
        if not self.sessions:
            print("No active sessions.")
            return
        print("\nID | Exploit      | Payload       | Target IP      | Port  | User    | Arch    | Platform    | Status")
        print("-" * 100)
        for session in self.sessions.values():
            info = session.get_info()
            print(f"{info['Session ID']:<3} | {info['Exploit']:<12} | {info['Payload']:<12} | {info['Target IP']:<15} | {info['Target Port']:<5} | {info['User']:<7} | {info['Arch']:<7} | {info['Platform']:<10} | {info['Status']}")

    def get_session_info(self, session_id):
        session = self.sessions.get(session_id)
        if session:
            for key, value in session.get_info().items():
                print(f"{key}: {value}")
        else:
            print("Session not found.")

    def close_session(self, session_id):
        session = self.sessions.get(session_id)
        if session:
            session.close()
            print(f"Session {session_id} closed.")
        else:
            print("Session not found.")

    def switch_session(self, session_id):
        if session_id in self.sessions and self.sessions[session_id].active:
            self.current_session = session_id
            print(f"Switched to session {session_id}.")
        else:
            print("Session not found or inactive.")


# Örnek Kullanım
if __name__ == "__main__":
    pass
    # manager = SessionManager()
    # manager.create_session("exploit1", "payload1", "192.168.1.10", 4444, "root", "x86", "linux")
    # manager.create_session("exploit2", "payload2", "192.168.1.20", 5555, "admin", "arm", "windows")
    # manager.list_sessions()
    # print("\nSwitching to Session 2:")
    # manager.switch_session(2)
    # print("\nSession 1 Details:")
    # manager.get_session_info(1)
    # print("\nClosing Session 1...")
    # manager.close_session(1)
    # manager.list_sessions()
