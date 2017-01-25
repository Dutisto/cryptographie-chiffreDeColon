def Cle(chaine):
#Cette fonction sert à entrer la clé dans un tableau.
    carré = [[0] *5 for i in range(5)]
    alphabet = "abcdefghijklmnopqrstuvxyz"
    alphabet = alphabet.upper()
    chaine = chaine.upper()
#Si le caractère n'est pas une lettre, on le supprime
    for car in chaine:
        if -1 < ord(car) < 65 or 90 < ord(car) < 97 or 122 < ord(car):
            chaine = chaine.replace(car,"")
    newChaine = ''
    for car in chaine:
        if car in newChaine:
            pass
        else:
            newChaine+= car
    chaine = newChaine
#si la chaine entré en paramètre ne posséde pas toutes les lettres de l'alphabet, on l'ajoute au tableau (sauf le W)
    for car in alphabet:
        if car in chaine:
            pass
        else:
            chaine += car
    longueur = len(chaine)
    a = 0
    for j in range(0, len(carré)):
        for y in range(0, len(carré[j])):
            if a == longueur :
                break
            carré[j][y] = chaine[a]
            a += 1
    for ligne in carré:
        for x in ligne:
            print(x, ' ', end='')
        print('\n')
    return carré


def chiffrage(lettre, cle):
#on entre une lettre, et en fonction de ses coordonnées X et Y dans la clé, on chiffre les 2 bigrammes correspondant.
    lettreX = 0
    lettreY = 0
    for x in range(0, len(cle)):
        for y in range(0, len(cle)):
            if cle[x][y] == lettre:
                lettreX = x
                lettreY = y
    bigramme1 = cle[lettreX][0]
    bigramme2 = cle[4][lettreY]
    return bigramme1, bigramme2


def chiffrementTexte(texte, cle, entier):
#on parcourt le texte et on encode chaque caractère en ne prennant pas en compte les espaces.
#Le premier bigramme va dans le texte1 et le deuxieme dans le texte2, qui représentent les deux chaines de caractères
#du chiffre de colon. Ensuite on ira piocher dans les deux pour obtenir le message codé.
    texte = texte.upper()
    texteCode = ""
    texte1 = ""
    texte2 = ""
    y = 0
    i = 0
    p = 0
    for car in texte:
        if car != ' ':
            texte = texte.replace(car,'')
            bigramme1, bigramme2 = chiffrage(car, cle)
            print(bigramme1, bigramme2)
            texte1 += bigramme1
            texte2 += bigramme2
    nombre = entier
    if entier < len(texte1):
        while y < len(texte1)*2:
            while i < nombre:
                texteCode += texte1[i]
                i +=1
                y += 1
                if i == len(texte1):
                    break
            while p < nombre:
                texteCode += texte2[p]
                y += 1
                p += 1
                if p == len(texte1):
                    break
            nombre = nombre + entier
    else:
        for i in range(len(texte1)):
            texteCode += texte1[i]
        for i in range(len(texte1)):
            texteCode += texte2[i]
    i = 5
    while i < len(texteCode):
        texteCode = texteCode[:i] + ' ' + texteCode[i:]
        i = i + 6
    print(texteCode)


def dechiffrage(bigramme1, bigramme2, cle):
#meme principe que pour le chiffrage, sauf qu'ici on récupère les 2 bigrammes et on récupère leur coordonné X ou Y
#pour obtenir la lettre décodée.
    lettreX = 0
    lettreY = 0
    for x in range(0, len(cle)):
        for y in range(0, len(cle)):
            if cle[x][y] == bigramme1:
                lettreX = x
            if cle[x][y] == bigramme2:
                lettreY = y
    return cle[lettreX][lettreY]

def dechiffrementTexte(texte, cle, entier):
#
    texte = texte.upper()
    texteDechiffre = ""
    texte1 = ""
    texte2 = ""
    for car in texte:
        if car == ' ':
            texte = texte.replace(car, '')
    y = 0
    nombre = entier
    if entier < len(texte):
        while y < len(texte):
            while y < nombre:
                texte1 += texte[y]
                y += 1
                if y == len(texte) - entier +1:
                    break
            nombre = nombre + entier
            while y < nombre:
                texte2 += texte[y]
                y += 1
                if y == len(texte):
                    break
            nombre = nombre + entier
    else:
        for i in range(0,len(texte)//2):
            texte1 += texte[i]
        for i in range(len(texte)//2, len(texte)):
            texte2 += texte[i]
    for i in range(len(texte1)):
        caractere = dechiffrage(texte1[i], texte2[i], cle)
        texteDechiffre += caractere
    print(texteDechiffre)

#Pour modifier une clé, merci de bien vouloir modifier les lignes qui sont placé en mode commentaire.
# Par défaut il s'agit de la clé donné avec l'énoncé. Mettez la ligne cle = "service academique" en commentaire
#et dé-commentez les 2 lignes qui suivent pour obtenir la clé qui m'était demandé.

cle = "service académique"
#cle = open(fichierCle, "r")
#cle = cle.read()
cle = Cle(cle)

#Pour modifier un chiffre, merci de bien vouloir modifier la ligne : cle = open(fichier, "r") où fichier est le
#fichier que vous désirez comme chiffre. Par défaut il s'agit du chiffre donné avec l'énoncé.

fichierChiffre = "chiffreColon.txt"
chiffre = open(fichierChiffre, 'r')
chiffre = chiffre.read()


dechiffrementTexte(chiffre, cle, 7)
