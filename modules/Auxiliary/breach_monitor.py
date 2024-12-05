import requests

# Have I Been Pwned API'yi kullanarak e-posta sızıntılarını kontrol etme
def check_breach(email):
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    
    # API isteği yap
    headers = {
        "User-Agent": "BreachMonitoringTool"
    }
    
    try:
        response = requests.get(url, headers=headers)
        
        # Eğer başarılıysa ve ihlaller varsa
        if response.status_code == 200:
            breaches = response.json()
            print(f"[+] {email} has been found in the following breaches:\n")
            for breach in breaches:
                print(f"- {breach['Title']} breach")
        elif response.status_code == 404:
            print(f"[+] No breaches found for {email}.")
        else:
            print("[!] Something went wrong, please try again later.")
    except requests.exceptions.RequestException as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    modul_adi = "breach_monitor"
    aciklama = "E-posta sızıntılarını izleme aracı"
    
    email = input(f"\033[91mint4 {modul_adi}[{aciklama}] > Enter email address to check for breaches: \033[0m")
    
    if email:
        check_breach(email)
    else:
        print("[!] Please enter a valid email address.")