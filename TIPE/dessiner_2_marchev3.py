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
import os
from PIL import Image


k=50

#a=fond.fond_test1(n)
#b=strategie.strategie(a)

"""
--
"""

dico = {-1 : "red", 2 : "yellow",1 :"blue", 0: "white", 4:"cyan"}

couleur = [[0 for x in range(n)] for y in range(n)]
fenetre = tkinter.Tk()
canvas = tkinter.Canvas(fenetre, width=k*n, height=k*n, highlightthickness=0)

for x in range(n):
    for y in range(n):
        couleur[y][x]=canvas.create_rectangle((x*k, y*k,(x+1)*k, (y+1)*k), outline="gray", fill=dico[a[y][x]])




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


os.chdir("D:/Cours/MPBIS/TIPE/")

canvas.pack()




fenetre.mainloop()

