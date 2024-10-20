import requests

def directory_bruteforce(target_url, wordlist):
    found_dirs = []

    with open(wordlist, 'r') as f:
        directories = f.readlines()

    for directory in directories:
        dir_path = directory.strip()
        url = target_url + "/" + dir_path
        response = requests.get(url)

        if response.status_code == 200:
            print(f"Bulundu: {url}")
            found_dirs.append(url)
    
    if not found_dirs:
        print("Dizin bulunamadı.")
    
    return found_dirs

# Kullanım örneği
target_url = "http://example.com"
wordlist = "common_directories.txt"  # Dizin listesi
directory_bruteforce(target_url, wordlist)