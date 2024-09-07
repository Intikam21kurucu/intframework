#!/usr/bin/env python3
import importlib
import argparse
import os
import sys

class PluginManager:
    def __init__(self):
        self.plugins = {}
        self.commands = {}
        self.plugin_counter = 1

    def load_plugin(self, plugin_path):
        """
        Verilen eklenti yolunu dinamik olarak yükler ve sıralı bir isimle kaydeder.
        """
        plugin_name = f'plugin{self.plugin_counter}'
        self.plugin_counter += 1

        try:
            plugin = importlib.import_module(plugin_path)
            self.plugins[plugin_name] = plugin

            # `description` veya `desc` değişkenini al
            description = getattr(plugin, 'description', None) or getattr(plugin, 'desc', 'No description available')
            status = self.check_status(plugin)
            print(f"{plugin_name:<20} {description:<30} {status:<10} {'working':<10}")

            # `argparse` modülünü kontrol et
            self.setup_argparse(plugin, plugin_name)

        except ModuleNotFoundError:
            status = "bad"
            description = "Plugin not found"
            print(f"{plugin_name:<20} {description:<30} {status:<10} {'working':<10}")
        except Exception as e:
            status = "bad"
            description = f"Error: {e}"
            print(f"{plugin_name:<20} {description:<30} {status:<10} {'working':<10}")

    def setup_argparse(self, plugin, plugin_name):
        """
        Eklenti içindeki argparse modülünü dinamik olarak ayarlar ve komutları çalıştırır.
        """
        if hasattr(plugin, 'get_parser'):
            parser = plugin.get_parser()
            if isinstance(parser, argparse.ArgumentParser):
                self.commands[plugin_name] = parser

                # Komutları ve argümanları al
                subparsers = parser._subparsers
                if subparsers:
                    for command_name, command_parser in subparsers.choices.items():
                        self.commands[(plugin_name, command_name)] = command_parser

    def check_status(self, plugin):
        """
        Eklentinin durumunu kontrol eder ve durumu belirler.
        """
        try:
            # Eklentinin çalışabilirliğini test et
            if hasattr(plugin, 'initialize'):
                plugin.initialize()
                return "best"
            return "good"
        except Exception as e:
            print(f"Error during status check: {e}")
            return "good"

    def run_command(self, plugin_name, *args):
        """
        Verilen eklentiyi ve argümanları kullanarak komutu çalıştırır.
        """
        if plugin_name in self.commands:
            try:
                parser = self.commands[plugin_name]
                parsed_args = parser.parse_args(args)
                func = getattr(self.plugins[plugin_name], 'run', None)
                if callable(func):
                    func(parsed_args)
                    status = "best"
                    description = getattr(self.plugins[plugin_name], 'description', None) or getattr(self.plugins[plugin_name], 'desc', 'No description available')
                else:
                    status = "bad"
                    description = "Command function not found"
            except Exception as e:
                status = "good"
                description = f"Error: {e}"
                print(f"Error during command execution: {e}")
        else:
            status = "bad"
            description = "Command not found"

        print(f"{plugin_name:<20} {description:<30} {status:<10} {'working':<10}")

    def list_plugins(self):
        """
        Yüklü eklentileri listeler.
        """
        if self.plugins:
            print("Yüklü Eklentiler:")
            print("{:<20} {:<30} {:<10} {:<10}".format('Name', 'Description', 'Status', 'State'))
            print("-" * 70)
            for plugin_name, plugin in self.plugins.items():
                description = getattr(plugin, 'description', None) or getattr(plugin, 'desc', 'No description available')
                status = self.check_status(plugin)
                print("{:<20} {:<30} {:<10} {:<10}".format(plugin_name, description, status, "working"))
        else:
            print("Yüklü eklenti bulunmuyor.")

def main():
    # Eklenti yöneticisini oluştur
    manager = PluginManager()

    # Komut satırından argümanları al
    if len(sys.argv) < 2:
        print("Kullanım: python script.py [plugin_path] [command] [args...]")
        return

    plugin_path = sys.argv[1]
    command = sys.argv[2] if len(sys.argv) > 2 else None
    args = sys.argv[3:] if len(sys.argv) > 3 else []

    # Eklentiyi yükle
    manager.load_plugin(plugin_path)

    # Eklenti listesini yazdır
    manager.list_plugins()

    # Komut varsa çalıştır
    if command:
        manager.run_command(command, *args)

if __name__ == "__main__":
    main()