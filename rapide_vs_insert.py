import time
import random
import matplotlib.pyplot as plt
import numpy as np

def insertion_sort(liste):
    for i in range(1, len(liste)):
        key = liste[i]
        j = i - 1
        while j >= 0 and liste[j] > key:
            liste[j + 1] = liste[j]
            j -= 1
        liste[j + 1] = key

def quick_sort(liste):
    if len(liste) <= 1:  # Si la liste est vide ou contient un seul élément
        return liste
    
    pivot = liste.pop()  # On choisit le dernier élément comme pivot
    liste_inf = [x for x in liste if x <= pivot]  
    liste_sup = [x for x in liste if x > pivot]   
    return quick_sort(liste_inf) + [pivot] + quick_sort(liste_sup)


# Mesurer le temps d'exécution de n'import quel tri
def measure_time(sort_function, liste):
    start_time = time.time()  #temps avant d'executer l'algo
    sort_function(liste)  #appeler la fonction
    end_time = time.time()    # temps après execution de l'algo
    return end_time - start_time  # retourne la diff de temps


nb_rep = 500  # Nombre de répétitions pour chaque taille
size = np.linspace(1, 100, 101)  #taille de la liste
t_insert_res = []
t_quick_res = []

for n in size:
    t_insert = 0  #initialiser les compteurs
    t_quick = 0

    for _ in range(nb_rep):  #répeter plusieurs fois l'expérience
        data = []  #créer une liste vide pour caque repet
        for _ in range(int(n)):
            data.append(random.randint(0, 1000))  #générer des nb aléatoires 

        d1 = data[:]   #une copie de data pour traiter séparement et ne pas affecter la liste originale
        t_insert += measure_time(insertion_sort, d1)

        
        d2 = data[:]
        t_quick += measure_time(quick_sort, d2)

    t_insert_res.append(t_insert / nb_rep)    #le temps d'execution en moyen
    t_quick_res.append(t_quick / nb_rep)


plt.figure(figsize=(10, 6))
plt.plot(size, t_insert_res, label="Insertion Sort", color='red')
plt.plot(size, t_quick_res, label="QuickSort", color='green')
plt.xlabel("Taille de la liste")
plt.ylabel("Temps d'exécution (en secondes)")
plt.title("Comparaison des temps d'exécution des algorithmes de tri : Insertion vs Rapide")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
