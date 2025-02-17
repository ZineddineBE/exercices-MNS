# Saisissez un montant TTC et appliquez une remise avec les conditions suivantes :
# — si le montant est compris entre 500 € et 1 000 €, le taux de remise est de 2 %,
# — si le montant est compris entre 1 000 € et 2 000 €, le taux de remise est de 5 %,
# — si le montant est supérieur à 2 000 €, le taux de remise est de 10 %.

print("=== ON APPLIQUE UNE REMISE EN FONCTION DU MONTANT TT QU'ON SAISI ===")

montant_TTC = float(input("Saisissez le montant TTC (en €) : "))

if (montant_TTC > 2000):
    prix_remise = montant_TTC*0.90
elif (montant_TTC >= 1000):
    prix_remise = montant_TTC*0.95
elif (montant_TTC >= 500):
    prix_remise = montant_TTC*0.98
else:
    prix_remise = montant_TTC

print(f"Le montant TTC après remise est de {round(prix_remise,2)}€")

print("=== FIN DU PROGRAMME ===")
