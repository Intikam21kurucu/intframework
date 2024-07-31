import smtplib
import argparse

def validate_email(email):
    try:
        domain = email.split('@')[1]
        with smtplib.SMTP('smtp.' + domain) as server:
            server.set_debuglevel(0)
            return True
    except Exception:
        return False

def check_emails(wordlist):
    print("Checking email addresses...")
    with open(wordlist, 'r') as file:
        for line in file:
            email = line.strip()
            if validate_email(email):
                print(f"{email} is valid")
            else:
                print(f"{email} is invalid")

def main():
    parser = argparse.ArgumentParser(description='Check if email addresses are valid.')
    parser.add_argument('wordlist', type=str, help='Path to the wordlist file with email addresses.')
    args = parser.parse_args()
    
    check_emails(args.wordlist)

if __name__ == '__main__':
    main()