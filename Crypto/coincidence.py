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
    print(bcolors.WARNING,"IL FAUT DONNER UN TEXTE A CHIFFRER EN ARGUMENT !!!")
    print(bcolors.WARNING,"python3 coincidence.py candide")
    sys.exit()

# Ouvrir le fichier texte
text = open(sys.argv[1])
text = text.read()
length_text = len(text)
max_key_length = 19

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

def textToVig(text,key,key_len,alphalist):
    result = ""
    x = 0
    skip = 0
    for char in text:
        if x == key_len:
            # Quand on a fait le tour de la clé on revient au début
            x = 0
        #print(bcolors.PURPLE,x,"\t",key[x],"\t",key_len-1,bcolors.RESET)
        #debug_x.append(x)
        if char not in alphalist:
            # On ne chiffre pas les espaces et la ponctuation
            result+=char
            skip = skip + 1
            continue
        if char in alphalist:
            # On chiffre chaque lettre avec la clé et on décale la clé à chaque opération
            letter_index = alphalist.index(char)
            new_index = ( letter_index + key[x] ) % 26
            new_letter = alphalist[new_index]
            result+=new_letter
        #print('x = ',x,'   key[x] = ',key[x],'   char =',char,'   letter_index = ',letter_index,'   new_index = ',new_index,'   new_letter = ',new_letter)
            x = x+1
    # Vérifier que le compte est bon
    print(nombreLettres, "lettres +", skip, "non-lettres = ", nombreLettres + skip, "/", length_text)
    #print(bcolors.PURPLE,debug_iteration_key,bcolors.RESET)
    return result

def vigToText(text,key,key_len,alphalist):
    result = ""
    x = 0
    skip = 0
    for char in text:
        if x == key_len:
            # Quand on a fait le tour de la clé on revient au début
            x = 0
        if char not in alphalist:
            # On ne déchiffre pas les espaces et la ponctuation
            result+=char
            skip = skip + 1
            continue
        if char in alphalist:
            # On déchiffre chaque lettre avec la clé et on décale la clé à chaque opération
            letter_index = alphalist.index(char)
            new_index = ( letter_index - key[x] ) % 26
            new_letter = alphalist[new_index]
            result+=new_letter
            x = x+1
        #print('x = ',x,'   key[x] = ',key[x],'   char =',char,'   letter_index = ',letter_index,'   new_index = ',new_index,'   new_letter = ',new_letter)
    return result

def RANDOM_CRYPT(filename,key,key_len,alphalist):
    text_vig = textToVig(text,key,key_len,alphalist)
    return text_vig

def WRITE_FICHIER_CODE(filename,code):
    filename = filename+'_code.txt'
    output = open(filename, 'a+')
    output.write(code)
    output.close()

def WRITE_FICHIER_DECODE(filename,decrypt):
    decode_filename = filename+'_decode.txt'
    output = open(decode_filename, 'a+')
    output.write(decrypt)
    output.close()

def nombreLettres(text):
    nombreLettres = 0
    for letter in alphalist:
        for char in text:
            if char == letter:
                nombreLettres = nombreLettres+1
    return nombreLettres

def indexC(text,alphalist,i):
    # Calculer la taille du fragment sans les espaces
    taille_fragment = 0
    resultIC = 0
    for letter in alphalist:
        for char in text:
            if char == letter:
                taille_fragment = taille_fragment+1
    # Compte le nombre de chacune des lettres
    compte_lettres = occurenceOfLetter(text,alphalist)
    for letter in alphalist:
        # (Nq x Nq -1) / (L * L -1)
        proba_lettre = ((compte_lettres[alphalist.index(letter)] * compte_lettres[alphalist.index(letter)] -1) / (taille_fragment * taille_fragment -1))
        #print("(",compte_lettres[alphalist.index(letter)], "x",compte_lettres[alphalist.index(letter)]-1 , ") / ( ", taille_fragment, "x", taille_fragment -1, ") = ", bcolors.CYAN,proba_lettre,bcolors.RESET)
        # (Nq / L) x (Nq - 1 / L -1)
        #proba_lettre = (compte_lettres[alphalist.index(letter)] / taille_fragment) * ((compte_lettres[alphalist.index(letter)] - 1) / (taille_fragment - 1))
        # IC = ICa + ICb + ICc ... + ICz
        resultIC = resultIC + proba_lettre
        #print("Le nombre de ", letter, " est ",compte_lettres[alphalist.index(letter)], " et sa proba est : ", proba_lettre)
    #print("L'indice de coincidence du texte est : ",resultIC)
    #print("Fragment ",bcolors.CYAN,i,bcolors.RESET, " : ",compte_lettres, "\t",bcolors.CYAN,taille_fragment,"\t",bcolors.RED,resultIC,bcolors.RESET)
    return resultIC

def textDecompose(text,alphalist,max_key_length):
    # longueur de clé minimale c'est 2, sinon c'est du césar
    test_key_l = 3
    compare = 0
    # Fragmenter le texte en ne prenant en compte que les lettres
    # Sinon les espaces et ponctuations decalent les lettres des fragmentss
    letters_only = []
    for char in text:
        if char in alphalist:
            letters_only.append(char)
    # Tester pour chaque longueur de clé possible, jusqu'à 9
    while test_key_l <= max_key_length:
        moyenneIC = 0
        listeIC = []
        # fragmenter le text en test_key_l morceaux
        # exemple avec 3 : abc efg devient ae, bf, cg
        # Il faut donc calculer les IC pour chaque fragment
        i = 0
        while i < test_key_l:
            frag_text = []

            # prendre chaque caractère du texte qui correspond a son fragment
            # 1 caractère sur 3, 1 caractère sur 4, 1 caractere sur 5 ...
            # Puis faire pareil mais en décallant le premier caractère de 1
            # Pour test_key_l = 3, on doit avoir 0,3,6,9 -- 1,4,7,10 -- 2,5,8,11
            for char in letters_only[i::test_key_l]:
                    frag_text.append(char)
            resultIC = indexC(frag_text,alphalist,i)
            listeIC.append(resultIC)
            i = i + 1
        standardDeviation = statistics.stdev(listeIC)
        standardDeviation = round(standardDeviation, 5)
        moyenneIC = sum(listeIC) / test_key_l
        moyenneIC = round(moyenneIC, 5)
        print(bcolors.BLUE,"Pour une clé de longueur ",bcolors.PURPLE,test_key_l,"\t",bcolors.BLUE,"nous avons un IC moyen de ",bcolors.PURPLE,moyenneIC,bcolors.BLUE,"\t±",bcolors.PURPLE,standardDeviation,bcolors.RESET)
        # Garder la plus grande moyenne en les comparant une par une quand elles sont générées
        if moyenneIC >= compare:
            compare = moyenneIC
            compare_l = test_key_l
        test_key_l = test_key_l + 1
    print(bcolors.BLUE,"\n IC est le plus grand (",bcolors.PURPLE,compare,bcolors.BLUE, ") pour une clé de longueur probable de ",bcolors.PURPLE, compare_l,"\n",bcolors.RESET)
    print(bcolors.BLUE,"Il faut donc tester avec ",bcolors.GREEN, compare_l,bcolors.BLUE,"fragments :")
    return compare_l

def e_attack(text,alphalist):
    # Version simplifiée de l'attaque par E
    # On utilie les fragments du texte chiffré
    # Car dans ces fragments le E est supposé être toujours la même lettre
    stats = occurenceOfLetter(text,alphalist)
    # le "E" chiffré doit être la lettre qui apparait le plus dans le fragment
    chercheE = max(stats)
    # Comparer l'index du E chiffré avec le véritable index pour déterminer la clé
    # qui a permis de chiffrer le fragment
    # Si le E chiffré = G, alors la clé est 6 - 4 = 2
    index_haute_frequence = stats.index(chercheE)
    prob_key = (index_haute_frequence - 4) % 26
    #print(prob_key)
    return prob_key

def decode(text,alphalist,prob_key_l):
    letters_only = []
    prob_key = []
    i = 0
    # Supprimer toute la ponctuation et les espaces :
    for char in text:
        if char in alphalist:
            letters_only.append(char)
    while i < prob_key_l:
        # On redivise le texte en fragments, autant que la longueur de clé probable :
        frag_text = []
        for char in letters_only[i::prob_key_l]:
            frag_text.append(char)
        # Pour chaque fragment, on applique l'attaque par E pour trouver un morceau de clé :
        E = e_attack(frag_text,alphalist)
        print(bcolors.BLUE,"Pour le fragment num ", bcolors.PURPLE,i,bcolors.BLUE, "\tla clé est probablement \t", bcolors.PURPLE,E,bcolors.RESET)
        prob_key.append(E)
        i = i+1
    print(bcolors.BLUE,"\n Clé probable : \t",bcolors.PURPLE,prob_key,bcolors.BLUE,"Longueur :",bcolors.PURPLE, len(prob_key),bcolors.RESET)
    print(bcolors.GREEN,"Clé aléatoire :\t",bcolors.ORANGE,key,bcolors.GREEN,"Longueur :",bcolors.ORANGE,len(key),bcolors.RESET,"\n")
    decrypt = vigToText(text,prob_key,len(prob_key),alphalist)
    printDecrypt(decrypt,prob_key)
    #if input('S pour stop, ou n''importe quelle autre touche pour continuer ') == 's':
        #print("La clé finale était ",x)
        #break
    return prob_key



###############################################################################################
# Calculer une clé aléatoire et l'afficher, au cas où
key = randomKey(max_key_length)
print(bcolors.CYAN,"Clé aléatoire :", key,bcolors.RESET)

# Rendre le texte sain et compter les lettres pour debug
text = clean(text)
nombreLettres = nombreLettres(text)


# Chiffrer le texte et ecrire dans fichier et terminal
text = RANDOM_CRYPT(sys.argv[1],key,len(key),alphalist)
WRITE_FICHIER_CODE(sys.argv[1],text)
printCrypt()

prob_key_l = textDecompose(text,alphalist,max_key_length)
prob_key = decode(text,alphalist,prob_key_l)
#decrypt = vigToText(text,prob_key,len(prob_key),alphalist)
#printDecrypt()
#WRITE_FICHIER_DECODE("candide",decrypt)
