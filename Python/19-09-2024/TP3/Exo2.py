# 2. Créer un script qui demande l'âge de l'utilisateur et affiche s'il est majeur ou mineur.

print("=== PROGRAMME QUI AFFICHE SI L'UTILISATEUR EST MAJEUR OU NON ===")

def majeur_ou_mineur():
    age = int(input("Quel est votre âge ? "))
    if (age >= 18):
        print("Vous êtes majeur !")
    else:
        print("Vous êtes mineur...")

majeur_ou_mineur()

print("=== FIN DU PROGRAMME ===")
