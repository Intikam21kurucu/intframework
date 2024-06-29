#!/bin/bash

# İlk olarak, betiği çalıştırılabilir yapın.
chmod +x start_kali.sh

# İlk çalıştırma için bir kontrol dosyası oluşturun.
if [ ! -f "$HOME/intframework/.install_done" ]; then
    sudo python3 "$HOME/intframework/installintconsole.py"
    touch "$HOME/intframework/.install_done"
fi

# Alias'ları tanımlayın. Kali Linux dizin yapısına göre düzenledim.
echo "alias intconsole='cd ~/intframework && sudo python3 intconsoleV3.py && source ~/.bashrc'" >> ~/.bashrc
echo "alias intweb='sudo python3 ~/intframework/intweb'" >> ~/.bashrc
echo "alias introjan='sudo python3 ~/intframework/introjan'" >> ~/.bashrc
echo "alias intvenom='sudo python3 ~/intframework/intvenom.py'" >> ~/.bashrc
echo "alias intofficial='sudo python3 ~/intframework/intcam.py'" >> ~/.bashrc
echo "alias intofficial='sudo python3 ~/intframework/İNTOFFİCİAL.py'" >> ~/.bashrc

# .bashrc dosyasını yeniden yükleyin.
source ~/.bashrc

# Betiği taşıyın ve PATH'e ekleyin.
chmod +x start_kali.sh
sudo mkdir -p /opt/intmodules
sudo mv start_kali.sh /opt/intmodules/
echo 'export PATH="/opt/intmodules:$PATH"' | sudo tee -a /etc/profile > /dev/null
source /etc/profile

# oip komutunun yardım menüsünü gösterin.
sudo oip -h