#ici, je vais créer 7 fonctions qui traduisent les algorithmes de tri :

import numpy as np
import math


#Récap :
# Insertion : comparer 2 à 2 a partir de 0
# Selection : chercher le min dans toute la liste
########################################################################################################################
#1. Tri par insertion :
def insertion(liste, complexité) :
    n = len(liste) 
    for i in range (1, n) :
        key = liste[i]  #un pointeur (element d'indice quelconque)
        j = i - 1    #initialiser j (se trouve avant i)
        while j >= 0 and liste[j] > key :   # si les premiers élements sont plus grand 
            liste[j + 1] = liste[j]   #décalage
            j -= 1
        liste[j+1] = key   # car L[j+1] = L[i]   essaie de faire un tableau avec les élement de la liste + 2 lignes contenant l'incrimentation des 2 indices i et j
    return liste
# Explication sur une feuille 
#################################################################################################################################################################
#2. Tri par selection
def selection(liste) :
    n = len(liste)
    for i in range(n) :
        min_index = i    # on suppose que i est l'indice du plus petit nombre (on le fixe) = selectionner un element et le stocker dans une variable temporaire
        for j in range(i + 1, n) :  # on parcourt la sous-liste qui reste (i+1 a n)
            if liste[j] < liste[min_index] : #on chercher le min 
                min_index = j # maintenant j devient l'indice du plus petit element
        liste[i], liste[min_index] = liste[min_index], liste[i]   #on échange les positions de l'élement d'indice i (qui se trouve au début de la liste) avec le plus petit élement de la liste non triées
    return liste

###################################################################################################################################################################
def bulle(liste) :   #le concept : tout revient à sa place, exemple d'un mélange d'eau et de l'huile
    n = len(liste) 
    for i in range(0, n-1) :  #les tours
        for j in range(0, (n-1)-i) :
            if liste[j] > liste[j+1] :
                liste[j], liste[j+1] = liste[j+1], liste[j]
    return liste

####################################################################################################################################################################
def fusion(gauche, droite) :
    res = []
    index_gauche, index_droite = 0,0
    while index_gauche < len(gauche) and index_droite < len(droite):
        if gauche[index_gauche] <= droite[index_droite]:
            res.append(gauche[index_gauche])
            index_gauche +=1
        else:
            res.append(droite[index_droite])
            index_droite +=1
    if gauche:
        res.extend(gauche[index_gauche:])
    if droite:
        res.extend(droite[index_droite:])
    return res

def tri_fusion(liste):
    if len(liste) <= 1:
        return liste
    milieu = len(liste)//2
    gauche= liste[:milieu]
    droite= liste[milieu:]
    gauche=tri_fusion(gauche)
    droite=tri_fusion(droite)
    return list(fusion(gauche, droite))




######################################################################################################################################

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
#####################################################################################################################################
def heap_sort(arr):
    def heapify(n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(n, largest)

    n = len(arr)

    # Construction du tas max
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)

    # Extraction des éléments un par un
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(i, 0)



#####################################################################################################################################################################
def rapide(liste, T) :
    n = len(liste)
    T0 = 1
    if n <= 1 :   # il y a un seul element dans la liste ou une liste vide
        return liste 
    #pivot = np.median(liste, axis=0)       #axis=0, cela signifie que nous calculons la médiane le long de l'axe des lignes
    pivot = liste.pop()         #une fonction qui renvoit le dernier element (Généralement, ce qu'on choisit)
    liste_inf = []
    liste_sup = []       #créer deux listes
    for i in range (0, n-1) :
        if liste[i] <= pivot :
            liste_inf.append(liste[i])
        else :
            liste_sup.append(liste[i])

<<<<<<< HEAD
    complexite = n * T0 + np.log2(n) * n 
=======
    # complexité = n * T0 + np.log2(n) * 
>>>>>>> 963fdb0afb462a5668ab2c80d6b093f646705206
    return rapide(liste_inf) + [pivot] + rapide(liste_sup)
# Ici pour rendre cet algorithme moins complexe, je choisit le pivot = mediane 
#####################################################################################################################################################################
#ajouter une fonction teste unitaire
#exemple : 
# liste = [8, 2, 6, 9, 5, 0, 4, 7, 1]
# print(rapide(liste))
#Ajoute le calcule de complexité temporelle de chaque algorithme + graphes et une condition de sélection d'un algo en fonction du problème (fichiers excels? txt?)