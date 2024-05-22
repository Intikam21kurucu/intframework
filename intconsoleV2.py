import requests
from bs4 import BeautifulSoup
import random

def get_github_issues():
    url = "https://github.com/Intikam21kurucu/intframework/issues"
    response = requests.get(url)
    if response.status_code != 200:
        return "GitHub Issues page is not accessible.", "GitHub Issues sayfasına erişilemedi."
    soup = BeautifulSoup(response.content, 'html.parser')
    issues = soup.find_all('a', {'data-hovercard-type': 'issue'})
    issues_list = []
    for issue in issues:
        issues_list.append(issue.text.strip())
    return issues_list

def analyze_error(error_message):
    issues = get_github_issues()
    if isinstance(issues, tuple):
        return issues  # Return error message if issues cannot be fetched
    
    for issue in issues:
        if error_message.lower() in issue.lower():
            return (f"A similar issue found: {issue}. Check GitHub Issues page for more info.",
                    f"Benzer bir sorun bulundu: {issue}. Daha fazla bilgi için GitHub Issues sayfasını kontrol edin.")
    
    return suggest_solution(error_message)

def suggest_solution(error_message):
    solutions_en = {
        "module not found": "Ensure the module is installed using pip.",
        "permission denied": "Check file permissions and ensure you have the necessary access rights.",
        "syntax error": "Check the syntax in your code for any mistakes."
    }
    solutions_tr = {
        "module not found": "Modülün pip ile yüklü olduğundan emin olun.",
        "permission denied": "Dosya izinlerini kontrol edin ve gerekli erişim haklarına sahip olduğunuzdan emin olun.",
        "syntax error": "Kodunuzdaki sözdizimini kontrol edin ve hataları düzeltin."
    }
    
    for key in solutions_en:
        if key in error_message.lower():
            return solutions_en[key], solutions_tr[key]
    
    return ("No solution found. Please check the error message or visit the GitHub Issues page.",
            "Çözüm bulunamadı. Lütfen hata mesajını kontrol edin veya GitHub Issues sayfasına göz atın.")

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
    else:
        return ("I can help with installation, error troubleshooting, or usage. Please ask a more specific question.",
                "Kurulum, hata giderme veya kullanım konularında yardımcı olabilirim. Lütfen daha spesifik bir soru sorun.")[0 if language == 'en' else 1]

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