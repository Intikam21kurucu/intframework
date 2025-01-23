import requests
import random
import string
from colorama import Fore, Style

# Rastgele dizin isimleri üretme fonksiyonu
def generate_random_paths(num_paths):
    paths = []
    for _ in range(num_paths):
        path = ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(5, 15)))
        paths.append(path)
    return paths

# Dizin taraması yapan fonksiyon
def directory_scan(url, paths, found_directories):
    for path in paths:
        try:
            response = requests.get(f"{url}/{path}", timeout=5)  # Timeout'u 5 saniye olarak ayarlıyoruz
            if response.status_code == 200:
                found_directories.append(f"{url}/{path}")
        except requests.exceptions.RequestException:
            pass

# Kullanıcıdan alınan URL'yi tarayan ana fonksiyon
def directory_scan_module():
    found_directories = []
    
    print(f"{Fore.GREEN}Rastgele Dizin Tarayıcı Modülü Başlatıldı!{Style.RESET_ALL}")
    print("start with: scandir (website)")
    while True:
        module = input(f"{Fore.RED + Style.BRIGHT}int4{Style.RESET_ALL} PRO({Fore.RED + Style.BRIGHT}DirectoryScanner{Style.RESET_ALL}) > ")
        
        if module.lower() == "exit":
            print(f"{Fore.YELLOW}Modülden çıkılıyor...{Style.RESET_ALL}")
            break
        
        elif module.startswith("scandir "):
            try:
                _, target_url = module.split(" ")
                print(f"{Fore.YELLOW}Tarama başlatılıyor: {target_url}{Style.RESET_ALL}")
                
                # Rastgele 100 tane dizin ismi oluşturuyoruz
                random_paths = generate_random_paths(100)
                
                # Dizin taramasını başlatıyoruz
                directory_scan(target_url, random_paths, found_directories)
                
                # Bulunan dizinleri yazdırıyoruz
                if found_directories:
                    print(f"{Fore.GREEN}Bulunan dizinler: {', '.join(found_directories)}{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}Hiçbir dizin bulunamadı!{Style.RESET_ALL}")
            
            except ValueError:
                print(f"{Fore.RED}Geçersiz komut! Doğru kullanım: scandir <URL>{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Geçersiz komut: {module}{Style.RESET_ALL}")
if __name__ == "__main__":
	directory_scan_module()