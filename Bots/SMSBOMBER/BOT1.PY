import os
import sys
from FerdiTayfurSmSbomber import start

control_file = "input_processed.flag"

def imports():
    global start
    import FerdiTayfurSmSbomber
    from FerdiTayfurSmSbomber import start

def write():
    with open(control_file, "w") as denet:
        denet.write("Girdi işlendi, dosyayı silebilirsin.")

def write_girdi(n):
    with open(control_file, "w") as denet:
        denet.write(n)

def denetle():
    if not os.path.exists(control_file):
        bot_inputter(num=1)
        write()
    else:
        bot_inputter(num=None)

def whiler():
    inp = input("BOT > ")
    global d1, d2, th, mh

    if inp.startswith("!help"):
        print("""
        Merhaba, ben sana özel bir botum ve komutlarım şunlardır:
        1. İlk başta botset smsthread'i ayarlamalısın
           Örnek kullanım: botset smsthread=0 (bu sınırsız yapacaktır)
        
        2. Thread sayısını ayarlamak için:
           Örnek kullanım: botset thread=1
        
        3. SMS bombalama başlatmak için:
           Örnek kullanım: !smsbomb 05xx xxx xx xx
        """)
        return

    if inp.startswith("botset thread="):
        th = inp.split('=')[1]
        d1 = False
        return

    if inp.startswith("botset smsthread="):
        mh = inp.split('=')[1]
        d2 = False
        return

    if inp.startswith("!smsbomb"):
        yakala = inp.split(' ')[1]
        print("SMS bomber başlatılıyor...")
        imports()
        start.number = yakala
        if d1:
            print("Lütfen thread sayısını girin. Örnek: botset thread=2")
        else:
            print("Thread sayısı gönderiliyor...")
            imports()
            start.worker_amount = th
        
        if d2:
            print("SMS thread kaydedilmemiş, otomatik olarak sınırsız moda geçiliyor...")
            start.amount = 0
        else:
            start.amount = int(mh)
        
        start.send(number=yakala, amount=start.amount, worker_amount=start.worker_amount)

def bot_inputter(num=None):
    if num == 1:
        one = input("Girdiler işlensin mi? [y/n] ")
        if one.lower() == "y":
            write_girdi("y")
    elif num is None:
        while True:
            whiler()

all_sends = 0
success_sends = 0
failed_sends = 0
clear = lambda: os.system("clear")
denetle()