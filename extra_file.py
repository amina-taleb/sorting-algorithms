# Dans ce fichier, on va créer les autres fonctions (importer un fichier, générer aléatoirement ....)
import numpy as np
import random as rnd
import csv

def impot_alea(liste) :
    liste = []
    n = len(liste)
    for i in range n :
        p = rnd.randint(0, 9)
        liste.append(p)