import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
import sorting
import random
import time

def afficher_interface() :
    window = ctk.CTk()
    ctk.set_default_color_theme('blue')
    ctk.set_appearance_mode('dark')
    window.geometry('1200x700')
    window.title('Algotric')
    window.grid_columnconfigure(0, weight=2)
    window.grid_columnconfigure(1, weight=3)
    window.grid_rowconfigure(0, weight=2) 
    window.grid_rowconfigure(1, weight=3)

    liste = []

    frame_title = ctk.CTkFrame(master=window, fg_color='grey', height=100)
    frame_title.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
    frame_title.grid_rowconfigure(0, weight=5)
    frame_title.grid_rowconfigure(1, weight=5)
    frame_title.grid_columnconfigure(0, weight=5)
    frame_title.grid_columnconfigure(1, weight=5)
    frame_title.grid_columnconfigure(2, weight=5)

    label_01 =  ctk.CTkLabel(master=frame_title, text='Insérez les valeurs', text_color='black', font=('Arial', 20))
    label_01.grid(row=0, column=0, padx=5, pady=5)

    champ = ctk.CTkEntry(master=frame_title, placeholder_text='Exemple : 2, 4, 1, 6, 3', width=250)
    champ.grid(row=1, column=0, padx=5, pady=5)

    label_02 = ctk.CTkLabel(master=frame_title, text='Générer aléatoirement', text_color='black', font=('Arial', 20))
    label_02.grid(row=0, column=1, padx=5, pady=5)

    button_gene = ctk.CTkButton(master=frame_title, text='Générer', width=200, fg_color='green', command=lambda: generer_liste(frame_graph, liste))
    button_gene.grid(row=1, column=1, padx=5, pady=5)

    label_03 = ctk.CTkLabel(master=frame_title, text='Importer un fichier', text_color='black', font=('Arial', 20))
    label_03.grid(row=0, column=2, padx=5, pady=5)

    button_imp = ctk.CTkButton(master=frame_title, text='Importer', width=200, fg_color='green')
    button_imp.grid(row=1, column=2, padx=5, pady=5)

    frame_graph = ctk.CTkFrame(master=window, fg_color='grey')
    frame_graph.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

    frame_menu = ctk.CTkFrame(master=window, fg_color='grey')
    frame_menu.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
    frame_menu.grid_columnconfigure(0, weight=1)
    frame_menu.grid_columnconfigure(1, weight=1)
    for i in range(10):
        frame_menu.grid_rowconfigure(i, weight=1)

    label1 = ctk.CTkLabel(master=frame_menu, text='Visualiser les algorithmes', text_color='black', font=('Arial', 20))
    label1.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    algos = [
        ('Sélection', sorting.selection),
        ('Insertion', sorting.insertion),
        ('Fusion', sorting.tri_fusion),
        ('Rapide', sorting.rapide),
        ('Peigne', sorting.peigne),
        ('Bulle', sorting.bulle),
        ('Tas', sorting.heap_sort),
    ]

    for i, (nom, algo) in enumerate(algos):
        btn = ctk.CTkButton(master=frame_menu, text=nom, width=200, fg_color='green', command=lambda a=algo: afficher_tri(frame_graph, liste, a))
        btn.grid(row=i+1, column=0, padx=10, pady=10)

    button_trier  = ctk.CTkButton(master=frame_menu, text='Trier (rapide)', width=200, fg_color='red', command=lambda: trier_plus_rapide(frame_graph, liste))
    button_trier.grid(row=1, column=1, padx=10, pady=10)

    button_visualiser  = ctk.CTkButton(master=frame_menu, text='Visualiser', width=200, fg_color='blue', command=lambda: afficher_comparaison(frame_graph, liste))
    button_visualiser.grid(row=2, column=1, padx=10, pady=10)

    button_comparaison_graphique  = ctk.CTkButton(master=frame_menu, text='Afficher Graphique', width=200, fg_color='purple',command=lambda: afficher_graphique(frame_graph))
    button_comparaison_graphique.grid(row=3, column=1, padx=10, pady=10)

    window.mainloop()

def generer_liste(frame, liste_cible):
    size = random.randint(5, 50)
    gen_liste = [random.randint(0, 100) for _ in range(size)]
    liste_cible.clear()
    liste_cible.extend(gen_liste)

    for widget in frame.winfo_children():
        widget.destroy()

    texte = ', '.join(str(x) for x in gen_liste)
    label = ctk.CTkLabel(master=frame, text=texte, font=("Arial", 18), text_color="black", wraplength=400)
    label.pack(padx=10, pady=10)


def afficher_tri(frame, liste, fonction_tri):
    for widget in frame.winfo_children():
        widget.destroy()

    nom_algo = fonction_tri.__name__.replace("_", " ").title()

    label_algo = ctk.CTkLabel(master=frame, text=f"Algorithme : {nom_algo}", font=("Arial", 20, "bold"), text_color="blue")
    label_algo.pack(pady=5)

    label_avant = ctk.CTkLabel(master=frame, text="Avant tri : " + ', '.join(map(str, liste)), font=("Arial", 16), text_color="black", wraplength=400)
    label_avant.pack(pady=5)

    debut = time.perf_counter()
    liste_triee = fonction_tri(liste.copy())
    fin = time.perf_counter()
    duree = fin - debut

    label_apres = ctk.CTkLabel(master=frame, text="Après tri : " + ', '.join(map(str, liste_triee)), font=("Arial", 16), text_color="green", wraplength=400)
    label_apres.pack(pady=5)

    label_temps = ctk.CTkLabel(master=frame, text=f"Temps d'exécution : {duree:.6f} secondes", font=("Arial", 16), text_color="purple")
    label_temps.pack(pady=5)


def trier_plus_rapide(frame, liste):
    algos = [
        sorting.selection,
        sorting.insertion,
        sorting.tri_fusion,
        sorting.rapide,
        sorting.peigne,
        sorting.bulle,
        sorting.heap_sort
    ]

    meilleurs_temps = {}
    for algo in algos:
        debut = time.perf_counter()
        _ = algo(liste.copy())
        fin = time.perf_counter()
        meilleurs_temps[algo] = fin - debut

    meilleur = min(meilleurs_temps, key=meilleurs_temps.get)
    afficher_tri(frame, liste, meilleur)


def afficher_comparaison(frame, liste):
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
        _ = fonction(liste.copy())
        fin = time.perf_counter()
        temps_exec[nom] = fin - debut

    for widget in frame.winfo_children():
        widget.destroy()

    fig, ax = plt.subplots(figsize=(6, 4))
    noms = list(temps_exec.keys())
    valeurs = list(temps_exec.values())

    ax.barh(noms, valeurs, color='skyblue')
    ax.set_xlabel('Temps (s)')
    ax.set_title('Comparaison des algorithmes')

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(padx=10, pady=10)

def afficher_graphique(frame):
    try :
        import numpy as np
        import matplotlib.pyplot as plt
        from sorting import insertion, selection, rapide, bulle, tri_fusion, peigne, heap_sort

        def measure_time(sort_function, liste):
            start_time = time.perf_counter()
            sort_function(liste)
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

        # Création du graphique
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

        # Affichage du graphique dans l'interface
        for widget in frame.winfo_children():
            widget.destroy()

        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack(padx=10, pady=10)

    except Exception as e:
        print(f"Erreur lors de l'affichage du graphique : {e}")

if __name__ == '__main__':
    afficher_interface()
