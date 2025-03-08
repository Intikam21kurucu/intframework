#!/usr/bin/env python3
# Title: Advenced Hash İdentifier (+50 Hash types)
#test: good
import argparse
import re

HASH_PATTERNS = {
    "MD4": r"^[a-fA-F0-9]{32}$",
    "MD5": r"^[a-fA-F0-9]{32}$",
    "SHA-1": r"^[a-fA-F0-9]{40}$",
    "SHA-224": r"^[a-fA-F0-9]{56}$",
    "SHA-256": r"^[a-fA-F0-9]{64}$",
    "SHA-384": r"^[a-fA-F0-9]{96}$",
    "SHA-512": r"^[a-fA-F0-9]{128}$",
    "SHA3-256": r"^[a-fA-F0-9]{64}$",
    "SHA3-512": r"^[a-fA-F0-9]{128}$",
    "RIPEMD-128": r"^[a-fA-F0-9]{32}$",
    "RIPEMD-160": r"^[a-fA-F0-9]{40}$",
    "RIPEMD-256": r"^[a-fA-F0-9]{64}$",
    "RIPEMD-320": r"^[a-fA-F0-9]{80}$",
    "Whirlpool": r"^[a-fA-F0-9]{128}$",
    "NTLM": r"^[a-fA-F0-9]{32}$",
    "LM": r"^[a-fA-F0-9]{16}$",
    "MySQL 5+": r"^\*[a-fA-F0-9]{40}$",
    "MySQL 3+": r"^[a-fA-F0-9]{16}$",
    "MSSQL 2000": r"^0x0100[a-fA-F0-9]{88}$",
    "MSSQL 2005": r"^0x0200[a-fA-F0-9]{136}$",
    "MSSQL 2012+": r"^0x0300[a-fA-F0-9]{136}$",
    "Oracle 7-10g": r"^[a-fA-F0-9]{16}$",
    "Oracle 11g": r"^[a-zA-Z0-9]{48}$",
    "Oracle 12c": r"^[a-zA-Z0-9]{64}$",
    "PostgreSQL": r"^md5[a-fA-F0-9]{32}$",
    "Cisco-PIX": r"^[a-zA-Z0-9./]{16}$",
    "Cisco-IOS": r"^\$1\$[a-zA-Z0-9./]{8}\$[a-zA-Z0-9./]{22}$",
    "Cisco Type 7": r"^.{4,}$",
    "Juniper Netscreen/SSG (ScreenOS)": r"^[a-zA-Z0-9]{30}$",
    "bcrypt (Blowfish)": r"^\$2[ayb]\$.{56}$",
    "PBKDF2-HMAC-SHA1": r"^\$pbkdf2-sha1\$[0-9]+\$[a-zA-Z0-9+/=]+\$[a-zA-Z0-9+/=]+$",
    "PBKDF2-HMAC-SHA256": r"^\$pbkdf2-sha256\$[0-9]+\$[a-zA-Z0-9+/=]+\$[a-zA-Z0-9+/=]+$",
    "PBKDF2-HMAC-SHA512": r"^\$pbkdf2-sha512\$[0-9]+\$[a-zA-Z0-9+/=]+\$[a-zA-Z0-9+/=]+$",
    "Argon2": r"^\$argon2[a-z]+\$v=\d+\$m=\d+,t=\d+,p=\d+\$.+",
    "SCRAM-SHA-1": r"^SCRAM-SHA-1\$.+$",
    "SCRAM-SHA-256": r"^SCRAM-SHA-256\$.+$",
    "CRC32": r"^[a-fA-F0-9]{8}$",
    "GOST": r"^[a-fA-F0-9]{64}$",
    "Skein-512": r"^[a-fA-F0-9]{128}$",
    "SAP MD5": r"^[a-fA-F0-9]{32}$",
    "SAP SHA1": r"^[a-fA-F0-9]{40}$",
    "bcrypt-SHA256": r"^\$bcrypt-sha256\$[0-9]+\$[a-zA-Z0-9+/=]+\$[a-zA-Z0-9+/=]+$",
    "Django PBKDF2": r"^\$pbkdf2-sha256\$[0-9]+\$[a-zA-Z0-9+/=]+\$[a-zA-Z0-9+/=]+$",
}

def identify_hash(hash_value):
    possible_types = []

    for hash_type, pattern in HASH_PATTERNS.items():
        if re.match(pattern, hash_value):
            possible_types.append(hash_type)

    return possible_types if possible_types else ["Unknown"]

def main():
    parser = argparse.ArgumentParser(description="Advanced Hash Identifier (50+ Hash Types)")
    parser.add_argument("-H", "--hash", required=True, help="Hash value to analyze")
    args = parser.parse_args()

    hash_value = args.hash.strip()
    possible_types = identify_hash(hash_value)

    print(f"\n[+] Given Hash: {hash_value}")
    print(f"[+] Possible Hash Types: {', '.join(possible_types)}\n")

if __name__ == "__main__":
    main()