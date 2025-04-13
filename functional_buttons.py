# Dans ce fichier, on va créer les autres fonctions (importer un fichier, générer aléatoirement ....)
import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
import sorting
import random
import time
from tkinter import filedialog
import os

###################################################################################################################################
#3. Créer une fonction qui genere aleatoirement n elements :
def generer_liste_aleatoire(frame, liste_cible):
    size = random.randint(5, 70)  
    gen_liste = [random.randint(0, 100) for _ in range(size)]  # y a pas i in range car y pas vraiment d'indice

    liste_cible.clear()  # efface d'abord la liste existante (c'est liste dans la fonction precedante)
    liste_cible.extend(gen_liste)  # Ajoute les éléments générés à la liste
 
    for widget in frame.winfo_children(): # Affichage
        widget.destroy()  # Supprime tous les widgets existants dans le frame

    texte = '[ ' + ', '.join(str(x) for x in gen_liste) + ' ]'  # Convertit les éléments en chaîne de caractères pour pouvoir les afficher
    label = ctk.CTkLabel(master=frame, text=f"L = {texte}", font=("Arial", 18), text_color="black", wraplength=400)  #afficher la liste que frame_graph
    label.pack(padx=10, pady=10)


    size_label = ctk.CTkLabel(master=frame, text=f"N = {size}", font=("Arial", 18), text_color="black")  #afficher le nombre d'élements
    size_label.pack(padx=10, pady=10)


####################################################################################################################################
#4. Créer une fonction qui convertit les element saisis dans le champs en une liste exploitable :
def inserer_valeurs_manuellement(frame, liste_cible, champ):
    texte = champ.get()  

    try:    
        liste_num = [int(x.strip()) for x in texte.split(',')]  # Essaie de convertir la chaîne en une liste de nombres
        liste_cible.clear()  #effacer l'existante
        liste_cible.extend(liste_num)  #ajouter les elements saisi a la liste vide

    except ValueError: 
        liste_cible.clear()
        liste_cible.extend(sorted(texte.split(',')))    #si pas num, on trie alphabétiquement avec la fonction sorted (tri rapide de python) en attendant de trouver comment trier avec l'algo avec ASCII


    for widget in frame.winfo_children():     # Affichage de la liste dans l'interface
        widget.destroy()  # Supprime tous les widgets existants dans le frame

    # Affichage de la liste 
    texte = '[]' + ', '.join(str(x) for x in liste_cible) + ']'  # Convertit les éléments en chaîne de caractères
    label = ctk.CTkLabel(master=frame, text=f"L = {texte}", font=("Arial", 18), text_color="black", wraplength=400)  # Crée un label pour afficher la liste
    label.pack(padx=10, pady=10)

    # Affichage de le size en bas
    size = len(liste_cible)  
    size_label = ctk.CTkLabel(master=frame, text=f"N = {size}", font=("Arial", 14), text_color="black")
    size_label.pack(padx=10, pady=10)

  
#########################################################################################################################################
#5. Importer des fichiers externes et copier leurs contenus dans le frame_graph
def importer_fichier(frame, liste_cible):
    initial_dir = os.getcwd()   #se connecter au dossier courant (de travail)
    filepath = filedialog.askopenfilename(   #ouvrir la boite de dialogue pour selectionner un fichier
        initialdir=initial_dir,   #réperoire de départ : celui selectionné précédemment
        title="Choix de fichier",
        filetypes=[("Fichiers texte", "*.txt")] #types de fichiers à traiter
    )
    if filepath:   #si on selectionne un fichier
        try:
            with open(filepath, 'r') as f:  #l'ouvrir
                contenu = f.read()   #le lire
                elements = [int(x) for x in contenu.replace(',', ' ').split()] #remplacer les virgules par des espaces, si déja espace, ne rien faire
                liste_cible.clear()   #supprimer le contenu de la liste si pas vide
                liste_cible.extend(elements)  #ajouter ces nouveaux elements

                for widget in frame.winfo_children():
                    widget.destroy()  #supprimer le contenu du frame

                texte = ', '.join(map(str, liste_cible))   #affichage de la liste (elements séparés par des virgules)
                label = ctk.CTkLabel(master=frame, text=f"L = {texte}", font=("Arial", 18), text_color="black", wraplength=400)
                label.pack(padx=10, pady=10)

                # Affichage de le size en bas
                size = len(liste_cible)  
                size_label = ctk.CTkLabel(master=frame, text=f"N = {size}", font=("Arial", 14), text_color="black")
                size_label.pack(padx=10, pady=10)
        except Exception as e:
            print(f"Erreur lors de l'importation : {e}")


########################################################################################################################################
#6. Créer une fonction qui affiche la liste_cible avant le tri, après le tri et le temps d'execution : 
def afficher_tri(frame, liste_cible, fonction_tri):
    font_size = 16
    # Supprimer les anciens widgets dans le cadre
    for widget in frame.winfo_children():
        widget.destroy()
 
    nom_algo = fonction_tri.__name__.replace("_", " ").title()   # Nom de l'algorithme, remplacement des underscores par des espaces et mise en majuscules

    label_algo = ctk.CTkLabel(master=frame, text=f"Algorithme utilisé: {nom_algo}", font=("Arial", font_size, "bold"), text_color="blue")
    label_algo.place(x=10, y=50)

    label_avant = ctk.CTkLabel(master=frame, text="Avant tri : " + '[' + ', '.join(map(str, liste_cible)) + ']', font=("Arial", font_size), text_color="black", wraplength=600)
    label_avant.place(x=10, y=150)


    debut = time.perf_counter()  # Prendre un horodatage avant l'exécution = pour les mesures precises = courtes durée
    liste_triee = fonction_tri(liste_cible.copy())  # Créer une copie de la liste pour ne pas modifier l'originale
    fin = time.perf_counter()  # Prendre un horodatage après l'exécution
    duree = fin - debut  # Calculer la durée en secondes

    label_apres = ctk.CTkLabel(master=frame, text="Après tri : " + '[' + ', '.join(map(str, liste_triee)) + ']', font=("Arial", font_size), text_color="green", wraplength=600)
    label_apres.place(x=10, y=250)

    size = len(liste_cible)
    label_temps = ctk.CTkLabel(master=frame, text=f"Temps d'exécution : {duree:.6f} secondes , N = {size}", font=("Arial", font_size), text_color="black")
    label_temps.place(x=10, y=350)
    

###########################################################################################################################################
#7. Créer une fonction qui selectionne l'algo le plus rapide pour la liste en question
def trier_plus_rapide(frame, liste_cible):
    algos = [
        sorting.selection,
        sorting.insertion,
        sorting.tri_fusion,
        sorting.rapide,
        sorting.peigne,
        sorting.bulle,
        sorting.heap_sort
    ]

    exec_temps = {}
    for algo in algos:
        debut = time.perf_counter()  #recalculer delta t
        _ = algo(liste_cible.copy())   
        fin = time.perf_counter()
        exec_temps[algo] = fin - debut

    min_t = min(exec_temps, key=exec_temps.get)  #choisir le min(t) parmis les temps d'execution de chaque algo
    afficher_tri(frame, liste_cible, min_t)

############################################################################################################################
#8. Créer une fonction qui 
def afficher_comparaison(frame, liste_cible):
    algos = {
        "Sélection": sorting.selection,
        "Insertion": sorting.insertion,
        "Fusion": sorting.tri_fusion,
        "Rapide": sorting.rapide,
        "Peigne": sorting.peigne,
        "Bulle": sorting.bulle,
        "Tas": sorting.heap_sort
    }

    temps_exec = {}
    for nom, fonction in algos.items():
        debut = time.perf_counter()
        _ = fonction(liste_cible.copy())
        fin = time.perf_counter()
        temps_exec[nom] = fin - debut     #pareil : recalculer le delta t

    for widget in frame.winfo_children():
        widget.destroy()  #clean la frame

    fig, ax = plt.subplots(figsize=(6, 4))     #créer une fenetre
    noms = list(temps_exec.keys())
    valeurs = list(temps_exec.values())

    ax.barh(noms, valeurs, color='red')   #graphe = barres
    ax.set_xlabel('Temps (s)')
    ax.set_title('Comparaison des algorithmes')

    canvas = FigureCanvasTkAgg(fig, master=frame)      #Ajouter le graphe au frame
    canvas.draw()
    canvas.get_tk_widget().pack(padx=10, pady=60)


#############################################################################################################################
#9. Tracer les temps d'execution moyen des 7 algorithmes en fonction de la taille n (simulations)
def afficher_graphique(frame):
    try :
        import numpy as np
        import matplotlib.pyplot as plt
        from sorting import insertion, selection, rapide, bulle, tri_fusion, peigne, heap_sort

        def measure_time(sort_function, liste_cible):
            start_time = time.perf_counter()
            sort_function(liste_cible)
            end_time = time.perf_counter()
            return end_time - start_time


        nb_rep = 50
        size = np.linspace(1, 100, 101)
        t_insert_res, t_quick_res, t_select_res, t_fusion_res, t_bulle_res = [], [], [], [], []
        t_tas_res, t_peigne_res = [], []

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

        
        fig, ax = plt.subplots(figsize=(12, 7))
        ax.plot(size, t_insert_res, label="Tri par insertion")
        ax.plot(size, t_quick_res, label="Tri rapide")
        ax.plot(size, t_select_res, label="Tri par sélection")
        ax.plot(size, t_fusion_res, label="Tri fusion")
        ax.plot(size, t_bulle_res, label="Tri à bulle")
        ax.plot(size, t_peigne_res, label="Tri à peigne")
        ax.plot(size, t_tas_res, label="Tri à tas")
        ax.set_xlabel("Taille de la liste")
        ax.set_ylabel("Temps d'exécution moyen (secondes)")
        ax.set_title(f"Comparaison des temps d'exécution des algorithmes de tri selon la taille de la liste pour {nb_rep} répétitions")
        ax.legend()
        ax.grid(True)
        plt.tight_layout()

    
        for widget in frame.winfo_children():
            widget.destroy()

        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack(padx=10, pady=10)

    except Exception as e:
        print(f"Erreur lors de l'affichage du graphique : {e}")
