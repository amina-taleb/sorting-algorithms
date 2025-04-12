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


# Mesurer le temps d'exécution d'un tri
def measure_time(sort_function, liste):
    start_time = time.time()  #temps avant d'executer l'algo
    sort_function(liste)
    end_time = time.time()    # temps après execution de l'algo
    return end_time - start_time  # diff de temps


nb_rep = 500  # Nombre de répétitions pour chaque taille
size = np.linspace(1, 100, 101)  #taille de la liste
t_insert_res = []
t_quick_res = []

for n in size:
    t_insert = 0
    t_quick = 0
    
    for _ in range(nb_rep):
        data = []
        for _ in range(int(n)):
            data.append(random.randint(0, 1000))

        d1 = data[:]
        t_insert += measure_time(insertion_sort, d1)

        
        d2 = data[:]
        t_quick += measure_time(quick_sort, d2)

    t_insert_res.append(t_insert / nb_rep)
    t_quick_res.append(t_quick / nb_rep)

# la complexité : 
n_values = np.linspace(1, 100, 101)
complexity_insertion = (n_values**2) / (n_values.max()**2)  # Normalisation 
complexity_quick = n_values * np.log2(n_values) / (n_values.max() * np.log(n_values.max()))  

#pour l'expérience
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


#pour la complexité
plt.figure(figsize=(10, 6))
plt.plot(n_values, complexity_insertion, label="O(n²) : Insertion", color='blue')
plt.plot(n_values, complexity_quick, label="O(n log n) : Rapide", color='orange')
plt.xlabel("Taille de la liste")
plt.ylabel("Complexité théorique (normalisée)")
plt.title("Comparaison des complexités théoriques dans le cas moyen : Insertion vs Rapide")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
