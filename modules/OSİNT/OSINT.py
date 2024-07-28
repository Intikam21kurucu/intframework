import sys
import subprocess
import os
from cmd import Cmd
from colorama import Fore, Style
from time import sleep
from art import *
from modules.auxiliary import dork, breachdb, intelx, extrametapy, exiftool, pw2mask

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

colors = [GREEN, RED, BLUE, WHITE, YELLOW, CYAN, PINK, BRIGHT, NORM, RST] # Colors dictionary.

# Splash Screen!
osint_art = text2art("OSINT\nframework", "random",)
for color in colors: # Makeshift rainbow loading screen :)
    print((color + "\r[*] Loading OSINTframework...\r" + RST), end="")
    sleep(.25)
print()
sleep(2)
os.system('clear')
print(BRIGHT + RED + osint_art + RST)


# Information on OSINTframework.
print(RED + "=[ OSINTframework v0.1a ]=" + RST)
print(BRIGHT + PINK + "=[ Written by. Jessi ]=" + RST)
print(YELLOW + "=[ 5 modules ]=\n" + RST)


# Module list - for autocomplete
modules = [
    'google_dork',
    'auxiliary/google_dork',
    'intelx_search',
    'auxiliary/intelx_search',
    'breachdb',
    'auxiliary/breachdb',
    'extrametapy',
    'auxiliary/extrametapy',
    'pw2mask',
    'auxiliary/pw2mask'
]

# Module list - screen
available_modules = """

Available Modules

    Auxiliary Modules                   Description
    -----------------                   -----------
    google_dork                         Run custom google dork queries
    intelx_search                       Query the public Intelx DB for email addresses
    breachdb                            Query the R7 breach DB for info
    extrametapy                         Dork for office documents and extract metadata
    pw2mask                             Get hashcat-like masks from passwords
    
"""

# Module options - for autocomplete
module_options = [
    'query',
    'QUERY',
    'limit',
    'LIMIT',
    'domain',
    'DOMAIN',
    'outfile',
    'OUTFILE',
    'outdir',
    'OUTDIR',
    'urllist',
    'URLLIST',
    'api_key',
    'API_KEY',
    'filetypes',
    'FILETYPES',
    'passwords_file',
    'PASSWORDS_FILE',
    'mask_file',
    'MASK_FILE',
    'common_count',
    'COMMON_COUNT'
]

# General list - for autocomplete
general_auto = [
    'options'
]

# CLI Processor.
class osfPrompt(Cmd):

    prompt = DIM + 'osf' + RST + '> ' +  RST # Default prompt
    intro = "OSINTframework Console - Type 'help' for commands" # Intro

    doc_header = 'Core Commands (type help <command>)'
    misc_header = 'Undef'
    undoc_header = 'Module Commands'

    ruler = '='
    module = ''

    def do_use(self, args): # Load a module
        if not args == '':
            if args in modules:
                print(BLUE + "\n[*]" + RST + " Using {}".format(args))
                sleep(.15)
                self.module = args
                self.prompt = DIM + 'osf' + RST + "(" + RED + args + RST + ")> " + RST
            else:
                print(RED + "\n[*]" + RST + " Module doesn't exist! Use 'list' to see available modules.")
        else:
            self.prompt = DIM + 'osf' + RST + '> ' +  RST
            self.module = ''

    def help_use(self):
        print("\nUse a module from the OSINTframework")
        print("Usage: use <type/module>")
        print("Example: use auxiliary/google_dork\n")

    def complete_use(self, text, line, begidx, endidx):
        mline = line.partition(' ')[2]
        offs = len(mline) - len(text)
        return [s[offs:] for s in modules if s.startswith(mline)]


    def do_show(self, args):
        if self.module == '':
            print(RED + "\n[-]" + RST + " No module loaded!\n")
        elif 'options' or '' in args:
            if 'google_dork' in self.module: # Google dork module options
                dork.pyDork.print_help()
            elif 'intelx_search' in self.module: # IntelX module options
                intelx.IntelX.print_help()
            elif 'breachdb' in self.module: # BreachDB module options
                breachdb.BreachDB.print_help()
            elif 'extrametapy' in self.module:
                extrametapy.extraMetaPy.print_help()
            elif 'pw2mask' in self.module:
                pw2mask.pw2mask.print_help()

    do_options = do_show # Shortcut

    def help_show(self):
        print("\nShow current module options\n")
        print("Usage: show options\n")

    def complete_show(self, text, line, begidx, endidx): # Show autocomplete
        mline = line.partition(' ')[2]
        offs = len(mline) - len(text)
        return [s[offs:] for s in general_auto if s.startswith(mline)]


    def do_run(self, args):
        if self.module == '':
            print(RED + "\n[-]" + RST + "No module loaded!\n")

        elif 'google_dork' in self.module:
            dork.main()

        elif 'intelx_search' in self.module:
            intelx.main()

        elif 'breachdb' in self.module:
            breachdb.main()

        elif 'extrametapy' in self.module:
            extrametapy.main()
            outfile = extrametapy.extraMetaPy.outfile
            outdir = extrametapy.extraMetaPy.outdir
            exiftool.main(outfile, outdir)

        elif 'pw2mask' in self.module:
            pw2mask.main()


    def do_set(self, args):
        if self.module == '':
            print(RED + "\n[-]" + RST + " No module loaded!\n")

        elif 'google_dork' in self.module: # Google dork module settings
            if 'QUERY' in args.upper():
                dork.pyDork.query = args.partition(' ')[2]
                print("QUERY => " + dork.pyDork.query)
            elif 'LIMIT' in args.upper():
                dork.pyDork.limit = int(args.partition(' ')[2])
                print("LIMIT => " + str(dork.pyDork.limit))
            elif 'OUTFILE' in args.upper():
                dork.pyDork.outfile = args.partition(' ')[2]
                print("OUTFILE => " + dork.pyDork.outfile)

        elif 'intelx_search' in self.module: # Intelx module settings
            if 'API_KEY' in args.upper():
                intelx.IntelX.api_key = args.partition(' ')[2]
                print("API_KEY => " + intelx.IntelX.api_key)
            elif 'DOMAIN' in args.upper():
                intelx.IntelX.domain = args.partition(' ')[2]
                print("DOMAIN => " + intelx.IntelX.domain)
            elif 'LIMIT' in args.upper():
                intelx.IntelX.limit = int(args.partition(' ')[2])
                print("LIMIT => " + str(intelx.IntelX.limit))
            elif 'OUTFILE' in args.upper():
                intelx.IntelX.outfile = args.partition(' ')[2]
                print("OUTFILE => " + intelx.IntelX.outfile)

        elif 'breachdb' in self.module: # BreachDB module settings
            if 'API_KEY' in args.upper():
                breachdb.BreachDB.api_key = args.partition(' ')[2]
                print("API_KEY => " + breachdb.BreachDB.api_key)
            elif 'DOMAIN' in args.upper():
                breachdb.BreachDB.domain = args.partition(' ')[2]
                print("DOMAIN => " + breachdb.BreachDB.domain)
            elif 'LIMIT' in args.upper():
                breachdb.BreachDB.limit = int(args.partition(' ')[2])
                print("LIMIT => " + str(breachdb.BreachDB.limit))
            elif 'OUTFILE' in args.upper():
                breachdb.BreachDB.outfile = args.partition(' ')[2]
                print("OUTFILE => " + breachdb.BreachDB.outfile)

        elif 'extrametapy' in self.module: # extrametapy module settings
            if 'FILETYPES' in args.upper():
                extrametapy.extraMetaPy.filetypes = list((args.partition(' ')[2]).split(', '))
                print("FILETYPES => " + str(extrametapy.extraMetaPy.filetypes))
            elif 'DOMAIN' in args.upper():
                extrametapy.extraMetaPy.domain = args.partition(' ')[2]
                print("DOMAIN => " + extrametapy.extraMetaPy.domain)
            elif 'LIMIT' in args.upper():
                extrametapy.extraMetaPy.limit = int(args.partition(' ')[2])
                print("LIMIT => " + str(extrametapy.extraMetaPy.limit))
            elif 'OUTFILE' in args.upper():
                extrametapy.extraMetaPy.outfile = args.partition(' ')[2]
                print("OUTFILE => " + extrametapy.extraMetaPy.outfile)
            elif 'OUTDIR' in args.upper():
                extrametapy.extraMetaPy.outdir = os.path.join(args.partition(' ')[2], '')
                print("OUTDIR => " + extrametapy.extraMetaPy.outdir)
            elif 'URLLIST' in args.upper():
                extrametapy.extraMetaPy.urllist = args.partition(' ')[2]
                print("URLLIST => " + extrametapy.extraMetaPy.urllist)

        elif 'pw2mask' in self.module:
            if 'PASSWORDS_FILE' in args.upper():
                pw2mask.pw2mask.passwords_file = args.partition(' ')[2]
                print("PASSWORDS_FILE => " + pw2mask.pw2mask.passwords_file)
            elif 'MASK_FILE' in args.upper():
                pw2mask.pw2mask.mask_file = args.partition(' ')[2]
                print("MASK_FILE => " + pw2mask.pw2mask.mask_file)
            elif 'COMMON_COUNT' in args.upper():
                pw2mask.pw2mask.common_count = int(args.partition(' ')[2])
                print("COMMON_COUNT => " + str(pw2mask.pw2mask.common_count))


    def complete_set(self, text, line, begidx, endidx): # Set autocomplete
        mline = line.partition(' ')[2]
        offs = len(mline) - len(text)
        return [s[offs:] for s in module_options if s.startswith(mline)]

    def do_shell(self, args): # Execute shell commands from osf console.
        subshell = subprocess.Popen(args, shell=True, stdin=None, stdout=None)
        subshell.communicate()
        subshell.terminate()

        print("")

    def help_shell(self):
        print("\nRun a shell command")
        print("Usage: shell <command>")
        print("Example: shell whoami\n")


    # List available modules.
    def do_list(self, args):
        print(available_modules)

    def help_list(self):
        print("\nList available modules\n")


    # Exit functions.
    def do_exit(self, args):
        sys.exit()

    def help_exit(self):
        print("\nExit the OSINTframework\n")

    def do_quit(self, args):
        return True

    def help_quit(self):
        print("\nSafely exit the OSINTframework\n")



if __name__ == '__main__':
    osfPrompt().cmdloop()