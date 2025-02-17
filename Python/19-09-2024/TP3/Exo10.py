# 10. Créer un script qui prend un nombre entier et affiche si ce nombre est divisible par 5 et 10.

print("=== PROGRAMME QUI AFFICHE SI UN NOMBRE EST DIVISIBLE PAR 5 OU 10 ===")

def divisible_par_5_10(nombre):
    if (nombre % 5 == 0 and nombre % 10 == 0):
        print(f"Le nombre {nombre} est divisible par 10 et par 5.")
    else:
        print(f"Le nombre {nombre} n'est PAS divisible par 10 et par 5.")

divisible_par_5_10(24)

print("=== FIN DU PROGRAMME ===")
