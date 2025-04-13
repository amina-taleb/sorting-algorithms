import matplotlib.pyplot as plt
import numpy as np
import math
import time
import random

# 1. Tri par insertion
def insertion(liste):
    n = len(liste)
    for i in range(1, n):
        key = liste[i]
        j = i - 1
        while j >= 0 and liste[j] > key:
            liste[j + 1] = liste[j]
            j -= 1
        liste[j + 1] = key
    return liste

# 2. Tri par sélection
def selection(liste):
    n = len(liste)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if liste[j] < liste[min_index]:
                min_index = j
        liste[i], liste[min_index] = liste[min_index], liste[i]
    return liste

# 3. Tri à bulles
def bulle(liste):
    n = len(liste)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
    return liste

# 4. Tri par fusion
def fusion(gauche, droite):
    res = []
    index_gauche, index_droite = 0, 0
    while index_gauche < len(gauche) and index_droite < len(droite):
        if gauche[index_gauche] <= droite[index_droite]:
            res.append(gauche[index_gauche])
            index_gauche += 1
        else:
            res.append(droite[index_droite])
            index_droite += 1
    res.extend(gauche[index_gauche:])
    res.extend(droite[index_droite:])
    return res

def tri_fusion(liste):
    if len(liste) <= 1:
        return liste
    milieu = len(liste) // 2
    gauche = tri_fusion(liste[:milieu])
    droite = tri_fusion(liste[milieu:])
    return fusion(gauche, droite)

# 5. Tri à peigne
def peigne(liste):
    permutation = True
    gap = len(liste)
    while permutation or gap > 1:
        permutation = False
        gap = int(gap / 1.28)
        if gap < 1:
            gap = 1
        for i in range(len(liste) - gap):
            if liste[i] > liste[i + gap]:
                liste[i], liste[i + gap] = liste[i + gap], liste[i]
                permutation = True
    return liste

# 6. Tri par tas (heap sort)
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
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(i, 0)
    return arr

# 7. Tri rapide (quick sort)
def rapide(liste):
    if len(liste) <= 1:
        return liste
    pivot = liste.pop()
    liste_inf = [x for x in liste if x <= pivot]
    liste_sup = [x for x in liste if x > pivot]
    return rapide(liste_inf) + [pivot] + rapide(liste_sup)

# Mesure du temps d'exécution
def measure_time(sort_function, liste):
    start_time = time.perf_counter()
    sort_function(liste)
    end_time = time.perf_counter()
    return end_time - start_time

# Initialisation
nb_rep = 500
size = np.linspace(1, 1000, 1001)
t_insert_res = []
t_quick_res = []
t_select_res = []
t_fusion_res = []
t_bulle_res = []
t_tas_res = []
t_peigne_res = []

for n in size:
    t_insert = t_quick = t_select = t_peigne = t_fusion = t_tas = t_bulle = 0

    for _ in range(nb_rep):
        data = np.random.randint(0, 1000, int(n)).tolist()

        t_insert += measure_time(insertion, data[:])
        t_quick += measure_time(rapide, data[:])
        t_select += measure_time(selection, data[:])
        t_bulle += measure_time(bulle, data[:])
        t_fusion += measure_time(tri_fusion, data[:])
        t_peigne += measure_time(peigne, data[:])
        t_tas += measure_time(heap_sort, data[:])

    t_insert_res.append(t_insert / nb_rep)
    t_quick_res.append(t_quick / nb_rep)
    t_select_res.append(t_select / nb_rep)
    t_fusion_res.append(t_fusion / nb_rep)
    t_bulle_res.append(t_bulle / nb_rep)
    t_peigne_res.append(t_peigne / nb_rep)
    t_tas_res.append(t_tas / nb_rep)

# Affichage des résultats
plt.figure(figsize=(12, 7))
plt.plot(size, t_insert_res, label="Tri par insertion")
plt.plot(size, t_quick_res, label="Tri rapide")
plt.plot(size, t_select_res, label="Tri par sélection")
plt.plot(size, t_fusion_res, label="Tri fusion")
plt.plot(size, t_bulle_res, label="Tri à bulle")
plt.plot(size, t_peigne_res, label="Tri à peigne")
plt.plot(size, t_tas_res, label="Tri à tas")
plt.xlabel("Taille de la liste")
plt.ylabel("Temps d'exécution moyen (secondes)")
plt.title("Comparaison des temps d'exécution des algorithmes de tri (500 répétitions)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
