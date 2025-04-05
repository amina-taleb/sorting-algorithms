import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
import sorting

def afficher_interface() :
    window = ctk.CTk()
    ctk.set_default_color_theme('blue')
    ctk.set_appearance_mode('dark')
    window.geometry('1200x700')
    window.title('Algotric')
    window.grid_columnconfigure(0, weight=2) # 1 s'étend peu
    window.grid_columnconfigure(1, weight=3)
    window.grid_rowconfigure(0, weight=2) 
    window.grid_rowconfigure(1, weight=3)

    # un exemple à traiter :
    liste = [8, 2, 6, 9, 5, 6, 0, 4, 7, 1]
######################################################################################################################################
    frame_title = ctk.CTkFrame(master=window, fg_color='grey', height=100)
    frame_title.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
    frame_title.grid_rowconfigure(0, weight=5)
    frame_title.grid_rowconfigure(1, weight=5)
    frame_title.grid_columnconfigure(0, weight=5)
    frame_title.grid_columnconfigure(1, weight=5)
    frame_title.grid_columnconfigure(2, weight=5)

    label_01 =  ctk.CTkLabel(master=frame_title, text='Inserez les valeurs', text_color='black', font=('Arial', 20))
    label_01.grid(row=0, column=0, padx=5, pady=5)

    champ = ctk.CTkEntry(master=frame_title, placeholder_text='Exemple : 2, 4, 1, 6, 3', width=250)
    champ.grid(row=1, column=0, padx=5, pady=5)

    label_02 = ctk.CTkLabel(master=frame_title, text='Générer aléatoirement', text_color='black', font=('Arial', 20))
    label_02.grid(row=0, column=1, padx=5, pady=5)

    button_gene = ctk.CTkButton(master=frame_title, text='Générer', width=200, fg_color='green')
    button_gene.grid(row=1, column=1, padx=5, pady=5)

    label_03 = ctk.CTkLabel(master=frame_title, text='Importer un fichier', text_color='black', font=('Arial', 20))
    label_03.grid(row=0, column=2, padx=5, pady=5)

    button_imp = ctk.CTkButton(master=frame_title, text='Importer', width=200, fg_color='green')
    button_imp.grid(row=1, column=2, padx=5, pady=5)
################################################################################################################################
    frame_graph = ctk.CTkFrame(master=window, fg_color='grey')
    frame_graph.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
    
###############################################################################################################################
    # Pour le bloc menu = choisir l'algorithme
    frame_menu = ctk.CTkFrame(master=window, fg_color='grey')
    frame_menu.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
    frame_menu.grid_columnconfigure(0, weight=5)
    frame_menu.grid_rowconfigure(0, weight=5)
    frame_menu.grid_rowconfigure(1, weight=5)
    frame_menu.grid_rowconfigure(2, weight=5)
    frame_menu.grid_rowconfigure(3, weight=5)
    frame_menu.grid_rowconfigure(4, weight=5)
    frame_menu.grid_rowconfigure(5, weight=5)
    frame_menu.grid_rowconfigure(6, weight=5)
    frame_menu.grid_rowconfigure(7, weight=5)


    label1 = ctk.CTkLabel(master=frame_menu, text='Choisir un algorithme', text_color='black', font=('Arial', 20))
    label1.grid(row=0, column=0, padx=10, pady=10)

    button1  = ctk.CTkButton(master=frame_menu, text='Selection', width=200, fg_color='green' ,command=lambda : sorting.selection(liste))
    button1.grid(row=1, column=0, padx=10, pady=10)

    button2  = ctk.CTkButton(master=frame_menu, text='Inserion', width=200, fg_color='green', command=lambda : sorting.insertion(liste))
    button2.grid(row=2, column=0, padx=10, pady=10)

    button3  = ctk.CTkButton(master=frame_menu, text='Fusion', width=200, fg_color='green')
    button3.grid(row=3, column=0, padx=10, pady=10)

    button4  = ctk.CTkButton(master=frame_menu, text='Rapide', width=200, fg_color='green')
    button4.grid(row=4, column=0, padx=10, pady=10)

    button5  = ctk.CTkButton(master=frame_menu, text='Peigne', width=200, fg_color='green')
    button5.grid(row=5, column=0, padx=10, pady=10)

    button6  = ctk.CTkButton(master=frame_menu, text='Bulle', width=200, fg_color='green')
    button6.grid(row=6, column=0, padx=10, pady=10)

    button7  = ctk.CTkButton(master=frame_menu, text='Tas', width=200, fg_color='green')
    button7.grid(row=7, column=0, padx=10, pady=10)


    window.mainloop()



#lancer l'interface :
#afficher_interface()