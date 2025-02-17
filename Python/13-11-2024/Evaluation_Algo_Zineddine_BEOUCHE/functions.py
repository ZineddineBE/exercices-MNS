
# Fonction qui ajoute un produit à la liste des produits et qui retourne une liste de produits
def ajouter_produit(liste_produits):
    #Initialise le nouveau produit
    produit = []
    
    nom = input(f"Entrez le nom du produit numéro {len(liste_produits)+1} : ")
    quantite = int(input(f"Entrez la quantité du produit \'{nom}\' : "))
    prix_unitaire = float(input(f"Entrez le prix unitaire du produit \'{nom}\' (en €) : "))
    #Ajoute les informations du nouveau produit dans une liste
    produit.extend([nom, quantite, prix_unitaire])
    #Ajoute le nouveau produit à la liste des produits
    liste_produits.append(produit)
    
    return liste_produits

#Fonction qui calcule et retourne le prix total de la liste des produits en euros
def calcul_prix_total(liste_produits):
    #Initialise le prix total à 0
    prix_total = 0
    for i in range(len(liste_produits)):
        prix_total = prix_total + liste_produits[i][1] * liste_produits[i][2]
    return prix_total

#Fonction qui affiche chaque produit de la liste au format "- produit : x unités à x€/unité"
def afficher_liste_produits(liste_produits):
    print(f"--------------Liste des produits--------------\n")
    for i in range(len(liste_produits)):
        print(f"- {liste_produits[i][0]} : {liste_produits[i][1]} unités à {liste_produits[i][2]}€/unité\n")


