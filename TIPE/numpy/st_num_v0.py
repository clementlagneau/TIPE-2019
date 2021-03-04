# -*- coding: utf-8 -*-
"""
Created on Mon May 20 08:45:32 2019

@author: Clement LAGNEAU
"""
import numpy as np
import random

"""
iteration
-1 : sortie
0 : libre
1 : il y a quelqu un
2 : mur

strategie :
3 : haut
4 : bas
5 : droite
6 : gauche
7 : impossible
8 : sortie
"""


def strategie(t):
    """
    Renvoie une strategie adaptee au tableau t
    strategie(t)
    """
    n=len(t)
    strat=np.zeros((n,n),int)
    for x in range(n):
        for y in range(n):
            if t[x,y] == 2:
                strat[x,y]=7
            elif t[x,y] == -1:
                strat[x,y]=8
            else:
                strat[x,y]=random.randrange(3,7)
    return(strat)

def strategie_case(t,x,y):
    """
    Renvoie une valeur adaptee de la case x y de t
    strategie_case(t,x,y)
    """
    if t[x,y] == 7:
        return(7)
    elif t[x,y] == -1:
        return(8)
    else:
        return(random.randrange(3,7))
