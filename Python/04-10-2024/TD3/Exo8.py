# L’élève placé au fond de la classe, près du radiateur, est le meilleur de la classe. Pour tuer le temps,
# il décide de plier une feuille en deux puis en deux, puis... en deux, puis... Écrivez un algorithme
# qui calcule l’épaisseur du pliage final à partir du nombre de plis et de l’épaisseur initiale de la
# feuille.

epaisseur_feuille = 0.1
nb_plis = 0

while (nb_plis != 8):
    epaisseur_feuille = epaisseur_feuille * 2
    nb_plis += 1

print(epaisseur_feuille)