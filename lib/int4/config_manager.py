import importlib.util
import json
import os
import ast

DB_PATH = "db/set.int4"
module_context = {}
option_schema = {}
locked_options = set()
loaded_module = None

def load_schema_from_module(module_path):
    global option_schema, loaded_module
    try:
        spec = importlib.util.spec_from_file_location("module", module_path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        loaded_module = mod

        if hasattr(mod, "option_schema") and isinstance(mod.option_schema, dict):
            option_schema.clear()
            option_schema.update(mod.option_schema)
        else:
            option_schema.clear()
    except Exception as e:
        print(f"[!] Critical: Failed to load module schema from {module_path}: {e}")
        option_schema.clear()
        loaded_module = None

def convert_value(value, target_type):
    try:
        if target_type == bool:
            return str(value).lower() in ("1", "true", "yes", "on")
        elif target_type == int:
            return int(value)
        elif target_type == float:
            return float(value)
        elif target_type == list:
            return ast.literal_eval(value) if isinstance(value, str) else value
        elif target_type == str:
            return str(value)
        return value
    except Exception:
        raise ValueError(f"Conversion error: Cannot convert '{value}' to {target_type.__name__}")

def set_option(key, value):
    key = key.strip().lower()
    if key not in option_schema or key in locked_options:
        return False

    meta = option_schema[key]
    expected_type = meta.get("type", str)
    try:
        converted = convert_value(value, expected_type)
        module_context[key] = converted
        save_context()
        if loaded_module and hasattr(loaded_module, "option_set_hook"):
            try:
                loaded_module.option_set_hook(key, converted)
            except Exception:
                pass
        return True
    except Exception:
        return False

def reset_option(key):
    """Reset a specific option to its default if available."""
    key = key.strip().lower()
    if key in option_schema:
        if "default" in option_schema[key]:
            module_context[key] = option_schema[key]["default"]
        elif key in module_context:
            del module_context[key]
        save_context()

def reset_all_options():
    """Reset all configurable options."""
    for key in list(module_context.keys()):
        reset_option(key)

def list_set_options():
    """Return only options that are currently set by user."""
    return {k: v for k, v in module_context.items() if k in option_schema}

def get_option(key):
    key = key.lower()
    if key in option_schema:
        return module_context.get(key, option_schema[key].get("default"))
    return None

def save_context():
    try:
        os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
        with open(DB_PATH, "w") as f:
            json.dump(module_context, f)
    except Exception as e:
        print(f"[!] Critical: Failed to save context: {e}")

def load_context():
    global module_context
    try:
        if os.path.exists(DB_PATH):
            with open(DB_PATH, "r") as f:
                module_context = json.load(f)
    except Exception:
        module_context = {}

def show_options():
    print("\nOptions:")
    print("{:<20} {:<25} {:<10} {}".format("Name", "Current Setting", "Required", "Description"))
    print("-" * 80)
    for key, meta in option_schema.items():
        current = module_context.get(key, meta.get("default", ""))
        required = "yes" if meta.get("required", False) else "no"
        description = meta.get("description", "")
        print(f"{key:<20} {str(current):<25} {required:<10} {description}")
    print()

def validate_required_options():
    missing = []
    for key, meta in option_schema.items():
        required = meta.get("required", False)
        default = meta.get("default")
        current = module_context.get(key)
        if required and (not current and not default):
            missing.append(key)
    if missing:
        print(f"[!] Missing required options:")
        for key in missing:
            print(f"    - {key}")
        return False
    return True

def option_lock(key):
    """Prevent an option from being changed."""
    locked_options.add(key.lower())

def option_unlock(key):
    """Allow a previously locked option to be changed."""
    locked_options.discard(key.lower())