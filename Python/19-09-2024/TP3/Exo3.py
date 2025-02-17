# 3. Écrire un script qui prend trois nombres en entrée et affiche le plus grand des trois.

print("=== PROGRAMME QUI AFFICHE LE PLUS GRAND NOMBRE DES TROIS ===")

def plus_grand(a, b, c):
    if (a > b and a > c):
        print(f"Le plus grand des trois est {a}")
    elif (b > a and b > c):
        print(f"Le plus grand des trois est {b}")
    else:
        print(f"Le plus grand des trois est {c}.")

plus_grand(2, 57, 8)

print("=== FIN DU PROGRAMME ===")
