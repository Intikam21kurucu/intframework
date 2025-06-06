import os
import importlib
from colorama import *

init(autoreset=True)

class EventManager:
    """Manages events and their associated plugins."""
    def __init__(self):
        self.events = {}  # Dictionary to store callbacks for each event

    def register_event(self, event_name, callback):
        """Registers a callback function to an event."""
        if event_name not in self.events:
            self.events[event_name] = []
        self.events[event_name].append(callback)

    def trigger_event(self, event_name, *args, **kwargs):
        """Triggers an event and calls all associated plugins."""
        if event_name in self.events:
            for callback in self.events[event_name]:
                callback(*args, **kwargs)
        else:
            print(f"[!] No plugins registered for event '{event_name}'.")

import os
import importlib
import argparse

class PluginManager:
    def __init__(self, plugin_folder="plugins"):
        self.plugin_folder = plugin_folder
        self.plugins = []
        self.command_map = {}

    def load_plugins(self):
        self.plugins.clear()
        self.command_map.clear()

        if not os.path.exists(self.plugin_folder):
            os.makedirs(self.plugin_folder)
            return

        for filename in os.listdir(self.plugin_folder):
            if filename.endswith(".py") and filename not in ("__init__.py", "base.py"):
                module_name = filename[:-3]
                try:
                    mod = importlib.import_module(f"{self.plugin_folder}.{module_name}")
                    if hasattr(mod, "Plugin"):
                        plugin = mod.Plugin()
                        self.plugins.append(plugin)
                        self.command_map.update(plugin.commands)
                except Exception as e:
                    print(f"[!] Plugin load error ({module_name}): {e}")

    def get_plugin_names(self):
        return [p.name for p in self.plugins]

    def get_commands(self):
        return self.command_map.keys()

    def run_command(self, name, args):
        if name in self.command_map:
            return self.command_map[name]["func"](args)
        else:
            return "[!] Command not found."

    def get_plugin_help(self):
        help_lines = []
        help_lines.append("\n[*] Available Plugin Commands:\n")
        help_lines.append(f"{'Command':<20} {'Description':<50} Usage")
        help_lines.append("-" * 90)

        # Eğer command_map yoksa veya boşsa hata vermeden bilgi döndür
        if not hasattr(self, 'command_map') or not isinstance(self.command_map, dict) or not self.command_map:
            help_lines.append(" [!] No commands available or plugin not loaded.\n")
            return "\n".join(help_lines)

        for name, data in self.command_map.items():
            try:
                desc = str(data.get("desc", "No description provided."))
                usage = str(data.get("usage", name))
            except Exception:
                desc = "No description provided."
                usage = name
            help_lines.append(f"{name:<20} {desc:<50} {usage}")

        help_lines.append("")
        return "\n".join(help_lines)

    def load_command(self, plugin_name):
        try:
            mod = importlib.import_module(f"{self.plugin_folder}.{plugin_name}")
            if hasattr(mod, "Plugin"):
                plugin = mod.Plugin()
                self.plugins.append(plugin)
                self.command_map.update(plugin.commands)
                return f"[+] Command '{plugin_name}' loaded."
            else:
                return f"[!] Class 'Plugin' not found in '{plugin_name}'."
        except Exception as e:
            return f"[!] Command load error ({plugin_name}): {e}"

    def list_plugins(self):
        if not self.plugins:
            return "[!] No plugins loaded."
        
        result = "[*] Loaded Plugins:\n"
        for plugin in self.plugins:
            result += f" - {plugin.name}\n"
        return result.strip()

    def load_plugin_module(self, plugin_name, path=None):
        try:
            if path:
                plugin_path = os.path.abspath(path)
                plugin_dir = os.path.dirname(plugin_path)
                plugin_file = os.path.basename(plugin_path)
                plugin_name = plugin_file[:-3] if plugin_file.endswith(".py") else plugin_file

                if plugin_dir not in os.sys.path:
                    os.sys.path.insert(0, plugin_dir)

                mod = importlib.import_module(plugin_name)
            else:
                mod = importlib.import_module(f"{self.plugin_folder}.{plugin_name}")

            if hasattr(mod, "initialize"):
                mod.initialize()
            return f"[+] Plugin module '{plugin_name}' loaded."
        except Exception as e:
            return f"[!] Plugin module load error ({plugin_name}): {e}"


