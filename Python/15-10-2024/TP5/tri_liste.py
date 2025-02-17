import random

def tri_croissant(list):
    liste_croissante = []

    print("Liste dans le désordre :",list)

    for i in range(len(list)):
        nbr = min(list)
        liste_croissante.insert(i, nbr)
        list.remove(min(list))
    print("La liste triée dans l'ordre croissant :",liste_croissante)

def tri_decroissant(list):
    liste_decroissante = []

    print("Liste dans le désordre :",list)

    for i in range(len(list)):
        nbr = max(list)
        liste_decroissante.insert(i,nbr)
        list.remove(max(list))
    print("La liste triée dans l'ordre décroissant :",liste_decroissante)

def liste_aleatoire(taille, nb_max):
    for i in range(len(taille)):
        max.insert(i, random.randint(0, nb_max))
    return max

random_list = []
taille_list = random.randint(0,20)

for i in range(taille_list):
    random_list.insert(i,random.randint(0,20))

tri_croissant(random_list)

for i in range(taille_list):
    random_list.insert(i,random.randint(0,20))

tri_decroissant(random_list)
