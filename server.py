#-*- coding: cp1254 -*-
import socket
import subprocess
from threading import Thread
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("www.google.com",80))
sockip = s.getsockname()[0]
s.close()

s = socket.socket()
host = sockip
port = 2015
s.bind((host, port))

print host
print port
print "Baglanti Bekleniyor."

s.listen(1000)
baglantilar = []
tumbaglantilar=[]
baglantiadresleri = []
tumbaglantilaradresleri=[]

def serverbaslat(s,b,ba,tb,tba):
    while True:
        baglanti, adres = s.accept()
        b.append(baglanti)
        ba.append(adres)
        tb.append(baglanti)
        tba.append(adres)
        baglanti.send("Hosgeldin->"+str(adres[0])+":"+str(adres[1]))
        
t = Thread(target=serverbaslat, args=(s,baglantilar,baglantiadresleri,tumbaglantilar,tumbaglantilaradresleri,))
t.start()

def linkal(b,ba):
    
    def mesajyolla(mesaj):
        hatalilar=[]
        for i in range(0,len(b)):
            try:
                b[i].send(mesaj)
                print "Yollandi->>",ba[i]
            except:
                hatalilar.append(b[i])
                print "Silindi->>",ba[i]
        for hatali in hatalilar:
            b.remove(hatali)
            ba.remove(hatali.getpeername())        
        
    while True:
        if(len(b)>0):
            giris = raw_input("Mesaj Girin: ")
            if("m=" in giris):
                mesajyolla(giris)

                    
                
            else:   
                if(giris=="active users"):
                    mesajyolla("usercontrol")
                    print len(b)
        else:
            time.sleep(5)
            
k = Thread(target=linkal, args=(baglantilar,baglantiadresleri))
k.start()
                    
    
