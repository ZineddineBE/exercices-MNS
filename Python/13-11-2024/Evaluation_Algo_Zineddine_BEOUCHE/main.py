#Importe le fichier qui contient les fonctions pour ajouter des nouveaux produits, afficher la liste des produits et le calcul du prix total
import functions

# Déclaration de la liste des produits
liste_produits = []

reponse = ""
#Ajout d'un nouveau produit si et seulement si l'utilisateur répond "oui" à la question
while reponse != "non":
    functions.ajouter_produit(liste_produits)
    reponse = input("Voulez-vous ajouter un autre produit ? (oui/non) : ")

#Affiche la liste des produits
functions.afficher_liste_produits(liste_produits)

#Affiche le prix total des produits
print(f"Prix total : {functions.calcul_prix_total(liste_produits)}€")
