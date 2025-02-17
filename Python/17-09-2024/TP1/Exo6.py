#Écrire un algorithme qui calcul le prix TTC à partir d’un prix HT et d’une TVA de 20 % (prestation de service en France).

print("=== JE CALCULE LE PRIX AVEC LA TVA (20%) ===")

prix_HT = float(input("Quel est le prix HT (en euros) ? "))

print("Le prix TTC de", prix_HT, "est de", round(prix_HT*1.2, 2), "€")

print("=== FIN DU PROGRAMME ===")
