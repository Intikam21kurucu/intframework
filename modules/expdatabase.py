#!/usr/bin/env python3
# exploit_framework.py

def create_option(name, description, default):
    return {
        'name': name,
        'description': description,
        'default': default,
        'value': default
    }

def create_exploit(name, lhost=None, lport=None, rhost=None, rport=None, payload=None):
    return {
        'name': name,
        'options': [
            create_option("LHOST", "Local Host IP Address", lhost or "127.0.0.1"),
            create_option("LPORT", "Local Port", lport or "4444"),
            create_option("RHOST", "Remote Host IP Address", rhost or "192.168.1.1"),
            create_option("RPORT", "Remote Port", rport or "80"),
            create_option("PAYLOAD", "Payload Type", payload or "windows/meterpreter/reverse_tcp")
        ]
    }

def show_options(exploit):
    print(f"{'Option':<20}{'Description':<40}{'Default':<20}{'Current Value':<20}")
    print("-" * 100)
    for option in exploit['options']:
        print(f"{option['name']:<20}{option['description']:<40}{option['default']:<20}{option['value']:<20}")

def set_option(exploit, name, value):
    for option in exploit['options']:
        if option['name'] == name:
            option['value'] = value
            print(f"Set {name} to {value}")
            return
    print(f"Option {name} not found")

def run_exploit(exploit):
    print("Starting exploit with the following options:")
    for option in exploit['options']:
        print(f"{option['name']}: {option['value']}")
    # Buraya gerçek exploit kodu eklenir
    print("Exploit launched!")

def use_framework(framework, exploit_name):
    if exploit_name in framework['exploits']:
        framework['current_exploit'] = framework['exploits'][exploit_name]
        print(f"Using exploit: {exploit_name}")
    else:
        print(f"Exploit {exploit_name} not found")

def initialize_framework():
    return {
        'exploits': {},
        'current_exploit': None
    }

def import_framework():
    return initialize_framework()