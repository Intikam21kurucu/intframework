import bluetooth

def scan_bluetooth_devices():
    print("Scanning for Bluetooth devices...")
    devices = bluetooth.discover_devices(duration=8, lookup_names=True)
    for addr, name in devices:
        print(f"Found Bluetooth device: {name} ({addr})")

if __name__ == "__main__":
    scan_bluetooth_devices()