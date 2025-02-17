# Saisissez les notes d’un élève pour les matières suivantes : français, mathématiques, géographie et
# informatique.
# Si la moyenne est comprise entre 16 et 20, la mention est « Très bien ».
# Si la moyenne est comprise entre 12 et 16, la mention est « Bien ».
# Si la moyenne est comprise entre 8 et 12, la mention est « Assez bien ».
# Si la moyenne est comprise entre 4 et 8, la mention est « Insuffisant ».
# Si la moyenne est comprise entre 0 et 4, la mention est « Nul ».

print("=== CALCUL DE LA MOYENNE DES NOTES SUR 20 ET AFFICHAGE DE L'APPRECIATION EN FONCTION DE LA NOTE ===")

note_francais = int(input("Quelle est la note de français (/20) ? "))
note_math = int(input("Quelle est la note de math (/20) ? "))
note_geometrie = int(input("Quelle est la note de géométrie (/20) ? "))
note_info = int(input("Quelle est la note d'informatique (/20) ? "))

moyenne_note = (note_francais + note_math + note_geometrie + note_info)/4

print(f"La moyenne des notes est de {moyenne_note}")

if (moyenne_note >= 16 and moyenne_note <= 20):
    print("Mention : Très bien !")
elif (moyenne_note >= 12):
    print("Mention : Bien !")
elif (moyenne_note >= 8):
    print("Mention : Assez bien !")
elif (moyenne_note >= 4 ):
    print("Mention : Insuffisant !")
elif (moyenne_note >= 0):
    print("Mention : Nul !")
else:
    print("Moyenne incorrect")

print("=== FIN DU PROGRAMME ===")