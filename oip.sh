chmod +x oip
mkdir -p $HOME/oipforintframework
mv oip $HOME/oipforintframework/
echo 'export PATH=$HOME/oipforintframework:$PATH' >> $HOME/.bashrc
source $HOME/.bashrc
oip -h
