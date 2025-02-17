# 5. Écrire un script qui prend un nombre en entrée et affiche "pair" ou "impair".

print("=== PROGRAMME QUI AFFICHE SI LE NOMBRE EST PAIR OU IMPAIR ===")

def pair_impair(nombre):
    if (nombre % 2 == 0):
        print(f"Le nombre {nombre} est pair.")
    else:
        print(f"Le nombre {nombre} est impair.")

pair_impair(0)

print("=== FIN DU PROGRAMME ===")
