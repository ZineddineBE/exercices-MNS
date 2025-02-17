#Calculez la moyenne des notes d’un élève après avoir saisi les notes de français, de math, de géométrie et d’informatique.

print("=== CALCUL DE LA MOYENNE DES NOTES SUR 20 ===")

note_francais = int(input("Quelle est la note de français (/20) ? "))
note_math = int(input("Quelle est la note de math (/20) ? "))
note_geometrie = int(input("Quelle est la note de géométrie (/20) ? "))
note_info = int(input("Quelle est la note d'informatique (/20) ? "))

moyenne_note = (note_francais + note_math + note_geometrie + note_info)/4

print(f"La moyenne des notes est de {moyenne_note}")

print("=== FIN DU PROGRAMME ===")
