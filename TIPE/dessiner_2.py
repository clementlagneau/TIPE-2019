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
#Rapport visible/n
k = 50


dico = {-1 : "red", 2 : "black",1 :"blue", 0: "white"}

def init():
    for x in range(n):
        for y in range(n):
            couleur[x][y]=canvas.create_rectangle((x*k, y*k,(x+1)*k, (y+1)*k), outline="gray", fill="red")

def calcul():
    global a
    c=avance(a,b)
    for x in range(n):
        for y in range(n):
            canvas.itemconfig(couleur[x][y], fill=dico[c[x][y]])
    a=deepcopy(c)
    

def final():
    calcul()
    fenetre.after(500, final)

couleur = [[0 for x in range(n)] for y in range(n)]

fenetre = tkinter.Tk()
canvas = tkinter.Canvas(fenetre, width=k*n, height=k*n, highlightthickness=0)
canvas.pack()
init()
final()
fenetre.mainloop()

