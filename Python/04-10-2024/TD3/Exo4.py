# Réalisez un compteur qui affiche toutes les valeurs comprises entre une borne de départ et une
# borne d’arrivée en tenant compte d’un pas d’incrément.
# Exemple :
# Borne de départ = 3
# Borne d’arrivée = 12
# Pas = 2
# Affichage de 3 5 7 9 11

def compteur(depart, arrivee, pas):
    
    for i in range(depart, arrivee, pas):
        print(i, end=" ")

compteur(3, 12, 2)