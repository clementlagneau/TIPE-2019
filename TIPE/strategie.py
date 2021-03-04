# -*- coding: utf-8 -*-
"""

TIPE CLEMENT LAGNEAU

Strategie
"""



"""
A[ligne][colonne]
strategie :
    h : haut
    b : bas
    d : droite
    g : gauche
    i : impossible
"""

import random

def strategie(t):
    """
    Renvoie une strategie adaptee au fond t
    """
    n=len(t)
    strat=[["" for x in range(n)] for x in range(n)]
    for x in range(n):
        for y in range(n):
            if t[x][y] == 2:
                strat[x][y]="i"
            elif t[x][y] == -1:
                strat[x][y]="s"
            else:
                r=random.random()
                if r<=0.25:
                    strat[x][y]="h"
                elif 0.25<r<=0.5:
                     strat[x][y]="b"
                elif 0.5<r<=0.75:
                     strat[x][y]="d"
                else:
                     strat[x][y]="g"
    return(strat)

def strategie_case(t,x,y):
    """
    Renvoie une strategie adaptee a la case x y du fond t
    """
    if t[x][y] == "i":
        return("i")
    elif t[x][y] == "s":
        return("s")
    else:
        r=random.random()
        if r<=0.25:
            return("h")
        elif 0.25<r<=0.5:
            return("b")
        elif 0.5<r<=0.75:
             return("d")
        else:
             return("g")


def strat2(t):
    leny=len(t[0])
    lenx=len(t)
    strat=[["" for y in range(leny)] for x in range(lenx)]
    for x in range(lenx):
        for y in range(leny):
            if t[x][y] == 2:
                strat[x][y]="i"
            elif t[x][y] == -1:
                strat[x][y]="s"
            else:
                r=random.random()
                if r<=0.25:
                    strat[x][y]="h"
                elif 0.25<r<=0.5:
                     strat[x][y]="b"
                elif 0.5<r<=0.75:
                     strat[x][y]="d"
                else:
                     strat[x][y]="g"
    return(strat)
