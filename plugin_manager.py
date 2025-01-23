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

class PluginManager:
    """Loads plugins and integrates them with the EventManager."""
    def __init__(self, plugin_dir="plugins", event_manager=None):
        if not os.path.exists(plugin_dir):
            raise FileNotFoundError(f"Plugin directory '{plugin_dir}' does not exist.")
        self.plugin_dir = plugin_dir
        self.plugins = {}  # Dictionary to store loaded plugins
        self.event_manager = event_manager or EventManager()  # EventManager instance

    def load_plugins(self):
        """Loads all plugins from the specified directory."""
        for filename in os.listdir(self.plugin_dir):
            if filename.endswith(".py"):
                plugin_name = filename[:-3]
                plugin_path = f"{self.plugin_dir}.{plugin_name}"
                try:
                    # Dynamically import the plugin module
                    module = importlib.import_module(plugin_path)
                    self.plugins[plugin_name] = module
                    
                    # Call the `register` function of the plugin
                    if hasattr(module, "register"):
                        module.register(self.event_manager)
                        print(f"{Fore.GREEN}[+] Plugin activated: {plugin_name}")
                    else:
                        print(f"{Fore.RED}[!] Plugin '{plugin_name}' does not have a 'register' function.")
                except Exception as e:
                    print(f"{Fore.RED}[!] Failed to load plugin: {filename}. Error: {e}")
                    
    def load_plugin(self, arg):
    	try:
    		os.system(f"cp {arg} $INTFRAMEWORK_PATH/plugins/")
    		print(f"{Fore.GREEN}[+] loaded plugin: {arg}")
    	except Exception as e:
    		print(f"{Fore.RED}[!] Failed to load plugin: {arg}")
    	
    def deactivate_plugins(self):
        """Deactivates all plugins (called when the system shuts down)."""
        for plugin_name, plugin in self.plugins.items():
            if hasattr(plugin, "deactivate"):
                plugin.deactivate()
                print(f"[-] Plugin deactivated: {plugin_name}")
                

    def list_plugins(self):
        """Displays a list of loaded plugins."""
        if not self.plugins:
            print("[!] No plugins loaded.")
        else:
            print("[+] Active Plugins:")
            for name, module in self.plugins.items():
                description = getattr(module, "PLUGIN_DESCRIPTION", "No description available.")
                version = getattr(module, "PLUGIN_VERSION", "Unknown")
                print(f"  - {name}: {description} (v{version})")