#!/usr/bin/env python
#
import os
import time
import sys
import unidecode
import random

alphalist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

text = open("candide")
text = text.read()
length_text = len(text)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def randomKey():
    key = random.randint(1,25)
    print("Key = ",key)
    return key

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
#        freq = x / length_text
#        freq = round(freq,3)
        compter_lettres.append(x)
    return compter_lettres

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

def textToCesar(text,key,alphalist):
    secret_text = ""
    for char in text:
        new_letter = charToCesar(char,key,alphalist)
        secret_text+=new_letter
    return secret_text

def cesarToText(text,key,alphalist):
    decode_text = ""
    for char in text:
        new_letter = cesarToChar(char,key,alphalist)
        decode_text+=new_letter
    return decode_text

def RANDOM_CRYPT(filename,key, alphalist):
    text_cesar = textToCesar(unidecode,key,alphalist)
    return text_cesar

def outputToFile(filename,decodeText):
    output_filename = filename+'_decode.txt'
    output = open(output_filename, 'w+')
    output.write(decodeText)
    output.close()
    print("Text écrit dans ",output_filename)

def attaque_brute_force_sa(text,alphalist):
    x = 0
    while True:
        x = x+1
        attempt_text = cesarToText(text,x,alphalist)
        print(x)
        if input('S pour stop, ou n''importe quelle autre touche pour continuer ') == 's':
            print("La clé finale était ",x)
            break
        print("\n\n\n")

def e_attack(text,alphalist,filename):
    x = 0
    stats = occurenceOfLetter(text,alphalist)
    while True:
        x = x+1
        chercheE = max(stats)
        index_haute_frequence = stats.index(chercheE)
        prob_key = index_haute_frequence - 4

        print("La lettre num ", alphalist[index_haute_frequence], index_haute_frequence," apparait ", chercheE, " fois. Testons avec la clé ", prob_key, ": \n")
        attempt_text = cesarToText(text,prob_key,alphalist)
        print(attempt_text)

        if input('S pour stop, ou n''importe quelle autre touche pour continuer ') == 's':
            print("\n\nLa clé finale était ",prob_key,"\n\n")
            outputToFile(filename,attempt_text)
            break
        print("\n\n\n")
        ### index_haute_frequence n'est pas E, donc on vire pour tester la suivante
        stats[index_haute_frequence] = 0

###############################################################################################
key = randomKey()
unidecode = clean(text)
STATS_BASE = occurenceOfLetter(unidecode,alphalist)
print("Nombre de E dans le texte de base : ", STATS_BASE[4],"\n\n")

text = RANDOM_CRYPT("candide",key,alphalist)
print("Texte chiffré :")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print(text)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n")

e_attack(text,alphalist,"candide")
