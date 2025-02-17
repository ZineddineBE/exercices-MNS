# Écrire un programme permettant de gérer la liste des stagiaires d'une promo, le programme doit exécuter les actions suivantes :
# Demander à l'utilisateur le nom de la promo
# Lui demander de saisir les noms, prénoms, âge pour chaque stagiaire tant que l'utilisateur n'a pas terminé sa saisie 
# ("Voulez-vous ajouter un autre stagiaire (O/N) ?)
# Afficher un menu permettant : d'afficher tous les stagiaires, d'afficher uniquement les prénoms, d'afficher uniquement les noms, 
# afficher le stagiaire le plus vieux, afficher le stagiaire le plus jeune
# Utilisez des fonctions !.

def creation_liste_stagiaires(promo):
    promo = []
    reponse = ''
    cpt = 1
    while reponse != 'N':
        stagiaire = []
        nom = input(f"Quel est le nom du stagiaire numéro {cpt} ?\n")
        prenom = input(f"Quel est le prenom de monsieur ou madame {nom} ?\n")
        age = int(input(f"Quel est l'âge de {prenom} {nom} ?\n"))
        stagiaire.extend([nom, prenom, age])
        reponse = input("Voulez-vous ajouter un autre stagiaire (O/N) ?\n")
        cpt += 1
        promo.append(stagiaire)
    return promo

def afficher_stagiaires(promo, nom_promo):
    print(f"--------------Liste des stagiaires de {nom_promo}--------------\n")
    for i in range(len(promo)):
        print(f"Prénom : {promo[i][1]} / Nom : {promo[i][0]} / Age : {promo[i][2]}")

def afficher_prenom_stagiaires(promo, nom_promo):
    print(f"--------------Liste des prénoms des stagiaires de {nom_promo}--------------\n")
    for i in range(len(promo)):
        print(f"{promo[i][1]}\n")

def afficher_nom_stagiaires(promo, nom_promo):
    print(f"--------------Liste des noms des stagiaires de {nom_promo}--------------\n")
    for i in range(len(promo)):
        print(f"{promo[i][0]}\n")

def afficher_plus_vieux_stagiaire(promo):
    liste_age = []
    index_age_max = 0
    for i in range(len(promo)):
        liste_age.append(promo[i][2])
    index_age_max = liste_age.index(max(liste_age))
    print(f"Le stagiaire le plus vieux a {max(liste_age)} ans, c'est {promo[index_age_max][1]} {promo[index_age_max][0]}")

def afficher_plus_jeune_stagiaire(promo):
    liste_age = []
    index_age_min = 0
    for i in range(len(promo)):
        liste_age.append(promo[i][2])
    index_age_min = liste_age.index(min(liste_age))
    print(f"Le stagiaire le plus jeune a {min(liste_age)} ans, c'est {promo[index_age_min][1]} {promo[index_age_min][0]}")

def menu(promo, nom_promo):
    menu = [
        [1, "afficher tous les stagiaires"],
        [2, "afficher uniquement les prénoms"],
        [3, "afficher uniquement les noms des stagiaires"],
        [4, "afficher le stagiaire le plus vieux"],
        [5, "afficher le stagiaire le plus jeune"],
    ]
    print("--------------MENU--------------\n")
    choix = 0
    fin = ""
    while fin != "N":
        for i in range(len(menu)):
            print(f"Choix {menu[i][0]} : {menu[i][1]}")
        
        choix = int(input("Quel est votre choix ?\n"))
        if choix == 1:
            afficher_stagiaires(promo, nom_promo)
        elif choix == 2:
            afficher_prenom_stagiaires(promo, nom_promo)
        elif choix == 3:
            afficher_nom_stagiaires(promo, nom_promo)
        elif choix == 4:
            afficher_plus_vieux_stagiaire(promo)
        elif choix == 5:
            afficher_plus_jeune_stagiaire(promo)
        
        fin = input("Voulez-vous afficher autre chose (O/N) ?\n")

promo = input("Quelle est le nom de la promo ?\n")
liste_promo = creation_liste_stagiaires(promo)
menu(liste_promo, promo)

