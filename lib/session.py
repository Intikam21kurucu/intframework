import subprocess
import time
import os

# Log dizinini oluştur
LOG_DIR = os.path.expanduser("~/.int4/")
os.makedirs(LOG_DIR, exist_ok=True)

session_codes = [0]  # Sadece 0 ile başlıyoruz

for _ in iter(int, 1):  # Sonsuz döngü
    max_session_code = max(session_codes)
    new_session_code = max_session_code + 1
    sm = new_session_code
    session_codes.append(new_session_code)

intframework_path = os.getenv("INTFRAMEWORK_PATH")

def detect_interpreter(module_path):
    """
    Detect the appropriate interpreter for a given file based on its extension, 
    shebang line, or defaults for Intikam21 Framework.
    """
    try:
        # 1. Dosya mevcut mu kontrol et
        if not os.path.isfile(module_path):
            print(f"{Fore.RED}[!] Module not found: {Fore.CYAN}{module_path}{Style.RESET_ALL}")
            return None  # Dosya yoksa None döndür

        # 2. Dosya uzantısını kontrol et
        extension = os.path.splitext(module_path)[1].lower()
        interpreter_by_extension = {
            ".py2": "python2",   # Özel Python 2 uzantısı
            ".py": "python3",    # Varsayılan olarak Python 3
            ".c": "gcc",
            ".cpp": "g++",
            ".cs": "csharp",
            ".js": "node",
            ".rb": "ruby",
            ".php": "php",
            ".pl": "perl",
            ".sh": "bash",
            ".go": "go run",
            ".sql": "sqlcmd",
            ".html": "browser",
            ".lua": "lua",
            ".ps1": "powershell"  # PowerShell desteği
        }

        # Uzantıya göre yorumlayıcı belirle
        if extension in interpreter_by_extension:
            # Eğer uzantı ".py" ise, kullanıcı Python 2 için mi yoksa Python 3 için mi çalıştıracağını seçebilir.
            if extension == ".py":
                with open(module_path, 'r', buffering=1024) as file:
                    first_line = file.readline().strip()
                    if "python2" in first_line:  # Shebang Python 2 mi işaret ediyor?
                        return "python2"
                    else:
                        return "python3"  # Varsayılan olarak Python 3
            return interpreter_by_extension[extension]

        # 3. Eğer uzantı bilinmiyorsa, shebang satırını kontrol et
        with open(module_path, 'r', buffering=1024) as file:
            first_line = file.readline().strip()
            if first_line.startswith("#!"):
                if "python2" in first_line:
                    return "python2"
                elif "python" in first_line or "python3" in first_line:
                    return "python3"
                elif "ruby" in first_line:
                    return "ruby"
                elif "php" in first_line:
                    return "php"
                elif "perl" in first_line:
                    return "perl"
                elif "node" in first_line or "javascript" in first_line:
                    return "node"
                elif "gcc" in first_line or "clang" in first_line:
                    return "gcc"
                elif "g++" in first_line or "cpp" in first_line:
                    return "g++"
                elif "bash" in first_line or "sh" in first_line:
                    return "bash"
                elif "go" in first_line:
                    return "go run"
                elif "lua" in first_line:
                    return "lua"
                elif "powershell" in first_line or "pwsh" in first_line:
                    return "powershell"
                elif "csharp" in first_line or "dotnet" in first_line:
                    return "csharp"
                elif "sql" in first_line:
                    return "sqlcmd"
                elif "html" in first_line:
                    return "browser"

        # 4. Ne uzantı ne de shebang tespit edilemiyorsa, varsayılan olarak Python 3 döndür
        print(f"{Fore.YELLOW}[+] No valid interpreter found. Defaulting to python3 for module: {Fore.CYAN}{module_path}{Style.RESET_ALL}")
        return "python3"

    except Exception as e:
        print(f"{Fore.RED}[!] Error detecting interpreter for {Fore.CYAN}{module_path}{Style.RESET_ALL}: {e}{Style.RESET_ALL}")
        return "python3"  # Hata durumunda python3 döndür
        
def start_module_session(module_path):
    script_path = f"{module_path}"  # intconsoleV4.py dosyasının tam yolu
    log_path = os.path.join(LOG_DIR, f"session_{module_path}.log")
    interpreter_m = detect_interpreter(module_path)
    # tmux içinde yeni bir session başlat
    subprocess.run(f"tmux new-session -d -s session_{sm} '{interpreter_m} {script_path} | tee {log_path}'", shell=True)
    print(f"[+] Session {session_id} started.")

# Yeni session başlatma
def start_new_session(session_id):
    script_path = f"{intframework_path}/intconsoleV4.py"  # intconsoleV4.py dosyasının tam yolu
    log_path = os.path.join(LOG_DIR, f"session_{session_id}.log")
    
    # tmux içinde yeni bir session başlat
    subprocess.run(f"tmux new-session -d -s session_{session_id} 'python3 {script_path} | tee {log_path}'", shell=True)
    print(f"[+] Session {session_id} started.")

# Session'ları listeleme
def list_sessions():
    result = subprocess.run("tmux ls", shell=True, capture_output=True, text=True)
    print(result.stdout)

# Belirli bir session'a geçiş
def switch_to_session(session_id):
    subprocess.run(f"tmux attach-session -t session_{session_id}", shell=True)

# Komut çıktısını renklendirip kaydetme
def log_to_file(session_id, cmd, response):
    ts = time.strftime("%Y-%m-%d %H:%M:%S")
    log_file = os.path.join(LOG_DIR, f"session_{session_id}.log")
    
    # Renkli çıktıyı log dosyasına yaz
    with open(log_file, "a") as f:
        f.write(f"[{ts}] $ {cmd}\n")
        f.write(response + "\n")

# Ana komut arayüzü
def example():
    print("intconsoleV4 Komut Arayüzüne Hoşgeldiniz!")
    
    while True:
        command = input("intconsoleV4> ")
        
        if command == "exit":
            print("Çıkılıyor...")
            break
        elif command.startswith("session -a"):
            session_id = command.split(" ")[-1]
            start_new_session(session_id)
        elif command.startswith("session -l"):
            list_sessions()
        elif command.startswith("session "):
            session_id = command.split(" ")[-1]
            switch_to_session(session_id)
        else:
            print("Geçersiz komut!")

# Scriptin ana fonksiyonunu çağırma
if __name__ == "__main__":
	print("this script is library, not executable!")