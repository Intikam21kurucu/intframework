import json
import os
import re
import warnings

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

# 📌 Kontrol edilecek dizinler (regex ile kontrol edilecek)
MODULE_PATTERNS = {
    r".*exploit.*": "exploit",
    r".*payload.*": "payload",
    r".*auxiliary.*": "auxiliary",
    r".*intpro.*": "intPRO",
    r".*tools.*": "tool",
    r".*cve.*": "cve"
}

class ModuleManager:
    def __init__(self, json_file="modules.json"):
        self.json_file = json_file
        self.modules = self.load_modules()

    def load_modules(self):
        """JSON dosyasından modülleri yükler"""
        if os.path.exists(self.json_file):
            with open(self.json_file, "r", encoding="utf-8") as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    warnings.warn("JSON dosyası bozuk, sıfırdan oluşturulacak.")
                    return {}
        return {}

    def save_modules(self):
        """Modülleri JSON dosyasına kaydeder"""
        try:
            with open(self.json_file, "w", encoding="utf-8") as f:
                json.dump(self.modules, f, indent=4, ensure_ascii=False)
        except Exception as e:
            warnings.warn(f"JSON dosyası kaydedilirken hata oluştu: {e}")

    def extract_metadata(self, file_path):
        """Dosya içindeki metadataları alır"""
        metadata = {
            "title": "Unknown",
            "cve": "Unknown",
            "google_dork": "Unknown",
            "author": "Intframework Team",
            "test_status": "Not Tested"
        }

        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                for line in f:
                    line = line.strip()
                    if line.startswith("#"):
                        match = re.match(r"#\s*(\w+)\s*:\s*(.+)", line)
                        if match:
                            key, value = match.groups()
                            key = key.lower()

                            if key == "title":
                                metadata["title"] = value
                            elif key == "cve":
                                metadata["cve"] = value
                            elif key == "google dork":
                                metadata["google_dork"] = value
                            elif re.match(r"^(exploit author|author)", key):
                                if not value.lower().startswith(("http://", "https://")):
                                    metadata["author"] = value
                            elif key == "test":
                                value = value.lower()
                                if value == "good":
                                    metadata["test_status"] = "✅ Good"
                                elif value == "bad":
                                    metadata["test_status"] = "❌ Bad"

        except Exception as e:
            warnings.warn(f"Metadata okuma hatası: {e}")

        return metadata

    def detect_module_type(self, file_path):
        """Regex kullanarak modül tipini belirler"""
        lower_path = file_path.lower()
        for pattern, module_type in MODULE_PATTERNS.items():
            if re.search(pattern, lower_path):
                return module_type
        return "unknown"

    def scan_modules(self):
        """Belirtilen dizinlerdeki modülleri tarayıp JSON'a kaydeder"""
        found_modules = {}

        for directory in MODULE_PATTERNS.values():
            if not os.path.exists(directory):
                os.makedirs(directory)

            for root, _, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    file_ext = os.path.splitext(file)[1]

                    if file_ext in SUPPORTED_LANGUAGES:
                        module_name = os.path.splitext(file)[0]
                        language = SUPPORTED_LANGUAGES[file_ext]
                        module_type = self.detect_module_type(file_path)

                        # Öncelikle __init__.py kontrol et
                        init_path = os.path.join(root, "__init__.py")
                        metadata = self.extract_metadata(init_path if os.path.exists(init_path) else file_path)

                        found_modules[module_name] = {
                            "name": module_name,
                            "language": language,
                            "command": f"{language} {file}",
                            "type": module_type,
                            **metadata  # Metadata'yı ekle
                        }

        self.modules = found_modules
        self.save_modules()
        return f"{len(found_modules)} module(s) saved"

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