#!/usr/bin/env python
#
import os
import time
import sys
import unidecode
import random

# Tableau avec toutes les lettres de lalphabet

alphalist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Ouvrir le fichier de texte a convertir et determiner sa longueur
#text = open("candide")
#text = text.read()
text = "ceci est une phrase vraie"
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
    key = random.randint(-25,25)
    print("Key = ",key)
    key = 12
    return key

# Pour chaque lettre du texte, supprimer les accents et mettre en minuscule
def clean(text):
    result = []
    for a in text:
        a = unidecode.unidecode(a)
        result.append(a.lower())
    return result

# Pour chaque lettre de l alphabet, compter le nombre de fois ou elle apparait dans le texte
# Determiner sa frequence en divisant par le nombre total de caractere
def occurenceOfLetter(text,alphalist):
    compter_lettres = []
    for letter in alphalist:
        x = 0
        for char in text:
            if char == letter:
                x = x+1
        freq = x / length_text
        freq = round(freq,3)
        compter_lettres.append(freq)
    return compter_lettres

# Ouvre le fichier en mode append pour ecrire a la fin, puis ecrire le contenu de la variable
def writeFile(filename,text):
    output = open(filename, 'a')
    output.write(text)
    output.close()

# Si le caractere n'est pas une lettre, ignorer
# Recuperer le numero de la lettre en la comparant avec alphalist et recuperer le numero index
# Ajouter la clé a l'index pour trouver nouvelle lettre dans alphalist
# Modulo pour revenir au debut de l'alphabet
def charToCesar(char,key,alphalist):
    if char not in alphalist:
        return char
    letter_number = alphalist.index(char)
    new_index = (letter_number + key)%26
    new_letter = alphalist[new_index]
#    print(char)
#    print(letter_number)
#    print(new_index)
#    print(new_letter)
    return new_letter

# Pareil que cesarToChar mais dans le sens inverse
def cesarToChar(char,key,alphalist):
    if char not in alphalist:
        return char
    letter_number = alphalist.index(char)
    new_index = (letter_number - key)%26
    new_letter = alphalist[new_index]
#    print(char)
#    print(letter_number)
#    print(new_index)
#    print(new_letter)
    return new_letter

# Pour chaque lettre dans le texte, convertir la lettre avec la fonction charToCesar et ajouter sur une nouvelle variable
def textToCesar(text,key,alphalist):
    secret_text = ""
    for char in text:
        new_letter = charToCesar(char,key,alphalist)
        secret_text+=new_letter
    return secret_text

# Pour chaque lettre en mode cesar, on utilise la fonction cesarToChar pour decoder le texte
def cesarToText(text,key,alphalist):
    decode_text = ""
    for char in text:
        new_letter = cesarToChar(char,key,alphalist)
        decode_text+=new_letter
    return decode_text

# Prendre le texte unicode et le passer dans la fonction textToCesar
# Creer le fichier de sortie avec extension '_code.txt'
# Puis ecrire le contenu du texte codé dans le fichier
def fileToCesar(filename,key, alphalist):
    text_cesar = textToCesar(unidecode,key,alphalist)
    filename = filename+'_code.txt'
    output = open(filename, 'w+')
    output.write(text_cesar)
    output.close()

# Retrouver le fichier texte chiffré avec son extension
# Lire le contenu de ce fichier secret
# Puis passer le contenu du fichier dans la fonction pour le dechiffrer
# Enfin, ecrire le contenu du resultat de la fonction dans un nouveau fichier decode
def cesarToFile(filename,key,alphalist):
    filename_cesar = filename+'_code.txt'
    secret_text = open(filename_cesar)
    secret_text = secret_text.read()
    decode_text = cesarToText(secret_text,key,alphalist)
    decode_filename = filename+'_decode.txt'
    output = open(decode_filename, 'w+')
    output.write(decode_text)
    output.close()
    print("Texte écrit dans ",decode_filename)

###############################################################################################
# Générer une clé aléatoire
key = randomKey()
# Transformer le texte pour supprimer les accents
unidecode = clean(text)
freq_lettres = occurenceOfLetter(unidecode,alphalist)
#print(freq_lettres)

# debug : test de convertir des lettres
# charToCesar('a',3,alphalist)
# charToCesar('b',3,alphalist)
# charToCesar('c',3,alphalist)
# charToCesar('x',3,alphalist)
# charToCesar('y',3,alphalist)
# charToCesar('z',3,alphalist)
# cesarToChar('a',3,alphalist)
# cesarToChar('b',3,alphalist)
# cesarToChar('c',3,alphalist)
# cesarToChar('x',3,alphalist)
# cesarToChar('y',3,alphalist)
# cesarToChar('z',3,alphalist)

cesar = textToCesar(unidecode,key,alphalist)
print("Texte chiffré :")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print(cesar)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n")

non_cesar = cesarToText(cesar,key,alphalist)
print("Texte déchiffré :")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print(non_cesar)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n")

fileToCesar("candide",key,alphalist)
cesarToFile("candide",key,alphalist)

#writeFile("log", text)
print(bcolors.OKCYAN,"Clé aléatoire :", key,bcolors.RESET)
