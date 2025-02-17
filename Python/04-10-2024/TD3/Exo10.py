# Écrire un algorithme qui demande successivement 20 nombres à l’utilisateur, et qui lui dise ensuite
# quel était le plus grand parmi ces 20 nombres.
# SANS TABLEAUX !!!

pg_nb = 0

for i in range(20):
    nb = int(input(f"Saisir le nombre {i+1} :\n"))
    if nb > pg_nb:
        pg_nb = nb

print(pg_nb)

