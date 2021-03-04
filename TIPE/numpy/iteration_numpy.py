# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 19:43:54 2019

@author: Clement LAGNEAU
"""

import numpy as np

from copy import deepcopy

def avance(a,b,score):
    global n
    c=deepcopy(a)
    for ligne in range(n):
        for colonne in range(n):
            if a[ligne,colonne]==1:
                if b[ligne,colonne]=="d":
                    if a[ligne,colonne+1]==0 and c[ligne,colonne+1]==0:
                        c[ligne,colonne]=0
                        c[ligne,colonne+1]=1
                    if a[ligne,colonne+1]==-1:
                        c[ligne,colonne]=0
                        score+=1
                if b[ligne,colonne]=="g":
                    if a[ligne,colonne-1]==0 and c[ligne,colonne-1]==0:
                        c[ligne,colonne]=0
                        c[ligne,colonne-1]=1
                    if a[ligne,colonne-1]==-1:
                        c[ligne,colonne]=0
                        score+=1
                if b[ligne,colonne]=="b":
                    if a[ligne+1,colonne]==0 and c[ligne+1,colonne]==0:
                        c[ligne,colonne]=0
                        c[ligne+1,colonne]=1
                    if a[ligne+1,colonne]==-1:
                        c[ligne,colonne]=0
                        score+=1
                if b[ligne,colonne]=="h":
                    if a[ligne-1,colonne]==0 and c[ligne-1,colonne]==0:
                        c[ligne,colonne]=0
                        c[ligne-1,colonne]=1
                    if a[ligne-1,colonne]==-1:
                        c[ligne,colonne]=0
                        score+=1
    return(c,score)


