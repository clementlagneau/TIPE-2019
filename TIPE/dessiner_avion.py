# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 10:22:39 2018

@author: Clement LAGNEAU
"""

k=50

import tkinter 

dico = {-1 : "red", 2 : "yellow",1 :"blue", 0: "white"}

couleur = [[0 for x in range(n)] for y in range(n)]

fenetre = tkinter.Tk()
canvas = tkinter.Canvas(fenetre, width=k*n, height=k*n, highlightthickness=0)
canvas.pack()

for x in range(n):
    for y in range(n):
        couleur[y][x]=canvas.create_rectangle((x*k, y*k,(x+1)*k, (y+1)*k), outline="gray", fill="red")

for x in range(n):
    for y in range(n):
        canvas.itemconfig(couleur[x][y], fill=dico[c[x][y]])


fenetre.mainloop()

