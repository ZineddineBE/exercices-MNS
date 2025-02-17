#Saisissez le prix unitaire HT d’un produit et la quantité commandée. Calculez le montant HT de la commande, appliquez une remise de 15% et calculez le prix TTC après avoir saisi le taux de TVA.

print("=== CALCUL D'UN PRIX REMISEE TTC EN EUROS ===")

prix_unitaire_HT = int(input("Quel est le prix unitaire HT ? "))
qt_commandee = int(input("Quel est la quantité commandée ? "))

montant_commande_HT = prix_unitaire_HT*qt_commandee

remise_quinze_pourcent = montant_commande_HT*0.85

prix_TTC = remise_quinze_pourcent*1.20

print("Le montant HT de la commande est de", montant_commande_HT , "€.")

print("Le montant TTC après remise de 15 % est de", prix_TTC, "€")

print("=== FIN DU PROGRAMME ===")
