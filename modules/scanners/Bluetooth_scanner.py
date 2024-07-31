import os

try:
    import bluetooth
except ImportError:
    print("pybluez library not found. Installing...")
    os.system("pip install pybluez")
    import bluetooth

class BluetoothScanner:
    def __init__(self):
        pass

    def scan(self):
        print("Scanning for Bluetooth devices...")
        nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True)

        if nearby_devices:
            for addr, name in nearby_devices:
                print(f"Device Name: {name}, Device Address: {addr}")
        else:
            print("No Bluetooth devices found.")

def main():
    scanner = BluetoothScanner()
    scanner.scan()

if __name__ == '__main__':
    main()