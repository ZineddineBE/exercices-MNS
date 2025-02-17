# Exercice 1 : Gestion d'une bibliothèque
# Créez une classe Python appelée "Livre" qui représente un livre avec les propriétés suivantes :
# Titre
# Auteur
# Année de publication
# Ensuite, créez une classe "Bibliotheque" qui peut stocker une liste de livres. La classe "Bibliotheque" devrait avoir les méthodes suivantes :
# ajouter_livre(livre): pour ajouter un livre à la bibliothèque.
# rechercher_livre(titre): pour rechercher un livre par titre et renvoyer les détails du livre s'il est présent.
# afficher_livres(): pour afficher la liste de tous les livres dans la bibliothèque.
# Créez une instance de la classe "Bibliotheque" et effectuez des opérations telles que l'ajout de livres, la recherche de livres et l'affichage de la liste de livres.

from livre import Livre
from bibliotheque import Bibliotheque

bibliotheque = Bibliotheque()

livre1 = Livre("Les Fleurs du Mal", "Charles Baudelaire", "21 juin 1857")

livre2 = Livre("Le Parfum", "Patrick Süskind", "1985")

livre3 = Livre("Les Misérables", "Victor Hugo", "1862")


bibliotheque.ajouter_livre(livre1)
bibliotheque.ajouter_livre(livre2)
bibliotheque.ajouter_livre(livre3)


bibliotheque.afficher_livres()

print(bibliotheque.rechercher_livre("Les Misérables", "Victor Hugo"))