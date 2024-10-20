#!/bin/bash

set -e

# Bu script, Termux'ta 'intconsole' komutu için bir alias oluşturur ve ~/.bashrc dosyasına ekler.
chmod +x terbuild.sh

# İlk çalıştırma için bir kontrol dosyası oluşturun.
if [ ! -f "$HOME/intframework/.install_done" ]; then
    python3 "$HOME/intframework/installintconsole.py"
    touch "$HOME/intframework/.install_done"
    echo "Kurulum tamamlandı."
fi

# Gerekli Python paketlerini yükleyin
pip3 install -r requirements.txt
echo "Gerekli Python paketleri yüklendi."

cd ~

# intconsole dosyasına çalıştırma izni ver ve PATH'e ekle
chmod +x ~/intframework/intconsole
mv ~/intframework/intconsole $PREFIX/bin/
mv ~/intframework $PREFIX/opt/
echo "intconsole dosyası taşındı."

# Zsh kurulumu, isteğe bağlı olarak
read -p "Zsh kurmak istiyor musunuz? (e/h): " choice
if [ "$choice" == "e" ]; then
    pkg install zsh
fi

# .bashrc dosyasına alias ekleyin
SHELLRC="$HOME/.bashrc"

if ! grep -q "export INTFRAMEWORK_PATH" $SHELLRC; then
    echo "export INTFRAMEWORK_PATH=$PREFIX/opt/intframework" >> $SHELLRC
fi

echo "alias ll='ls -la'" >> $SHELLRC
echo "alias intupdate='apt update && apt upgrade -y && rm -rf ~/intframework && git clone https://github.com/Intikam21kurucu/intframework'" >> $SHELLRC
echo "export INTDIR=$PREFIX/opt/" >> $SHELLRC
echo "alias intframework=\$INTFRAMEWORK_PATH" >> $SHELLRC
echo "alias c='clear'" >> $SHELLRC
echo "alias gs='git status'" >> $SHELLRC

# intconsole fonksiyonunu ekleyin
echo 'intconsole() { ORIGINAL_DIR=$(pwd); cd $INTFRAMEWORK_PATH; python3 intconsoleV4.py; cd $ORIGINAL_DIR; }; alias intconsole="intconsole"' >> $SHELLRC

# Diğer alias'ları ekleyin
echo "alias introjan='python3 \$INTFRAMEWORK_PATH/introjan.py'" >> $SHELLRC
echo "alias intvenom='python3 \$INTFRAMEWORK_PATH/intvenom.py'" >> $SHELLRC
echo "alias intofficial='python3 \$INTFRAMEWORK_PATH/intcam.py'" >> $SHELLRC
echo "alias intninja='python3 \$INTFRAMEWORK_PATH/intninja.py'" >> $SHELLRC
echo "alias intmail='python3 \$INTFRAMEWORK_PATH/intmail.py'" >> $SHELLRC
echo "alias intmeterpreter='python3 \$INTFRAMEWORK_PATH/intmeterpreter.py'" >> $SHELLRC

# ~/.bashrc dosyasını yeniden yükleyin.
source $SHELLRC

# Ekstra kurulumlar
chmod +x oip
mkdir -p ~/intmodules
mv oip ~/intmodules/
mv ~/intmodules/ $PREFIX/opt/
echo 'export PATH=$PREFIX/opt/intmodules:$PATH' >> ~/.profile
source ~/.profile
oip -h

cd $PREFIX/opt/intframework