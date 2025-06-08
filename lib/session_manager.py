import socket
import threading
import sys
import time

sessions = []

class Session:
    def __init__(self, session_id, ip, port, conn):
        self.id = session_id
        self.ip = ip
        self.port = port
        self.conn = conn

    def send(self, data):
        try:
            self.conn.send(data.encode())
        except:
            pass

    def receive(self, size=1024):
        try:
            return self.conn.recv(size).decode(errors="ignore")
        except:
            return ""

    def close(self):
        try:
            self.conn.close()
        except:
            pass

def add_session(ip, port, conn):
    try:
        if not (ip.startswith("127.0.0.1") or ip.startswith("192.168.1.")):
            print(f"[!] Rejected: {ip} is not in allowed IP range.")
            conn.close()
            return

        conn.settimeout(3)
        banner = conn.recv(128).decode(errors="ignore").lower()
        honeypot_keywords = ["honeypot", "monitor", "log", "welcome"]

        if any(keyword in banner for keyword in honeypot_keywords):
            print(f"[!] Suspicious connection detected from {ip} -> {banner.strip()}")
            conn.close()
            return

        session_id = len(sessions)
        session = Session(session_id, ip, port, conn)
        sessions.append(session)
        print(f"[+] Session added: {session_id} ({ip}:{port})")

    except Exception as e:
        print(f"[!] Could not add session: {e}")
        try:
            conn.close()
        except:
            pass

def list_sessions():
    if not sessions:
        print("[-] No active sessions.")
        return
    print("ID | IP Address      | Port")
    print("---|-----------------|------")
    for s in sessions:
        print(f"{s.id:<3}| {s.ip:<16} | {s.port}")

def print_session_help():
    print("""
Session commands:
  session list              -> List active sessions
  session -i <id>           -> Interact with specified session
  session -k <id>           -> Kill specified session
  session -h                -> Show this help
""")

def interact_with_session(session):
    print(f"[~] Connected to session {session.id} ({session.ip}:{session.port}). Type 'exit' to quit.")
    try:
        while True:
            cmd = input(f"Session-{session.id}> ")
            if cmd.strip().lower() == "exit":
                break
            session.send(cmd + "\n")
            response = session.receive(4096)
            print(response)
    except KeyboardInterrupt:
        print("\n[!] User interrupted session.")
    except Exception as e:
        print(f"[!] Error during interaction: {e}")

def kill_session(session_id):
    if 0 <= session_id < len(sessions):
        sessions[session_id].close()
        del sessions[session_id]
        # Re-index session IDs
        for i, s in enumerate(sessions):
            s.id = i
        print(f"[+] Session {session_id} killed.")
    else:
        print("[!] Invalid session ID.")

def handle_session_command(command):
    parts = command.strip().split()
    if len(parts) == 0:
        return

    if parts[0] != "session":
        return

    if len(parts) == 1 or parts[1] == "-h":
        print_session_help()
        return

    if parts[1] == "list":
        list_sessions()
        return

    if parts[1] == "-i":
        if len(parts) != 3:
            print("[!] Usage: session -i <id>")
            return
        try:
            sid = int(parts[2])
            if 0 <= sid < len(sessions):
                interact_with_session(sessions[sid])
            else:
                print("[!] Invalid session ID.")
        except:
            print("[!] Session ID must be a number.")
        return

    if parts[1] == "-k":
        if len(parts) != 3:
            print("[!] Usage: session -k <id>")
            return
        try:
            sid = int(parts[2])
            kill_session(sid)
        except:
            print("[!] Session ID must be a number.")
        return

    print("[!] Invalid session command. Use 'session -h' for help.")

# --- Server thread ---

def server_thread(ip, port):
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind((ip, port))
    server_sock.listen(5)
    print(f"[+] Server listening on {ip}:{port}")

    while True:
        try:
            client_sock, addr = server_sock.accept()
            ip_client, port_client = addr
            print(f"[+] Server accepted connection from {ip_client}:{port_client}")

            # Banner gönder (basit hoşgeldin mesajı)
            client_sock.send(b"Welcome to intSpLoiT honeypot!\n")

            # Burada direkt session ekleme yerine manuel kontrol yaptık, eğer istersek
            # add_session fonksiyonunu çağırabiliriz.
            # Örnek:
            # add_session(ip_client, port_client, client_sock)

            # Ancak demo için basit echo server olarak devam edelim:
            threading.Thread(target=handle_client_connection, args=(client_sock, ip_client, port_client), daemon=True).start()

        except Exception as e:
            print(f"[!] Server error: {e}")

def handle_client_connection(conn, ip, port):
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"[Server] Received from {ip}: {data.decode(errors='ignore').strip()}")
            # Echo yap
            conn.sendall(data)
    except Exception:
        pass
    finally:
        conn.close()
        print(f"[+] Connection from {ip}:{port} closed")

# --- Client tarafında tek session oluşturma ---

def create_single_session(target_ip, target_port):
    try:
        threading.Thread(target=server_thread, args=(target_ip, target_port), daemon=True).start()
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target_ip, target_port))

        session = Session(0, target_ip, target_port, sock)
        sessions.clear()
        sessions.append(session)
        print(f"[+] Single session 0 created with {target_ip}:{target_port}")
        return session
    except Exception as e:
        print(f"[!] Connection failed: {e}")
        return None

# --- Main ---

if __name__ == "__main__":
    IP = "127.0.0.1"
    PORT = 2023

    # Server thread başlat
    threading.Thread(target=server_thread, args=(IP, PORT), daemon=True).start()

    time.sleep(1)  # Serverin başlaması için bekle

    # Komut satırından IP ve port verilirse ona bağlanıp session aç
    if len(sys.argv) == 3:
        target_ip = sys.argv[1]
        target_port = int(sys.argv[2])
        session = create_single_session(target_ip, target_port)
        if session:
            interact_with_session(session)

    else:
        # Yoksa otomatik olarak localhost:1002'ye bağlan
        session = create_single_session(IP, PORT)
        if session:
            print("Session yönetim konsoluna hoşgeldiniz. 'session -h' yazınız yardım için.")
            try:
                while True:
                    command = input("intconsole> ").strip()
                    if command.lower() in ["exit", "quit"]:
                        break
                    handle_session_command(command)
            except KeyboardInterrupt:
                print("\n[!] Çıkış yapıldı.")