# 4. Créer un script qui calcule la moyenne de trois notes et affiche si l'étudiant a réussi (moyenne >= 10).

print("=== PROGRAMME QUI CALCUL LA MOYENNE DE TROIS NOTES ET AFFICHE SI L'ETUDIANT A REUSSI ===")

def reussite(note1, note2, note3):

    moyenne = round((note1 + note2 + note3)/3, 2)

    if (moyenne >= 10):
        print(f"Bravo, tu as réussi ! Ta moyenne est de {moyenne}/20.")
    else:
        print(f"Dommage, tu as malheureusement échoué... Ta moyenne est de {moyenne}/20 !")

reussite(8, 4, 5)

print("=== FIN DU PROGRAMME ===")
