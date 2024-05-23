import requests
from bs4 import BeautifulSoup
import random

def fetch_page_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
    return None

def extract_relevant_info(error_message, content):
    if error_message.lower() in content.lower():
        return True
    return False

def analyze_error(error_message):
    urls = [
        "https://github.com/Intikam21kurucu/intframework",
        "https://github.com/Intikam21kurucu/intframework/issues",
        "https://github.com/Intikam21kurucu/int-formations",
        "https://github.com/Intikam21kurucu/int-formations/issues",
        "https://github.com/Intikam21kurucu/Intikam21",
        "https://github.com/Intikam21kurucu/Intikam21/issues",
        "https://github.com/nmap/nmap",
        "https://github.com/nmap/nmap/issues",
        "https://www.metasploit.com/",
        "https://rapid7.github.io/metasploit-framework/docs/using-metasploit/getting-started/nightly-installers.html",
        "https://www.kali.org/",
        "https://www.kali.org/tools/",
        "https://www.google.com/"
    ]

    for url in urls:
        content = fetch_page_content(url)
        if content and extract_relevant_info(error_message, content):
            return (f"A relevant section found in {url}. Please check it for more info.",
                    f"İlgili bir bölüm {url} adresinde bulundu. Daha fazla bilgi için kontrol edin.")

    return suggest_solution(error_message)

def suggest_solution(error_message):
    solutions_en = {
        "module not found": "Ensure the module is installed using pip.",
        "permission denied": "Check file permissions and ensure you have the necessary access rights.",
        "syntax error": "Check the syntax in your code for any mistakes.",
        "timeout error": "Increase the timeout limit or check your internet connection.",
        "connection refused": "Check if the server is running and reachable."
    }
    solutions_tr = {
        "module not found": "Modülün pip ile yüklü olduğundan emin olun.",
        "permission denied": "Dosya izinlerini kontrol edin ve gerekli erişim haklarına sahip olduğunuzdan emin olun.",
        "syntax error": "Kodunuzdaki sözdizimini kontrol edin ve hataları düzeltin.",
        "timeout error": "Zaman aşımı limitini artırın veya internet bağlantınızı kontrol edin.",
        "connection refused": "Sunucunun çalışır durumda ve erişilebilir olduğundan emin olun."
    }
    
    for key in solutions_en:
        if key in error_message.lower():
            return solutions_en[key], solutions_tr[key]
    
    default_responses_en = [
        "No solution found. Please check the error message or visit the provided links.",
        "Couldn't find an exact solution. Try searching the provided links for more help.",
        "The error isn't directly addressed in the resources. Please double-check the links for more info."
    ]
    default_responses_tr = [
        "Çözüm bulunamadı. Lütfen hata mesajını kontrol edin veya verilen linkleri ziyaret edin.",
        "Tam olarak bir çözüm bulunamadı. Daha fazla yardım için verilen linkleri kontrol edin.",
        "Hata doğrudan kaynaklarda ele alınmamış. Daha fazla bilgi için linkleri kontrol edin."
    ]
    
    return random.choice(default_responses_en), random.choice(default_responses_tr)

def get_installation_info():
    messages_en = [
        "For installation, on Kali Linux, install necessary dependencies and clone the repository using 'git clone'.",
        "On Termux, install required packages and clone the repository using 'git clone'.",
        "Ensure all dependencies are installed correctly before using 'git clone' to complete the installation."
    ]
    messages_tr = [
        "Kurulum için Kali Linux'ta gerekli bağımlılıkları yükleyin ve 'git clone' komutuyla intframework'ü indirin.",
        "Termux üzerinde gerekli paketleri yükledikten sonra 'git clone' komutunu kullanarak intframework'ü indirin.",
        "Bağımlılıkların eksiksiz kurulduğundan emin olduktan sonra 'git clone' komutunu kullanarak kurulumu tamamlayın."
    ]
    return random.choice(messages_en), random.choice(messages_tr)

def get_error_info():
    messages_en = [
        "During installation, ensure all dependencies are fully installed.",
        "For runtime errors, check file permissions and grant necessary permissions.",
        "Ensure correct versions of dependencies are used and update if necessary."
    ]
    messages_tr = [
        "Kurulum sırasında bağımlılıkların tam olarak yüklendiğinden emin olun.",
        "Çalıştırma hatalarında dosya izinlerini kontrol edin ve gerekli yetkileri verin.",
        "Bağımlılıkların doğru sürümlerini kullandığınızdan emin olun ve gerekirse güncelleyin."
    ]
    return random.choice(messages_en), random.choice(messages_tr)

def get_usage_info():
    messages_en = [
        "To start the tool, use the command 'python3 intframework.py'.",
        "For usage, first configure necessary settings, then run the tool with 'python3 intframework.py'.",
        "Run the tool from the command line by typing 'python3 intframework.py'."
    ]
    messages_tr = [
        "Aracı başlatmak için 'python3 intframework.py' komutunu kullanın.",
        "Kullanım için önce gerekli konfigürasyonları yapın, ardından 'python3 intframework.py' ile aracı çalıştırın.",
        "Komut satırından 'python3 intframework.py' yazarak aracı çalıştırabilirsiniz."
    ]
    return random.choice(messages_en), random.choice(messages_tr)

def provide_info(query, language):
    if "kurulum" in query or "install" in query:
        return get_installation_info()[0 if language == 'en' else 1]
    elif "hata" in query or "error" in query:
        error_message = input("Please enter the error message / Lütfen aldığınız hata mesajını girin: ").strip()
        return analyze_error(error_message)[0 if language == 'en' else 1]
    elif "kullanım" in query or "usage" in query:
        return get_usage_info()[0 if language == 'en' else 1]
    elif "araştırma" in query or "research" in query:
        research_topic = input("What topic would you like to research? / Hangi konuda araştırma yapmak istiyorsunuz?: ").strip()
        search_url = f"https://www.google.com/search?q={research_topic.replace(' ', '+')}"
        return (f"You can start your research here: {search_url}", 
                f"Araştırmanıza buradan başlayabilirsiniz: {search_url}")
    else:
        return ("I can help with installation, error troubleshooting, usage, or research. Please ask a more specific question.",
                "Kurulum, hata giderme, kullanım veya araştırma konularında yardımcı olabilirim. Lütfen daha spesifik bir soru sorun.")[0 if language == 'en' else 1]

def main():
    print("Merhaba ben intai'yim! / Hello, I am intai!")
    language = input("Please choose a language (en/tr): ").strip().lower()
    while True:
        user_input = input("\nWhat do you need help with? (type 'exit' to quit) / Ne konuda yardıma ihtiyacınız var? (çıkmak için 'exit' yazın): ").strip().lower()
        if user_input == 'exit':
            break
        if user_input:  # Sadece kullanıcı bir şey yazdığında yanıt ver
            response = provide_info(user_input, language)
            print(response)

if __name__ == "__main__":
    main()