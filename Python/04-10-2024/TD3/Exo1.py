# Réalisez un jeu de dés utilisant les aiguillages conditionnels. Au démarrage du programme, il
# calcule au hasard un nombre entre 1 à 6 (utilisez la fonction suivante : valeur <— HASARD(valeur
# mini , valeur maxi)). Le programme affiche « Vous avez fait un six » et il affiche la face du dé, sur 3
# lignes, par exemple :
# «0 0»
# « 0 »
# «0 0»

import random

nombre = random.randint(1, 6)

print(f"Vous avez fait un {nombre}")

if (nombre == 1):
    print("   \n 0 \n   ")
elif(nombre == 2):
    print("  0\n   \n0  ")
elif(nombre == 3):
    print("  0\n 0 \n0  ")
elif(nombre == 4):
    print("0 0\n   \n0 0")
elif(nombre == 5):
    print("0 0\n 0 \n0 0")
else:
    print("0 0\n0 0\n0 0")