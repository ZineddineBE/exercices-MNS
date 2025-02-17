from livre import Livre

class Bibliotheque(Livre):
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)

    def rechercher_livre(self, titre, auteur):
        for i in range(len(self.livres)):
            if titre == self.livres[i].titre and auteur == self.livres[i].auteur:
                return f"Le livre {self.livres[i].titre} est présent dans cette bibliothèque.\nVoici ses informations :\n   - Auteur : {self.livres[i].auteur}\n   - Année de publication : {self.livres[i].annee_publication}"

    def afficher_livres(self):
        for livre in self.livres:
            print(f"Titre du livre numéro {self.livres.index(livre) + 1} : {livre.titre} / Auteur : {livre.auteur} / Année de publication : {livre.annee_publication}")