# -------------------- La station de ski "Les ours bruns" --------------------

forfaits = [
    [1, "enfants", 18.70],
    [1, "adultes", 25.80],
    [1, "seniors", 21.40],
    [2, "enfants", 300.00],
    [2, "adultes", 510.00],
    [2, "seniors", 340.00],
]

def Tarif_beneficiaire(TypeForfait, Age):

    Statut = ""
    
    while(isTypeForfaitValid(TypeForfait) == False):
        print("Le type de forfait est incorrect !")
        TypeForfait = int(input("Quel est le type de votre forfait ? (1 : 1 journée / 2: Saison)\n"))

    if (TypeForfait == 1):
        if (Age < 12):
            Statut = "Enfant de moins de 12 ans"
            return forfaits[0][2], Statut
        elif (Age < 60):
            Statut = "Adulte"
            return forfaits[1][2], Statut
        else:
            Statut = "Sénior de plus de 60 ans"
            return forfaits[2][2], Statut
    elif (TypeForfait == 2):
        if (Age < 12):
            Statut = "Enfant de moins de 12 ans"
            return forfaits[3][2], Statut
        elif (Age < 60):
            Statut = "Adulte"
            return forfaits[4][2], Statut
        else:
            Statut = "Sénior de plus de 60 ans"
            return forfaits[5][2], Statut

def isTypeForfaitValid(TypeForfait):
    if TypeForfait == 1 or TypeForfait == 2:
        return True
    else:
        return False

TypeForfait = int(input("Quel est le type de votre forfait ? (1 : 1 journée / 2: Saison)\n"))
Age = int(input("Quel est votre âge ?\n"))

Tarif = Tarif_beneficiaire(TypeForfait, Age)[0]
Statut = Tarif_beneficiaire(TypeForfait, Age)[1]
        
print(f"\nVotre statut est \"{Statut}\" et votre tarif est de {Tarif}€.")