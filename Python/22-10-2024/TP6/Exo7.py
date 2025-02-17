# Créez une liste d'entiers comprenant des nombres positifs et négatifs.
# 2. Écrivez une fonction qui compte combien de nombres positifs et combien de nombres
# négatifs se trouvent dans la liste.
# 3. Affichez le nombre total de valeurs positives et négatives.

import random

d = random.randint(1, 20)
liste = []

for i in range(d):
    liste.append(random.randint(-50, 50))

def negatif(array):
    liste_negatifs = []
    for i in range(len(array)):
        if array[i] < 0:
            liste_negatifs.append(array[i])
    print(f"La liste des nombres négatifs : {liste_negatifs}")

def positif(array):
    liste_positifs = []
    for i in range(len(array)):
        if array[i] > 0:
            liste_positifs.append(array[i])
    print(f"La liste des nombres positifs : {liste_positifs}")

print(f"La liste d'entiers générée aléatoirement : {liste}")
negatif(liste)
positif(liste)