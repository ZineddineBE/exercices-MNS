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

def entree_foret_magique():

    print(f"{color.PURPLE}🌲 Bienvenue dans la Forêt Enchantée.{color.END} 🌲\n")
    chemin = int(input(f"{color.BOLD}Deux chemins s'offrent à toi.\nChoisis 1 pour le sentier sombre.\nChoisis 2 pour le sentier éclairé.{color.END}\n"))

    if (chemin == 1):
        print("Tu avances prudemment, mais tu entends un bruit étrange venant des arbres. 🔊\n")
        choix = int(input(f"{color.BOLD}Tu as deux choix.\nChoisis 1 si tu veux t'arrêter et chercher à identifier la source du bruit.\nChoisis 2 si tu veux continuer à avancer rapidement en espérant que cela ne te suive pas.{color.END}\n"))
        if (choix == 1):
            print(f"{color.RED}C'était un piège ! Un groupe de brigands t'attrape et te vole tout ce que tu possèdes. Tu as échoué !{color.END} 💀")
        elif (choix == 2):
            print(f"{color.GREEN}Bonne décision ! Tu as évité le piège et tu continues ton chemin.{color.END} 👏\n")
            riviere_magique()

    elif (chemin == 2):
        print("Tu marches tranquillement, mais soudain, un loup-garou apparaît. 🐺\n")
        choix = int(input(f"{color.BOLD}Tu as deux choix.\nChoisis 1 si tu veux courir vers un grand arbre pour te cacher.\nChoisis 2 si tu veux te battre avec une épée que tu trouves par terre.{color.END}\n"))
        if (choix == 1):
            print(f"{color.RED}Malheureusement, le loup-garou te rattrape. Tu n'as pas été assez rapide. Fin de l'aventure.{color.END} 💀")
        elif (choix == 2):
            print(f"{color.GREEN}Incroyable ! Tu as réussi à le vaincre, et tu continues ta route.{color.END} 👏\n")
            riviere_magique()

def riviere_magique():

    print(f"{color.CYAN}🏞️ Bienvenue à la rivière magique.{color.END} 🏞️\n")
    option = int(input(f"{color.BOLD}Après avoir évité le danger, tu arrives devant une rivière. Deux options s'offrent à toi :\nChoisis 1 si tu veux traverser la rivière à la nage.\nChoisis 2 si tu veux suivre la rivière en espérant trouver un pont plus loin.{color.END}\n"))

    if (option == 1):
        print(f"{color.RED}Mauvais choix. L'eau de la rivière est empoisonnée. Fin de l'aventure.{color.END} 💀")
    elif (option == 2):
        print(f"{color.GREEN}Bravo ! Tu trouves un pont après quelques minutes de marche.{color.END} 👏\n")

        print(f"{color.DARKCYAN}🌉 Bienvenue au pont maudit.{color.END} 🌉\n")
        reponse = int(input(f"{color.BOLD}Tu arrives finalement à un vieux pont en bois, mais une étrange créature apparaît et tedit que tu dois résoudre une énigme pour traverser.\nL'énigme est la suivante :\n\"Je suis léger comme une plume, mais personne ne peut me tenir longtemps. Qui suis-je ?\"\nTrois réponses te sont proposées:\nRéponse 1 : \"Le souffle.\"\n\nRéponse 2 : \"L'eau.'\"\n\nRéponse 3 : \"L'ombre.\"{color.END}\n"))

        if (reponse == 1):
            print(f"{color.GREEN}Félicitations ! La créature te laisse passer, et tu continues ta quête.{color.END} 👏\n")

            #Sortie de la forêt :
            option = int(input(f"{color.BOLD}Après avoir traversé le pont, tu aperçois enfin la sortie de la forêt. Cependant, undernier choix crucial s'impose :\nChoisis 1 si tu veux prendre un raccourci à travers un champs de fleurs toxiques.\nChoisis 2 si tu veux suivre le sentier principal qui est plus long mais sûr.{color.END}\n"))

            if (option == 1):
                print(f"{color.RED}Le champ de fleurs toxiques t'endort à jamais.\nFin de l'aventure...{color.END} 💀")
            elif (option == 2):
                print(f"{color.GREEN}🏆 FÉLICITATIONS ! Tu sors enfin de la forêt enchantée, sain et sauf.{color.END} 🏆\n")
            
        elif (reponse == 2 or reponse == 3):
            print(f"{color.RED}Mauvaise réponse. La créature te jette dans la rivière et tu échoues.{color.END} 💀")

entree_foret_magique()


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#CORRECTION : Utilisation du booléen game_over / import os.system et utilisation de system("cls") pour clear la console après chaque choix

# from os import system

# print("Bienvenue dans la Forêt Enchantée.")
# chemin = int(input("Deux chemins s'offrent à toi. Choisis 1 pour le sentier sombre, ou 2 pour le sentier éclairé : "))
# system("cls")

# game_over = False

# if chemin == 1:
#     print("Tu entends un bruit étrange.")
#     action = int(input("Que fais-tu ? 1 : T'arrêter pour écouter. 2 : Continuer rapidement. "))
#     system("cls")
    
#     if action == 1:
#         print("C'était un piège ! Les brigands t'ont attrapé. Fin de l'aventure.")
#         game_over = True
#     elif action == 2:
#         print("Tu as évité le danger et tu continues ta route.")
#         # Continuer l'aventure...
# elif chemin == 2:
#     print("Un loup-garou apparaît !")
#     action = int(input("Que fais-tu ? 1 : Courir pour te cacher. 2 : Te battre avec une épée trouvée par terre. "))
#     system("cls")
#     if action == 1:
#         print("Le loup-garou t'a rattrapé. Fin de l'aventure.")
#         game_over = True
#     elif action == 2:
#         print("Tu as vaincu le loup-garou et continues ta route.")
        
        
# # if (chemin == 1 or chemin == 2) and action == 2: 
# # on peut continer
    
# if not game_over: # game_over == False
#     print("Tu arrives à la rivière magique.")
#     option = int(input("Deux options s'offrent à toi. Choisis 1 pour traverser la ribvière à la nage, ou 2 pour suivre la rivière dans l'espoir de trouver un pont  : "))
#     system("cls")
#     if option == 1:
#         print("Mauvais choix ! La rivière est empoisonnée.. Fin de l'aventure")
#         game_over = True
#     elif option == 2:
#         print("Bravo ! Tu trouves un pont après quelques minute de marche.")
        
#         system("cls")
        
#         print("Tu arrives finalement à un vieux pont en bois, mais une étrange créature apparaît et te dit que tu dois résoudre une énigme pour traverser. L'énigme est la suivante : \"Je suis léger comme une plume, mais personne ne peut me tenir longtemps. Qui suis-je ?\"")
#         print("Réponse 1 : Le souffle.")
#         print("Réponse 2 : L'eau.")
#         print("Réponse 3 : L'ombre.")
#         reponse = int(input("Votre réponse 1, 2 ou 3 : "))
#         system("cls")
#         if reponse == 1:
#             print("Félicitations ! La créature te laisse passer, et tu continues ta quête.")
            
#             print("Après avoir traversé le pont, tu aperçois enfin la sortie de la forêt. Cependant, un dernier choix crucial s'impose :")
#             option = int(input("Deux options s'offrent à toi. Choisis 1 pour prendre un raccourcis par le champ de fleurs toxiques, ou 2 pour uivre le sentier principal, plus long mais sûr. : "))
#             system("cls")
            
#             if option == 1:
#                 print("Le champ de fleurs toxiques t'endort à jamais. Fin de l'aventure.")
#             elif option == 2:
#                 print("Félicitations ! Tu sors enfin de la forêt enchantée, sain et sauf.");
#         else:
#             print("Mauvaise réponse. La créature te jette dans la rivière et tu échoues.")
            
from os import system
from time import sleep

# while True:
#     print("->")
#     sleep(0.2)
#     system("cls")
#     print(" ->")
#     sleep(0.2)
#     system("cls")
#     print("  ->")
#     sleep(0.2)
#     system("cls")
#     print("   ->")
#     sleep(0.2)
#     system("cls")
#     print("    ->")
#     sleep(0.2)
#     system("cls")
    
#     for i in range(0,100):
#         print(i * " " + "→")
#         sleep(0.05)
#         system("cls")
        