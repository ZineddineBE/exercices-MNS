import random
from time import *


def recherche_sequentielle(list, valeur):
    for i in range(len(list)):
        if list[i] == valeur:
            return i
    return -1
        
def recherche_binaire(list, valeur):
    check = False
    while check != True:
        list_gauche = list[:len(list)//2]
        list_droite = list[len(list)//2:]
        if list[len(list)//2] == valeur:
            return len(list)//2
        elif valeur < list[len(list)//2]:
            for i in range(len(list_gauche)):
                if list_gauche[i] == valeur:
                    return i
                check = True
        elif valeur > list[len(list)//2]:
            for i in range(len(list_droite)):
                if list_droite[i] == valeur:
                    return i+len(list_gauche)
                check = True
    return -1


taille_liste = 100000
#Création liste pour la recherche séquentielle

random_list = []        
for i in range(taille_liste):
    random_list.append(random.randint(1, 500))


#Création liste pour la recherche binaire

random_list_binaire = []        
for i in range(taille_liste):
    random_list_binaire.append(random.randint(1, 500))
random_list_binaire.sort()

# Calcul du temps d'éxécution de la recherche séquentielle

tps1_seq = time()
print(recherche_sequentielle(random_list, 250))
tps2_seq = time()
tps_total_seq = tps2_seq-tps1_seq

print("Le temps d'éxécution de la recherche séquentielle : ", tps_total_seq)

# Calcul du temps d'éxécution de la recherche binaire

tps1 = time()
print(recherche_binaire(random_list, 250))
tps2 = time()
tps_total_binaire = tps2-tps1

print("Le temps d'éxécution de la recherche binaire : ", tps_total_binaire)

#Quelle recherche est la plus rapide ?

if tps_total_binaire == tps_total_seq:
    print("Les 2 recherches sont équivalentes")
elif tps_total_binaire < tps_total_seq:
    print("La recherche binaire est plus rapide")
else:
    print("La recherche séquentielle est plus rapide")



