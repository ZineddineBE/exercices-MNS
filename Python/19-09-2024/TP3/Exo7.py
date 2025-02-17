# Écrire un script qui simule un login : demander un nom d'utilisateur et un mot de passe, et afficher un message de bienvenue si les informations sont correctes.

print("=== PROGRAMME QUI SIMULE UN LOGIN ===")

def login(user, password):
    pseudo = input("Quel est votre nom d'utilisateur ? ")
    mdp = input("Quel est votre mot de passe ? ")

    if (pseudo != user):
        print("Le nom d'utilisateur est incorrecte !")
    elif (mdp != password):
        print("Les informations sont incorrectes !")
    elif (pseudo == user and mdp == password):
        print("Bienvenue !")

login("zizou", "03101998")

print("=== FIN DU PROGRAMME ===")
