chmod +x oip
mkdir -p ~/bin
mv oip ~/bin/
echo 'export PATH=$HOME/bin:$PATH' >> ~/.profile
source ~/.profile
oip -h