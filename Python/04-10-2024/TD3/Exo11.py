# Réécrire l’algorithme précédent, mais cette fois-ci on ne connaît pas d’avance combien l’utilisateur
# souhaite saisir de nombres. La saisie des nombres s’arrête lorsque l’utilisateur entre un zéro.

pg_nb = 0
i_pg_nb = 0
nb = None
i = 1

while (nb != 0):
    nb = int(input(f"Saisir le nombre {i} :\n"))
    i += 1
    if nb > pg_nb:
        pg_nb = nb
        i_pg_nb = i-1

print(f"Le plus grand nombre saisi était {pg_nb} (position : {i_pg_nb})")
