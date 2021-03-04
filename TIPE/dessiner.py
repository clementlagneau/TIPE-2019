# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 20:10:43 2018

@author: Clement LAGNEAU
"""

import tkinter 

#Rapport visible/n
k = 50
# Creation de la fenetre
fenetre = tkinter.Tk()
# Creation du canevas
canvas = tkinter.Canvas(fenetre, width=k*n, height=k*n, background='white')

def dessiner(t):
    #supprime l'ancien canvas
    canvas.delete(tkinter.ALL)
    
    #creation des lignes
    for x in range(1,n):
        canvas.create_line(x*k, 0, x*k, k*n)
        canvas.create_line(0, x*k, k*n, x*k)
    #Creation des rectangles
    for x in range(n):
        for y in range(n):
            if t[x][y] == 1: 
                canvas.create_rectangle(x*k,y*k,(x+1)*k,(y+1)*k,fill="blue")
            if t[x][y] == -1: 
                canvas.create_rectangle(x*k,y*k,(x+1)*k,(y+1)*k,fill="red")
            if t[x][y] == 2: 
                canvas.create_rectangle(x*k,y*k,(x+1)*k,(y+1)*k,fill="black")                
    canvas.pack()
    fenetre.mainloop()
