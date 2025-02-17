#Tous les enfants qui ont moins de 3 ans doivent recevoir une palette de petits pots. Saisissez l’année
#de naissance et calculez si le bébé a gagné une palette ou pas.

print("=== PROGRAMME QUI CALCULE L'AGE D'UN ENFANT EN FONCTION DE SON ANNEE DE NAISSANCE, S'IL A MOINS DE 3 ANS IL GAGNE UNE PALETTE DE PETITS POTS ===")

annee_naissance = int(input("Quelle est l'année de naissance de l'enfant ? "))
annee_actuelle = int(input("Quelle est l'année actuelle ? "))

age = annee_actuelle - annee_naissance

if (age < 3):
    print("Le bébé gagne une palette de petits pois !")
else:
    print("L'enfant est trop agé pour gagner une palette de petits pois.")

print("=== FIN DU PROGRAMME ===")