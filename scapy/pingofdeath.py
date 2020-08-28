#!/usr/bin/env python
import os
import time
from scapy.all import *



send( fragment(IP(dst="192.168.0.218")/ICMP()/("X"*60000)) )
