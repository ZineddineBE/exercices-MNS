# Une pointe est constituée d’une tête symbolisée par le caractère « _ » et d’une tige symbolisée par le
# caractère « | ». La dimension d’une pointe est la longueur de sa tige, qui correspond au nombre de
# caractères « | » présents.
# Ainsi :
# _
# |
# |
# |
# |
# est une pointe de dimension 4.
# L’objectif est d’afficher des pointes d’une dimension donnée.
# Écrire un algorithme affichant p pointes (côte à côte) de dimension d.

p = int(input("Saisissez le nombre de pointe : \n"))

d = int(input("Saisissez la dimension des pointes : \n"))

print("_ "*p, "\n")

for i in range(d):
    print("| "*p, "\n")


