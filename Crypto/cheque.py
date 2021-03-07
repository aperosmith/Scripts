#!/usr/bin/env python
#
import os
import time
import sys
import unidecode
import random
import math

class bcolors:
    # Définir quelques couleurs pour que ça soit joli
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    ORANGE = '\033[93m'
    WARNING = '\033[101m'
    RED = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

max_key_length = 10
message = "abcdefghijklmnopqrstuvwxyz"

def randomPrime():
    randomPrime = ""
    i = 1
    for i in range (0, max_key_length):
        if i == 0:
            part_number = str(random.randint(1,9))
        else:
            part_number = str(random.randint(0,9))
        randomPrime = randomPrime+part_number
    randomPrime=int(randomPrime)
    return randomPrime

def checkprime(number):
    if number % 2 == 0:
        return False
    if number % 3 == 0:
        return False
    # test rapide mais pas forcement fiable
    #print("++++++++++++++",number,"++++++++++++++")
    for i in liste_premiers:
        if i == number:
            continue
        #print(number,"%",i,"=",number%i)
        if number % i == 0:
            return False
    # vérifier jusqu'a racine carré du nombre
    # si x * y = number, l'un de x ou y sera plus petit que V(number)
    #for i in range(3, int(number**0.5)+2, 2):
    #print("Deuxieme test...")
    while (i*i < number):
        print("Test :",number,"...",i,"/",int(number**0.5)+2)
        if number % i == 0:
            return False
        if number % (i+2) == 0:
            return False
        i=i+6
    return True

def eratosteme(max_key_length):
    # Retourne une liste de nombres premiers
    liste_premiers = []
    n = ""
    for i in range (0, 5):
        n=n+"9"
    n = int(n)
    print("Taille de la liste :",n)
    premiers = []
    for i in range(0,n+1):
        # Créer une liste remplie de vrai
        #print("\t",bcolors.PURPLE,"Initilisation liste ...",i, bcolors.RESET,end="\r")
        premiers.append(True)
    testpremier = 2
    while (testpremier * testpremier <= n):
        print("\t",bcolors.PURPLE,"Elimination des multiples de",testpremier, bcolors.RESET,end="\r")
        if (premiers[testpremier] == True):
            for i in range(testpremier * testpremier, n+1, testpremier):
                premiers[i] = False
        testpremier += 1
    print("\n")
    for testpremier in range(2, n+1):
        if premiers[testpremier]:
            print("\t",bcolors.PURPLE,"Ajout de",testpremier,"à la liste.", bcolors.RESET,end="\r")
            liste_premiers.append(testpremier)
    print("\n")
    return(liste_premiers)


def generatePrime(name):
    testprime = False
    while testprime != True:
        randomNumber = randomPrime()
        print("\t",bcolors.PURPLE,"Test de nombre aléatoire ...",randomNumber, bcolors.RESET,end="\r")
        testprime = checkprime(randomNumber)
    print(bcolors.GREEN,"\nNombre premier",name,"=",randomNumber,bcolors.RESET)
    return(randomNumber)

def moduleChiffrement():
    P = generatePrime("P")
    Q = generatePrime("Q")
    module = (P, Q)
    N = P*Q
    print(bcolors.GREEN,"Module N =",module,bcolors.RESET)
    return module,N,P,Q

def indicatriceEuler(module):
    phi = (module[0] - 1)*(module[1] - 1)
    print(bcolors.GREEN,"phi =",module[0] - 1,"*",module[1] - 1,"=",phi,bcolors.RESET)
    return phi

def exposantChiffrement(phi):
    exposant = 0
    randomNumber = 0
    while math.gcd(randomNumber,phi) != 1:
        randomNumber = random.randrange(1, phi)
        #if randomNumber < phi:
        #    print(True)
    return randomNumber

def exposantDechiffrement(exposant,phi):
    # Magie Voodoo
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi
    while exposant > 0:
        temp1 = temp_phi//exposant
        temp2 = temp_phi - temp1 * exposant
        temp_phi = exposant
        exposant = temp2
        x = x2 - temp1 * x1
        y = d - temp1 * y1
        x2 = x1
        x1 = x
        d = y1
        y1 = y
    if temp_phi == 1:
        d = d+phi
        return d

def myrsakeys():
    module,N,P,Q = moduleChiffrement()
    phi = indicatriceEuler(module)
    E = exposantChiffrement(phi)
    D = exposantDechiffrement(E,phi)
    print("P =",P,"\tQ =",Q,"\tN =",N,"\tModule =",module, "\tphi =",phi, "\texposant =", E,"\tDecodeur =",D)
    pub = (E,N)
    #pub = (119, 391)
    priv = (D,N)
    #priv = (423, 391)
    print("pub:",pub,"\tpriv:",priv)
    return pub,priv

def encryption(message,E,N):
    code = []
    for char in message :
        newchar = pow(ord(char),E,N)
        code.append(newchar)
    str(code)
    return code

def decrypt(code,D,N):
    clair = ""
    for char in code:
        newchar = pow(char,D,N)
        clair = clair + chr(int(newchar))
    str(clair)
    return clair

def echeque():
    NUMCHEQUE = 1
    SECRETCHEQUE = 1
    PROPRIETAIRE = 1
    return NUMCHEQUE,SECRETCHEQUE,PROPRIETAIRE

def testCode(message,key):
    code=encryption(message,key[0],key[1])
    print("Message secret \t\t: ",code)
    return code

def testDecode(code,key):
    clair = decrypt(code,key[0],key[1])
    print("Messagé déchiffré \t:",clair)
    return clair


liste_premiers = eratosteme(max_key_length)
#print(liste_premiers)

result = []
for i in range (0, 10):
    numtest = generatePrime(i)
    result.append(numtest)
print(result)
pub,priv = myrsakeys()
print("Messagé de base \t:",message)
code = testCode(message,pub)
clair = testDecode(code,priv)
