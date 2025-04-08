#tri à peigne
#On compare tous les éléments situés à un intervalle défini à l'avance. 
#une fois tous les éléments comparés, on choisit un facteur de réduction compris entre 1.25 et 1.3 pour réduire la taille de l'intervalle
#on compare à nouveau les éléments, jusqu'à arriver à un intervalle de 1 pour finir les derniers éléments non triés.

import math

def peigne(liste):
    permutation=True
    gap=len(liste)
    while (permutation == True) or gap>1:
        permutation=False
        gap = math.floor(gap/1.28)
        if gap<1:
            gap=1
        for en_cours in range(0, len(liste)-gap):
            if liste[en_cours]>liste[en_cours+gap]:
                permutation=True
                liste[en_cours], liste[en_cours+gap]=liste[en_cours+gap], liste[en_cours]
    return liste

liste = [8, 2, 6, 9, 5, 6, 0, 4, 7, 1]
print(peigne(liste))