# -*- coding: utf-8 -*-
"""
Created on Mon May 20 09:09:13 2019

@author: Clement LAGNEAU
"""
"""
iteration
-1 : sortie : de couuleur rouge
0 : libre : de couleur blanche
1 : il y a quelqu un : de couleur bleu
2 : mur : de couleur jaune

strategie :
3 : haut
4 : bas
5 : droite
6 : gauche
7 : impossible
8 : sortie
"""

import tkinter 
import it_num_v0
import numpy as np
import st_num_v0
import ba_num_v0

#Rapport pixel / n
k=50
n=10

"""
a=ba_num_v0.baground_test1(n)
b=st_num_v0.strategie(a)
"""


dico = {-1 : "red", 2 : "yellow",1 :"blue", 0: "white"}
score = 0


def init():
    for x in range(n):
        for y in range(n):
            couleur[x,y]=canvas.create_rectangle((x*k, y*k,(x+1)*k, (y+1)*k), outline="gray", fill="red")

def calcul():
    global score
    global a
    c,score=it_num_v0.avance(a,b,score)
    for x in range(n):
        for y in range(n):
            canvas.itemconfig(couleur[x,y], fill=dico[c[x,y]])
    a=c


def final():
    calcul()
    fenetre.after(1000, final)

couleur = np.zeros((n,n),int)

fenetre = tkinter.Tk()
canvas = tkinter.Canvas(fenetre, width=k*n, height=k*n, highlightthickness=0)
canvas.pack()
init()
for x in range(n):
    for y in range(n):
        if b[x,y] == 3: 
            canvas.create_line(((y+0.5)*k, (x+0.5)*k, (y+0.5)*k, (x-0.5)*k),arrow='last')
        if b[x,y] == 4: 
            canvas.create_line(((y+0.5)*k, (x+0.5)*k, (y+0.5)*k, (x+1.5)*k),arrow='last')     
        if b[x,y] == 5: 
            canvas.create_line(((y+0.5)*k, (x+0.5)*k, (y+1.5)*k, (x+0.5)*k),arrow='last')     
        if b[x,y] == 6: 
            canvas.create_line(((y+0.5)*k, (x+0.5)*k, (y-0.5)*k, (x+0.5)*k),arrow='last')

final()
fenetre.mainloop()

