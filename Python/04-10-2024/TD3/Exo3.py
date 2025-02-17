# Saisissez un nombre compris entre 1 et 10. En cas d’erreur de saisie, il y a affichage d’un message «
# Valeur non permise ». Si le nombre est égal au nombre magique connu du programme, il affiche «
# Gagné » sinon il affiche un message « Trop petit » ou « Trop grand » suivant la valeur saisie.
# (reprise de « Chiffre magique 1 » pour utiliser des boucles)

import random

nombre = 0
nb_magique = random.randint(1,10)
nb_essai = 0

while(nombre!=nb_magique):

    nombre = int(input("Saisissez un nombre entre 1 et 10 :\n"))

    if (nombre > 10 or nombre < 1):
        print("Valeur non permise")
    elif (nombre < nb_magique):
        print("Trop petit !")
    else:
        print("Trop grand !")
    nb_essai += 1
    
print(f"Vous avez gagné en {nb_essai} essais !")

