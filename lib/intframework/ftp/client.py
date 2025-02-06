#!/usr/bin/env python3
import socket

class FtpClient:
    def __init__(self, host, port, timeout=10):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.sock = None
        self.datasocket = None
        self.banner = ""
        self.buffer = ""

    def connect(self):
        self.sock = socket.create_connection((self.host, self.port), self.timeout)
        self.banner = self.recv_response()
        return self.sock

    def data_connect(self, mode=None):
        if mode:
            res = self.send_cmd(["TYPE", mode])
            if not res.startswith("200"):
                return None

        if self.datasocket:
            self.datasocket.close()
            self.datasocket = None

        res = self.send_cmd(["PASV"])
        if not res.startswith("227"):
            return None

        # Extract host and port from the response
        start = res.find("(")
        end = res.find(")")
        if start == -1 or end == -1:
            return None
        parts = res[start + 1:end].split(",")
        datahost = ".".join(parts[:4])
        dataport = (int(parts[4]) * 256) + int(parts[5])
        self.datasocket = socket.create_connection((datahost, dataport), self.timeout)
        return self.datasocket

    def data_disconnect(self):
        if self.datasocket:
            self.datasocket.close()
            self.datasocket = None

    def connect_login(self, user, password):
        if not user or not password:
            return False

        self.connect()
        res = self.send_user(user)
        if not res.startswith(("331", "2")):
            return False

        res = self.send_pass(password)
        if not res.startswith("2"):
            return False

        return True

    def send_user(self, user):
        return self.raw_send_recv(f"USER {user}\r\n")

    def send_pass(self, password):
        return self.raw_send_recv(f"PASS {password}\r\n")

    def send_quit(self):
        return self.raw_send_recv("QUIT\r\n")

    def send_cmd(self, args):
        cmd = " ".join(args) + "\r\n"
        return self.raw_send_recv(cmd)

    def send_cmd_data(self, args, data=None, mode='a'):
        cmd_type = None
        if args[0].upper() in ["DIR", "LS"]:
            args[0] = "LIST"
            cmd_type = "get"
        elif args[0].upper() == "GET":
            args[0] = "RETR"
            cmd_type = "get"
        elif args[0].upper() == "PUT":
            args[0] = "STOR"
            cmd_type = "put"

        if not cmd_type:
            return self.send_cmd(args)

        self.data_connect(mode)

        res = self.send_cmd(args)
        if not res.startswith(("150", "125")):
            return None

        if cmd_type == "get":
            data = self.datasocket.recv(4096)
        elif cmd_type == "put" and data:
            self.datasocket.sendall(data)

        self.data_disconnect()
        return self.recv_response()

    def raw_send_recv(self, cmd):
        self.sock.sendall(cmd.encode())
        return self.recv_response()

    def recv_response(self):
        response = b""
        while True:
            data = self.sock.recv(4096)
            if not data:
                break
            response += data
            if response.endswith(b"\r\n"):
                break
        return response.decode().strip()

    def raw_send(self, cmd):
        self.sock.sendall(cmd.encode())

    def close(self):
        if self.sock:
            self.sock.close()
            self.sock = None