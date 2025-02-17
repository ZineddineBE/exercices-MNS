def listMatieres(nbMatiere):
    matieres = []
    for i in range(nbMatiere):
        matieres.append(input(f"Saisir le nom de la matière numéro {i+1} : \n"))
    return matieres


def isNoteValid(note):
    if note <= 20 and note >=0:
        return True
    else:
        return False


def isCoeffValid(coeff):
    if coeff <= 10 and coeff >=0:
        return True
    else:
        return False


def listsNotes(matieres):
    notes = []
    for matiere in matieres:
        note = float(input(f"Saisir la note de {matiere} : \n"))
        while(isNoteValid(note) != True):
            note = int(input(f"Note incorrecte ! Saisir la note de {matiere} : \n"))
        notes.append(note)
    return notes


def listsCoeffs(matieres):
    coeffs = []
    for matiere in matieres:
        coeff = int(input(f"Saisir le coeff de {matiere} : \n"))
        while(isCoeffValid(coeff) != True):
            coeff = int(input(f"Coefficient incorrect ! Saisir le coeff de {matiere} : \n"))
        coeffs.append(coeff)
    return coeffs

    
def moyenneEleve(notes, coeffs):
    moyenneMatieres = []
    sommeCoeffs = 0
    sommeMoyennes = 0
    for i in range(len(notes)):
        sommeCoeffs = sommeCoeffs + coeffs[i]
        moyenneMatiere = notes[i] * coeffs[i]
        moyenneMatieres.append(moyenneMatiere)

    for moyenneMatiere in moyenneMatieres:
        sommeMoyennes = sommeMoyennes + moyenneMatiere 
    moyenne = round((sommeMoyennes/sommeCoeffs),1)

    return moyenne


def mention(moyenneEleve):
    if (moyenneEleve >= 16 and moyenneEleve <= 20):
        print("Mention : Très bien !")
    elif (moyenneEleve >= 12):
        print("Mention : Bien !")
    elif (moyenneEleve >= 8):
        print("Mention : Assez bien !")
    elif (moyenneEleve >= 4 ):
        print("Mention : Insuffisant !")
    elif (moyenneEleve >= 0):
        print("Mention : Nul !")
    else:
        print("Moyenne incorrect")


nbMatiere = int(input("Saisir le nombre de notes : \n"))

matieres = listMatieres(nbMatiere)

notes = listsNotes(matieres)
coeffs = listsCoeffs(matieres)

moyenne = moyenneEleve(notes, coeffs)
print(f"Vous avez une moyenne de {moyenne}")

mention(moyenne)
