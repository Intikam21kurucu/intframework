#!/usr/bin/env python3
# oip - Özelleştirilmiş Ağ Tarama ve Araştırma Aracı

import socket
import argparse
from concurrent.futures import ThreadPoolExecutor
import requests
from tqdm import tqdm  # İlerleme çubukları için
from time import sleep  # Gecikmeleri simüle etmek için
from colorama import init, Fore, Style
import itertools
import threading
import sys

# Renkli çıktı ve terminal işlemleri için colorama başlat
init(autoreset=True)

# ASCII Sanatı
ASCII_ART = """
#                                                                                                 
#                                                                                                 
#                                                                                                 
#                                                                                                 
#                                                                                                 
#                                                                                                 
#                                                                                                 
#                                                                                                 
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
#                                          .I~~~~~~~~~~~!^                                        
#                                                                                                 
#                                                                                                 
#                                                                                                 
#                                                                                                 
#                                                                                                 
#                                                                                                 
#                                                                                                 

"""

# Port tarama fonksiyonu
def scan_port(port, ip, timeout):
    print(ASCII_ART)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        try:
            sock.connect((ip, port))
            return (port, True)
        except:
            return (port, False)

# Sosyal medya ve diğer sitelerde arama fonksiyonu
def search_sites(query, max_sites):
    print(ASCII_ART)
    sites = [
    f"https://www.facebook.com/search/top?q={query}",
    f"https://www.instagram.com/{query}/",
    f"https://www.youtube.com/results?search_query={query}",
    "https://www.twitter.com/search?q=" + query,
    "https://www.linkedin.com/search/results/all/?keywords=" + query,
    "https://www.reddit.com/search/?q=" + query,
    "https://www.pinterest.com/search/pins/?q=" + query,
    "https://www.tumblr.com/search/" + query,
    "https://www.twitch.tv/search?term=" + query,
    "https://www.wikipedia.org/wiki/" + query,
    "https://www.stackoverflow.com/search?q=" + query,
    "https://www.github.com/search?q=" + query,
    "https://www.medium.com/search?q=" + query,
    "https://www.quora.com/search?q=" + query,
    "https://www.snapchat.com/search/" + query,
    "https://www.whatsapp.com/search/" + query,
    "https://www.tiktok.com/tag/" + query,
    "https://www.google.com/search?q=" + query,
    "https://www.yahoo.com/search?p=" + query,
    "https://www.bing.com/search?q=" + query,
    "https://www.ask.com/web?q=" + query,
    "https://www.duckduckgo.com/?q=" + query,
    "https://www.baidu.com/s?wd=" + query,
    "https://www.yandex.com/search/?text=" + query,
    "https://www.aol.com/search?q=" + query,
    "https://www.wolframalpha.com/input/?i=" + query,
    "https://www.wikihow.com/wikiHowTo?search=" + query,
    "https://www.about.com/search?q=" + query,
    "https://www.search.com/search?q=" + query,
    "https://www.info.com/serp?q=" + query,
    "https://www.ixquick.com/do/search?q=" + query,
    "https://www.sogou.com/web?query=" + query,
    "https://www.ecosia.org/search?q=" + query,
    "https://www.startpage.com/do/dsearch?query=" + query,
    "https://www.mojeek.com/search?q=" + query,
    "https://www.dogpile.com/search/web?q=" + query,
    "https://www.searchencrypt.com/search/?q=" + query,
    "https://www.hotbot.com/search/web?q=" + query,
    "https://www.lycos.com/web/?q=" + query,
    "https://www.metacrawler.com/serp?q=" + query,
    "https://www.webcrawler.com/serp?q=" + query,
    "https://www.dmoz.org/search?q=" + query,
    "https://www.altavista.com/web/results?q=" + query,
    "https://www.alltheweb.com/search?q=" + query,
    "https://www.infospace.com/search/web?q=" + query,
    "https://www.teoma.com/web?q=" + query,
    "https://www.blekko.com/ws/" + query,
    "https://www.gigablast.com/search?q=" + query,
    "https://www.entireweb.com/search/?q=" + query,
    "https://www.yippy.com/search/?v%3aproject=clusty-new&query=" + query,
]

    if len(sites) > max_sites:
        sites = sites[:max_sites]

    results = []
    for site in tqdm(sites, desc="Siteler aranıyor"):
        try:
            response = requests.get(site)
            if response.status_code == 200:
                results.append((site, "Başarılı"))
            else:
                results.append((site, f"Başarısız (Durum Kodu: {response.status_code})"))
        except requests.RequestException as e:
            results.append((site, f"Hata: {e}"))
        sleep(0.1)  # Daha iyi görselleştirme için bazı gecikmeleri simüle et

    return results

# Dönen yükleme simgesi fonksiyonu
def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor

# Argümanları ayrıştır
parser = argparse.ArgumentParser(description='oip - Özelleştirilmiş Ağ Tarama ve Araştırma Aracı')
parser.add_argument('-ip', type=str, help='Hedef IP adresi veya domain')
parser.add_argument('-p', type=str, help='Port aralığı (örn: 80,443 veya 1-65535)')
parser.add_argument('-t', action='store_true', help='Turbo modu aktif')
parser.add_argument('-time', type=int, default=1, help='Her port için zaman aşımı (saniye)')
parser.add_argument('-oip', type=str, help='Araştırılacak isim veya email')
parser.add_argument('-th', type=int, default=10, help='Araştırılacak maksimum site sayısı (en fazla 500)')
args = parser.parse_args()

# Port aralığını ayrıştır
if args.p:
    if ',' in args.p:
        ports = args.p.split(',')
        ports = [int(port) for port in ports]
    elif '-' in args.p:
        start_port, end_port = args.p.split('-')
        ports = list(range(int(start_port), int(end_port) + 1))
    else:
        ports = [int(args.p)]

    print(f"Toplam taranacak port sayısı: {len(ports)}")
    print(f"{args.ip} adresindeki portlar taranıyor...")

    spinner = spinning_cursor()
    stop_spinner = False

    def spin():
        while not stop_spinner:
            sys.stdout.write(next(spinner))
            sys.stdout.flush()
            sleep(0.1)
            sys.stdout.write('\b')
            sys.stdout.flush()

    # Taramayı başlat
    if args.t:
        spinner_thread = threading.Thread(target=spin)
        spinner_thread.start()
        with ThreadPoolExecutor(max_workers=100) as executor:
            results = list(tqdm(executor.map(lambda port: scan_port(port, args.ip, args.time), ports), total=len(ports), desc="Portlar taranıyor"))
        stop_spinner = True
        spinner_thread.join()
    else:
        spinner_thread = threading.Thread(target=spin)
        spinner_thread.start()
        results = []
        for port in tqdm(ports, desc="Portlar taranıyor"):
            results.append(scan_port(port, args.ip, args.time))
        stop_spinner = True
        spinner_thread.join()

    for port, is_open in results:
        status = "opened" if is_open else "closed"
        color = Fore.GREEN if is_open else Fore.RED
        print(f"Port {port} {color}{status}{Style.RESET_ALL}")

    print("Port tarama tamamlandı.")

# Araştırma kısmı
if args.oip:
    if args.th > 50:
        print("Maksimum 50 site araştırılabilir. -th 50 olarak ayarlanıyor.")
        args.th = 50

    print(f"'{args.oip}' için {args.th} site aranıyor...")
    search_results = search_sites(args.oip, args.th)

    for site, status in search_results:
        print(f"{site}: {status}")

    print("Araştırma tamamlandı.")