
# İntikam21 Framework

![Gitter chat](https://github.com/Intikam21kurucu/TestReadme.md/blob/main/%C4%B0ntikam21_20240525_100218_0000.png)
![Supported OS](https://img.shields.io/badge/Supported%20OS-Linux-yellow.svg)
![License](https://img.shields.io/badge/license-BSL--1.0-blue.svg)
![FRAMEWORK SÜRÜMÜ](https://img.shields.io/badge/FRAMEWORK%20SÜRÜMÜ-İntikam21--Framework%20console%20v4.0.15--dev--bbf096e-green.svg)
![Python](https://img.shields.io/badge/Python-3-green.svg)
![Exploits](https://img.shields.io/badge/EXPLOIT-2456-red.svg)
![Build](https://img.shields.io/badge/BUILD-1079-red.svg)
![Modules](https://img.shields.io/badge/modules-545-red.svg) 





İntikam21 hiçbir sorumluluğu kabul etmez yaptığınız hersey size ozgudur😀

-----------------------------------------------
# Note
````
We apologize, intconsoleV4 is not yet complete, but this will not be that easy because commands have been added to it, traceroute, many modules, exploits, almost everything in the cyber security world, so we kindly ask you to wait patiently, if you want, let's see if you want to download tools to other consoles, and in this 4th console, it has its own modules. and there will be commands, bye bye.
````

# OLD GİF

-----------------------------------------------
![](https://github.com/Intikam21kurucu/intframework/blob/43b69f75b8bce99b2300ce8c885f314cb4da0c30/lv_0_20240504124041.gif)

-----------------------------------------------

 # Instructions

*** Please do the following before running the program: ***

** 1. After terbuild.sh is finished: **

````
source ~/.bashrc
````

*** 2. If intframework has been added to /usr/opt/intframework /usr/opt, then: ***

````
cd $PREFIX/opt/
mkdir -p intframework
mv $PREFIX/opt/* $PREFIX/opt/intframework
````

*** 3. Before running intconsole: ***

````
cd $INTFRAMEWORK_PATH
mv inttable/inttable $PREFIX/lib/python3.12/
````

*** 4. If you want to use inttable: ***

````
import inttable.inttable as inttable

inttable.core.activate("root")
inttable.console.run("command")
````



  
 

# intframework

[![Github Badge](https://github.com/Intikam21kurucu/intframework/blob/Intikam21kurucu-patch-1/%5BOrijinal%20boyut%5D%20Renkli%20Modern%20Yuvarlak%20Okul%20Logo_20240423_141004_0000.png?style=quare&labelColor=000&logo=Github&logoColor=white&link=link)](link) 


# İNSTALL KALİ:
````apt update & apt upgrade
sudo apt install git
sudo apt install python3-pyfiglet
sudo apt install python3 
sudo apt install python3-base64
sudo apt install python3-colorama
sudo apt install python3-requests

git clone https://github.com/Intikam21kurucu/intframework

cd intframework

chmod +x start_kali.sh

./start_kali.sh
````

# EKRAN GÖRÜNTÜSÜ 

system photos:
![İntikam21 photos:](https://github.com/Intikam21kurucu/intframework/blob/d5cb19b49875d0eb9a949c379202999d5c609e22/Photos/IMG_20241008_184826.jpg) 




# İNSTALL TERMUX
````apt update && apt upgrade
pkg update && pkg upgrade
pkg install python3
pkg install git
pip3 install requests
git clone https://github.com/Intikam21kurucu/intframework
cd intframework

chmod +x terbuild.sh

./terbuild.sh
````










# Examples

```
int4 (modular) > use network_scan
[*] Module selected: network_scan
int4 module(network_scan) > show optiosn
[-] Invalid command. Type 'help' for available commands.
int4 module(network_scan) > show options
[*] Available options for module: network_scan
fs: None
timeout: None
int4 module(network_scan) > set timeout 0.1
[*] timeout = 0.1
int4 module(network_scan) > run
Network Scanner
IP Address    | Device Name        | Status
---------------------------------------------
192.168.5.1     | Network Scan       | Port Active, Ping Active, Subprocess Ping Successful, HTTP Active
192.168.5.3     | Unknown Device       | Inactive
192.168.5.5     | Unknown Device       | Inactive
192.168.5.6     | Unknown Device       | Inactive
192.168.5.8     | Unknown Device       | Inactive
192.168.5.4     | Unknown Device       | Inactive
192.168.5.7     | Unknown Device       | Inactive
192.168.5.11    | Unknown Device       | Inactive
192.168.5.10    | Unknown Device       | Inactive
192.168.5.2     | Unknown Device       | Inactive
192.168.5.9     | Unknown Device       | Inactive
192.168.5.12    | Unknown Device       | Inactive
192.168.5.13    | Unknown Device       | Inactive
192.168.5.14    | Unknown Device       | Inactive
192.168.5.15    | Unknown Device       | Inactive
192.168.5.16    | Unknown Device       | Inactive
192.168.5.17    | Unknown Device       | Inactive
192.168.5.18    | Unknown Device       | Inactive
192.168.5.19    | Unknown Device       | Inactive
192.168.5.20    | Unknown Device       | Inactive
192.168.5.21    | Unknown Device       | Inactive
192.168.5.22    | Unknown Device       | Inactive
192.168.5.23    | Unknown Device       | Inactive
192.168.5.24    | Unknown Device       | Inactive
```
**using inthandler**
```
int4 (exploiter) > use multi/handler
Exploit 'multi/handler' selected.
int4 exploit(multi/handler) > run
python: can't open file '/storage/emulated/0/intframework/modules/exploits/multi.handler': [Errno 2] No such file or directory
int4 exploit(multi/handler) > back
int4 exploit(multi/handler) > reset
Options for multi/handler reset to default.
int4 exploit(multi/handler) > run
Exploit file is not defined for this exploit.
int4 exploit(multi/handler) > set FILENAME multi/handler/inthandler.py
FILENAME set to multi/handler/inthandler.py.
int4 exploit(multi/handler) > run
Listening on 0.0.0.0:4444
Connection from ('127.0.0.1', 34170)
İntShell > Connection from ('127.0.0.1', 34172)
h
İntShell > GET / HTTP/1.1
Host: 0.0.0.0:4444
Connection: keep-alive
Accept-Language: ******
Upgrade-Insecure-Requests: 1
User-Agent: anonymous
Referer: android-app://com.google.android.googlequicksearchbox/
Accept-Encoding: gzip, deflate


İntShell >
```



