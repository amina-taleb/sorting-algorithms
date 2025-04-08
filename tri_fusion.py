print("Test VSCode fonctionne ✅")

#ici, je vais créer 7 fonctions qui traduisent les algorithmes de tri :

#import numpy as np

# #1. Tri par insertion :
# def insertion(liste) :
#     n = len(liste)
#     for i in range(n) :
#         for j in range(i+1, n) :
#             if liste[j] < liste[i] :
#                 liste[i], liste[j] = liste[j], liste[i]   #l'échange se fait au même temps, si on écrit deux lignes diff, l'échange ne se fait pas au même temps
#             else :
#                 pass
#     return liste

# #2. Tri par selection
# def selection(liste) :
#     n = len(liste)
#     for i in range(n) :
#         #on suppose que le,plus petit indice est a la position i 
#         min_index = i
#         for j in range(i + 1, n) : #on cheche le plus petit element dans le reste de la liste
#             if liste[j] < liste[min_index]:
#                 min_index = j  # Si on trouve plus petit, on met à jour min_index
        
#         liste[i], liste[min_index] = liste[min_index], liste[i]   #échange

#     return liste

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
#exemple : 
liste = [8, 2, 6, 9, 5, 6, 0, 4, 7, 1]
print(tri_fusion(liste))
print("Hello VSCode 👋")