#!/usr/bin/env python
#
import os
import time
import sys
import unidecode
import random
import itertools

alphalist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

class bcolors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    TEST = '\033[101m'
    RED = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print(bcolors.PURPLE,"test test test ",bcolors.RESET)
print(bcolors.BLUE,"test test test ",bcolors.RESET)
print(bcolors.CYAN,"test test test ",bcolors.RESET)
print(bcolors.GREEN,"test test test ",bcolors.RESET)
print(bcolors.WARNING,"test test test ",bcolors.RESET)
print(bcolors.RED,"test test test ",bcolors.RESET)
print(bcolors.TEST,"test test test ",bcolors.RESET)

if len(sys.argv) == 1:
    print("IL FAUT DONNER UN TEXTE A CHIFFRER !!!")
    sys.exit()

text = open(sys.argv[1])
text = text.read()
print(text)
