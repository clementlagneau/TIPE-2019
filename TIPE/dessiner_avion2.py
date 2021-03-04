# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 10:26:25 2018

@author: Clement LAGNEAU
"""
from copy import deepcopy
from avion import a
from strategie import strat2
from iteration import avance2
#b=strat2(a)

k=40
n=20


import tkinter 

dico = {-1 : "red", 2 : "yellow",1 :"blue", 0: "white"}
score = 0
def init():
    for x in range(9):
        for y in range(n):
            couleur[y][x]=canvas.create_rectangle((x*k, y*k,(x+1)*k, (y+1)*k), outline="gray", fill="red")

def calcul():
    global score
    global a
    c,score=avance2(a,b,score)
    for y in range(9):
        for x in range(n):
            canvas.itemconfig(couleur[x][y], fill=dico[c[x][y]])
    a=deepcopy(c)
    

def final():
    calcul()
    fenetre.after(1000, final)

couleur = [[0 for x in range(9)] for y in range(n)]

fenetre = tkinter.Tk()
canvas = tkinter.Canvas(fenetre, width=k*n, height=k*n, highlightthickness=0)
canvas.pack()
init()
for y in range(9):
    for x in range(n):
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

"""

[['s', 's', 's', 's', 'g', 's', 's', 's', 's'], ['i', 'i', 'i', 'i', 'h', 'i', 'i', 'i', 'i'], ['i', 'd', 'd', 'd', 'h', 'g', 'g', 'g', 'i'], ['i', 'i', 'i', 'i', 'h', 'i', 'i', 'i', 'i'], ['i', 'd', 'd', 'd', 'h', 'g', 'g', 'g', 'i'], ['i', 'i', 'i', 'i', 'h', 'i', 'i', 'i', 'i'], ['i', 'd', 'd', 'd', 'h', 'g', 'g', 'g', 'i'], ['i', 'i', 'i', 'i', 'h', 'i', 'i', 'i', 'i'], ['i', 'd', 'd', 'd', 'h', 'g', 'g', 'g', 'i'], ['i', 'i', 'i', 'i', 'b', 'i', 'i', 'i', 'i'], ['i', 'd', 'd', 'd', 'b', 'g', 'g', 'g', 'i'], ['i', 'i', 'i', 'i', 'b', 'i', 'i', 'i', 'i'], ['i', 'd', 'd', 'd', 'b', 'g', 'g', 'g', 'i'], ['i', 'i', 'i', 'i', 'b', 'i', 'i', 'i', 'i'], ['i', 'd', 'd', 'd', 'b', 'g', 'g', 'g', 'i'], ['i', 'i', 'i', 'i', 'b', 'i', 'i', 'i', 'i'], ['i', 'd', 'd', 'd', 'b', 'g', 'g', 'g', 'i'], ['i', 'i', 'i', 'i', 'b', 'i', 'i', 'i', 'i'], ['i', 'i', 'i', 'i', 'b', 'i', 'i', 'i', 'i'], ['i', 's', 's', 's', 'd', 's', 's', 's', 'i']]

"""