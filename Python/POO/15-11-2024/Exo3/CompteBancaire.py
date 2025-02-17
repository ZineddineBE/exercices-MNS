class CompteBancaire():
    def __init__(self, titulaire_compte, solde):
        self.titulaire_compte = titulaire_compte
        self.solde = solde
        

    def deposer(self, montant):
        self.solde += montant

    def retirer(self, montant):
        if montant > self.solde:
            print(f"Retrait impossible ! Vous avez moins de {montant}€ sur votre compte.")
        else:
            self.solde -= montant
            
            


    def afficher_solde(self):
        print(f"Votre solde est de : {self.solde}€")
