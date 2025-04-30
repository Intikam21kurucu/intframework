import importlib.util
import json
import os

DB_PATH = "db/set.int4"
module_context = {}
option_schema = {}

def load_schema_from_module(module_path):
    global option_schema
    spec = importlib.util.spec_from_file_location("module", module_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    if hasattr(mod, "option_schema"):
        option_schema = mod.option_schema
    else:
        option_schema = {}

def set_option(key, value):
    key = key.lower()
    if key in option_schema:
        module_context[key] = value
        save_context()
    else:
        print(f"[!] '{key}' is not a valid option and was ignored.")

def save_context():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    with open(DB_PATH, "w") as f:
        json.dump(module_context, f)

def load_context():
    global module_context
    if os.path.exists(DB_PATH):
        with open(DB_PATH, "r") as f:
            module_context = json.load(f)

def show_options():
    print("\nOptions:")
    print("{:<20} {:<25} {:<10} {}".format("Name", "Current Setting", "Required", "Description"))
    print("-" * 70)
    for key, meta in option_schema.items():
        current = module_context.get(key, meta.get("default", ""))
        required = "yes" if meta.get("required", False) else "no"
        description = meta.get("description", "")
        print(f"{key:<20} {str(current):<25} {required:<10} {description}")
    print()

def validate_required_options():
    missing = []
    for key, meta in option_schema.items():
        if meta.get("required") and not module_context.get(key) and not meta.get("default"):
            missing.append(key)
    if missing:
        print(f"[!] The following required options are missing and have no default:")
        for k in missing:
            print(f"    - {k}")
        return False
    return True