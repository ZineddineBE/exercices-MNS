# Saisissez un nombre au clavier et affichez un des messages « Positif », « Nul », ou « Négatif »
# suivant sa valeur.

print("=== PROGRAMME QUI INDIQUE SI LE NOMBRE SAISI EST POSITIF, NUL OU NEGATIF ===")

nombre = int(input("Quel est le nombre choisi ? "))

if (nombre == 0):
    print("Le nombre saisi est nul")
elif (nombre > 0):
    print("Le nombre saisi est positif")
else:
    print("Le nombre saisi est négatif")

print("=== FIN DU PROGRAMME ===")