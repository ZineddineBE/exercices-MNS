# 1. Créez une liste d'entiers : [1, 3, 7, 8, 7, 5, 6, 7, 9, 2] .
# 2. Écrivez une fonction qui compte combien de fois un nombre donné apparaît dans la
# liste.
# 3. Testez la fonction avec le nombre 7 .

liste = [1, 3, 7, 8, 7, 5, 6, 7, 9, 2]
cpt = 0

for i in range(len(liste)):
    if liste[i] == 7:
        cpt += 1
print(cpt)

