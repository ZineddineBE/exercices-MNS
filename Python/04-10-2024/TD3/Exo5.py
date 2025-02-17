# On se propose de calculer la moyenne des notes d’un élève pour certaines matières ; français,
# maths, géographie et informatique.
# Pour chacune de ces matières, il faudra saisir un coefficient de pondération compris entre 1 et 10.
# Calculez la moyenne en tenant compte des coefficients de pondération.
# Affichez une appréciation :
# Si la moyenne est comprise entre 16 et 20, la mention est « Très bien ».
# Si la moyenne est comprise entre 12 et 16, la mention est « Bien ».
# Si la moyenne est comprise entre 8 et 12, la mention est « Assez bien ».
# Si la moyenne est comprise entre 4 et 8, la mention est « Insuffisant ».
# Si la moyenne est comprise entre 0 et 4, la mention est « Nul ».

# Il faut contrôler que les notes sont comprises entre 0 et 20 et que les coefficients sont compris
# entre 1 et 10. (reprise de l’exercice 9 feuille niveau II pour utiliser des boucles)

matiere = ["français", "maths", "géographie", "informatique"]

notes = []
coefficients = []

somme_coeff = 0

for i in range(len(matiere)):
    note = float(input(f"Saisir la note de {matiere[i]} (/20):\n"))
    while (note < 0 or note > 20):
        print("Note invalide, elle doit être comprise entre 0 et 20")
        note = float(input(f"Saisir la note de {matiere[i]} (/20):\n"))
    else:
        notes.append(note)
    
    coeff = int(input(f"Saisir le coefficient de {matiere[i]} (/10):\n"))

    while (coeff < 0 or coeff > 10):
        print("Coefficient invalide, il doit être comprise entre 0 et 10")
        coeff = float(input(f"Saisir le coefficient de {matiere[i]} (/10):\n"))
    else:
        coefficients.append(coeff)

for i in range(len(coefficients)):
    somme_coeff = somme_coeff + coefficients[i]
    
moyenne = (notes[0] * coefficients[0] + notes[1] * coefficients[1] + notes[2] * coefficients[2] + notes[3] * coefficients[3])/somme_coeff

print(round(moyenne, 1))


if (moyenne >= 16 and moyenne <= 20):
    print("Mention : Très bien !")
elif (moyenne >= 12):
    print("Mention : Bien !")
elif (moyenne >= 8):
    print("Mention : Assez bien !")
elif (moyenne >= 4 ):
    print("Mention : Insuffisant !")
elif (moyenne >= 0):
    print("Mention : Nul !")
else:
    print("Moyenne incorrect")