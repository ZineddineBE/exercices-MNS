# 1. Créez une liste d'entiers aléatoires.
# 2. Écrivez deux fonctions : l’une pour extraire tous les nombres pairs de la liste, l’autre
# pour extraire les nombres impairs.
# 3. Affichez les listes de nombres pairs et impairs.

import random

d = random.randint(1, 20)
liste = []

for i in range(d):
    liste.append(random.randint(0, 50))

def pair(array):
    liste_pair = []
    for i in range(len(array)):
        if array[i] % 2 == 0:
            liste_pair.append(array[i])
    print(f"La liste des nombres pairs : {liste_pair}")

def impair(array):
    liste_impair = []
    for i in range(len(array)):
        if array[i] % 2 == 1:
            liste_impair.append(array[i])
    print(f"La liste des nombres impairs : {liste_impair}")

print(f"La liste d'entiers générée aléatoirement : {liste}")
pair(liste)
impair(liste)