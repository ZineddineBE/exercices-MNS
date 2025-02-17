# 6. Créer un script qui demande un mois en entrée et affiche le nombre de jours dans ce mois.

print("=== PROGRAMME QUI AFFICHE LE NOMBRE DE JOURS DANS LE MOIS ===")

def nb_jours(mois):
    if (mois == "janvier" or mois == "mars" or mois == "mai" or mois == "juillet" or mois == "août" or mois == "octobre" or mois == "décembre"):
        print(f"Il y a 31 jours dans ce mois ({mois}).")
    elif (mois == "février"):
        print(f"Il y a 29 jours dans ce mois ({mois}).")
    else:
        print(f"Il y a 30 jours dans ce mois ({mois}).")

nb_jours("avril")

print("=== FIN DU PROGRAMME ===")

