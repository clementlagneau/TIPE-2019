# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 19:45:17 2018

@author: Clement LAGNEAU
"""

import tkinter 

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

#Creation des rectangles  create_rectangle(x1,y1,x2,y2)
#create_rectangle(x1,y1,x2,y2)
x,y=4,4
canvas.create_rectangle(x*k,y*k,(x+1)*k,(y+1)*k,fill="black")

canvas.pack()

fenetre.mainloop()

    