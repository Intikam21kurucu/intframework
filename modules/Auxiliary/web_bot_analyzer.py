import requests

def analyze_bot_traffic(target_domain):
    try:
        # Örnek bir User-Agent kontrol listesi
        bot_user_agents = [
            "Googlebot", "Bingbot", "Slurp", "DuckDuckBot",
            "Baiduspider", "YandexBot", "Sogou", "Exabot", "facebot", "ia_archiver"
        ]

        print(f"Target domain: {target_domain}")
        
        # GET isteği gönder
        response = requests.get(target_domain, headers={"User-Agent": "TestAgent/1.0"})
        server_headers = response.headers.get('Server', 'Unknown')

        print("\n--- Response Headers ---")
        print(response.headers)

        print("\n--- Bot Analysis ---")
        for bot in bot_user_agents:
            if bot.lower() in server_headers.lower():
                print(f"[!] Bot detected: {bot}")
                return
        print("[-] No bot signatures detected.")
    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    # Modül adı ve açıklama
    modul_adi = "web_bot_analyze"
    aciklama = "Web bot ve tarayıcı analiz aracı"

    # Kullanıcıdan hedef domain al
    target_domain = input(f"\033[91mint4 {modul_adi}[{aciklama}] > \033[0m")
    if target_domain.startswith("http"):
        analyze_bot_traffic(target_domain)
    else:
        print("[!] Please provide a valid URL starting with http or https.")