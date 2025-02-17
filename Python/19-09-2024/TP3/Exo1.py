# 1. Écrire un script Python qui demande un nombre à l'utilisateur et affiche s'il est positif, négatif ou nul.

print("=== PROGRAMME QUI TEST SI UN NOMBRE EST POSITIF, NEGATIF OU NUL ===")

def verif_Valeur():
    number = int(input("Choisissez un nombre : "))
    if (number == 0):
        print(f"{number} est un nombre nul")
    elif (number < 0):
        print(f"{number} est un nombre négatif")
    else:
        print(f"{number} est un nombre positif")

verif_Valeur()

print("=== FIN DU PROGRAMME ===")
