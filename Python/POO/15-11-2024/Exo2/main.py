# Exercice 2 : Gestion d'une liste de tâches
# Créez une classe Python appelée "Tache" qui représente une tâche à faire avec les propriétés suivantes :
# Description
# Date limite
# Statut (complet ou incomplet)
# Ensuite, créez une classe "ListeDeTaches" qui peut stocker une liste de tâches. La classe "ListeDeTaches" devrait avoir les méthodes suivantes :
# ajouter_tache(tache): pour ajouter une tâche à la liste.
# marquer_complet(description): pour marquer une tâche comme complète en fonction de sa description.
# afficher_taches(): pour afficher la liste de toutes les tâches avec leur description, date limite et statut.
# Créez une instance de la classe "ListeDeTaches" et effectuez des opérations telles que l'ajout de tâches, le marquage de tâches comme complètes et l'affichage de la liste de tâches.

from tache import Tache
from liste_de_taches import ListeDeTaches

liste_taches = ListeDeTaches()

tache1 = Tache("Faire la vaisselle", "16/12/2024")

tache2 = Tache("Sortir les poubelles", "18/12/2024")

tache3 = Tache("Laver ses vêtements", "20/12/2024")

liste_taches.ajouter_tache(tache1)
liste_taches.ajouter_tache(tache2)
liste_taches.ajouter_tache(tache3)

liste_taches.afficher_taches()

liste_taches.marquer_complet("Faire la vaisselle")

liste_taches.afficher_taches()