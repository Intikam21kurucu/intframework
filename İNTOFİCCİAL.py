import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import subprocess
import time
from tkhtmlview import HTMLLabel
import requests
from bs4 import BeautifulSoup

class VirtualPC(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("İNTOFİCCİAL")
        self.geometry("1024x768")

        # Arka plan resmi
        self.background_image = "/storage/emulated/0/int/int.png"
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

    def create_desktop_icons(self):
        self.create_icon(20, 20, "intOffical", self.open_window, "int.png")
        self.create_icon(200, 20, "İNTCONSOLE", self.open_intconsole, "int.png")
        self.create_icon(480, 20, "Settings", self.open_settings, "dos.png")
        self.create_icon(760, 20, "Chrome", self.open_chrome, "chrome.png")

    def create_icon(self, x, y, text, command, image_file):
        try:
            icon_image = Image.open(f"/storage/emulated/0/int/{image_file}").resize((64, 64), Image.LANCZOS)
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
            start_image = Image.open("/storage/emulated/0/int/int.png").resize((50, 50), Image.LANCZOS)
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

        wifi_image = Image.open("/storage/emulated/0/int/IMG_20240625_202557.jpg").resize((24, 24), Image.LANCZOS)
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
            subprocess.run(["python3", "intconsoleV4.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

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

        change_bg_button = tk.Button(new_window, text="Change Background", command=self.change_background)
        change_bg_button.pack(pady=20)

    def open_chrome(self):
        new_window = tk.Toplevel(self)
        new_window.title("Chrome")
        new_window.geometry("800x600")

        browser_frame = tk.Frame(new_window)
        browser_frame.pack(expand=True, fill=tk.BOTH)

        html_label = HTMLLabel(browser_frame, html="<h1>Welcome to Chrome!</h1>")
        html_label.pack(expand=True, fill=tk.BOTH)

    def open_notepad(self):
        new_window = tk.Toplevel(self)
        new_window.title("Notepad")
        new_window.geometry("600x400")

        text_area = tk.Text(new_window)
        text_area.pack(expand=True, fill=tk.BOTH)

    def open_calculator(self):
        new_window = tk.Toplevel(self)
        new_window.title("Calculator")
        new_window.geometry("300x400")

        display = tk.Entry(new_window, width=28, font=('Arial', 24), borderwidth=2, relief='solid')
        display.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0
        for button in buttons:
            action = lambda x=button: self.click_event(x, display)
            tk.Button(new_window, text=button, command=action, width=5, height=2).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def click_event(self, button, display):
        if button == "=":
            try:
                result = str(eval(display.get()))
                display.delete(0, tk.END)
                display.insert(0, result)
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")
        else:
            current_text = display.get()
            display.delete(0, tk.END)
            display.insert(0, current_text + button)

    def change_background(self):
        new_bg = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if new_bg:
            self.background_image = new_bg
            img = Image.open(new_bg)
            img = img.resize((self.winfo_width(), self.winfo_height()), Image.LANCZOS)
            self.background_label.config(image=ImageTk.PhotoImage(img))

    def open_settings(self):
        new_window = tk.Toplevel(self)
        new_window.title("Settings")
        new_window.geometry("400x300")

        change_bg_button = tk.Button(new_window, text="Change Background", command=self.change_background)
        change_bg_button.pack(pady=20)

if __name__ == "__main__":
    app = VirtualPC()
    app.mainloop()