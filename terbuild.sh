#!/bin/bash

# Bu script, Termux'ta 'intconsole' komutu için bir alias oluşturur ve .bashrc dosyasına ekler.

chmod +x terbuild.sh

# İlk çalıştırma için bir kontrol dosyası oluşturun.
if [ ! -f "$HOME/intframework/.install_done" ]; then
    python3 "$HOME/intframework/installintconsole.py"
    touch "$HOME/intframework/.install_done"
fi

# 'intconsole' komutunu tanımlayın.
echo "alias intconsole='cd ~/intframework && python3 intconsoleV2.py && source ~/.bashrc'" >> ~/.bashrc

# .bashrc dosyasını yeniden yükleyin.
source ~/.bashrc

touch ~/.bash_aliases
nano ~/.bash_aliases
chmod +x introjan
mkdir -p ~/bin/
mv introjan ~/bin/
echo $PATH
export PATH=$HOME/bin:$PATH
alias introjan='python3 introjan'>>~/.bash_aliases
source ~/.bash_aliases
introjan -h

chmod +x oip
mkdir -p ~/intmodules
mv oip ~/intmodules/
echo 'export PATH=$HOME/intmodules:$PATH' >> ~/.profile
source ~/.profile
oip -h

echo "LAUNCEDED INTCONSOLE"