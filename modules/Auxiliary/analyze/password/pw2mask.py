#!/usr/bin/env python3
# Module: pw2mask
# Author: Jessi

import argparse
from time import sleep
from collections import Counter
from colorama import Fore, Style

# Define colorama colors.
GREEN = Fore.GREEN
RED = Fore.RED
BLUE = Fore.BLUE
WHITE = Fore.WHITE
YELLOW = Fore.YELLOW
CYAN = Fore.CYAN
PINK = Fore.MAGENTA
BRIGHT = Style.BRIGHT
DIM = Style.DIM
NORM = Style.NORMAL
RST = Style.RESET_ALL


def checkMask(char):
    if char.isdigit():
        return "?d"
    if char.isupper():
        return "?u"
    if char.islower():
        return "?l"
    return "?s"


class PW2Mask:
    def __init__(self, passwords_file, common_count, mask_file):
        self.passwords_file = passwords_file
        self.common_count = common_count
        self.mask_file = mask_file
        self.mask_table = []
        self.formatted_table = ""

    def process(self):
        with open(self.passwords_file, "r") as file:
            lines = file.readlines()

        # Get masks for passwords in file.
        for line in lines:
            mask = []  # Blank array for generating the mask.
            cleanLine = line.strip()  # Cleanup the line.
            for c in cleanLine:
                mask.append(checkMask(c))
            self.mask_table.append("".join(mask))  # Add masks to table.

    def table_func(self):
        with open(self.mask_file, mode="wt", encoding="utf-8") as maskFile:
            maskFile.write("\n".join(self.mask_table))

        # Get top x masks.
        common = Counter(self.mask_table)
        mostCommon = common.most_common(self.common_count)
        commonTable = ["%i. %s" % (index + 1, value) for index, value in enumerate(mostCommon)]  # Index with +1 to start at 1.
        self.formatted_table = "\n".join(commonTable)


def main():
    parser = argparse.ArgumentParser(description="Convert passwords to Hashcat-style masks.")
    parser.add_argument("-p", "--passwords", required=True, help="File containing passwords")
    parser.add_argument("-c", "--count", type=int, default=3, help="Number of top masks to display")
    parser.add_argument("-o", "--output", default="masks.txt", help="File to save generated masks")
    args = parser.parse_args()

    print(BLUE + "\n[*]" + RST + " Processing passwords...\n")
    sleep(1.5)

    pw2mask = PW2Mask(args.passwords, args.count, args.output)
    pw2mask.process()
    pw2mask.table_func()

    print("     Password Mask Key\n-----------------------------")
    print("?d: Digit\n?l: Lowercase letter\n?u: Uppercase letter\n?s: Special character\n")
    print(f"    Top {pw2mask.common_count} Password Masks\n-----------------------------")
    print(pw2mask.formatted_table.replace("(","").replace(")","").replace(","," :").replace("'",""))
    print(GREEN + "\n[+]" + RST + f" Wrote Password Masks to {pw2mask.mask_file}\n")


if __name__ == "__main__":
    main()