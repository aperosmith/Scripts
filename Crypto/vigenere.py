#!/usr/bin/env python
#
import os
import time
import sys
import unidecode

alphalist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
key = [1, 2, 3]
text = 'objectif'

file = open("candide")
file = file.read()

###############################################################################################
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

def clean(text):
    result = []
    for char in text:
        char = unidecode.unidecode(char)
        result.append(char.lower())
    return result

def textToVig(text,key,alphalist):
    text = clean(text)
    result = ""
    x = 0
    for char in text:
        if char not in alphalist:
            result+=char
            continue
        letter_index = alphalist.index(char)
        new_index = ( letter_index + key[x] ) % 26
        new_letter = alphalist[new_index]
#        print('x = ',x,'   key[x] = ',key[x],'   char =',char,'   letter_index = ',letter_index,'   new_index = ',new_index,'   new_letter = ',new_letter)
        x = x+1
        if x > 2:
            x = 0
        result+=new_letter
    return result

def vigToText(text,key,alphalist):
    result = ""
    x = 0
    for char in text:
        if char not in alphalist:
            result+=char
            continue
        letter_index = alphalist.index(char)
        new_index = ( letter_index - key[x] ) % 26
        new_letter = alphalist[new_index]
#        print('x = ',x,'   key[x] = ',key[x],'   char =',char,'   letter_index = ',letter_index,'   new_index = ',new_index,'   new_letter = ',new_letter)
        x = x+1
        if x > 2:
            x = 0
        result+=new_letter
    return result

def fileToVig(filename,key,alphalist):
    text_vigenere = textToVig(file,key,alphalist)
    print(text_vigenere)
    filename = filename+'_code.txt'
    output = open(filename, 'w+')
    output.write(text_vigenere)
    output.close()

def vigToFile(filename,key,alphalist):
    filename_vigenere = filename+'_code.txt'
    secret_text = open(filename_vigenere)
    secret_text = secret_text.read()
    decode_text = vigToText(secret_text,key,alphalist)
    print(decode_text)
    decode_filename = filename+'_decode.txt'
    output = open(decode_filename, 'w+')
    output.write(decode_text)
    output.close()
    print("Text écrit dans ",decode_filename)

###############################################################################################

print(file)
fileToVig("candide",key,alphalist)
vigToFile("candide",key,alphalist)
