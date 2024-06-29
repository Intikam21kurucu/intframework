mkdir -p int
cd int
wget https://github.com/Intikam21kurucu/intmages/blob/main/IMG_20240625_202557.jpg
mkdir -p /storage/emulated/0/int/
cp IMG_20240625_202557.jpg
mv IMG_20240625_202557.jpg /storage/emulated/0/int/
wget https://github.com/Intikam21kurucu/intmages/blob/main/Start.gif
cp Start.gif
mv Start.gif /storage/emulated/0/int/
wget https://github.com/Intikam21kurucu/intmages/blob/main/chrome.png
cp chrome.png
mv chrome.png /storage/emulated/0/int/
wget https://github.com/Intikam21kurucu/intmages/blob/main/dos.png
cp dos.png
mv dos.png /storage/emulated/0/int/
wget https://github.com/Intikam21kurucu/intmages/blob/main/int.png
cp int.png
mv int.png /storage/emulated/0/int/
wget https://github.com/Intikam21kurucu/intmages/blob/main/intconsole.png
cp intconsole.png
mv intconsole.png /storage/emulated/0/
pip install virtualenv
mkdir intikam21-desktop
cd intikam21-desktop
python -m venv venv
source venv/bin/activate
pkg install tigervnc
pkg install x11vnc
Xvnc -localhost no -geometry 1024x768 :1
x11vnc -display :1 -localhost no -nopw -xkb -ncache 10
echo "STARTED YOUR VİRTUAL PC"
alias intofficial="python3 intOffical.py">>~/.bashrc or alias intoffical="intvenom">>~/.bashrc
cd intoficcial 
python3 intOffical.py