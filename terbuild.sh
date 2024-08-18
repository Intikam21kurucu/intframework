#!/bin/bash

# Bu script, Termux'ta 'intconsole' komutu için bir alias oluşturur ve .bashrc dosyasına ekler.

chmod +x terbuild.sh

# İlk çalıştırma için bir kontrol dosyası oluşturun.
if [ ! -f "$HOME/intframework/.install_done" ]; then
    python3 "$HOME/intframework/installintconsole.py"
    touch "$HOME/intframework/.install_done"
fi

cd ~

mv intconsole $PREFIX/bin

pkg install zsh

# 'intconsole' komutunu tanımlayın.

echo "alias ll=ls -la" >> ~/.bashrc or ~/.zshrc
echo "alias intupdate='apt update && apt upgrade -y && rm -rf ~/intframework && git clone https://github.com/Intikam21kurucu/intframework'" >> ~/.bashrc or ~/.zshrc
echo "export INTFRAMEWORK_PATH=$PREFIX/opt/intframework" >> ~/.bashrc or ~/.zshrc
echo "export INTDIR=$PREFIX/opt/" >> ~/.bashrc or ~/.zshrc
echo "alias intframework=$INTFRAMEWORK_PATH"
echo "alias c='clear'" >> ~/.bashrc or ~/.zshrc
alias gs='git status' >> ~/.bashrc or ~/.zshrc

echo 'intconsole() { ORIGINAL_DIR=$(pwd); cd $INTFRAMEWORK_PATH; python3 intconsoleV4.py; cd $ORIGINAL_DIR; [ -n "$BASH" ] && source ~/.bashrc || source ~/.zshrc; }; alias intconsole="intconsole"' >> ~/.bashrc && echo 'intconsole() { ORIGINAL_DIR=$(pwd); cd $INTDIR; python3 intconsoleV4.py; cd $ORIGINAL_DIR; [ -n "$BASH" ] && source ~/.bashrc || source ~/.zshrc; }; alias intconsole="intconsole"' >> ~/.zshrc

echo "alias introjan='python3 $INTFRAMEWORK_PATH/introjan'" >> ~/.bashrc or ~/.zshrc

echo "alias intvenom='python3 $INTFRAMEWORK_PATH/intvenom.py" >> ~/.bashrc or ~/.zshrc

echo "alias intofficial='python3 $INTFRAMEWORK_PATH/intcam.py" >> ~/.bashrc or ~/.zshrc

echo "alias intofficial='python3 $INTFRAMEWORK_PATH/İNTOFFİCİAL.py" >> ~/.bashrc or ~/.zshrc

echo "alias intninja='python3 $INTFRAMEWORK_PATH/intninja.py">> ~/.bashrc or ~/.zshrc

echo "alias intmail='python3 $INTFRAMEWORK_PATH/intmail.py' ">> ~/.bashrc or ~/.zshrc

echo "alias intmeterpreter='python3 $INTFRAMEWORK_PATH/intmeterpreter.py' ">> ~/.bashrc or ~/.zshrc


# .bashrc dosyasını yeniden yükleyin.
source ~/.bashrc

introjan -h
intmail -h

chmod +x oip
mkdir -p ~/intmodules
mv oip ~/intmodules/
mv ~/intmodules/ $PREFIX/opt/
echo 'export PATH=$PREFIX/opt/intmodules:$PATH' >> ~/.profile
source ~/.profile
oip -h
cd intframework