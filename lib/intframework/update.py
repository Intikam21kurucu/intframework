import os
os.system("rm -rf intframework/* && rm -rf intframework")
os.system("git clone https://github.com/intSpLoiT/intframework")
os.system("""
cd intframework
chmod +x terbuild.sh
./terbuild.sh
""")