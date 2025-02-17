#Calculez la moyenne des notes d’un élève après avoir saisi les notes de français, de math, de
#géométrie et d’informatique. Il faut tenir compte de coefficients de pondération par matière qui
#seront saisis eux aussi.

print("=== CALCUL DE LA MOYENNE D'UN ELEVE EN PRENANT EN COMPTE DES COEFFICIENTS ===")

note_francais = float(input("Quelle est la note de français (/20) ? "))
coeff_francais = int(input("Quelle est le coefficient de la note de français (/20) ? "))

note_math = float(input("Quelle est la note de mathématique (/20) ? "))
coeff_math = int(input("Quelle est le coefficient de la note de mathématique (/20) ? "))

note_geometrie = float(input("Quelle est la note de géométrie (/20) ? "))
coeff_geometrie = int(input("Quelle est le coefficient de la note de geometrie (/20) ? "))

note_info = float(input("Quelle est la note d'informatique (/20) ? "))
coeff_info = int(input("Quelle est le coefficient de la note d'informatique (/20) ? "))

moyenne_note = round((note_francais*coeff_francais + note_math*coeff_math + note_geometrie*coeff_geometrie + note_info*coeff_info)/(coeff_francais + coeff_math + coeff_geometrie + coeff_info), 1)

print(f"La moyenne des notes est de {moyenne_note}/20.")

print("=== FIN DU PROGRAMME ===")