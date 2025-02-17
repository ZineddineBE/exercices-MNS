import random
import time

# Pour ajouter de la couleur, mettre en gras ou souligner du texte
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def tour_maudite():
    print(f"{color.PURPLE}{color.BOLD}{color.UNDERLINE}LA TOUR MAUDITE{color.END}\n")

    print("Tu es un aventurier emprisonné dans une tour maudite, où des énigmes et des pièges complexes t'attendent à chaque étage.\nTon objectif est de t'échapper de la tour en atteignant son sommet.\nPour cela, tu devras résoudre des énigmes et prendre des décisions stratégiques.\nTes choix seront déterminants pour ta survie et ta libération.\n")
    print(f"{color.BOLD}{color.UNDERLINE}Début de l'aventure{color.END}\n")

    arme = int(input(f"Tu trouves 3 armes dans ta cellule.\n{color.BOLD}Choisis 1 pour l'épée rouillée (attaque = 10 / défense = 2).\nSaisis 2 pour la baguête magique abîmée (attaque = 6 / défense = 5).\nSaisis 3 pour le bouclier en bois (attaque = 3 / défense = 8){color.END}\n"))

    if (arme == 1):
        print(f"{color.BOLD}Tu as choisi l'épée rouillée !{color.END} 🗡\n")
        attaque = 10
        defense = 2

    elif (arme == 2):
        print(f"{color.BOLD}Tu as choisi la baguette magique abîmée !{color.END} 🥖\n")
        attaque = 6
        defense = 5

    elif (arme == 3):
        print(f"{color.BOLD}Tu as choisi le bouclier en bois !{color.END} 🛡\n")
        attaque = 3
        defense = 8

    print(f"{color.PURPLE}{color.BOLD}{color.UNDERLINE}Premier étage – La porte verrouillée{color.END}\n")

    print("Après avoir pris ton arme, tu montes au premier étage et trouves une porte fermée.\nTrois mécanismes sont disponibles pour l'ouvrir :\nMécanisme 1 : Résoudre une énigme mathématique (si la réponse est correcte, la porte s'ouvre).\nMécanisme 2 : Forcer la porte avec ton arme (la réussite dépend de ton arme).\nMécanisme 3 : Tenter de trouver une clé cachée dans la pièce (la clé est cachée, il faut de la chance pour la trouver)\n\n")
    mecanisme = int(input(f"{color.BOLD}Saisissez 1 pour le premier mécanisme.\nSaisissez 2 pour le second mécanisme.\nSaisissez 3 pour le troisième mécanisme{color.BOLD}\n"))

    if (mecanisme == 1):
        réponse = int(input(f"{color.BOLD}Combien font 8 + 3 * 2 ?.\nSi la réponse est correcte, la porte s'ouvre. Sinon, le piège s'active, et l'aventure se termine.{color.END}\n"))
        if (réponse == 14):
            print(f"{color.GREEN}Bonne réponse ! La porte s'ouvre...\nEtage suivant...{color.END}")
            deuxieme_etage(attaque, defense, arme)
        else:
            print(f"{color.RED}Mauvaise réponse ! Tu actives le piège et tu meurs.\nFin de l'aventure...{color.END}")

    elif (mecanisme == 2):
        if (arme == 1):
            nombre = random.randint(1, 2)
            if (nombre == 1):
                print(f"{color.GREEN}Tu as de la chance ! La porte s'ouvre...\nEtage suivant...{color.END}\n")
                deuxieme_etage(attaque, defense, arme)
            else:
                print(f"{color.RED}Tu n'as pas de chance ! La porte ne s'ouvre pas.\nFin de l'aventure...{color.END}")

        elif (arme == 2):
            print(f"{color.RED}Mauvais choix d'arme ! Le bouclier n'est pas capable d'ouvrir la porte !\n Fin de l'aventure...{color.END}")
        
        elif (arme == 3):
            nombre = random.randint(1, 10)
            if (nombre <= 3):
                print(f"{color.GREEN}Tu as de la chance ! La porte s'ouvre...\nEtage suivant...{color.END}\n")
                deuxieme_etage(attaque, defense, arme)
            else:
                print(f"{color.RED}Mauvais choix d'arme ! La magie est instable et elle n'est pas capable d'ouvrir la porte !\n Fin de l'aventure...{color.END}")

    elif (mecanisme == 3):
        nombre = random.randint(1, 10)
        if (nombre <= 4):
            print(f"{color.GREEN}Bravo tu as trouvé la clé ! Tu peux donc ouvrir la porte...\nEtage suivant...{color.END}\n")
            deuxieme_etage(attaque, defense, arme)
        else:
            print(f"{color.RED}Tu n'as pas de chance ! Tu n'as pas réussi à trouver la clé.\nFin de l'aventure...{color.END}")
        
def fuite(arme): #20% de chance de fuir
    print(f"{color.BOLD}Tentive de fuite...{color.END}")
    fuite = random.randint(1, 10) 
    if (fuite == 1 or fuite == 2):
        print(f"{color.GREEN}Tu as de la chance, tu arrives à fuir le combat !\nEtage suivant...{color.END}\n")
        troisieme_etage(arme)
    else:
        print(f"{color.RED}Tu n'as pas de chance, tu n'arrives pas à fuir le combat !\nFin de l'aventure...{color.END}")

def deuxieme_etage(atq, df, arme):
    print(f"{color.BLUE}{color.BOLD}{color.UNDERLINE}Deuxième étage - Combat contre un garde spectrale{color.END}\n")

    print("Tu arrives au deuxième étage et fais face à un garde spectral.\n")
    print("Le garde spectral a une attaque de 8 et une défense de 6.\n")
    print(f"{color.BOLD}Combat en cours...\n{color.END}")
    loading()
    if (atq >= 6):
        print(f"{color.GREEN}Bravo ! L'attaque de ton épée est suffisante pour blesser le garde.\nEtage suivant...{color.END}\n")
        troisieme_etage(arme)
    elif (atq <= 6 and df >= 8):
        print(f"{color.GREEN}L'attaque du garde n'est pas assez puissante pour te blesser.\nEtage suivant...{color.END}\n") 
        fuite(arme)                  
    elif (atq <= 6 and df < 8):
        print(f"{color.RED}Tu n'est pas assez puissant ! Tu perds le combat. Fin de l'aventure...{color.END}")

def troisieme_etage(arme):
    print(f"{color.CYAN}{color.BOLD}{color.UNDERLINE}Troisième étage – La salle du miroir magique{color.END}\n")

    reponse = int(input(f"Au troisième étage, tu rencontres un miroir magique qui te pose une énigme et t'offre trois choix en fonction de ta réponse.\n\nL'énigme est la suivante :\n\"Je suis toujours devant toi, mais tu ne peux jamais me dépasser. Qui suis-je ?\"\n\nTrois réponses te sont proposées:\n{color.BOLD}Réponse 1 : \"Le futur.\"\n\nRéponse 2 : \"Le chemin.'\"\n\nRéponse 3 : \"Ton ombre.\"{color.END}\n"))
    if (reponse == 1):
        print(f"{color.RED}Le miroir te montre l'avenir... Tu prends peur et tu décides de faire demi-tour. Fin de l'aventure...{color.END}")
    elif (reponse == 2):
        print(f"{color.GREEN}Bonne réponse ! Le miroir t'ouvre.\nEtage suivant...{color.END}\n")
        dernier_etage(arme)
    elif (reponse == 3):
        print(f"{color.RED}Le miroir t'emprisonne dans une boucle temporelle. Fin de l'aventure...{color.END}")

def dernier_etage(arme):
    print(f"{color.DARKCYAN}{color.BOLD}{color.UNDERLINE}Dernier étage -  Le gardien du sommet{color.END}\n")
    porte = int(input(f"Au sommet de la tour, tu fais face au Gardien du Sommet, un puissant sorcier qui te lance un défi.\n{color.BOLD}Il te demande de choisir une porte parmi trois :\nPorte 1 : Une porte enflammée.\nPorte 2 : Une porte gelée.\nPorte 3 : Une porte d'ombre.{color.END}\n"))
    if ((porte == 1 and arme == 2 or porte == 1 and arme == 3) or (porte == 2 and arme == 1 or porte == 2 and arme == 2) or (porte == 3 and arme == 1 or porte == 3 and arme == 3)):
        print(f"{color.RED}Tu es emprisonné pour toujours dans la tour ! Fin de l'aventure...{color.END}")
    else:
        print(f"{color.GREEN}BRAVO ! Tu as réussi à t'échapper de la tour !{color.END}")

def loading():
    bar = [
        f" 🥊[{color.BOLD}.  {color.END}]🥊",
        f" 🥊[{color.BOLD}.. {color.END}]🥊",
        f" 🥊[{color.BOLD}...{color.END}]🥊",
        f" 🥊[{color.BOLD}.  {color.END}]🥊",
        f" 🥊[{color.BOLD}.. {color.END}]🥊",
        f" 🥊[{color.BOLD}...{color.END}]🥊",
    ]
    i = 0

    while i!=20:
        print(bar[i % len(bar)], end="\r")
        time.sleep(.4)
        i += 1

tour_maudite()


################## CORRECTION ###########################

# # Début de l'aventure : choix de l'arme
# import random

# game_over = False

# print("Bienvenue dans la tour maudite.")
# print("Choisis une arme pour commencer ton aventure :")
# print("1. Épée rouillée\n2. Baguette magique abîmée\n3. Bouclier en bois")
# arme = int(input("Fais ton choix (1, 2, ou 3) : "))

# # Initialisation des statistiques selon l'arme choisie
# if arme == 1:
#     attaque = 10
#     defense = 2
#     print("Tu as choisi l'épée. Attaque puissante, faible défense.")
# elif arme == 2:
#     attaque = 6
#     defense = 5
#     print("Tu as choisi la baguette. Magie instable.")
# elif arme == 3:
#     attaque = 3
#     defense = 8
#     print("Tu as choisi le bouclier. Grande défense, faible attaque.")

# # Premier étage : la porte verrouillée
# print("\nTu arrives à une porte fermée avec trois mécanismes pour l'ouvrir.")
# print("1. Résoudre une énigme\n2. Forcer la porte avec ton arme\n3. Chercher une clé")
# mecanisme = int(input("Quel mécanisme choisis-tu (1, 2, ou 3) ? "))

# if mecanisme == 1:
#     reponse = int(input("Combien font 8 + 3 * 2 ? "))
#     if reponse == 14:
#         print("Bonne réponse ! La porte s'ouvre.")
#     else:
#         print("Mauvaise réponse. Le piège s'active. Fin de l'aventure.")
#         game_over = True
# elif mecanisme == 2:
#     if arme == 1:  # Épée
#         print("Tu forces la porte avec l'épée.")
#         open_door = random.randint(0,1)
#         if open_door:
#             print("La porte s'ouvre !")
#         else:
#             print("La poorte ne s'ouvre pas malgré tes efforts... Fin de l'aventure.")
#             game_over = True
#     elif arme == 2:  # Baguette
#         open_door = random.random() < 0.3 # or random.randint(1,10) <= 3
#         if open_door:
#             print("Avadakedavra sur la porte TMTC !")
#         else:
#             print("La porte rest de marbre... Magie instable... Fin de l'aventure")
#             game_over = True
        
#     elif arme == 3:  # Bouclier
#         print("Le bouclier ne peut pas forcer la porte. Fin de l'aventure.")
#         game_over = True
#         # Compléter les autres conditions pour la baguette...
# elif mecanisme == 3:
#     print("Tu cherches une clé dans les coffres.")
#     find_key = random.random() < 0.4
#     if find_key:
#         print("Tu trouves la clé. La porte s'ouvre.")
#     else:
#         print("La clé est introuvable...")
#         print("La porte reste fermée... Fin de l'aventure.")
#         game_over = True
        
# # Deuxième étage
# if not game_over:
#     print("Tu arrives devant un garde spectrale.")
#     if arme == 1:
#         print("Tu fumes le garde. Easy !")
#     elif arme == 2:
#     # Compléter les autres conditions pour la baguette...
#         attaque = attaque * random.randint(1,2)
#         if attaque > 6:
#             print("Les dégâts de ton sors ont doublé ! Tu défonces le garde.")
#         else:
#             print("Aucun dégats infligés, le garde contre-attaque et te démontes... Fin de l'aventure.")
#             game_over = True
#     elif arme == 3:
#         print("Tu resistes mais tu ne pourras pas en venir à bout. Que souhaites-tu faire ?")
#         print("1. Pour fuir, 2. Pour continuer le combat")
#         choix = int(input("Alors ? "))
#         if choix == 1:
#             print("Tu fuis tel un lâche.. Mais tu survis !")
#         else:
#             print("Tu es tué. Fin de l'aventure.")
#             game_over = True
            
# # Troisième étage
# if not game_over:
#     print("Tu arrives devant un mirroir magique qui te poses une énigme :")
#     print("\"Je suis toujours devant toi, mais tu ne peux jamais me dépasser. Qui suis-je ?\"")
#     print("Réponse 1 : Le futur")
#     print("Réponse 2 : Le chemin")
#     print("Réponse 3 : Ton ombre")
#     reponse = int(input("Quelle réponse choisis-tu (1, 2, ou 3) ? "))
    
#     if reponse == 1:
#         print("Le miroir te montre un futur dangereux, et tu dois faire demi-tour. Fin de l'aventure.")
#         game_over = True
#     elif reponse == 2:
#         print("Le miroir s'ouvre et tu continues.")
#     elif reponse == 3:
#         print("Le miroir t'emprisonne dans une boucle temporelle. Fin de l'aventure.")
#         game_over = True
        
# # Quatrième étage
# if not game_over:
#     print("Tu rencontres le Gardien de Sommet. Il te demande de chosir entre 3 portes.")
#     print("Porte 1 : Une porte enflammée.")
#     print("Porte 2 : Une porte gelée.")
#     print("Porte 3 : Une porte d'ombre.")
#     choix = int(input("Quelle porte choisis-tu (1, 2, ou 3) ? "))
    
#     if choix == 1 and arme == 1:
#         print("Tu traverse la porte sans te blesser.")
#     elif choix == 2 and arme == 3:
#         print("Tu peux te protéger du froid et traverser la porte gelée.")
#     elif choix == 3 and arme == 2:
#         print("Tu peux dissiper l'ombre et traverser la porte d'ombre")
#     else:
#         print("Ton arme ne te permet de passer la porte choisie. Fin de l'aventure.")
#         game_over = True
        
        
# # Final
# if not game_over:
#     print("Tu as terminé l'aventure et tu as survécu.")
#     print("Tu sors de la tour et rentre chez toi rejoindre ta femme, ton fils et ton domaine.")
#     print("Akim, le fils du forgeron viendra te chercher...")
# else:
#     print("Tu restes emprisonné dans la tour et attendra que ton/ta prince/princesse charmant.e vienne te sauver")