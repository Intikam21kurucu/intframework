import wifi
import argparse

def wifi_scan(wlan):
    cells = wifi.Cell.all(wlan)
    networks = []
    for cell in cells:
        networks.append(cell.ssid)
        print(f"SSID: {cell.ssid}, Sinyal: {cell.signal}")
    return networks

parser = argparse.ArgumentParser(prog="dronescan", description='scaning wifis')

parser.add_argument("wlan", help="your want to scaning wlan")
parser.add_argument("-s", "--scan-ip", help="scaning", dest="scan")

args = parser.parse_args()

if args.scan:
	wifis = wifi_scan(args.wlan)
	print(f"[{Fore.RED}intbase{Fore.RESET}]" + """
	""" + wifis)