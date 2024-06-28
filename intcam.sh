#!/bin/bash

python3 $HOME/intcam "$@"
chmod +x $HOME/bin/intcam
nano ~/.bashrc
export PATH="$HOME/bin:$PATH"
source ~/.bashrc
intcam -h