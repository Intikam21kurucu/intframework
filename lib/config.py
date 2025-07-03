# lib/config.py
import os
import sys

INTFRAMEWORK_PATH = os.environ.get("INTFRAMEWORK_PATH")
if INTFRAMEWORK_PATH is None or not os.path.isdir(INTFRAMEWORK_PATH):
    print("[!] INTFRAMEWORK_PATH geçerli değil.")
    sys.exit(1)

INTFRAMEWORK_PATH = os.path.abspath(INTFRAMEWORK_PATH)