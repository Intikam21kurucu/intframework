import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import subprocess
import time
import os
import platform
import psutil
import socket
import scapy.all as scapy  # Scapy kütüphanesi

class VirtualPC(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("İNTOFİCCİAL")
        self.geometry("1024x768")

        # Arka plan resmi
        self.background_image = None
        self.background_label = tk.Label(self)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Masaüstü simgeleri
        self.create_desktop_icons()

        # Görev çubuğu
        self.create_taskbar()

        # Başlat menüsü
        self.start_menu = None

        # Açık uygulamalar listesi
        self.open_windows = []

        # Varsayılan arka planı ayarla
        self.set_default_background()

    def create_desktop_icons(self):
        self.create_icon(20, 20, "intOffical", self.open_window, "int.png")
        self.create_icon(200, 20, "İNTCONSOLE", self.open_intconsole, "int.png")
        self.create_icon(480, 20, "Settings", self.open_settings, "dos.png")
        self.create_icon(760, 20, "Chrome", self.open_chrome, "chrome.png")
        self.create_icon(20, 100, "File Manager", self.open_file_manager, "file_manager.png")
        self.create_icon(200, 100, "Network Scanner", self.open_network_scanner, "network_scanner.png")
        self.create_icon(480, 100, "System Info", self.open_system_info, "system_info.png")
        self.create_icon(760, 100, "Network Status", self.open_network_status, "network_status.png")

    def create_icon(self, x, y, text, command, image_file):
        try:
            icon_image = Image.open(f"~/intframework/int/{image_file}").resize((64, 64), Image.LANCZOS)
            icon_photo = ImageTk.PhotoImage(icon_image)
            icon_button = tk.Button(self, image=icon_photo, command=lambda: command(text), bd=0)
            icon_button.image = icon_photo
            icon_button.place(x=x, y=y)

            icon_label = tk.Label(self, text=text, bg="white")
            icon_label.place(x=x, y=y + 70)
        except FileNotFoundError:
            messagebox.showerror("Error", f"Icon image {image_file} not found.")

    def create_taskbar(self):
        taskbar = tk.Frame(self, bg="gray", height=40)
        taskbar.pack(side=tk.BOTTOM, fill=tk.X)

        try:
            start_image = Image.open("~/intframework/int/int.png").resize((50, 50), Image.LANCZOS)
            start_photo = ImageTk.PhotoImage(start_image)
            start_button = tk.Button(taskbar, image=start_photo, command=self.show_start_menu, bd=0)
            start_button.image = start_photo
            start_button.pack(side=tk.LEFT, padx=10, pady=5)
        except FileNotFoundError:
            messagebox.showerror("Error", "Start button image not found.")

        self.open_apps_frame = tk.Frame(taskbar, bg="gray")
        self.open_apps_frame.pack(side=tk.LEFT, padx=10)

        self.clock_label = tk.Label(taskbar, bg="gray", fg="white", font=("Helvetica", 12))
        self.clock_label.pack(side=tk.RIGHT, padx=10)
        self.update_clock()

        wifi_image = Image.open("~/intframework/int/IMG_20240625_202557.jpg").resize((24, 24), Image.LANCZOS)
        wifi_photo = ImageTk.PhotoImage(wifi_image)
        wifi_label = tk.Label(taskbar, image=wifi_photo, bg="gray")
        wifi_label.image = wifi_photo
        wifi_label.pack(side=tk.RIGHT, padx=10)

        other_apps_label = tk.Label(taskbar, text="Apps", bg="gray", fg="white")
        other_apps_label.pack(side=tk.RIGHT, padx=10)

    def update_clock(self):
        current_time = time.strftime('%H:%M:%S')
        self.clock_label.config(text=current_time)
        self.after(1000, self.update_clock)

    def show_start_menu(self):
        if self.start_menu:
            self.start_menu.destroy()

        self.start_menu = tk.Toplevel(self)
        self.start_menu.title("Start Menu")
        self.start_menu.geometry("300x400+50+200")
        self.start_menu.resizable(False, False)

        apps = ["Notepad", "Calculator", "Terminal", "İntconsole", "Search"]
        for app in apps:
            button = tk.Button(self.start_menu, text=app, command=lambda a=app: self.open_application(a))
            button.pack(fill=tk.X)

    def open_application(self, app):
        if app == "Notepad":
            self.open_notepad()
        elif app == "Calculator":
            self.open_calculator()
        elif app == "Terminal":
            self.open_terminal()
        elif app == "İntconsole":
            self.open_intconsole()
        elif app == "Search":
            self.open_search()

    def open_window(self, text):
        new_window = tk.Toplevel(self)
        new_window.title(text)
        new_window.geometry("800x600")

        label = tk.Label(new_window, text=f"This is a new window: {text}.")
        label.pack(pady=20)

        text_area = tk.Text(new_window, bg="black", fg="white", wrap=tk.WORD)
        text_area.pack(expand=True, fill=tk.BOTH)

        scrollbar = tk.Scrollbar(new_window, command=text_area.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        text_area.config(yscrollcommand=scrollbar.set)

        def execute_command():
            command = text_area.get('1.0', tk.END)
            try:
                process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate()
                text_area.insert(tk.END, stdout.decode())
                if stderr:
                    text_area.insert(tk.END, stderr.decode())
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")

        execute_button = tk.Button(new_window, text="Execute Command", command=execute_command)
        execute_button.pack(pady=5)

    def open_intconsole(self):
        new_window = tk.Toplevel(self)
        new_window.title("İNTCONSOLE")
        new_window.geometry("600x400")

        console_frame = tk.Frame(new_window)
        console_frame.pack(expand=True, fill=tk.BOTH)

        text_area = tk.Text(console_frame)
        text_area.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        scrollbar = tk.Scrollbar(console_frame, command=text_area.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        text_area.config(yscrollcommand=scrollbar.set)

        def start_console():
            subprocess.Popen(["python3", "intconsoleV4.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        start_button = tk.Button(new_window, text="Start Console", command=start_console)
        start_button.pack(pady=5)

    def open_search(self):
        new_window = tk.Toplevel(self)
        new_window.title("Search")
        new_window.geometry("600x400")

        search_label = tk.Label(new_window, text="Search:")
        search_label.pack(pady=5)
        search_entry = tk.Entry(new_window)
        search_entry.pack(fill=tk.X, padx=10)
        search_entry.bind("<Return>", lambda event: self.search_web(search_entry.get()))

        self.search_result_area = tk.Text(new_window)
        self.search_result_area.pack(expand=True, fill=tk.BOTH)

    def search_web(self, query):
        search_url = f"https://www.google.com/search?q={query}"
        try:
            response = requests.get(search_url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            results = soup.find_all('div', class_='BNeawe iBp4i AP7Wnd')
            self.search_result_area.delete('1.0', tk.END)

            for result in results:
                self.search_result_area.insert(tk.END, result.get_text() + '\n')

        except requests.RequestException as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def open_settings(self):
        new_window = tk.Toplevel(self)
        new_window.title("Settings")
        new_window.geometry("400x300")

        label = tk.Label(new_window, text="Settings")
        label.pack(pady=20)

        # Arka plan değiştirme
        change_bg_button = tk.Button(new_window, text="Change Background", command=self.change_background)
        change_bg_button.pack(pady=10)

        # Dosya indirme
        download_button = tk.Button(new_window, text="Download File", command=self.download_file)
        download_button.pack(pady=10)

    def change_background(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png")])
        if file_path:
            try:
                img = Image.open(file_path).resize((self.winfo_width(), self.winfo_height()))
                self.background_image = ImageTk.PhotoImage(img)
                self.background_label.config(image=self.background_image)
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while changing background: {str(e)}")

    def download_file(self):
        url = filedialog.askstring("Download File", "Enter the URL of the file to download:")
        if url:
            file_name = url.split("/")[-1]
            save_path = filedialog.asksaveasfilename(initialfile=file_name, defaultextension=".bin")
            if save_path:
                try:
                    response = requests.get(url, stream=True)
                    response.raise_for_status()
                    with open(save_path, "wb") as file:
                        for chunk in response.iter_content(chunk_size=8192):
                            file.write(chunk)
                    messagebox.showinfo("Success", "File downloaded successfully.")
                except requests.RequestException as e:
                    messagebox.showerror("Error", f"An error occurred while downloading file: {str(e)}")

    def open_file_manager(self):
        new_window = tk.Toplevel(self)
        new_window.title("File Manager")
        new_window.geometry("800x600")

        file_listbox = tk.Listbox(new_window)
        file_listbox.pack(expand=True, fill=tk.BOTH)

        def refresh_files():
            file_listbox.delete(0, tk.END)
            for file_name in os.listdir("."):
                file_listbox.insert(tk.END, file_name)

        refresh_button = tk.Button(new_window, text="Refresh", command=refresh_files)
        refresh_button.pack(pady=5)

        refresh_files()

    def open_network_scanner(self):
        new_window = tk.Toplevel(self)
        new_window.title("Network Scanner")
        new_window.geometry("800x600")

        scan_result_area = tk.Text(new_window)
        scan_result_area.pack(expand=True, fill=tk.BOTH)

        def scan_network():
            scan_result_area.delete('1.0', tk.END)
            try:
                arp_request = scapy.ARP(pdst="192.168.1.0/24")  # Ağ aralığını uygun şekilde ayarlayın
                broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
                arp_request_broadcast = broadcast/arp_request
                answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
                for element in answered_list:
                    scan_result_area.insert(tk.END, f"IP: {element[1].psrc}, MAC: {element[1].hwsrc}\n")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred during network scan: {str(e)}")

        scan_button = tk.Button(new_window, text="Scan Network", command=scan_network)
        scan_button.pack(pady=5)

    def open_system_info(self):
        new_window = tk.Toplevel(self)
        new_window.title("System Information")
        new_window.geometry("800x600")

        system_info_area = tk.Text(new_window)
        system_info_area.pack(expand=True, fill=tk.BOTH)

        def gather_system_info():
            system_info_area.delete('1.0', tk.END)
            uname = platform.uname()
            system_info_area.insert(tk.END, f"System: {uname.system}\n")
            system_info_area.insert(tk.END, f"Node Name: {uname.node}\n")
            system_info_area.insert(tk.END, f"Release: {uname.release}\n")
            system_info_area.insert(tk.END, f"Version: {uname.version}\n")
            system_info_area.insert(tk.END, f"Machine: {uname.machine}\n")
            system_info_area.insert(tk.END, f"Processor: {uname.processor}\n")
            system_info_area.insert(tk.END, f"CPU Count: {psutil.cpu_count(logical=True)}\n")
            system_info_area.insert(tk.END, f"Memory: {psutil.virtual_memory().total / (1024 ** 3):.2f} GB\n")

        gather_system_info_button = tk.Button(new_window, text="Gather System Info", command=gather_system_info)
        gather_system_info_button.pack(pady=5)
        gather_system_info()

    def open_network_status(self):
        new_window = tk.Toplevel(self)
        new_window.title("Network Status")
        new_window.geometry("800x600")

        network_status_area = tk.Text(new_window)
        network_status_area.pack(expand=True, fill=tk.BOTH)

        def get_network_status():
            network_status_area.delete('1.0', tk.END)
            hostname = socket.gethostname()
            ip_address = socket.gethostbyname(hostname)
            network_status_area.insert(tk.END, f"Hostname: {hostname}\n")
            network_status_area.insert(tk.END, f"IP Address: {ip_address}\n")

        network_status_button = tk.Button(new_window, text="Get Network Status", command=get_network_status)
        network_status_button.pack(pady=5)

if __name__ == "__main__":
    app = VirtualPC()
    app.mainloop()