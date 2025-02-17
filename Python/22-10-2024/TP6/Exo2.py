# 1. Créez une liste de nombres entiers : [10, 20, 30, 40, 50] .
# 2. Calculez et affichez la somme de tous les éléments de la liste.
# 3. Calculez et affichez la moyenne des éléments de la liste.
# 4. Trouvez et affichez le plus grand et le plus petit nombre de la liste.

from math import inf
import random


#list_int = [10, 20, 30, 40, 50]

d = random.randint(1, 20)
list_int = []

for i in range(d):
    list_int.append(random.randint(-50, 50))

somme = 0

pp_liste = inf
pg_liste = 0

for i in range(len(list_int)):
    somme += list_int[i]
    if list_int[i] < pp_liste:
        pp_liste = list_int[i]
    if list_int[i] > pg_liste:
        pg_liste = list_int[i]

print(f"La liste originale : {list_int}")
print(f"La somme des entiers de tous les éléments de la liste est de : {somme}")
print(f"La moyenne des éléments de la liste est de : {round(somme/len(list_int),2)}")
print(f"Le plus petit nombre de la liste est : {pp_liste}")
print(f"Le plus grand nombre de la liste est : {pg_liste}")
