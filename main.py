#1. Importer les librairies et les fichiers necessaires :
import customtkinter as ctk
import sorting
import functional_buttons

########################################################################################################################"
#2. Créer une fonction qui affiche l'interface customtkinter :
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

    button_ok = ctk.CTkButton(master=frame_title, text='OK', width=50, command=lambda: functional_buttons.inserer_valeurs_manuellement(frame_graph, liste, champ))
    button_ok.grid(row=1, column=0, padx=(260, 5), pady=5, sticky="e")


    label_02 = ctk.CTkLabel(master=frame_title, text='Générer aléatoirement', text_color='black', font=('Arial', 20))
    label_02.grid(row=0, column=1, padx=5, pady=5)

    button_gene = ctk.CTkButton(master=frame_title, text='Générer', width=200, fg_color='green', command=lambda: functional_buttons.generer_liste_aleatoire(frame_graph, liste))
    button_gene.grid(row=1, column=1, padx=5, pady=5)

    label_03 = ctk.CTkLabel(master=frame_title, text='Importer un fichier', text_color='black', font=('Arial', 20))
    label_03.grid(row=0, column=2, padx=5, pady=5)

    button_imp = ctk.CTkButton(master=frame_title, text='Importer', width=200, fg_color='green', command= lambda : functional_buttons.importer_fichier(frame_graph, liste))
    button_imp.grid(row=1, column=2, padx=5, pady=5)

    frame_graph = ctk.CTkFrame(master=window, fg_color='grey')
    frame_graph.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

    frame_menu = ctk.CTkFrame(master=window, fg_color='grey')
    frame_menu.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

    frame_menu.grid_columnconfigure(0, weight=1)
    frame_menu.grid_columnconfigure(1, weight=1)
    frame_menu.grid_rowconfigure(0, weight=1)
    frame_menu.grid_rowconfigure(1, weight=1)
    frame_menu.grid_rowconfigure(2, weight=1)
    frame_menu.grid_rowconfigure(3, weight=1)
    frame_menu.grid_rowconfigure(4, weight=1)
    frame_menu.grid_rowconfigure(5, weight=1)
    frame_menu.grid_rowconfigure(6, weight=1)
    frame_menu.grid_rowconfigure(7, weight=1)
    frame_menu.grid_rowconfigure(8, weight=1)
    frame_menu.grid_rowconfigure(9, weight=1)


    label1 = ctk.CTkLabel(master=frame_menu, text='Visualiser les algorithmes', text_color='black', font=('Arial', 20))
    label1.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    btn1 = ctk.CTkButton(master=frame_menu, text='Sélection', width=200, fg_color='green', command=lambda a=sorting.selection: functional_buttons.afficher_tri(frame_graph, liste, a))
    btn1.grid(row=1, column=0, padx=10, pady=10)

    btn2 = ctk.CTkButton(master=frame_menu, text='Insertion', width=200, fg_color='green', command=lambda a=sorting.insertion: functional_buttons.afficher_tri(frame_graph, liste, a))
    btn2.grid(row=2, column=0, padx=10, pady=10)

    btn3 = ctk.CTkButton(master=frame_menu, text='Fusion', width=200, fg_color='green', command=lambda a=sorting.tri_fusion: functional_buttons.afficher_tri(frame_graph, liste, a))
    btn3.grid(row=3, column=0, padx=10, pady=10)

    btn4 = ctk.CTkButton(master=frame_menu, text='Rapide', width=200, fg_color='green', command=lambda a=sorting.rapide: functional_buttons.afficher_tri(frame_graph, liste, a))
    btn4.grid(row=4, column=0, padx=10, pady=10)

    btn5 = ctk.CTkButton(master=frame_menu, text='Peigne', width=200, fg_color='green', command=lambda a=sorting.peigne: functional_buttons.afficher_tri(frame_graph, liste, a))
    btn5.grid(row=5, column=0, padx=10, pady=10)

    btn6 = ctk.CTkButton(master=frame_menu, text='Bulle', width=200, fg_color='green', command=lambda a=sorting.bulle: functional_buttons.afficher_tri(frame_graph, liste, a))
    btn6.grid(row=6, column=0, padx=10, pady=10)

    btn7 = ctk.CTkButton(master=frame_menu, text='Tas', width=200, fg_color='green', command=lambda a=sorting.heap_sort: functional_buttons.afficher_tri(frame_graph, liste, a))
    btn7.grid(row=7, column=0, padx=10, pady=10)


    button_trier  = ctk.CTkButton(master=frame_menu, text='Trier', width=200, fg_color='red', command=lambda: functional_buttons.trier_plus_rapide(frame_graph, liste))
    button_trier.grid(row=1, column=1, padx=10, pady=10)

    button_visualiser  = ctk.CTkButton(master=frame_menu, text='Visualiser', width=200, fg_color='blue', command=lambda: functional_buttons.afficher_comparaison(frame_graph, liste))
    button_visualiser.grid(row=2, column=1, padx=10, pady=10)

    button_comparaison_graphique  = ctk.CTkButton(master=frame_menu, text='Simulation', width=200, fg_color='purple',command=lambda: functional_buttons.afficher_graphique(frame_graph))
    button_comparaison_graphique.grid(row=3, column=1, padx=10, pady=10)

    window.mainloop()


##################################################################################################################
#
afficher_interface()
