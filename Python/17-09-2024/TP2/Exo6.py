# Saisissez le prix HT d’un produit. Affichez les taux de TVA possibles ainsi qu’un code :
# Pour une TVA de 5,5 %, saisissez 1
# Pour une TVA de 19,6 %, saisissez 2
# Pour une TVA de 33 %, saisissez 3
# L’utilisateur saisit un code (1, 2 ou 3). Calculez le prix TTC et affichez un message : « Le prix HT
# est de 100 €, la TVA est de 19,6 % et le prix TTC est de 119,60 €. »

print("=== PROGRAMME QUI CALCULE ET AFFICHE LE HT (en €), LA TVA (en %) ET LE PRIX TTC (en €) SELON LE CODE DE TVA (1, 2 ou 3) QU'ON ENTRE ===")

prix_HT = float(input("Quel est le prix HT (en €) ? "))
print("Pour une TVA de 5,5 %, saisissez 1\nPour une TVA de 19,6 %, saisissez 2\nPour une TVA de 33 %, saisissez 3")
code_TVA = int(input("Quel est le code de TVA (1, 2 ou 3) ? "))

taux_tva = 0

if (code_TVA == 1):
    taux_tva = 5.5
elif (code_TVA == 2):
    taux_tva = 19.6
elif (code_TVA == 3):
    taux_tva = 33


if taux_tva:
    prix_TTC = prix_HT* (1+taux_tva/100)
    print(f"Le prix HT est de {prix_HT} €, la TVA est de {taux_tva} % et le prix TTC est de {round((prix_TTC),2)} €.")
else:
    print("Le code de TVA saisi est invalide, recommencez")