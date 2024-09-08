#!/bin/bash

# Bu script, Termux'ta 'intconsole' komutu için bir alias oluşturur ve .bashrc ya da .zshrc dosyasına ekler.

chmod +x terbuild.sh

# İlk çalıştırma için bir kontrol dosyası oluşturun.
if [ ! -f "$HOME/intframework/.install_done" ]; then
    python3 "$HOME/intframework/installintconsole.py"
    touch "$HOME/intframework/.install_done"
fi

cd ~

chmod +x ~/intframework/intconsole
mv ~/intframework/intconsole $PREFIX/bin

pkg install zsh

# '.bashrc' veya '.zshrc' kontrolü
if [ -f "~/.bashrc" ]; then
    SHELLRC="~/.bashrc"
else
    SHELLRC="~/.zshrc"
fi

# 'intconsole' komutunu tanımlayın ve alias ekleyin.
echo "alias ll='ls -la'" >> $SHELLRC
echo "alias intupdate='apt update && apt upgrade -y && rm -rf ~/intframework && git clone https://github.com/Intikam21kurucu/intframework'" >> $SHELLRC
echo "export INTFRAMEWORK_PATH=$PREFIX/opt/intframework" >> $SHELLRC
echo "export INTDIR=$PREFIX/opt/" >> $SHELLRC
echo "alias intframework=\$INTFRAMEWORK_PATH" >> $SHELLRC
echo "alias c='clear'" >> $SHELLRC
echo "alias gs='git status'" >> $SHELLRC

echo 'intconsole() { ORIGINAL_DIR=$(pwd); cd $INTFRAMEWORK_PATH; python3 intconsoleV4.py; cd $ORIGINAL_DIR; [ -n "$BASH" ] && source ~/.bashrc || source ~/.zshrc; }; alias intconsole="intconsole"' >> $SHELLRC

echo "alias introjan='python3 \$INTFRAMEWORK_PATH/introjan.py'" >> $SHELLRC
echo "alias intvenom='python3 \$INTFRAMEWORK_PATH/intvenom.py'" >> $SHELLRC
echo "alias intofficial='python3 \$INTFRAMEWORK_PATH/intcam.py'" >> $SHELLRC
echo "alias intninja='python3 \$INTFRAMEWORK_PATH/intninja.py'" >> $SHELLRC
echo "alias intmail='python3 \$INTFRAMEWORK_PATH/intmail.py'" >> $SHELLRC
echo "alias intmeterpreter='python3 \$INTFRAMEWORK_PATH/intmeterpreter.py'" >> $SHELLRC

# .bashrc veya .zshrc dosyasını yeniden yükleyin.
source $SHELLRC

# Ekstra kurulumlar
chmod +x oip
mkdir -p ~/intmodules
mv oip ~/intmodules/
mv ~/intmodules/ $PREFIX/opt/
echo 'export PATH=$PREFIX/opt/intmodules:$PATH' >> ~/.profile
source ~/.profile
oip -h

cd intframework