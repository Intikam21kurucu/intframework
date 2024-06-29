import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import subprocess
import time
from tkhtmlview import HTMLLabel

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
        # intOffical simgesi
        self.create_icon(20, 20, "intOffical", self.open_window, "int.png")

        # İNTCONSOLE simgesi
        self.create_icon(200, 20, "İNTCONSOLE", self.open_intconsole, "intconsole.png")

        # Settings simgesi
        self.create_icon(480, 20, "Settings", self.open_settings, "dos.png")

        # Chrome simgesi
        self.create_icon(760, 20, "Chrome", self.open_chrome, "chrome.png")

    def create_icon(self, x, y, text, command, image_file):
        try:
            icon_image = Image.open(f"/storage/emulated/0/int/{image_file}").resize((64, 64), Image.LANCZOS)
            icon_photo = ImageTk.PhotoImage(icon_image)
            icon_button = tk.Button(self, image=icon_photo, command=command, bd=0)
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

        # Açık uygulamalar için çerçeve
        self.open_apps_frame = tk.Frame(taskbar, bg="gray")
        self.open_apps_frame.pack(side=tk.LEFT, padx=10)

        # Saat göstergesi
        self.clock_label = tk.Label(taskbar, bg="gray", fg="white", font=("Helvetica", 12))
        self.clock_label.pack(side=tk.RIGHT, padx=10)
        self.update_clock()

        # WiFi göstergesi (simge yer tutucu)
        wifi_image = Image.open("/storage/emulated/0/int/IMG_20240625_202557.jpg").resize((24, 24), Image.LANCZOS)
        wifi_photo = ImageTk.PhotoImage(wifi_image)
        wifi_label = tk.Label(taskbar, image=wifi_photo, bg="gray")
        wifi_label.image = wifi_photo
        wifi_label.pack(side=tk.RIGHT, padx=10)

        # Diğer küçük uygulamalar (yer tutucu)
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

        # Uygulama listesi
        apps = ["Notepad", "Calculator", "Terminal", "İntconsole"]
        for app in apps:
            button = tk.Button(self.start_menu, text=app, command=lambda a=app: self.open_application(a))
            button.pack(fill=tk.X)

        # Arama motoru
        search_label = tk.Label(self.start_menu, text="Search Applications:")
        search_label.pack(pady=5)
        search_entry = tk.Entry(self.start_menu)
        search_entry.pack(fill=tk.X, padx=10)
        search_entry.bind("<Return>", lambda event: self.search_applications(search_entry.get()))

    def open_application(self, app):
        if app == "Notepad":
            self.open_notepad()
        elif app == "Calculator":
            self.open_calculator()
        elif app == "Terminal":
            self.open_terminal()
        elif app == "İntconsole":
                self.open_intconsole
    def open_intconsole(self):
        try:
            new_window = tk.Toplevel(self)
            new_window.title("İNTCONSOLE")
            new_window.geometry("600x400")
            change_bg_button = tk.button(new_window, text="start intconsole", command=self.start)
            def start(self):
                    subprocess.run([new_window, "python3", "intconsoleV3.py"])
        except FileNotFoundError:
            messagebox.showerror("Error", "intconsoleV3.py not found.")
        except Exception as e:
            messagebox.showerror("Error", f"The error has occurred: {str(e)}")
        self.add_to_taskbar(new_window, "İNTCONSOLE")

    def open_settings(self):
        new_window = tk.Toplevel(self)
        new_window.title("Settings")
        new_window.geometry("400x300")

        change_bg_button = tk.Button(new_window, text="Change Background", command=self.change_background)
        change_bg_button.pack(pady=20)
        self.add_to_taskbar(new_window, "Settings")

    def open_notepad(self):
        new_window = tk.Toplevel(self)
        new_window.title("Notepad")
        new_window.geometry("600x400")

        text_area = tk.Text(new_window)
        text_area.pack(expand=True, fill=tk.BOTH)
        self.add_to_taskbar(new_window, "Notepad")

    def open_calculator(self):
        new_window = tk.Toplevel(self)
        new_window.title("Calculator")
        new_window.geometry("300x400")
        # Ekran
        display = tk.Entry(new_window, width=28, font=('Arial', 24), borderwidth=2, relief='solid')
        display.grid(row=0, column=0, columnspan=4)

        # Butonları ekleyin
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
            tk.Button(new_window, text=button, width=5, height=2, font=('Arial', 18), command=action).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1
        self.add_to_taskbar(new_window, "Calculator")
    def click_event(self, key, display):
        current_text = display.get()
        if key == '=':
            try:
                result = str(eval(current_text))
                display.delete(0, tk.END)
                display.insert(tk.END, result)
            except:
                display.delete(0, tk.END)
                display.insert(tk.END, "Error")
        else:
            display.insert(tk.END, key)
BOTH

    def open_terminal(self):
            subprocess.run["python3", "TERM.py"]

    def open_window(self):
        new_window = tk.Toplevel(self)
        new_window.title("My Computer")
        new_window.geometry("700x350")

        label = tk.Label(new_window, text="This is a Computer")
        label.pack(pady=20)
        self.add_to_taskbar(new_window, "My Computer")

    def open_chrome(self):
        new_window = tk.Toplevel(self)
        new_window.title("Chrome")
        new_window.geometry("800x600")

        html_content = """
        <html>
        <head>
        <title>Chrome</title>
        </head>
        <body>
        <h1>Welcome to Chrome</h1>
        <p>This is a basic browser using for intikam21 users.</p>
        <a href="https://www.google.com">Go to Google</a>
        </body>
        </html>
        """

        html_label = HTMLLabel(new_window, html=html_content)
        html_label.pack(expand=True, fill=tk.BOTH)
        self.add_to_taskbar(new_window, "Chrome")

    def add_to_taskbar(self, window, name):
        # Ekleme fonksiyonu
        self.open_windows.append((window, name))
        button = tk.Button(self.open_apps_frame, text=name, command=lambda: self.bring_to_front(window))
        button.pack(side=tk.LEFT, padx=5)

    def bring_to_front(self, window):
        # Pencereyi öne getir
        window.lift()

    def change_background(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            image = Image.open(file_path)
            image = image.resize((2099.9, 1050), Image.LANCZOS)
            self.background_image = ImageTk.PhotoImage(image)
            self.background_label.config(image=self.background_image)

if __name__ == "__main__":
    app = VirtualPC()
    app.mainloop()