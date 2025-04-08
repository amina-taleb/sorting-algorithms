#ici, je vais créer 7 fonctions qui traduisent les algorithmes de tri :

#import numpy as np

#Récap :
# Insertion : comparer 2 à 2 a partir de 0
# Selection : chercher le min dans toute la liste
########################################################################################################################
#1. Tri par insertion :
def insertion(liste) :
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
        min_index = i    # on suppose que i est l'indice du plus petit nombre (on le fixe)
        for j in range(i + 1, n) :  # on le pointe sur le reste de la liste et on cherche le min
            if liste[j] < liste[min_index] :
                min_index = j # maintenant j devient l'indice du plus petit element
        liste[i], liste[min_index] = liste[min_index], liste[i]   #on échange les positions de l'élement d'indice i (qui se trouve au début de la liste) avec le plus petit élement de la liste non triées
    return liste

###################################################################################################################################################################
def bulle(liste) :
    print(f"")

####################################################################################################################################################################
def fusion(liste) :
    print(f"")

#####################################################################################################################################################################
def rapide(liste) :
    print(f"")

#####################################################################################################################################################################
#exemple : 
liste = [8, 2, 6, 9, 5, 6, 0, 4, 7, 1]
print(insertion(liste))
