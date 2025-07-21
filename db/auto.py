import argparse
import ujson
import shlex
import os
import re
import warnings
from datetime import datetime

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

MODULE_PATTERNS = {
    r"exploit": "exploit",
    r"payload": "payload",
    r"auxiliary": "auxiliary",
    r"intpro": "intPRO",
    r"tools": "tool",
    r"cve": "cve"
}

module_directorys = ["intPRO", "modules", "tools"]

class ModuleManager:
    def __init__(self, json_file="modules.json"):
        self.json_file = json_file
        self.modules = self.load_modules()

    def load_modules(self):
        if os.path.exists(self.json_file):
            try:
                with open(self.json_file, "r", encoding="utf-8") as f:
                    return ujson.load(f)
            except (ujson.JSONDecodeError, ValueError):
                warnings.warn(f"Warning: {self.json_file} is corrupted. Creating a new JSON structure.")
        return {}

    def save_modules(self):
        try:
            with open(self.json_file, "w", encoding="utf-8") as f:
                f.write(ujson.dumps(self.modules, indent=2, ensure_ascii=False).replace("\\/", "/"))
            print(f"Successfully saved to {self.json_file}.")
        except Exception as e:
            warnings.warn(f"Error while saving {self.json_file}: {e}")

    def extract_metadata(self, file_path):
        metadata = {
            "title": "Unknown",
            "description": "Unknown",
            "cve": "Unknown",
            "google_dork": "Unknown",
            "author": "Intframework Team",
            "test_status": "Not Tested"
        }

        metadata_regex = re.compile(
    r"#\s*(?:Exploit\s*|Auxiliary\s*|Encoder\s*|Evasion\s*)?(title|cve|google dork|author|test|description)\s*:\s*(.+)", 
    re.IGNORECASE
)

        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                for line in f:
                    match = metadata_regex.match(line.strip())
                    if match:
                        key, value = match.groups()
                        key = key.lower()

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
                        	if value.lower() in ["perfect", "good", "bad", "best", "worst", "lousy", "good+", "best+", "perfect+", "great", "great+"]:
                        		metadata["test_status"] = value.lower()
        except Exception as e:
            warnings.warn(f"Metadata read error: {e}")

        return metadata

    def detect_module_type(self, file_path):
        for pattern, module_type in MODULE_PATTERNS.items():
            if re.search(pattern, file_path, re.IGNORECASE):
                return module_type
        return "unknown"

    def get_file_info(self, file_path):
        try:
            size = round(os.path.getsize(file_path) / 1024, 2)  
            modified_time = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d %H:%M:%S')
            executable = os.access(file_path, os.X_OK)  
            return {"size_kb": size, "last_modified": modified_time, "executable": executable}
        except Exception as e:
            warnings.warn(f"File info retrieval error: {e}")
            return {"size_kb": 0, "last_modified": "Unknown", "executable": False}

    def extract_extra_info(self, directory):
        extra_info = {}
        readme_path = os.path.join(directory, "README.md")
        config_path = os.path.join(directory, "config.json")

        if os.path.exists(readme_path):
            try:
                with open(readme_path, "r", encoding="utf-8") as f:
                    extra_info["readme_summary"] = f.readline().strip()  
            except Exception as e:
                warnings.warn(f"Error reading README: {e}")

        if os.path.exists(config_path):
            try:
                with open(config_path, "r", encoding="utf-8") as f:
                    config_data = ujson.load(f)
                    extra_info["config"] = config_data
            except Exception as e:
                warnings.warn(f"Error reading config: {e}")

        return extra_info

    def scan_modules(self):
        found_modules = {}

        def scan_directory(directory):
            if not os.path.exists(directory):
                os.makedirs(directory)

            for root, _, files in os.walk(directory):
                for file in files:
                    file_path = shlex.quote(os.path.normpath(os.path.join(root, file)))
                    file_ext = os.path.splitext(file)[1]

                    if file_ext in SUPPORTED_LANGUAGES:
                        module_name = os.path.splitext(file)[0]
                        language = SUPPORTED_LANGUAGES[file_ext]
                        module_type = self.detect_module_type(file_path)

                        init_path = os.path.join(root, "__init__.py")
                        metadata_source = init_path if os.path.exists(init_path) else file_path
                        metadata = self.extract_metadata(metadata_source)

                        file_info = self.get_file_info(file_path)
                        extra_info = self.extract_extra_info(root)

                        found_modules[file_path] = {
                            "name": module_name,
                            "path": file_path,
                            "language": language,
                            "command": f"{language} {file}",
                            "type": module_type,
                            **metadata,
                            **file_info,
                            **extra_info
                        }

        for directory in module_directorys:
            scan_directory(directory)

        self.modules = found_modules
        self.save_modules()

        return f"{len(found_modules)} module(s) found and saved to modules.json"

    def list_modules(self):
        return list(self.modules.keys())

    def get_module(self, name):
        return self.modules.get(name, None)

# Exportable for import use
def run_scan():
    manager = ModuleManager()
    return manager.scan_modules()

def main():
    parser = argparse.ArgumentParser(description="Module Manager CLI")
    parser.add_argument("action", choices=["scan", "list", "get"], help="Action to perform")
    parser.add_argument("--name", help="Module name (required for 'get')")

    args = parser.parse_args()
    manager = ModuleManager()

    if args.action == "scan":
        print(manager.scan_modules())
    elif args.action == "list":
        print(manager.list_modules())
    elif args.action == "get":
        if not args.name:
            print("Error: --name is required for 'get' action.")
        else:
            module = manager.get_module(args.name)
            print(module if module else f"Module '{args.name}' not found.")

if __name__ == "__main__":
    main()