#!/bin/bash

set -e

# Bu script, Kali Linux'ta 'intconsole' komutu için bir alias oluşturur ve .bashrc dosyasına ekler.

# Scriptin çalıştırılabilir olması için izinleri ayarla
chmod +x start_kali.sh

# İlk çalıştırma için bir kontrol dosyası oluşturun.
if [ ! -f "$HOME/intframework/.install_done" ]; then
    python3 "$HOME/intframework/installintconsole.py"
    touch "$HOME/intframework/.install_done"
    echo "Kurulum tamamlandı."
fi

# intconsole dosyasını uygun dizine taşıyın
if [ -f "$HOME/intframework/intconsole" ]; then
    mv "$HOME/intframework/intconsole" "$PREFIX/bin/"
    echo "'intconsole' dosyası $PREFIX/bin/ dizinine taşındı."
else
    echo "Hata: 'intconsole' dosyası bulunamadı."
    exit 1
fi

# 'intconsole' komutunu tanımlayın. Eğer daha önce eklenmemişse.
if ! grep -q "alias intconsole" "$HOME/.bashrc"; then
    echo "alias intconsole='cd ~/intframework && python3 intconsoleV4.py && cd -'" >> "$HOME/.bashrc"
    echo "'intconsole' komutu başarıyla .bashrc dosyanıza eklendi."
else
    echo "'intconsole' komutu zaten mevcut."
fi

# .bashrc dosyasını yeniden yükleyin.
source "$HOME/.bashrc"

# Kullanıcıya scriptin başarıyla eklendiğini bildirin.
echo "Kali Linux'ta 'intconsole' komutu .bashrc dosyanıza başarıyla eklendi ve hazır."