#!/usr/bin/env python
import os
import time
from scapy.all import *





a=IP(dst="192.168.0.200/30")
print(a)
[p for p in a]

b=IP(ttl=[1,2,(5,9)])
b
[p for p in b]

c=TCP(dport=[80,443])
[p for p in a/c]
