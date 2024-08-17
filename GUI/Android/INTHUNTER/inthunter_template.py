from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.core.window import Window
import subprocess

class MainApp(App):
    def build(self):
        # Ana pencere düzeni
        main_layout = FloatLayout()
        
        # Arka plan resmi
        background_image = Image(source='$INTFRAMEWORK_PATH/intframework/int/int.png', allow_stretch=True, keep_ratio=False, size_hint=(1, 1))
        main_layout.add_widget(background_image)
        
        # Butonlar yerleştirilecek container
        button_layout = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint=(0.3, 0.3), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        
        # Konsol butonu
        console_button = Button(text='Console', size_hint_y=None, height=50, background_color=(0.2, 0.2, 0.2, 1))
        console_button.bind(on_press=self.open_console)
        
        # Modül butonları
        pentesting_button = Button(text='Pentesting', size_hint_y=None, height=50, background_color=(0.2, 0.2, 0.2, 1))
        vulnerability_button = Button(text='Vulnerability', size_hint_y=None, height=50, background_color=(0.2, 0.2, 0.2, 1))
        browsing_button = Button(text='Browsing', size_hint_y=None, height=50, background_color=(0.2, 0.2, 0.2, 1))
        information_gathering_button = Button(text='Information Gathering', size_hint_y=None, height=50, background_color=(0.2, 0.2, 0.2, 1))
        wifi_attacking_button = Button(text='Wifi Attacking', size_hint_y=None, height=50, background_color=(0.2, 0.2, 0.2, 1))
        
        pentesting_button.bind(on_press=self.open_pentesting)
        vulnerability_button.bind(on_press=self.open_vulnerability)
        browsing_button.bind(on_press=self.open_browsing)
        information_gathering_button.bind(on_press=self.open_information_gathering)
        wifi_attacking_button.bind(on_press=self.open_wifi_attacking)
        
        button_layout.add_widget(console_button)
        button_layout.add_widget(pentesting_button)
        button_layout.add_widget(vulnerability_button)
        button_layout.add_widget(browsing_button)
        button_layout.add_widget(information_gathering_button)
        button_layout.add_widget(wifi_attacking_button)
        
        main_layout.add_widget(button_layout)
        
        return main_layout
    
    def open_console(self, instance):
        # Console penceresi
        layout = FloatLayout()
        text_input = TextInput(size_hint=(0.9, 0.8), pos_hint={'center_x': 0.5, 'center_y': 0.6}, readonly=True, multiline=True, background_color=(0, 0, 0, 1), foreground_color=(1, 1, 1, 1))
        command_input = TextInput(size_hint=(0.9, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.1}, multiline=False, background_color=(0.2, 0.2, 0.2, 1), foreground_color=(1, 1, 1, 1))
        
        layout.add_widget(text_input)
        layout.add_widget(command_input)
        
        popup = Popup(title='Console', content=layout, size_hint=(0.9, 0.9))
        popup.open()
        
        # subprocess ile komut çalıştırma
        def execute_command(instance):
            command = command_input.text
            if command:
                process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate()
                text_input.text += stdout.decode() + stderr.decode() + '\n'
                command_input.text = ''
        
        command_input.bind(on_text_validate=execute_command)
    
    def open_pentesting(self, instance):
        self.open_module_window('Pentesting', ['Scan Network', 'Check Vulnerabilities', 'Exploit', 'Enumerate Services'])
    
    def open_vulnerability(self, instance):
        self.open_module_window('Vulnerability', ['Scan for Vulnerabilities', 'Analyze Reports', 'Patch Management', 'Pen Test'])
    
    def open_browsing(self, instance):
        self.open_module_window('Browsing', ['Google Dork', 'Search', 'Site Search', 'Advanced Search'])
    
    def open_information_gathering(self, instance):
        self.open_module_window('Information Gathering', ['Whois Lookup', 'DNS Enumeration', 'IP Geolocation', 'Social Media'])
    
    def open_wifi_attacking(self, instance):
        self.open_module_window('Wifi Attacking', ['Scan Networks', 'Crack WPA/WPA2', 'Monitor Traffic', 'Injection'])
    
    def open_module_window(self, module_name, button_labels):
        # Modül penceresi
        content = BoxLayout(orientation='vertical', spacing=10, padding=[10, 10, 10, 10])
        grid = GridLayout(cols=2, spacing=10, size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))
        
        for label in button_labels:  # Kullanıcı tarafından belirlenen buton adları
            button = Button(text=label, size_hint_y=None, height=50, background_color=(0.2, 0.2, 0.2, 1))
            button.bind(on_press=lambda btn: self.run_task(module_name, btn.text))
            grid.add_widget(button)
        
        content.add_widget(grid)
        popup = Popup(title=module_name, content=content, size_hint=(0.9, 0.9))
        popup.open()
    
    def run_task(self, module_name, task_name):
        # Görev çalıştırma (örnek)
        print(f'{module_name} - {task_name} çalıştırıldı.')
        # Gerçek işlem burada yapılabilir

if __name__ == '__main__':
    MainApp().run()