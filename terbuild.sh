#!/bin/bash

# Bu script, Termux'ta 'intconsole' komutu için bir alias oluşturur ve .bashrc dosyasına ekler.

chmod +x terbuild.sh

# İlk çalıştırma için bir kontrol dosyası oluşturun.
if [ ! -f "$HOME/intframework/.install_done" ]; then
    python3 "$HOME/intframework/installintconsole.py"
    touch "$HOME/intframework/.install_done"
fi

cd ~

pkg install zsh

# 'intconsole' komutunu tanımlayın.
echo "alias intconsole='cd ~/intframework && python3 intconsoleV4.py && source ~/.bashrc'" >> ~/.bashrc
echo "alias intweb='python3 /data/data/com.termux/files/home/intframework/intweb'" >> ~/.bashrc
echo "alias introjan='python3 /data/data/com.termux/files/home/intframework/introjan'" >> ~/.bashrc
echo "alias intvenom='python3 /data/data/com.termux/files/home/intframework/intvenom.py'" >> ~/.bashrc
echo "alias intofficial='python3 /data/data/com.termux/files/home/intframework/intcam.py'" >> ~/.bashrc
echo "alias intninja='python3 /data/data/com.termux/files/home/intframework/modules/intninja.py'" >> ~/.bashrc
echo "alias intmail='python3 /data/data/com.termux/files/home/intframework/modules/intmail.py'" >> ~/.bashrc
echo "alias intmeterpreter='python3 /data/data/com.termux/files/home/intframework/modules/intmeterpreter.py'" >> ~/.bashrc
echo "alias intai='python3 /data/data/com.termux/files/home/intframework/İntAİV2.py'" >> ~/.bashrc

# .bashrc dosyasını yeniden yükleyin.
source ~/.bashrc

introjan -h
intmail -h

chmod +x oip
mkdir -p ~/intmodules
mv /data/data/com.termux/files/home/intframework/oip ~/intmodules/
echo 'export PATH=$HOME/intmodules:$PATH' >> ~/.profile
source ~/.profile
oip -h
cd intframework
