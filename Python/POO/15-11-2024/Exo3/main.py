# Créez une classe Python appelée "CompteBancaire" qui représente un compte bancaire
# avec les propriétés suivantes :
# Titulaire du compte
# Solde
# La classe "CompteBancaire" devrait avoir les méthodes suivantes :
# deposer(montant): pour déposer de l'argent sur le compte.
# retirer(montant): pour retirer de l'argent du compte (sous réserve que le solde soit suffisant).
# afficher_solde(): pour afficher le solde actuel du compte.


from CompteBancaire import CompteBancaire

my_CB = CompteBancaire("Zineddine BEOUCHE", 6500)

my_CB.deposer(500)
my_CB.retirer(8000)

my_CB.afficher_solde()