#!/bin/bash

# Bu script, Termux'ta 'intconsole' komutu için bir alias oluşturur ve .bashrc dosyasına ekler.

# 'intconsole' komutunu tanımlayın.
echo "alias intconsole='cd intframework && python3 installintconsole && python3 intconsoleV2.py'" >> ~/.bashrc

# .bashrc dosyasını yeniden yükleyin.
source ~/.bashrc

# Scriptin çalıştığını doğrulayın.
echo "downloaded intconsole and added it to the intconsole command line"