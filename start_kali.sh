#!/bin/bash

# Bu script, Termux'ta Kali Linux ortamında 'intconsole' komutu için bir alias oluşturur.

# Kali Linux shell'ini başlatmak için bir fonksiyon tanımlayın.
start_kali() {
    # Kali Linux shell'ini başlatın.
    ./start-kali.sh
}

# 'intconsole' komutunu tanımlayın.
echo "alias intconsole='cd ~/intframework && python3 installintconsole.py && python3 intconsoleV2.py'" >> ~/.bashrc

# .bashrc dosyasını yeniden yükleyin.
source ~/.bashrc

# Kullanıcıya scriptin başarıyla eklendiğini bildirin.
echo "Kali Linux ortamında 'intconsole' komutu '.bashrc' dosyanıza başarıyla eklendi ve hazır."
