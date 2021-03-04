# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 20:53:14 2018

@author: Clement LAGNEAU
"""
"""
-1 : sortie
0 : libre
1 : il y a quelqu un
2 : mur
"""


import tkinter 
import iteration
from copy import deepcopy


"""
rajout
"""
import baground
import strategie

k=50

#a=baground.baground_test1(n)
#b=strategie.strategie(a)

"""
--
"""

dico = {-1 : "red", 2 : "yellow",1 :"blue", 0: "white"}
score = 0
def init():
    for x in range(n):
        for y in range(n):
            couleur[y][x]=canvas.create_rectangle((x*k, y*k,(x+1)*k, (y+1)*k), outline="gray", fill=dico[b[x][y]])

def calcul():
    global score
    global a
    c,score=iteration.avance(a,b,score)
    for x in range(n):
        for y in range(n):
            canvas.itemconfig(couleur[x][y], fill=dico[c[x][y]])
    a=deepcopy(c)
    

def final():
    calcul()
    fenetre.after(1000, final)

couleur = [[0 for x in range(n)] for y in range(n)]

fenetre = tkinter.Tk()
canvas = tkinter.Canvas(fenetre, width=k*n, height=k*n, highlightthickness=0)
canvas.pack()
init()
for x in range(n):
    for y in range(n):
        if b[x][y] == "h": 
            canvas.create_line(((y+0.5)*k, (x+0.5)*k, (y+0.5)*k, (x-0.5)*k),arrow='last')
        if b[x][y] == "b": 
            canvas.create_line(((y+0.5)*k, (x+0.5)*k, (y+0.5)*k, (x+1.5)*k),arrow='last')     
        if b[x][y] == "d": 
            canvas.create_line(((y+0.5)*k, (x+0.5)*k, (y+1.5)*k, (x+0.5)*k),arrow='last')     
        if b[x][y] == "g": 
            canvas.create_line(((y+0.5)*k, (x+0.5)*k, (y-0.5)*k, (x+0.5)*k),arrow='last')



final()
fenetre.mainloop()

