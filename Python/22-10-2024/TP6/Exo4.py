# 1. Créez une liste de nombres : [1, 2, 3, 4, 5] .
# 2. Multipliez chaque élément de la liste par 2.
# 3. Affichez la nouvelle liste.

liste = [1, 2, 3, 4, 5]

liste_mult = []

for i in range(len(liste)):
    liste_mult.append(liste[i]*2)
print(f"Si on multiplie chaque élément de la liste {liste} par 2, on obtient la liste {liste_mult}")