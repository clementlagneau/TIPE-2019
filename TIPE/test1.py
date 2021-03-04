# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 10:25:39 2018

@author: Clement LAGNEAU
"""

n=10 #taille du tableau

Init = [[0 for x in range(n)] for x in range(n)]

# 0 de base
# 1 est en vie
# 2 mur

def print_perso(A):
    for x in A:
        print(x)

print_perso(A)


def avance(A,B,x,y):
    a=abs(x-n)
    b=abs(y-n)
    if a<b or x<y:
        if a<x:
            fuite_droite(A,B,x,y)
        else:
            fuite_gauche(A,B,x,y)
    else:
        if b<y:
            fuite_bas(A,B,x,y)
        else:
            fuite_haut(A,B,x,y)


def fuite_droite(A,B,x,y):
    if A[x+1][y]==0:
        B[x+1][y]=0
    if A[x+1][y]==0:
        B[x+1][y]=0

    

def interation(A):
    B=Init.copy()
    for x in range(n):
        for y in range(n):
            if A[x][y] == 1:
                avance(A,B,x,y)
            