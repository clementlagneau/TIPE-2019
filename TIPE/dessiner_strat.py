# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 22:03:39 2018

@author: Clement LAGNEAU
"""
import tkinter 


def dessiner_strat(b):
    #Rapport visible/n
    k = 50
    # Creation de la fenetre
    fenetre = tkinter.Tk()
    # Creation du canevas
    canvas = tkinter.Canvas(fenetre, width=k*n, height=k*n, background='white')
    
    #creation des lignes
    for x in range(1,n):
        canvas.create_line(x*k, 0, x*k, k*n)
        canvas.create_line(0, x*k, k*n, x*k)
        
    #Creation des rectangles
    for x in range(n):
        for y in range(n):
            if b[x][y] == "s":
                canvas.create_rectangle((x*k, y*k,(x+1)*k, (y+1)*k), outline="gray", fill="red")
            if b[x][y] == "i":
                canvas.create_rectangle((x*k, y*k,(x+1)*k, (y+1)*k), outline="gray", fill="yellow")  
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

    
    canvas.pack()
    fenetre.mainloop()

