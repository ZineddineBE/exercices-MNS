from tache import Tache

class ListeDeTaches(Tache):
    def __init__(self):
        self.liste_taches = []

    def ajouter_tache(self, tache): 
        self.liste_taches.append(tache)

    def marquer_complet(self, description):
        for tache in self.liste_taches:
            if tache.description == description:
                tache.statut = "complet" 

    def afficher_taches(self):
        for tache in self.liste_taches:
            print(f"Tâche numéro {self.liste_taches.index(tache) + 1} : {tache.description} / Date : {tache.date_limite} / Statut : {tache.statut}") 
        
