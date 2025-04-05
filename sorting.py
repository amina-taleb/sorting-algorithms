#ici, je vais créer 7 fonctions qui traduisent les algorithmes de tri :

#import numpy as np

#1. Tri par insertion :
def insertion(liste) :
    n = len(liste)
    for i in range(n) :
        for j in range(i+1, n) :
            if liste[j] < liste[i] :
                liste[i], liste[j] = liste[j], liste[i]   #l'échange se fait au même temps, si on écrit deux lignes diff, l'échange ne se fait pas au même temps
            else :
                pass
    return liste

#2. Tri par selection
def selection(liste) :
    n = len(liste)
    for i in range(n) :
        min_index = i    # on suppose que i est l'indice du plus petit nombre (on le fixe)
        for j in range(i + 1, n) :  # on le pointe sur le reste de la liste et on cherche le min
            if liste[j] < liste[min_index] :
                min_index = j # maintenant j devient l'indice du plus petit element
        liste[i], liste[min_index] = liste[min_index], liste[i]   #on échange les positions de l'élement d'indice i (qui se trouve au début de la liste) avec le plus petit élement de la liste non triées
    return liste

def bulle() :
    print(f"")
def fusion() :
    print(f"")
#exemple : 
# liste = [8, 2, 6, 9, 5, 6, 0, 4, 7, 1]
# print(selection(liste))
