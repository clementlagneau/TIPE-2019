# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 09:58:23 2018

@author: Clement LAGNEAU
"""

import random

"""
A[ligne][colonne]
strategie :
    h : haut
    b : bas
    d : droite
    g : gauche
    i : impossible
"""


def strategie(t):
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
