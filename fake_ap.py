#!/usr/bin/python
from scapy.all import *
import subprocess
import string
import random
import time

subprocess.call(["airmon-ng","stop","mon0"],stdout=open(os.devnull,"w"),stderr=subprocess.STDOUT)
subprocess.call(["airmon-ng","start","wlan0"],stdout=open(os.devnull,"w"),stderr=subprocess.STDOUT)
def gen_ssid(size=8,chars=string.letters+string.digits):
    size=random.randrange(7,10,1)
    return ''.join(random.choice(chars) for maa in range(size))

def gen_s_ssid(size=5,chars='12'):
   return ''.join(random.choice(chars) for maa in range(size))

def gen_mac(size=6,chars=string.digits+'abcdef'):
   return ':'.join(random.choice(chars)+random.choice(chars) for maa in range(size))

dst='ff:ff:ff:ff:ff:ff'
rates='\x03\x02\x01'
Rsn='\x01\x00\x00\x0f\xac\x02\x01\x00\x00\x0f\xac\x02\x01\x00\x00\x0f\xac\x02\x01\x00\x00\x0f\xac\x02\x01\x00'

beacon=Dot11Beacon(cap=0x2104)
rates=Dot11Elt(ID='Rates',info=rates)
dsset=Dot11Elt(ID='DSset',info='\x01')
tim=Dot11Elt(ID='TIM',info='\x00\x01\x00\x00')
rsn=Dot11Elt(ID='RSNinfo',info=Rsn)
while 1:
   ssid=gen_ssid()
   src='00:11:22:33:44:00'
   bssid=src
   essid=Dot11Elt(ID='SSID',info=ssid)
   packet=RadioTap()/Dot11(type=0,subtype=8,addr1=dst,addr2=src,addr3=bssid)/beacon/essid/rates/dsset/tim

   sendp(packet,iface='wlan0',count=15)
   
