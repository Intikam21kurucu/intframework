
#!/bin/bash

# Bu script, Termux'ta 'intconsole' komutu için bir alias oluşturur ve .bashrc dosyasına ekler.

chmod +x terbuild.sh

# İlk çalıştırma için bir kontrol dosyası oluşturun.
if [ ! -f "$HOME/intframework/.install_done" ]; then
    python3 "$HOME/intframework/installintconsole.py"
    touch "$HOME/intframework/.install_done"
fi

# 'intconsole' komutunu tanımlayın.
echo "alias intconsole='cd ~/intframework && python3 intconsoleV3.py && source ~/.bashrc'" >> ~/.bashrc

echo "alias intweb='python3 /data/data/com.termux/files/home/intframework/intweb'" >> ~/.bashrc

echo "alias introjan='python3 /data/data/com.termux/files/home/intframework/introjan'" >> ~/.bashrc

echo "alias intvenom='python3 /data/data/com.termux/files/home/intframework/intvenom.py" >> ~/.bashrc

echo "alias intofficial='python3 /data/data/com.termux/files/home/intframework/İNTOFFİCİAL.py" >> ~/.bashrc

# .bashrc dosyasını yeniden yükleyin.
source ~/.bashrc

introjan -h

chmod +x oip
mkdir -p ~/intmodules
mv oip ~/intmodules/
echo 'export PATH=$HOME/intmodules:$PATH' >> ~/.profile
source ~/.profile
oip -h