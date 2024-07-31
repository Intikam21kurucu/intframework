import wifi
import argparse

def wifi_scan(wlan):
    cells = wifi.Cell.all(wlan)
    networks = []
    for cell in cells:
        networks.append(cell.ssid)
        print(f"SSID: {cell.ssid}, Signal: {cell.signal}")
    return networks

def connect_to_network(ssid, password, wlan):
    cell = None
    for c in wifi.Cell.all(wlan):
        if c.ssid == ssid:
            cell = c
            break
    
    if cell:
        scheme = wifi.Scheme.for_cell(wlan, 'home', cell, password)
        scheme.save()
        scheme.activate()
        print(f"{ssid} connecting...")
    else:
        print(f"{ssid} not found")

def main():
	parser = argparse.ArgumentParser(prog="drone", description='drones')
	parser.add_argument("wlan", help="your want to scaning wlan")
	parser.add_argument("-s", "--scan-ip", help="scaning", dest="scan")
	parser.add_argument("entry", help="entrying but drones")
	parser.add_argument("ssid", help="your ssid")
	parser.add_argument("password", help="your password")
	args = parser.parse_args()
	if args.scan:
		wifis = wifi_scan(args.wlan)
		print(f"[{Fore.RED}intbase{Fore.RESET}]" + """
	""" + wifis)
	if args.en:
		try:
			connect_to_network(args.ssid, args.passw)
		except:
			print(f"[{Fore.RED}intbase{Fore.RESET}] drone entrying failed")

if __name__ == "__main__":
	main()