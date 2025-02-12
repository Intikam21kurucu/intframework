#!/usr/bin/env python3
import argparse
import os
import string

# En yaygın zayıf şifrelerin listesi (istenirse genişletilebilir)
COMMON_WEAK_PASSWORDS = {
    "123456", "password", "123456789", "qwerty", "12345678",
    "111111", "123123", "abc123", "password1", "1234"
}

def calculate_strength(password):
    length = len(password)
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    if password in COMMON_WEAK_PASSWORDS:
        return "Very Weak (Common Password)"

    if length < 8:
        return "Very Weak"
    elif length < 12:
        return "Weak"
    elif length >= 12 and (has_lower and has_upper and has_digit and has_special):
        return "Strong"
    elif length >= 16:
        return "Very Strong"
    
    return "Medium"

def analyze_passwords(file_path):
    if not os.path.exists(file_path):
        print(f"[!] File not found: {file_path}")
        return

    with open(file_path, "r") as file:
        passwords = file.read().splitlines()

    results = []
    for password in passwords:
        strength = calculate_strength(password)
        results.append(f"{password}: {strength}")

    print("\n".join(results))

def main():
    parser = argparse.ArgumentParser(description="Analyze password strength from a file.")
    parser.add_argument("-f", "--file", required=True, help="File containing passwords (one per line)")
    args = parser.parse_args()

    analyze_passwords(args.file)

if __name__ == "__main__":
    main()