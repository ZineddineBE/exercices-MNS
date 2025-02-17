# Ce jeu se passe entre deux joueurs. Ils montrent en même temps une main qui désigne un certain
# nombre. Le gagnant se détermine par la procédure suivante :
# — prendre connaissance du nombre de doigts de A,
# — prendre connaissance du nombre de doigts de B,
# — calculer la somme de ces deux nombres,
# — si la somme est paire, A est le gagnant,
# — si la somme est impaire, B est le gagnant.

print("=== Jeu qui additione le nombre de doigts d'une main que 2 joueurs montrent. Si la somme est paire le premier joueur gagne, si elle est impaire le second gagne ===")

nombre_doigts_premier_joueur = int(input("Combien de doigts le premier joueur montre ? "))
nombre_doigts_second_joueur = int(input("Combien de doigts le second joueur montre ? "))

somme_doigts = nombre_doigts_premier_joueur + nombre_doigts_second_joueur

if (somme_doigts%2 == 0):
    print("Le premier joueur gagne, bravo !")
else:
    print("Le second joueur gagne, bravo !")

print("=== FIN DU PROGRAMME ===")