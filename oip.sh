GNU nano 8.0                       oip.sh
chmod +x oip
mkdir -p $HOME/intframework
mv oip $HOME/intframework/
echo 'export PATH=$HOME/intframework:$PATH' >> $HOME/.bashrc
source $HOME/.bashrc
oip -h
