#!/usr/bin/env python3
# Module: pw2mask
# Author: Jessi

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

    return "?s";

class pw2mask:

    passwords_file = ''
    common_count = 3
    mask_file = 'masks.txt'

    mask_table = []

    formatted_table = []

    @classmethod
    def print_help(cls):
        module_help = f"""

Module Options (auxiliary/pw2mask):

    Name                  Description                 Current Setting
    ----                  -----------                 ---------------
    PASSWORDS_FILE        File with passwords         {cls.passwords_file}
    COMMON_COUNT          Get top X                   {cls.common_count}
    MASK_FILE             File to write masks to      {cls.mask_file}

        """
        print(module_help)

    @classmethod
    def process(cls):
        lines = open(cls.passwords_file, "r").readlines() # Open password file and set lines to strings.

        # Get masks for passwords in file.
        for line in lines:
            mask = [] # Blank array for generating the mask.
            cleanLine = line.replace('\r\n','').replace('\n','') # Cleanup the line.
            for c in cleanLine:
                mask.append(checkMask(c))
            cls.mask_table.append("".join(mask)) # Add masks to table.

    @classmethod
    def table_func(cls):
        with open(cls.mask_file, mode="wt", encoding="utf-8") as maskFile:
            maskFile.write("\n".join(cls.mask_table))

        # Get top x masks.
        common = Counter(cls.mask_table)
        mostCommon = common.most_common(cls.common_count)
        commonTable = ["%i. %s" % (index + 1, value) for index, value in enumerate(mostCommon)] # Index with +1 to start at 1.
        cls.formatted_table = "\n".join(commonTable)



def main():
    print(BLUE + "\n[*]" + RST + " Processing passwords...\n")
    sleep(1.5)
    pw2mask.process()
    pw2mask.table_func()
    print("     Password Mask Key\n-----------------------------")
    print("?d: Digit\n?l: Lowercase letter\n?u: Uppercase letter\n?s: Special character\n")
    print(f"    Top {pw2mask.common_count} Password Masks\n-----------------------------")
    print(pw2mask.formatted_table.replace("(","").replace(")","").replace(","," :").replace("'",""))
    print(GREEN + "\n[+]" + RST + " Wrote Passwords Masks to {}\n".format(pw2mask.mask_file))