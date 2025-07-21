import argparse
import ujson
import os
import re
import warnings
import logging
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from lib.ai_score import IntelligenceAnalyzer

# Logger ayarları - konsola ve dosyaya log yazma
logger = logging.getLogger("ModuleManager")
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

file_handler = logging.FileHandler("module_manager.log", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Yapay zeka analiz motoru (dış modül)
analyzer = IntelligenceAnalyzer()

# Desteklenen dosya uzantıları ve diller
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

# Modül tipi regex eşlemeleri
MODULE_PATTERNS = {
    r"exploit": "exploit",
    r"payload": "payload",
    r"auxiliary": "auxiliary",
    r"intpro": "intPRO",
    r"tools": "tool",
    r"cve": "cve"
}

# Tarama yapılacak ana dizinler
MODULE_DIRECTORIES = ["intPRO", "modules", "tools"]

class ModuleManager:
    def __init__(self, base_path=".", json_file="modules.json", max_workers=8):
        self.base_path = os.path.abspath(base_path)
        self.json_file = os.path.join(self.base_path, json_file)
        self.modules = {}
        self.max_workers = max_workers
        self.load_modules()
        logger.info(f"ModuleManager initialized at base path: {self.base_path}")

    def load_modules(self):
        if os.path.exists(self.json_file):
            try:
                with open(self.json_file, "r", encoding="utf-8") as f:
                    self.modules = ujson.load(f)
                logger.info(f"Loaded existing modules from {self.json_file}. Total: {len(self.modules)}")
            except (ujson.JSONDecodeError, ValueError) as e:
                logger.warning(f"Failed to load modules JSON ({self.json_file}): {e}. Will rebuild.")
                self.modules = {}
        else:
            logger.info(f"No existing module file found at {self.json_file}. Starting fresh.")
            self.modules = {}

    def save_modules(self):
        try:
            with open(self.json_file, "w", encoding="utf-8") as f:
                f.write(ujson.dumps(self.modules, indent=2, ensure_ascii=False).replace("\\/", "/"))
            logger.info(f"Modules saved to {self.json_file} (Count: {len(self.modules)})")
        except Exception as e:
            logger.error(f"Failed to save modules: {e}")

    def extract_metadata(self, file_path):
        metadata = {
            "title": "Unknown",
            "description": "Unknown",
            "cve": "Unknown",
            "google_dork": "Unknown",
            "author": "Intframework Team",
            "test_status": "Not Tested"
        }
        pattern = re.compile(
            r"#\s*(?:Exploit|Auxiliary|Encoder|Evasion)?\s*(title|cve|google dork|author|test|description)\s*:\s*(.+)",
            re.IGNORECASE
        )
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                for line in f:
                    m = pattern.match(line.strip())
                    if m:
                        key, value = m.groups()
                        key = key.lower()
                        value = value.strip()
                        if key == "title":
                            metadata["title"] = value
                        elif key == "description":
                            metadata["description"] = value
                        elif key == "cve":
                            metadata["cve"] = value
                        elif key == "google dork":
                            metadata["google_dork"] = value
                        elif "author" in key:
                            metadata["author"] = value
                        elif "test" in key:
                            allowed = ["perfect", "good", "bad", "best", "worst", "lousy", "good+", "best+", "perfect+", "great", "great+"]
                            if value.lower() in allowed:
                                metadata["test_status"] = value.lower()
            return metadata
        except Exception as e:
            logger.warning(f"Metadata extraction failed for {file_path}: {e}")
            return metadata

    def detect_module_type(self, file_path):
        for regex, m_type in MODULE_PATTERNS.items():
            if re.search(regex, file_path, re.IGNORECASE):
                return m_type
        return "unknown"

    def get_file_info(self, file_path):
        try:
            size_kb = round(os.path.getsize(file_path) / 1024, 2)
            mod_time = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime("%Y-%m-%d %H:%M:%S")
            executable = os.access(file_path, os.X_OK)
            return {"size_kb": size_kb, "last_modified": mod_time, "executable": executable}
        except Exception as e:
            logger.warning(f"File info retrieval failed for {file_path}: {e}")
            return {"size_kb": 0, "last_modified": "Unknown", "executable": False}

    def extract_extra_info(self, directory):
        extra = {}
        readme = os.path.join(directory, "README.md")
        config = os.path.join(directory, "config.json")

        if os.path.exists(readme):
            try:
                with open(readme, "r", encoding="utf-8") as f:
                    extra["readme_summary"] = f.readline().strip()
            except Exception as e:
                logger.warning(f"Failed to read README.md in {directory}: {e}")

        if os.path.exists(config):
            try:
                with open(config, "r", encoding="utf-8") as f:
                    extra["config"] = ujson.load(f)
            except Exception as e:
                logger.warning(f"Failed to read config.json in {directory}: {e}")

        return extra

    def analyze_code_intelligence(self, file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                code = f.read()
            result = analyzer.analyze_module_code(code)
            return result if isinstance(result, dict) else {}
        except Exception as e:
            logger.warning(f"AI analysis failed for {file_path}: {e}")
            return {}

    def _process_file(self, file_path):
        ext = os.path.splitext(file_path)[1]
        mod_name = os.path.splitext(os.path.basename(file_path))[0]
        root = os.path.dirname(file_path)

        mod_type = self.detect_module_type(file_path)
        metadata_source = os.path.join(root, "__init__.py") if os.path.exists(os.path.join(root, "__init__.py")) else file_path

        metadata = self.extract_metadata(metadata_source)
        file_info = self.get_file_info(file_path)
        extra = self.extract_extra_info(root)
        intelligence = self.analyze_code_intelligence(file_path)

        module_data = {
            "name": mod_name,
            "path": file_path,
            "type": mod_type,
            "command": f"{SUPPORTED_LANGUAGES.get(ext, 'unknown')} {mod_name}",
            **metadata,
            **file_info,
            **extra,
            **intelligence
        }
        return file_path, module_data

    def scan_modules(self):
        logger.info(f"Starting module scan in: {MODULE_DIRECTORIES}")
        found_modules = {}

        # Toplam dosya sayısı ve işlenecek dosyalar listesi oluşturma
        all_files = []
        for mod_dir in MODULE_DIRECTORIES:
            full_path = os.path.join(self.base_path, mod_dir)
            if not os.path.exists(full_path):
                logger.warning(f"Module directory does not exist: {full_path}")
                continue
            for root, _, files in os.walk(full_path):
                for file in files:
                    ext = os.path.splitext(file)[1]
                    if ext in SUPPORTED_LANGUAGES:
                        all_files.append(os.path.normpath(os.path.join(root, file)))

        logger.info(f"Total candidate module files found: {len(all_files)}")

        # Çoklu iş parçacığı ile dosya işlemleri paralel yapılıyor
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = {executor.submit(self._process_file, f): f for f in all_files}

            for future in as_completed(futures):
                file_path, module_data = future.result()
                found_modules[file_path] = module_data
                logger.debug(f"Processed module: {file_path}")

        self.modules = found_modules
        self.save_modules()
        logger.info(f"Module scan completed. {len(found_modules)} modules indexed.")
        return f"[+] {len(found_modules)} module(s) found and saved."

    def list_modules(self):
        return list(self.modules.keys())

    def get_module(self, name):
        # Modül isimlerine göre arama, benzersiz isimlere göre performanslı
        for mod in self.modules.values():
            if mod.get("name", "").lower() == name.lower():
                return mod
        return None

# CLI Komutları için
def main():
    parser = argparse.ArgumentParser(description="INTFramework Module Manager CLI")
    parser.add_argument("action", choices=["scan", "list", "get"], help="Action to perform")
    parser.add_argument("--name", help="Module name for 'get' action")

    args = parser.parse_args()
    manager = ModuleManager()

    if args.action == "scan":
        print(manager.scan_modules())
    elif args.action == "list":
        modules = manager.list_modules()
        print("\n".join(modules))
    elif args.action == "get":
        if not args.name:
            logger.error("[-] --name parameter is required for 'get' action.")
            print("[-] --name parameter is required for 'get' action.")
        else:
            module = manager.get_module(args.name)
            if module:
                print(ujson.dumps(module, indent=2, ensure_ascii=False))
            else:
                print(f"[-] Module '{args.name}' not found.")

if __name__ == "__main__":
    main() 