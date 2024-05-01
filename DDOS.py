import os
from pyfiglet import Figlet
f = Figlet(font='slant')
print(f.renderText('İNTİKAM21 CYBER TEAM'))

print("                ")

print("""
    [+]Tool Name:DDOS
    [+]Creator:ARES
    [+]Team:ARES
    [+]Github:https://github.com/ARESCYBERTEAM
    [+]Version: V2.84""")

E = '\033[0m'
H = '\033[95m'

def exit():
	os.system("clear")
	os.system("exit")
print("     ")

tip = input('ARES>DDOS>[')

print("DDOS İÇİN 1'E ÇÎKMAK İÇİN 2'YE BASÎNÎZ")

tip = input(E+'ARES»DDOS»'+H)

if tip == "2":
	exit()

if tip == "1":	 
	print("DDOS TOOLUNA GİRMEK İSTEDİĞİNE EMİN MİSİN?")
	print("KLAVUZU GÖRMEK İÇİN 4'E TIKLA")
	f = input("")

	print("başlatacağız ama yapmak istediğine emin misin")
	print("başlatmak istediğine emin misin?")
	k = input("eminim veya değilim yaz : ")
if tip == "3":
	
	 print(f.renderText('DDOS TOOLUNA HOSGELDIN'))
	 print("Lütfen ddos atacağın ip'yi veya siteyi gir :")
	 ip = input("  ")
	 os.system("ping "+ip)
	 
if f == "4":
	 print("""
	FSM CYBER TEAMÎN HİÇBİR SORUMLULUĞU YOKTUR EĞLENCE VE TEST AMAÇLI YAPILMIŞTIR
	EĞER DDOS TOOLU İLE BİR SİSTEM ÇÖKERTİLİRSE BİZİM HİÇBİR SORUMLULUĞUMUZ YOKTUR
		
	""")
	 
	 
if k == "eminim":
	print("başlatmak için 3'e bas")
	
	
	
if k == "değilim":
	print(" o zaman görüşürüz.... ")
	exit()