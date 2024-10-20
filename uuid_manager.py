import uuid
import json
import os
import atexit

# Kullanıcı veritabanı (intrpc ve intuser tanımlı)
user_database = {
    "intrpc": "root@int",   # Birinci kullanıcı
    "intuser": "root",      # İkinci kullanıcı
}

# Session ID'lerini saklayacağımız bir sözlük
session_ids = {}

# JSON dosyası
session_file = 'sessions.json'

# Program kapandığında oturum dosyasını silen işlev
def cleanup():
    print("Program kapatılıyor...")
    # Eğer oturum dosyası varsa sil
    if os.path.exists(session_file):
        os.remove(session_file)
        print("file removed")

# JSON dosyasından oturumları yükleme
def load_sessions():
    global session_ids
    if os.path.exists(session_file):
        with open(session_file, 'r') as json_file:
            session_ids = json.load(json_file)
    else:
        pass

# UUID'yi Intikam21 Framework için özelleştir
def customize_uuid(session_id):
    return f"int-{session_id}"

def create_session(kullanici_adi, sifre):
    if kullanici_adi in user_database and user_database[kullanici_adi] == sifre:
        session_id = str(uuid.uuid4())  # Benzersiz UUID oluştur
        session_ids[session_id] = kullanici_adi  # Session ID ve kullanıcıyı sakla
        customized_id = customize_uuid(session_id)  # Özelleştirilmiş UUID
        print(f"New session created: {customized_id}")
        return session_id  # UUID'yi geri döndür
    else:
        return None

def kill_session(session_id):
    if session_id in session_ids:
        del session_ids[session_id]  # Session ID'yi sil
        print(f"session exited: {session_id}")
        return True
    print("session not found.")
    return False

def session_listele():
    return session_ids

def session_bilgi(session_id):
    return session_ids.get(session_id, None)  # Session ID'ye göre kullanıcıyı döndür

# Program kapandığında cleanup işlevini çağır
atexit.register(cleanup)

# Program başladığında oturumları yükle
load_sessions()

