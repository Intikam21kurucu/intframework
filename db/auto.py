#!/usr/bin/env python3
import argparse
import ujson
import os
import re
import hashlib
import logging
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from lib.ai_score import IntelligenceAnalyzer
import os

# Logger yapılandırması - sadece önemli loglar
logger = logging.getLogger("ModuleManager")
logger.setLevel(logging.WARNING)  # DEBUG -> WARNING sessiz, sadece hata ve uyarı
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)  # Sadece errorları göster
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

file_handler = logging.FileHandler("module_manager.log", encoding="utf-8")
file_handler.setLevel(logging.WARNING)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

analyzer = IntelligenceAnalyzer()

SUPPORTED_LANGUAGES = {
    ".py2": "python2", ".py": "python3", ".c": "gcc", ".cpp": "g++", ".cs": "csharp",
    ".js": "node", ".rb": "ruby", ".php": "php", ".pl": "perl", ".sh": "bash",
    ".go": "go run", ".sql": "sqlcmd", ".html": "browser", ".lua": "lua", ".ps1": "powershell"
}

MODULE_PATTERNS = {
    r"exploit": "exploit",
    r"payload": "payload",
    r"auxiliary": "auxiliary",
    r"intpro": "intPRO",
    r"tools": "tool",
    r"cve": "cve"
}

MODULE_DIRECTORIES = ["intPRO", "modules", "tools"]

class ModuleManager:
    def __init__(self, base_path=".", json_file="modules.json", max_workers=16, use_cache=True):
        self.base_path = os.path.abspath(base_path)
        self.json_file = os.path.join(self.base_path, json_file)
        self.modules = {}
        self.max_workers = max_workers
        self.use_cache = use_cache
        self._file_cache = {}  # path -> (mtime, size, hash)
        self.load_modules()
        logger.info(f"ModuleManager initialized at base path: {self.base_path}")

    def load_modules(self):
        if os.path.exists(self.json_file):
            try:
                with open(self.json_file, "r", encoding="utf-8") as f:
                    self.modules = ujson.load(f)
                # Cache dosya bilgisi oluştur
                for path, data in self.modules.items():
                    self._file_cache[path] = (data.get("last_modified", None), data.get("size_kb", 0), data.get("file_hash", None))
                logger.info(f"Loaded modules from {self.json_file}. Total: {len(self.modules)}")
            except Exception as e:
                logger.warning(f"Failed to load modules JSON: {e}. Will rebuild.")
                self.modules = {}
                self._file_cache = {}
        else:
            self.modules = {}
            self._file_cache = {}

    def save_modules(self):
        try:
            with open(self.json_file, "w", encoding="utf-8") as f:
                f.write(ujson.dumps(self.modules, indent=2, ensure_ascii=False).replace("\\/", "/"))
            logger.info(f"Modules saved to {self.json_file}. Count: {len(self.modules)}")
        except Exception as e:
            logger.error(f"Failed to save modules: {e}")

    def _hash_file(self, file_path, block_size=65536):
        """ Dosya hash hesaplama (MD5) """
        md5 = hashlib.md5()
        try:
            with open(file_path, "rb") as f:
                while chunk := f.read(block_size):
                    md5.update(chunk)
            return md5.hexdigest()
        except Exception as e:
            logger.warning(f"Failed hashing file {file_path}: {e}")
            return None

    def _is_cached_and_unchanged(self, file_path):
        """ Dosyanın önceden işlenip işlenmediğini ve değişip değişmediğini kontrol eder """
        try:
            stat = os.stat(file_path)
            mtime = datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
            size_kb = round(stat.st_size / 1024, 2)
            cached = self._file_cache.get(file_path)
            if not cached:
                return False
            cached_mtime, cached_size, cached_hash = cached
            if cached_mtime == mtime and cached_size == size_kb:
                # Hash kontrolü istenirse açılabilir. Performans için kapalı.
                return True
            return False
        except Exception as e:
            logger.warning(f"Failed to stat file {file_path}: {e}")
            return False

    def extract_metadata(self, file_path):
        metadata = {
            "title": "Unknown", "description": "Unknown", "cve": "Unknown",
            "google_dork": "Unknown", "author": "Intframework Team", "test_status": "Not Tested"
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
            stat = os.stat(file_path)
            size_kb = round(stat.st_size / 1024, 2)
            mod_time = datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
            executable = os.access(file_path, os.X_OK)
            file_hash = self._hash_file(file_path)
            return {"size_kb": size_kb, "last_modified": mod_time, "executable": executable, "file_hash": file_hash}
        except Exception as e:
            logger.warning(f"File info retrieval failed for {file_path}: {e}")
            return {"size_kb": 0, "last_modified": "Unknown", "executable": False, "file_hash": None}

    def extract_extra_info(self, directory):
        extra = {}
        candidates = {
            "readme_summary": "README.md",
            "license": "LICENSE",
            "config": "config.json"
        }
        for key, filename in candidates.items():
            path = os.path.join(directory, filename)
            if os.path.exists(path):
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        if key == "readme_summary":
                            extra[key] = f.readline().strip()
                        elif key == "config":
                            extra[key] = ujson.load(f)
                        else:
                            extra[key] = f.read().strip()
                except Exception as e:
                    logger.warning(f"Failed to read {filename} in {directory}: {e}")
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
        # Eğer cache aktifse ve dosya değişmemişse önceki veriyi kullan
        if self.use_cache and self._is_cached_and_unchanged(file_path):
            return file_path, self.modules.get(file_path, {})

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
        found_modules = {}

        all_files = []
        for mod_dir in MODULE_DIRECTORIES:
            full_path = os.path.join(self.base_path, mod_dir)
            if not os.path.exists(full_path):
                logger.warning(f"Module directory missing: {full_path}")
                continue
            for root, _, files in os.walk(full_path):
                for file in files:
                    ext = os.path.splitext(file)[1]
                    if ext in SUPPORTED_LANGUAGES:
                        all_files.append(os.path.normpath(os.path.join(root, file)))

        if not all_files:
            logger.warning("No module files found in configured directories.")
            return "[!] No module files found."

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = {executor.submit(self._process_file, f): f for f in all_files}
            for future in as_completed(futures):
                try:
                    file_path, module_data = future.result()
                    found_modules[file_path] = module_data
                except Exception as e:
                    logger.error(f"Error processing file: {e}")

        self.modules = found_modules
        self.save_modules()
        return f"[+] {len(found_modules)} module(s) indexed silently."

    def list_modules(self):
        return list(self.modules.keys())

    def get_module(self, name):
        for mod in self.modules.values():
            if mod.get("name", "").lower() == name.lower():
                return mod
        return None

def main():
    parser = argparse.ArgumentParser(description="INTFramework Module Manager CLI")
    parser.add_argument("action", choices=["scan", "list", "get"], help="Action to perform")
    parser.add_argument("--name", help="Module name for 'get' action")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output (optional)")

    args = parser.parse_args()
    manager = ModuleManager()

    if args.action == "scan":
        result = manager.scan_modules()
        if args.verbose:
            print(result)
    elif args.action == "list":
        modules = manager.list_modules()
        if args.verbose:
            print("\n".join(modules))
    elif args.action == "get":
        if not args.name:
            logger.error("[-] --name parameter required for 'get' action.")
            if args.verbose:
                print("[-] --name parameter is required for 'get' action.")
        else:
            module = manager.get_module(args.name)
            if module:
                print(ujson.dumps(module, indent=2, ensure_ascii=False))
            elif args.verbose:
                print(f"[-] Module '{args.name}' not found.")

if __name__ == "__main__":
    os.system("rm -rf module_manager.log")
    main()
    os.system("rm -rf module_manager.log")
    
    