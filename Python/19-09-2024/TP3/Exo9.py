# 9. Écrire un script qui demande deux nombres et affiche "Plus grand", "Plus petit" ou "Égal" selon leur comparaison.

print("=== PROGRAMME QUI COMPARE DEUX NOMBRE ET AFFICHE SI LE PREMIER EST PLUS GRAND, PLUS PETIT OU EGAL ===")

def comparaison_nombre():
    nombre1 = int(input("Premier nombre : "))
    nombre2 = int(input("Deuxième nombre : "))

    if (nombre1 == nombre2):
        print(f"Les nombres {nombre1} et {nombre2} sont ÉGAUX !")
    elif (nombre1 < nombre2):
        print(f"{nombre1} est PLUS PETIT que {nombre2} !")
    else:
        print(f"{nombre1} est PLUS GRAND que {nombre2} !")

comparaison_nombre()

print("=== FIN DU PROGRAMME ===")
