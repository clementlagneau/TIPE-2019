# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 10:56:31 2019

@author: Clement LAGNEAU
"""

"""
-1 : sortie
0 : libre
1 : il y a quelqu un
2 : mur
"""

n=10
import tkinter 
import random
from copy import deepcopy


"""
rajout
"""
import baground

k=50

a=baground.baground_test1(n)

dico = {-1 : "red", 2 : "yellow",1 :"blue", 0: "white"}

score = 0

def init():
    for x in range(n):
        for y in range(n):
            couleur[y][x]=canvas.create_rectangle((x*k, y*k,(x+1)*k, (y+1)*k), outline="gray", fill="red")

def suivant(a,score):
    c=deepcopy(a)
    for ligne in range(n):
        for colonne in range(n):
            if a[ligne][colonne]==1:
                r=random.random()
                # On avance
                if r<0.25:
                    if a[ligne][colonne+1]==0 and c[ligne][colonne+1]==0:
                        c[ligne][colonne]=0
                        c[ligne][colonne+1]=1
                    if a[ligne][colonne+1]==-1:
                        c[ligne][colonne]=0
                        score+=1
                if 0.25<=r<0.5:
                    if a[ligne][colonne-1]==0 and c[ligne][colonne-1]==0:
                        c[ligne][colonne]=0
                        c[ligne][colonne-1]=1
                    if a[ligne][colonne-1]==-1:
                        c[ligne][colonne]=0
                        score+=1
                if 0.5<=r<0.75:
                    if a[ligne+1][colonne]==0 and c[ligne+1][colonne]==0:
                        c[ligne][colonne]=0
                        c[ligne+1][colonne]=1
                    if a[ligne+1][colonne]==-1:
                        c[ligne][colonne]=0
                        score+=1
                if 0.75<=r:
                    if a[ligne-1][colonne]==0 and c[ligne-1][colonne]==0:
                        c[ligne][colonne]=0
                        c[ligne-1][colonne]=1
                    if a[ligne-1][colonne]==-1:
                        c[ligne][colonne]=0
                        score+=1
    return(c,score)

def calcul():
    global score
    global a
    c,score=suivant(a,score)
    for x in range(n):
        for y in range(n):
            canvas.itemconfig(couleur[x][y], fill=dico[c[x][y]])
    a=deepcopy(c)
    

def final():
    calcul()
    fenetre.after(10, final)

couleur = [[0 for x in range(n)] for y in range(n)]

fenetre = tkinter.Tk()
canvas = tkinter.Canvas(fenetre, width=k*n, height=k*n, highlightthickness=0)
canvas.pack()
init()


final()
fenetre.mainloop()