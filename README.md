# intSpLoiT Framework

<p align="center">
  <img src="https://github.com/Intikam21kurucu/intmages/blob/main/lv_0_20250104175232.gif" alt="intSpLoiT Framework">
</p>

![Supported OS](https://img.shields.io/badge/Supported%20OS-Linux-yellow.svg)
![License](https://img.shields.io/badge/license-intLICENSE--1.3-blue.svg)
![Version](https://img.shields.io/badge/Framework%20Version-intSpLoiT%20Console%20v4.2.90--dev--bbf096e-green.svg)
![Python](https://img.shields.io/badge/Python-3-green.svg)
![Exploits](https://img.shields.io/badge/EXPLOITS-500%2B-red.svg)
![Post Exploits](https://img.shields.io/badge/POST%20EXPLOITS-120+-red.svg)
![Auxiliary](https://img.shields.io/badge/AUXILIARY-108-red.svg)
![Modules](https://img.shields.io/badge/MODULES-500%2B-red.svg)
![Encoders](https://img.shields.io/badge/ENCODERS-50-red.svg)
![Payloads](https://img.shields.io/badge/PAYLOADS-8-red.svg)
![OSINT Modules](https://img.shields.io/badge/OSINT%20Modules-50+-blue.svg)

> **We are currently editing this repository! Stay tuned for updates.**  

---

## 🚀 Features  

✅ **Wide Module Support** – Over 800+ modules, including OSINT,exploits,auxiliary,encoders, ... 

✅ **Advanced Exploitation** – 500+ exploits (aiming for 2500)  
✅ **Post-Exploitation Tools** – 120+ post-exploit modules (targeting 500+) for persistence and privilege escalation  
✅ **Auxiliary Modules** – 108 supporting tools, with a goal to expand to 1250  
✅ **OSINT-Specific Modules** – 50+ tools for open-source intelligence gathering  
✅ **Payload Generation** – 8+ payloads with encoding support (50 encoders)  
✅ **Multi-Platform Support** – Works on Termux, Kali Linux, and Debian-based systems 
✅ **Interactive Shell** – Real-time command execution with a powerful shell  

---

## 🔮 Future Roadmap  

🚧 **Expanding Exploit Library** – Increasing to 2500+ exploits and 500+ post-exploit modules  
🚧 **More Auxiliary Tools** – Targeting 1250+ auxiliary modules  
🚧 **Advanced OSINT Capabilities** – Enhancing OSINT modules beyond 200+  
🚧 **Cloud-Based Modules** – Remote exploitation capabilities  
🚧 **Mobile Device Support** – Dedicated Android & iOS modules  
🚧 **Self-Updating Framework** – Automatic module and exploit updates  
🚧 **Real-Time Attack Analysis** – In-depth monitoring of active exploits  
🚧 **More Commands** – want to you are use other commands
 
---

## ⚠️ Disclaimer  

**intSpLoiT and its developers disclaim any responsibility or liability for improper use of this framework.**  

---

## ⚙️ Installation Guide  

### **Before Running the Framework:**
Ensure that all dependencies are installed properly.

#### **1️⃣ After executing `terbuild.sh`**
```bash
source ~/.bashrc
```
2️⃣ If intframework is located under /usr/opt
```bash
cd $PREFIX/opt/
mkdir -p intframework
mv $PREFIX/opt/* $PREFIX/opt/intframework
```
3️⃣ Before running intconsole
```bash
cd $INTFRAMEWORK_PATH
mv inttable/inttable $PREFIX/lib/python3.12/
```
4️⃣ Using inttable module in Python
```python
import inttable.inttable as inttable

inttable.core.activate("root")
inttable.console.run("command")
```

---

## 📷 Screenshots

**System Interface**:
system photos:
![İntikam21 photos:](https://github.com/intSpLoiT/intframework/blob/d5cb19b49875d0eb9a949c379202999d5c609e22/Photos/IMG_20241008_184826.jpg) 
 
**More UI Previews**:
 
![Photo2](https://github.com/intSpLoiT/intframework/blob/%C4%B0ntframeworkV4/IMG_20241027_122034.jpg)
![Github Badge](https://github.com/intSpLoiT/intframework/blob/%C4%B0ntframeworkV4/IMG_20240916_191945.jpg)
 
 
 
---

## 📲 Installing on Termux
```bash
apt update && apt upgrade
pkg update && pkg upgrade
pkg install python3
pkg install git
pip3 install requests
git clone https://github.com/intSpLoiT/intframework
cd intframework 

chmod +x terbuild.sh
./terbuild.sh
```

---

## 🔍 Usage Examples
### in the console
```bash
int4-pro > use modules/Auxiliary/social/userscan.py
int4-pro userscan.py(modules/Auxiliary/social/userscan.py) > run <example --lang en>
not rooted
[*] Inspecting module: modules/Auxiliary/social/userscan.py
[+] Module inspection complete.
[*] Running module: modules/Auxiliary/social/userscan.py
[>] Command: python3 modules/Auxiliary/social/userscan.py example --lang en
[+] Find Profile by Username [+]
[+] Username found on: github
[+] Profile URL: https://api.github.com/users/example/events/public
---------------------------------------------------------------------------
[+] Username found on: github
[+] Profile URL: https://api.github.com/users/example
---------------------------------------------------------------------------
[+] Username found on: twitter
[+] Profile URL: https://twitter.com/example
---------------------------------------------------------------------------
^C

[!] Error during module execution: module 'inttable' has no attribute 'write'
int4-pro userscan.py(modules/Auxiliary/social/userscan.py) >
```
### in Modular
#### 1️⃣ Running a Network Scan Module
```
int4 (modular) > use network_scan
[*] Module selected: network_scan
int4 module(network_scan) > show options
[*] Available options for module: network_scan
fs: None
timeout: None
int4 module(network_scan) > set timeout 0.1
[*] timeout = 0.1
int4 module(network_scan) > run
```
Example Output:
```
Network Scanner
IP Address    | Device Name       | Status
---------------------------------------------
192.168.5.1   | Network Scan      | Port Active, Ping Active, HTTP Active
192.168.5.3   | Unknown Device    | Inactive
192.168.5.8   | Unknown Device    | Inactive
```

---

### in Exploiter
#### 2️⃣ Using inthandler for Exploitation
```
int4 (exploiter) > use multi/handler
Exploit 'multi/handler' selected.
int4 exploit(multi/handler) > run
python: can't open file '/storage/emulated/0/intframework/modules/exploits/multi.handler': [Errno 2] No such file or directory
int4 exploit(multi/handler) > set FILENAME multi/handler/inthandler.py
FILENAME set to multi/handler/inthandler.py.
int4 exploit(multi/handler) > run
Listening on 0.0.0.0:4444
Connection from ('127.0.0.1', 34170)
```
