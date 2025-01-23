#!/usr/bin/env python3
import sys
import time
import os

def scroll_credits(text, delay=0.1):
    lines = text.split('\n')
    empty_lines = [''] * 20  # 20 satır boşluk
    total_lines = len(lines) + 20

    if total_lines > 40:
        credits = lines[:40]
    else:
        credits = lines + empty_lines[:40 - len(lines)]

    for i in range(total_lines):
        if i < total_lines - 20:
            visible_lines = credits[i:i+20]
        else:
            visible_lines = credits[-20:]

        sys.stdout.write('\r' + '\n'.join(visible_lines))
        sys.stdout.flush()
        time.sleep(delay)

credits_text = """












İntikam21 Cyber Team
2024






















Contributors:
- Killer Cyber
- Hileci777
- Linux Cyber


















For:
- İntikam21 Cyber

































Yönetmen:
- Ares Cyber

























Teşekkürler/Thanks:
- Killer Cyber
- Hileci777
- Linux Cyber
"""
os.system("clear")
scroll_credits(credits_text)
