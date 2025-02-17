def chiffrement_cesar(word, key):

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    mot_chiffre = ""

    for i in range(len(word)):
        indice = alphabet.index(word[i])
        if indice + key >= len(alphabet):
            indice = (indice - len(alphabet)) + key
            lettre = alphabet[indice]
        else:
            lettre = alphabet[indice+key]

        mot_chiffre = mot_chiffre + lettre
    return mot_chiffre

def dechiffrement_cesar(word, key):

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    mot_dechiffre = ""

    for i in range(len(word)):
        indice = alphabet.index(word[i])
        if indice + key >= len(alphabet):
            indice = (indice - len(alphabet)) - key
            lettre = alphabet[indice]
        else:
            lettre = alphabet[indice-key]

        mot_dechiffre = mot_dechiffre + lettre
    return mot_dechiffre


prenom = input("Saisir le mot que vous voulez chiffrer :\n")
cle = int(input("Saisir la clé de chiffrement :\n"))
mot_chiffre = chiffrement_cesar(prenom, cle)
print(f"Le mot chiffre est : {mot_chiffre}")

print("Le mot chiffre est :", dechiffrement_cesar(mot_chiffre, cle))
