# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 18:27:06 2018

@author: Clement LAGNEAU
"""

import tkinter

haut = 30 # hauteur du tableau
larg = 30 # largeur du tableau
cote = 15 # côté d'une cellule
vivant = 1
mort = 0
# Créer les matrices
cell = [[0 for row in range(haut)] for col in range(larg)]
etat = [[mort for row in range(haut)] for col in range(larg)]
temp = [[mort for row in range(haut)] for col in range(larg)]




fenetre = Tk()
fenetre.title("Torus")
canvas = Canvas(fenetre, width=cote*larg, height=cote*haut, highlightthickness=0)
canvas.pack()
init()
tableau()
fenetre.mainloop()