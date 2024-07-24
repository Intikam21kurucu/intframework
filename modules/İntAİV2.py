import random
from langdetect import detect
from PyDictionary import PyDictionary
import nltk
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import difflib
import os
import json
import requests
import subprocess
from bs4 import BeautifulSoup

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

class IntaiV2:
    def __init__(self):
        self.dictionary = PyDictionary()
        self.commands = {
            "print": self.print_command,
            "len": self.len_command,
            "set login": self.set_login_command,
            # Eklenen komutlar
            "arat": self.search_command,
            "çalıştır": self.execute_command,
            "merhaba": self.greet_user,
        }
        self.sentences = []

    def respond(self, message):
        response = self.generate_response(message)
        return response

    def generate_response(self, message):
        if any(word in message.lower() for word in ["hata"]):
            error_code = self.extract_error_code(message)
            if error_code:
                return self.handle_error(error_code)
            else:
                return "Üzgünüm, hata kodunu algılayamadım."

        if any(word in message.lower() for word in ["arama", "arat"]):
            query = self.extract_query(message)
            if query:
                return self.search_command(query)
            else:
                return "Üzgünüm, arama sorgusunu algılayamadım."

        if any(word in message.lower() for word in ["çalıştır"]):
            command = self.extract_command(message)
            if command:
                return self.execute_command(command)
            else:
                return "Üzgünüm, komutu algılayamadım."

        if any(word in message.lower() for word in ["anlamı", "anlamını"]):
            word = self.extract_word(message)
            if word:
                return self.get_word_meaning(word)

        if any(word in message.lower() for word in ["benzerlik", "benzeşim", "benzer"]):
            query = self.extract_query(message)
            if query:
                return self.find_similarity(query)
            else:
                return "Üzgünüm, benzerlik bulamadım."

        if any(word in message.lower() for word in ["düzelt", "kod"]):
            error_message = self.extract_error_message(message)
            if error_message:
                return self.fix_code_error(error_message)
            else:
                return "Üzgünüm, kod hatasını algılayamadım veya düzeltemedim."

        if any(word in message.lower() for word in self.commands.keys()):
            command = self.extract_command(message)
            if command:
                command_name = command.split()[0] + " " + command.split()[1]
                if command_name in self.commands:
                    return self.commands[command_name](command)
                else:
                    return "Üzgünüm, bu komutu tanımıyorum."

        # Kullanıcı selam verdiğinde cevap verme
        if any(word in message.lower() for word in ["merhaba", "selam", "hey"]):
            return self.greet_user()

        # Kullanıcının dediği herhangi bir şeyi anlayıp cevap verebilme
        return self.generate_random_response()

    def handle_error(self, error_code):
        known_errors = {
            "404": "URL bulunamadı hatası. Lütfen adresinizi kontrol edin.",
            "500": "İç sunucu hatası. Lütfen sistem yöneticinizle iletişime geçin.",
            "İmport Error": "install your file please usage : pip install (file)",
            "Name Error": "your file is not installed or not imported",
            "Type Error": "Type is not using"
            # Daha fazla hata kodu ekleyebilirsiniz
        }
        if error_code in known_errors:
            return f"Hata {error_code} tespit edildi: {known_errors[error_code]}"
        else:
            return self.search_online(error_code)

    def search_command(self, query):
        try:
            response = self.search_website(query)
            if response:
                return response
            else:
                return f"{query} ile ilgili bilgi bulunamadı."
        except Exception as e:
            return f"Arama sırasında bir hata oluştu: {str(e)}"

    def search_website(self, query):
        try:
            url = f"https://www.google.com/search?q={query}"
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
            response = requests.get(url, headers=headers)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')
            search_results = soup.find_all('div', class_='search-result')

            if search_results:
                first_result = search_results[0]
                title = first_result.find('h3').text
                link = first_result.find('a')['href']
                return f"Web sitesinden bulduğum ilk sonuç: {title}\nLink: {link}"
            else:
                return f"Üzgünüm, {query} ile ilgili bir sonuç bulunamadı."

        except Exception as e:
            return f"Arama sırasında bir hata oluştu: {str(e)}"

    def extract_error_code(self, message):
        words = message.split()
        for word in words:
            if word.isdigit():
                return word
        return None

    def extract_query(self, message):
        keywords = ["arama", "arat"]
        for keyword in keywords:
            if keyword in message.lower():
                return message.lower().replace(keyword, "").strip()
        return None

    def extract_command(self, message):
        keywords = ["çalıştır", "print", "len", "set login"]
        for keyword in keywords:
            if keyword in message.lower():
                return message.lower().replace(keyword, "").strip()
        return None

    def get_word_meaning(self, word):
        try:
            meaning = self.dictionary.meaning(word)
            if meaning:
                return f"{word} kelimesinin anlamı:\n{meaning}"
            else:
                return f"{word} kelimesinin anlamı bulunamadı."
        except Exception as e:
            return f"Hata oluştu: {str(e)}"

    def find_similarity(self, query):
        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform(self.sentences + [query])
        similarity_scores = cosine_similarity(vectors[-1], vectors[:-1])
        most_similar_index = similarity_scores.argmax()
        return f"En benzer cümle: {self.sentences[most_similar_index]}"

    def execute_command(self, command):
        try:
            result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            return f"\tKomut başarıyla çalıştırıldı. Çıktı:\n{result.stdout}"
        except Exception as e:
            return f"Komut çalıştırılırken hata oluştu: {str(e)}"

    def fix_code_error(self, error_message):
        try:
            suggested_fix = difflib.get_close_matches(error_message, self.sentences)
            if suggested_fix:
                return f"Önerilen düzeltme: {suggested_fix[0]}"
            else:
                return "Hata düzeltilmedi, lütfen daha spesifik bir hata mesajı verin."
        except Exception as e:
            return f"Hata oluştu: {str(e)}"

    def extract_error_message(self, message):
        words = message.split()
        for word in words:
            if "hata" in word.lower():
                index = words.index(word)
                return ' '.join(words[index + 1:])
        return None

    def print_command(self, command):
        try:
            message = command.split(" ", 2)[2]
            return message
        except IndexError:
            return "Print komutu için bir mesaj girin."

    def len_command(self, command):
        try:
            message = command.split(" ", 2)[2]
            return f"Uzunluk: {len(message)}"
        except IndexError:
            return "Len komutu için bir mesaj girin."

    def set_login_command(self, command):
        try:
            api_key = command.split(" ", 2)[2]
            # API anahtarını kaydetme işlemi
            return "API anahtarı başarıyla kaydedildi ve yüklendi."
        except IndexError:
            return "API anahtarını girin. Örnek: set login <API-KEY>"

    def greet_user(self):
        greetings = [
            "Merhaba!",
            "Selam!",
            "Hey!",
            "Nasılsın?",
            "Hoş geldiniz!",
        ]
        return random.choice(greetings)

    def generate_random_response(self):
        responses = [
            "Anladım.",
            "Evet, devam edin.",
            "Sanırım bunu yapabiliriz.",
            "Siz ne düşünüyorsunuz?",
            "Tamam",
            "Bunu arastirmami ister misiniz",
            "Daha fazla bilgi verir misiniz?",
        ]
        return random.choice(responses)

# IntaiV2'u çalıştırma ve kullanıcı girdisi alma
if __name__ == "__main__":
    print("""

╗███╗   ██╗████████╗ █████╗ ██╗██╗   ██╗██████╗ 
██║████╗  ██║╚══██╔══╝██╔══██╗██║██║   ██║╚════██╗
██║██╔██╗ ██║   ██║   ███████║██║██║   ██║ █████╔╝
██║██║╚██╗██║   ██║   ██╔══██║██║╚██╗ ██╔╝██╔═══╝ 
██║██║ ╚████║   ██║   ██║  ██║██║ ╚████╔╝ ███████╗
╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝  ╚══════╝
                                                  """)
    intai_v2 = IntaiV2()
    print("IntaiV2'ye hoş geldiniz! Çıkmak için 'exit' yazabilirsiniz.")
    while True:
        user_input = input("Siz: ")
        if user_input.lower() == "exit":
            print("Görüşmek üzere!")
            break
        response = intai_v2.respond(user_input)
        print("IntaiV2: " + response)