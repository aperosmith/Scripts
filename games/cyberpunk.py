#!/usr/bin/env python
#########################################################################################################
#
# Affiche le nombre de jour restant avant le 17 septembre 2020 sous forme d'emoji en forme de tableau
#
#########################################################################################################
from datetime import date
from os import system, name

def clear():
      if name == 'nt':
        _ = system('cls')
      else:
        _ = system('clear')
clear()

f_date = date.today()
l_date = date(2020, 9, 17)
delta = l_date - f_date
system('clear')

i = 1
k = 1


print()
print("       ________  ______  __________  ____  __  ___   ____ __")
print("      / ____/\ \/ / __ )/ ____/ __ \/ __ \/ / / / | / / //_/")
print("     / /      \  / __  / __/ / /_/ / /_/ / / / /  |/ / , <  ")
print("    / /___    / / /_/ / /___/ _, _/ ____/ /_/ / /|  / /| |  ")
print("    \____/   /_/_____/_____/_/ |_/_/    \____/_/ |_/_/ |_|  ")
print("                                                            2077")
print()

while i <= delta.days:
    if k == 1:
        print("              ", end = '')
    if k <= 10:
        print("\U0001F7E1", "", end = '')
        k += 1
        i += 1
    else:
        print()
        k = 1

print()
print()
print()
