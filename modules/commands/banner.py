#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pyfiglet import Figlet
from colorama import Fore, init, Style
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
import subprocess
import socket
from netaddr import IPNetwork, IPAddress
import argparse
import socket
import threading
import time
import sys
import random
import urllib.request
from queue import Queue

init()
from colorama import *

# Renkleri tanımla
s2 = Fore.RESET
s3 = Fore.GREEN
s4 = Fore.RED
s0 = Fore.RESET

# ASCII sanatını oluştur
rtbn = f"""
{s3}  ⢠⡾⠃⠀⠀⠀⠀  ⠀⠰⣶⡀⠀{s0}
{s3}⢠⡿⠁⣴⠇⠀⠀⠀     ⠸⣦⠈⢿  {s0}
{s3} ⣾⡇⢸⡏⢰⡇⠀   ⠀  ⢸⡆⢸⡆⢸ {s0}    {s4}intframework{s0}
{s3}⢹⡇⠘⣧⡈⠃{s0}  ⢰⡆{s2} {s3}  ⠘⢁⣼⠁⣸⠀{s0}
{s3}⠈⢿⣄⠘⠃{s0} {s2}  ⢸⡇{s3}⠀   ⠘⠁⣰⡟{s0}  by root{s4}@{s0}{s3}int{s0}
  {s3}⠙⠃    {s0}{s2}⢸⡇{s0}{s3}   ⠘⠋
⠀ ⠀{s2}⠀⠀⠀⠀ ⢸⡇⠀⠀⠀⠀⠀⠀
⠀ ⠀{s2}⠀⠀⠀⠀ ⢸⡇⠀⠀⠀⠀⠀⠀
⠀ ⠀{s2}⠀⠀⠀⠀ ⠘⠃⠀⠀{s0}⠀⠀⠀⠀
"""
def banner():
        import random
        global banners
        banners = [
    """{Fore.RED} THİS İS SPARTA! {Fore.RESET}
    
    {Fore.BLUE}
        ⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣷⡀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⣿⣄⠀⠀⠀⠀⠀⠀⣀⣿⣯⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣸⣿⣿⣿⡦⠀⠀⠀⠀⢰⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠙⠻⣿⡿⠁⠀⠀⠀⠀⣤⣄⡈⢁⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⡄⠀⠀⠀⠀⠹⣿⡇⢸⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⢹⡇⠀⠀⠀⠀⠀⠈⠁⠈⣁⣠⣤⣤⣤⣤⣀⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⣿⡀⠀⠀⠀⠀⢀⣴⡾⠋⢉⣀⣀⣀⣈⠉⠻⢶⡄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢹⣇⠀⠀⠀⢠⡾⠋⣠⣾⣿⣿⣿⣿⣿⣿⣦⡀⢻⣆⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡄⠀⢀⣿⠁⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⢿⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⠀⢸⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢸⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡀⠀⣿⡀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢀⣿⠃
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣇⠀⠘⢷⣄⠙⢿⣿⣿⣿⣿⣿⡿⠋⢀⣾⠃⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⢻⡀⠀⠀⠙⠷⣦⣄⣈⣉⣉⣠⣤⡶⠟⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠇⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀intpro⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀ for TERMUX
{Fore.RESET}⠀⠀⠀⠀⠀⠀⠀
    """,
    Fore.RED + """ 
    ___ _   _ _____ ___ _  __    _    __  __ ____  _ _ ____
|_ _| \ | |_   _|_ _| |/ /   / \  |  \/  |___ \/ ( ) ___|
 | ||  \| | | |  | || ' /   / _ \ | |\/| | __) | |/\___ \
 | || |\  | | |  | || . \  / ___ \| |  | |/ __/| |  ___) |
|___|_| \_| |_| |___|_|\_\/_/   \_\_|  |_|_____| """ + Fore.RESET,
    """
 {Fore.BLUE}   intninja is waiting for his prey {Fore.RESET}
{Fore.RED}
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡠⠖⠊⠉⠉⠉⠑⠒⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠠⡪⡻⣣⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢢⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡽⠀⠹⣴⣄⡀⠀⣄⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀⠙⢝⢽⢻⣿⣟⡀⠀⠀⠀⡄⡸⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡜⣉⠀⠀⠈⡤⠅⠫⣿⠙⠀⠀⠀⣉⢳⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣳⢻⡚⠶⣤⡀⠸⡶⠟⢀⣠⠴⢛⡿⡜⠀⠀⠀⠀⠀⠀⠀
⣄⠀⠀⠀⠀⠀⡜⢹⣌⢷⠤⠤⠽⡳⠷⢞⠯⠄⠤⡾⣁⠇⢀⠀⠀⠀⠀⢠
 ⢸⢦⡀⠀⠀⠸⡵⣹⠉⣳⠨⡀⠀⠀⠀⠀⠈⢈⠥⡾⠗⡉⢩⠛⠉⡏  
⠀⢧⠙⢦⡀⠀⠙⢷⢞⣒⡇  intikam21 ⢰⠁⠦⢍⡩⠃⠀⢀⡠⠊⠁
⠀⠀⠳⣐⢌⠲⢄⡈⠳⣀⣱⣄⠀ninja⠀⠀⣀⠜⣉⣑⠭⢀⡠⠔⡉⢀⠔
⠀⠀⠀⠈⠓⢤⡂⢈⠓⠤⣉⡙⠳⠤⠀⠤⠞⠓⠉⣁⠤⠒⡉⢄⡨⠖⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠑⠪⢴⣠⠍⡓⠢⣄⡠⠔⢒⠉⣄⡢⠕⠊⠁⠀⠀⠀⠀⠀⠀⡠⠤⠀⡀⡀⡀⠀⠠⠂⢱⠔⣛⠋⢭⣐⣦⡽⠒⣛⠣⡎⠁⡦⠀⡀⣀⢀
⠠⢤      {Fore.RESET}  [{Fore.BLUE}int{Fore.RESET}]  [{Fore.RED}intninja{Fore.RESET}] [{Fore.BLUE}intmeterpreter{Fore.RESET}]
{Fore.RED}⠧⠠⠄⠇⠧⠬⠼⠴⣇⣂⠖⠒⠉⠁⠀⠀⠈⠉⠒⠲⣡⣰⠥⠤⠦⠀⠄⢠⠀⠸
{Fore.RESET}
""",
   """
   {Fore.BLUE}
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
    {Fore.RESET}""",
    """
    {Fore.BLUE}
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
   {Fore.RESET} """, 
    """{Fore.RED}

 ██▓ ███▄    █ ▄▄▄█████▓
▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒
▒██▒▓██  ▀█ ██▒▒ ▓██░ ▒░
░██░▓██▒  ▐▌██▒░ ▓██▓ ░ 
░██░▒██░   ▓██░  ▒██▒ ░ 
░▓  ░ ▒░   ▒ ▒   ▒ ░░   
 ▒ ░░ ░░   ░ ▒░    ░    
 ▒ ░   ░   ░ ░   ░      
 ░           ░          @intikam21
                        
                                                                                                                                                                                        {Fore.RESET}        """, 
        """ {Fore.RED}
                            ..,;:ccc,.                             
                          ......''';lxO.                           
                ...............,:ld;                           
                           .';;;:::;,,.x,                          
                      ..'''.            0Xxoc:,.  ...               
                  ....                ,ONkc;,;cokOdc',.            
                 .                   OMo           ':ddo.          
                                    dMc               :OO;          
                                    0M.                 .:o.       
                                    ;Wd                            
                                     ;XO,                         \033[93mCreated By @intikam21 \033[34m                         
                                       ,d0Odlc;,..                 
                                           ..',;:cdOOd::,.        
                                                    .:d;.':;.     
                                                       'd,  .'     
                                                         ;l   ..    
                                                          .o       
                                                            c
                                                            .'                      
                 ▐ ▄                ▄▄▄▄▄        
   ██         •█▌▐█            •██          
   ▐█·        ▐█▐▐▌           ▐█.▪        
   ▐█▌        ██▐█▌         ▐█▌·        
   ▀▀▀        ▀▀ █▪            ▀▀▀  {Fore.RESET}""",
   """
                             ########                  #
                      #################            #
                   ######################         #
                  #########################      #
                ############################
               ##############################
               ###############################
              ###############################
              ##############################
                              #    ########   #
                 {Fore.RED}###{Fore.RESET}      {Fore.RED}###{Fore.RESET}       ####   ##
                                      ###   ###
                                    ####   ###
               ####          ##########   ####
               #######################   ####
                 ####################   ####
                  ##################  ####
                    ############      ##
                       ########        ###
                      #########        #####
                    ############      ######
                   ########      #########
                     #####       ########
                       ###       #########
                      ######    ############
                     #######################
                     #   #   ###  #   #   ##
                     ########################
                      ##     ##   ##     ##
                            intpro 
   """,
   """
+-------------------------------------------------------+
|  {Fore.RED}İNTPRO FOR TERMUX    {Fore.RESET}                       |
+---------------------------+---------------------------+
|     {Fore.BLUE} __________________ {Fore.RESET}  |                           |
| {Fore.BLUE} ==c(______(o(______(_()  | |""""""""""""|======[***  |{Fore.RESET}
|   {Fore.BLUE}          )=\\  {Fore.RESET}  {Fore.GREEN}       | |  EXPLOIT   \\            |
|  {Fore.RESET}{Fore.BLUE}         // \\\\  {Fore.RESET} {Fore.GREEN}       | |_____________\\_______    |
|   {Fore.RESET} {Fore.BLUE}       //   \\\\ {Fore.RESET} {Fore.GREEN}       | |=={Fore.RESET}[int >]{Fore.GREEN}============\\   |{Fore.RESET}
|  {Fore.BLUE}        //     \\\\        | |______________________\\  |
|    {Fore.RESET}  {Fore.BLUE}   // {Fore.RESET}RECON{Fore.BLUE} \\\\       | \\(@)(@)(@)(@)(@)(@)(@)/   |
|        {Fore.BLUE}//         \\\\      |  *********************    |
+---------------------------+---------------------------+
|      o O o                |        \\'\\/\\/\\/\\/'/         |
|              o O          |         )======(          |
|                 o         |   {Fore.RESET}  {Fore.YELLOW}  .' {Fore.RESET} LOOT  '.   {Fore.YELLOW}     |
|{Fore.RED} |^^^^^^^^^^^^^^{Fore.RESET} {Fore.GREEN}|l___      |      /    _||__   {Fore.RESET}\\       |
{Fore.RED}| |    PAYLOAD     |""\\___,{Fore.GREEN} |     /    (_||_     \\      |{Fore.RESET}
{Fore.RED}| |________________|__|{Fore.RESET}){Fore.YELLOW}__| |    |     __||_)  {Fore.RESET}   |     |
{Fore.RED}| |(@)(@)''""**|(@)(@)**|(@){Fore.YELLOW} |    "       ||       "     |{Fore.RESET}
{Fore.RED}|  = = = = = = = = = = = =  {Fore.RESET}| {Fore.YELLOW}    '--------------'      | {Fore.RESET}
+---------------------------+---------------------------+

   """,
   """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⢆⣴⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⣤⡄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠠⣤⣀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣤⣾⣿⣿⡇⠛⠿⢿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠀⣿⣿⣿⣦⡀⠀⠀
⠀⠀⠀⣾⣿⣿⣿⣿⣇⡀   @İNTPRO     ⠀⢀⣰⣿⣿⣿⣿⣷⠀
⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣶⣤⣀⣀⣀⣀⣀⣀⣤⣶⣿⣿⣿⣿⣿⣿⡟⠀
⠀⠀⠀⠀⠈⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠛⣻⠿⠿⣿⣿⣿⣿⣿⡿⠿⠿⠟⠛⠉⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠛⠛⠿⠖⢀⣶⣶⣶⣶⣶⡶⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀⣠⣶⠄⠙⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀   ⠠⣔⡏⠋⠁⠀⠐⣾⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠈⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀{Fore.RESET}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        
   """,
   """⠀⠀⠀
   {Fore.RED}
        ⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣷⣦⣄⠀⠀⠀⠀⠀
⠀⠀⢀⣴⣿⣿⣿⠟⠛⠛⠛⠛⠿⣿⣿⣿⣦⡀⠀⠀
⠀⢠⣾⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣷⡄⠀
⢠⣿⣿⣿⠇⠀⠀⢠⣶⠀⠀⣶⡄⠀⠀⠹⣿⣿⣿⡄
⣿⣿⡟⠁⠀⣀⣴⣿⡟⠀⠀⢻⣿⣦⣄⠀⠉⢻⣿⣿
⣿⣿⡇⠀⠀⠿⠿⠟⠁⣰⣦⠈⠻⠿⠿⠀⠀⢸⣿⣿ 
⣿⣿⣷⣄⡀⠀⠀⠀⠀⣉⣈⠀⠀⠀⠀⢀⣠⣾⣿⣿
⢹⣿⣿⣿⣿⣆⠀⠀⢸⣿⣿⡇⠀⠀⣰⣿⣿⣿⣿⠏
⠀⢻⣿⣿⣿⣿⡄⠀⠈⣿⣿⠁⠀⢠⣿⣿⣿⣿⡟⠀
⠀⠈⢻⣿⣿⣿⣿⠀⠀⣿⣿⠀⢀⣿⣿⣿⣿⡟⠀⠀
⠀⠀⠈⢻⣿⣿⣿⣧⠀⠸⠇⠀⣼⣿⣿⣿⠟⠀⠀⠀
⠀⠀⠀⠀⠙⢿⣿⣿⣧⣤⣤⣾⣿⣿⡿⠋⠀intpro?⠀⠀
⠀⠀⠀⠀⠀⠀⠙⠿⣿⣿⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀
⠀⠀       ⠀⠀⠀⠀⠈⠁        ⠀⠀⠀
{Fore.RESET}⠀⠀⠀⠀⠀
   """,
   """
   {Fore.RED}
   ____      __  _ __                  ___  ___
   /  _/___  / /_(_) /______ _____ ___ |__ \<  /
   / // __ \/ __/ / //_/ __ `/ __ `__ \__/ // /
 _/ // / / / /_/ / ,< / /_/ / / / / / / __// /
/___/_/ /_/\__/_/_/|_|\__,_/_/ /_/ /_/____/_/

   ______      __                   ______
  / ____/_  __/ /_  ___  _____     /_  __/__  ____ _____ ___
 / /   / / / / __ \/ _ \/ ___/      / / / _ \/ __ `/ __ `__ \
/ /___/ /_/ / /_/ /  __/ /         / / /  __/ /_/ / / / / / /
\____/\__, /_.___/\___/_/         /_/  \___/\__,_/_/ /_/ /_/
     /____/
{Fore.RESET}
    +-------------------------------------------------------------+
     | [+] the {Fore.YELLOW}system{Fore.RESET} was infiltrated                             |
     | [~] Coder: intikam21                                       |
     | [~] Team: {Fore.RED}İntikam21{Fore.RESET} Cyber Team                              |
     | [~] Designer: İntikam21 Design Team                         |
     | [~] Supporters: Not                                                |
   +--------------------------------------------------------------+
    """,
    f"{rtbn}"
    # Daha fazla banner eklenebilir
    ]
    # Rastgele bir banner seçimi yapılıyor
        chosen_banner = random.choice(banners)
        # Print the formatted text
        print(chosen_banner.format(Fore=Fore))
def menu_banner():
        print("" + Fore.RESET)
        print(f"""
=[          {Fore.YELLOW}İNTPRO console v1.2.90-dev-bbf096e1f{Style.RESET_ALL}                 ]=
+ --=[ 2456 exploits        - 1248 auxiliary    - 500 post       ]=
+ --=[ 1465 payloads        - 50 encoders       - 1 nops         ]=
+ --=[ 40 evasion           - 10 PRO MODULES                     ]=
+ --=[ Osint Framework      - 2 shodan          - 90 network     ]=
+ --=[ 2 pro plugins        - intbash           - int4 reader    ]=

İntikam21 Documentation:{Style.RESET_ALL} https://sites.google.com/view/intilam21-cyber-team/kay%C4%B1t
""" + Fore.RESET)

