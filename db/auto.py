import json
import os
import re

# 📌 Desteklenen uzantılar
SUPPORTED_LANGUAGES = {
    ".py2": "python2",
    ".py": "python3",
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
    ".ps1": "powershell"
}

# 📌 Kontrol edilecek dizinler
SCAN_DIRECTORIES = ["modules", "intPRO", "tools", "cve"]

class ModuleManager:
    def __init__(self, json_file="modules.json"):
        self.json_file = json_file
        self.modules = self.load_modules()

    def load_modules(self):
        """JSON dosyasından modülleri yükler"""
        if os.path.exists(self.json_file):
            with open(self.json_file, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def save_modules(self):
        """Modülleri JSON dosyasına kaydeder"""
        with open(self.json_file, "w", encoding="utf-8") as f:
            json.dump(self.modules, f, indent=4, ensure_ascii=False)

    def extract_metadata(self, file_path):
        """Dosya içindeki metadataları alır"""
        metadata = {
            "exploit_title": "None",
            "cve": "None",
            "google_dork": "None",
            "author": "Intframework Team",
            "test_status": "⚠️ Not Tested"
        }

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
                for line in lines:
                    line = line.strip()

                    if line.lower().startswith("# exploit title:"):
                        metadata["exploit_title"] = line.split(":", 1)[1].strip()

                    elif line.lower().startswith("# cve:"):
                        metadata["cve"] = line.split(":", 1)[1].strip()

                    elif line.lower().startswith("# google dork:"):
                        metadata["google_dork"] = line.split(":", 1)[1].strip()

                    elif re.match(r"^# *(exploit author|author):", line.lower()):
                        author = line.split(":", 1)[1].strip()
                        if not author.lower().startswith(("http://", "https://")):
                            metadata["author"] = author

                    elif line.lower().startswith("# test:"):
                        test_status = line.split(":", 1)[1].strip().lower()
                        if test_status == "good":
                            metadata["test_status"] = "✅ Good"
                        elif test_status == "bad":
                            metadata["test_status"] = "❌ Bad"

        except Exception as e:
            print(f"Hata: {e}")

        return metadata

    def scan_modules(self):
        """Belirtilen dizinlerdeki modülleri tarayıp JSON'a kaydeder"""
        found_modules = {}

        for directory in SCAN_DIRECTORIES:
            if not os.path.exists(directory):
                os.makedirs(directory)

            for file in os.listdir(directory):
                file_path = os.path.join(directory, file)
                file_ext = os.path.splitext(file)[1]

                if file_ext in SUPPORTED_LANGUAGES:
                    module_name = os.path.splitext(file)[0]
                    language = SUPPORTED_LANGUAGES[file_ext]

                    # Eğer __init__.py varsa, öncelikle onu oku
                    init_path = os.path.join(directory, "__init__.py")
                    if os.path.exists(init_path):
                        metadata = self.extract_metadata(init_path)
                    else:
                        metadata = self.extract_metadata(file_path)

                    found_modules[module_name] = {
                        "name": module_name,
                        "language": language,
                        "command": f"{language} {file}",
                        **metadata  # Metadata'yı ekle
                    }

        self.modules = found_modules
        self.save_modules()
        return f"{len(found_modules)} modül JSON dosyasına kaydedildi."

    def list_modules(self):
        """Tüm modülleri listele"""
        return list(self.modules.keys())

    def get_module(self, name):
        """Belirli bir modülü getir"""
        return self.modules.get(name, None)

# 📌 Örnek Kullanım:
manager = ModuleManager()
print(manager.scan_modules())  # Modülleri tara ve kaydet
print(manager.list_modules())  # Modülleri listele