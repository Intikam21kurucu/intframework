import os
import requests
import json
import shutil
import platform

tool_link = "https://github.com/Intikam21kurucu/intframework"

def check_for_updates():
    try:
        print("Checking for updates...")
        # GitHub API'sini kullanarak deposundaki dosyaların listesini al
        api_url = f"https://api.github.com/repos/Intikam21kurucu/intframework/contents"
        response = requests.get(api_url)
        contents = json.loads(response.content)

        # 'intframework' dizinindeki dosyaları al
        os.chdir("intframework")
        local_files = os.listdir()

        # GitHub'daki dosyaları kontrol et
        for content in contents:
            file_name = content['name']
            if file_name not in local_files:
                # Eğer dosya mevcut değilse, GitHub'dan indir
                download_url = content['download_url']
                download_file(download_url, file_name)
                print(f"{file_name} has been added/updated.")
            else:
                # Dosya mevcutsa, karşılaştır
                local_content = open(file_name, 'rb').read()
                github_content = requests.get(download_url).content
                if local_content != github_content:
                    # Eğer dosya farklıysa, güncelle
                    download_file(download_url, file_name)
                    print(f"{file_name} has been updated.")
                else:
                    print(f"{file_name} is up-to-date.")

        print("Update check complete.")
    except Exception as e:
        print("An error occurred while checking for updates:", e)

def download_file(url, file_name):
    response = requests.get(url)
    with open(file_name, 'wb') as f:
        f.write(response.content)

def main():
    try:
        # Güncelleme kontrolünü yap
        check_for_updates()

        # Güncelleme işlemlerinin tamamlandığından emin olun
        print("All updates have been completed.")
        
        # Uygulama işlemlerini buraya ekleyin

    except KeyboardInterrupt:
        print("\nExiting...")

if __name__ == "__main__":
    # İşletim sistemini kontrol et
    if platform.system() == "Linux":
        # Eğer Linux ise, masaüstünde mi kontrol et
        desktop_path = os.path.expanduser("~/Desktop")
        if os.path.exists(desktop_path):
            # Masaüstünde ise, replit ortamında mı kontrol et
            if os.path.exists("/run/repl"):
                # Replit'te ise, güncelleme işlemlerini gerçekleştir
                main()
            else:
                # Replit'te değilse, Kali Linux'te mi kontrol et
                os.chdir(desktop_path)
                main()
        else:
            # Masaüstünde değilse, Kali Linux'te mi kontrol et
            main()
    elif platform.system() == "Android":
        # Eğer Android ise, Termux'ta mı kontrol et
        termux_path = os.path.expanduser("~/storage/shared/termux")
        if os.path.exists(termux_path):
            os.chdir(termux_path)
            main()
        else:
            print("Termux environment not found.")
    else:
        print("Unsupported operating system.")