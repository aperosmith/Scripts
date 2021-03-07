#!/usr/bin/env python
#
import os
import time
import sys
import unidecode
import random
import itertools
import statistics

alphalist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

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


if len(sys.argv) == 1:
    # Fermer le programme si aucun fichier texte n'est passé en argument
    print(bcolors.WARNING,"IL FAUT DONNER UN TEXTE A CHIFFRER !!!")
    sys.exit()

# Ouvrir le fichier texte
text = open(sys.argv[1])
text = text.read()
#text = "em ymdot ba em bg fqxxqyqzf oq oappq "
#key = random.randint(2,25)

def randomKey(max_key_length):
    key = []
    i = 1
    # Longueur de clé aléatoire
    rand_keylength = random.randint(3,max_key_length)
    while i <= rand_keylength:
        # Remplir la liste avec clés alétoires
        part_key = random.randint(0,25)
        key.append(part_key)
        i = i+1
    return key

def printCrypt():
    print("Texte chiffré :")
    print(bcolors.RED,"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++",bcolors.RESET)
    print(text)
    print(bcolors.RED,"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n",bcolors.RESET)

def printDecrypt(decrypt,prob_key):
    # print("Texte déchiffré avec prob_key :")
    print(bcolors.RED,"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++",bcolors.RESET)
    print(decrypt)
    print(bcolors.RED,"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++",bcolors.RESET)

def clean(text):
    result = []
    for a in text:
        a = unidecode.unidecode(a)
        result.append(a.lower())
    return result

def occurenceOfLetter(text,alphalist):
    compter_lettres = []
    for letter in alphalist:
        x = 0
        for char in text:
            if char == letter:
                x = x+1
        # Créer une liste du nombre des 26 lettres
        compter_lettres.append(x)
    return compter_lettres

def textToCesar(text,key,alphalist):
    secret_text = ""
    for char in text:
        new_letter = charToCesar(char,key,alphalist)
        secret_text+=new_letter
    return secret_text
def charToCesar(char,key,alphalist):
    if char not in alphalist:
        return char
    letter_number = alphalist.index(char)
    new_index = (letter_number + key)%26
    new_letter = alphalist[new_index]
    return new_letter

def cesarToChar(char,key,alphalist):
    if char not in alphalist:
        return char
    letter_number = alphalist.index(char)
    new_index = (letter_number - key)%26
    new_letter = alphalist[new_index]
    return new_letter
def cesarToText(text,key,alphalist):
    decode_text = ""
    for char in text:
        new_letter = cesarToChar(char,key,alphalist)
        decode_text+=new_letter
    return decode_text

def findemot(text,alphalist):
    last_letter = ""
    double_lettres = 0
    letter_1 = ""
    letter_2 = ""
    letter_3 = ""
    for char in text:
        if char == " ":
            if letter_3 not in alphalist:
                continue
            if letter_1 == letter_2:
                double_lettres = double_lettres+1
                # print(letter_1+letter_2+letter_3)
                last_letter = last_letter+letter_3
        letter_1 = letter_2
        letter_2 = letter_3
        letter_3 = char
    print(last_letter)
    stats = occurenceOfLetter(last_letter,alphalist)
    chercheE = max(stats)
    print("Derniere lettre après double-lettre :",double_lettres)
    index_haute_frequence = stats.index(chercheE)
    prob_key = (index_haute_frequence - 4) % 26
    return prob_key


###############################################################################################
#print("VRAIE CLE : ", key)
text = clean(text)

#text = textToCesar(text,key,alphalist)
prob_key = findemot(text,alphalist)
dechiffre = cesarToText(text,prob_key,alphalist)
print(dechiffre)
print("CLE HACKÉ :", prob_key)
