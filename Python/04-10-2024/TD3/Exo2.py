# Demandez à saisir une date de la forme AAAA/MM/JJ (par exemple 2011/10/17) et afficher « Le
# 17 octobre 2011 est un lundi. » Pour connaitre le nom du jour, on part de la date avec :
# • A = année complète (dans l’exemple 2011),
# • M = numéro du mois (dans l’exemple 10),
# • J = numéro du jour (dans l’exemple 17).
# Si MM vaut 1 ou 2, il faut :
# • retrancher 1 à A,
# • ajouter 12 à M.
# Avec ces valeurs, on calcule un nombre N
# • N = J + ENT((13 * M + 3) / 5) + ENT(5 * A / 4) — ENT(A / 100) + ENT(A / 400)
# • N = MOD(N ; 7)
# N donne le nom du jour avec : 0 pour lundi, 1 pour mardi, ..., 6 pour dimanche

date = input("Saisissez une date au format AAAA/MM/JJ :\n")

A = int(date[0] + date[1] + date[2] + date[3]) # ou date[0:4] ou date[:4]

M = int(date[5] + date[6]) # ou date[5:7]

J = int(date[8] + date[9]) # ou date[8:10] ou date[8:]

if (M == 1 or M == 2):
    A = A - 1
    M = M + 12
    
N = J + (13 * M + 3)/5 + 5 * A / 4 - A /100 + A / 400
N = int(N % 7)

jours = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
mois = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "aout", "septembre", "octobre", "novembre", "décembre"]

print(f"Le {J} {mois[M-1]} {A} était un {jours[N]}.")