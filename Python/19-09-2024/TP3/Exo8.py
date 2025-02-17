# 8. Créer un script qui demande une année et affiche si elle est bissextile ou non.

print("=== PROGRAMME QUI AFFICHE SI L'ANNEE EST BISSEXTILE OU NON ===")

def bissextile():
    annee = int(input("Quelle année voulez vous tester ? "))

    if (annee % 4 == 0):
        print(f"{annee} est une année bissextile !")
    else:
        print(f"{annee} n'est PAS une année bissextile !")

bissextile()

print("=== FIN DU PROGRAMME ===")
