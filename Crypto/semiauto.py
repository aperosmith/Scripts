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

def cesarToFile(filename,key,alphalist):
    filename_cesar = filename+'_code.txt'
    secret_text = open(filename_cesar)
    secret_text = secret_text.read()
    decode_text = cesarToText(secret_text,key,alphalist)
    decode_filename = filename+'_decode.txt'
    output = open(decode_filename, 'w+')
    output.write(decode_text)
    output.close()

def outputToFile(filename,decodeText):
    output_filename = filename+'_decode.txt'
    output = open(output_filename, 'w+')
    output.write(decodeText)
    output.close()
    print("Text écrit dans ",output_filename)

def attaque_brute_force_sa(text,alphalist,filename):
    x = 0
    while True:
        x = x+1
        test_bruteforce = cesarToText(text,x,alphalist)
        print(test_bruteforce)
        print('key = ',x)
        print('Est-ce que le texte est lisible ? ')
        if input('S si oui, ou n''importe quelle autre touche pour continuer sur la prochaine clé') == 's':
            print("La clé finale était ",x)
            outputToFile(filename,test_bruteforce)
            break
        print("\n\n\n")

###############################################################################################
key = randomKey()
unidecode = clean(text)

RANDOM_CRYPT = RANDOM_CRYPT("candide",key,alphalist)
print("Texte chiffré :")
print(RANDOM_CRYPT)
attaque_brute_force_sa(RANDOM_CRYPT,alphalist,"candide")
