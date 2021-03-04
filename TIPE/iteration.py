F# -*- coding: utf-8 -*-
"""

TIPE CLEMENT LAGNEAU 2019

Iteration
"""

"""
-1 : sortie
0 : libre
1 : il y a quelqu un
2 : mur
"""


from copy import deepcopy

def avance(a,b,score):
    """
    Renvoie le tableau et le score avance avec une iteration
    """
    n=len(a)
    c=deepcopy(a)
    for ligne in range(n):
        for colonne in range(n):
            if a[ligne][colonne]==1:
                # On avance
                if b[ligne][colonne]=="d":
                    if a[ligne][colonne+1]==0 and c[ligne][colonne+1]==0:
                        c[ligne][colonne]=0
                        c[ligne][colonne+1]=1
                    if a[ligne][colonne+1]==-1:
                        c[ligne][colonne]=0
                        score+=1
                if b[ligne][colonne]=="g":
                    if a[ligne][colonne-1]==0 and c[ligne][colonne-1]==0:
                        c[ligne][colonne]=0
                        c[ligne][colonne-1]=1
                    if a[ligne][colonne-1]==-1:
                        c[ligne][colonne]=0
                        score+=1
                if b[ligne][colonne]=="b":
                    if a[ligne+1][colonne]==0 and c[ligne+1][colonne]==0:
                        c[ligne][colonne]=0
                        c[ligne+1][colonne]=1
                    if a[ligne+1][colonne]==-1:
                        c[ligne][colonne]=0
                        score+=1
                if b[ligne][colonne]=="h":
                    if a[ligne-1][colonne]==0 and c[ligne-1][colonne]==0:
                        c[ligne][colonne]=0
                        c[ligne-1][colonne]=1
                    if a[ligne-1][colonne]==-1:
                        c[ligne][colonne]=0
                        score+=1
    return(c,score)


def avance2(a,b,score):
    lenx=len(a)
    leny=len(a[0])
    c=deepcopy(a)
    for ligne in range(lenx):
        for colonne in range(leny):
            if a[ligne][colonne]==1:
                # On avance
                if b[ligne][colonne]=="d":
                    if a[ligne][colonne+1]==0 and c[ligne][colonne+1]==0:
                        c[ligne][colonne]=0
                        c[ligne][colonne+1]=1
                    if a[ligne][colonne+1]==-1:
                        c[ligne][colonne]=0
                        score+=1
                if b[ligne][colonne]=="g":
                    if a[ligne][colonne-1]==0 and c[ligne][colonne-1]==0:
                        c[ligne][colonne]=0
                        c[ligne][colonne-1]=1
                    if a[ligne][colonne-1]==-1:
                        c[ligne][colonne]=0
                        score+=1
                if b[ligne][colonne]=="b":
                    if a[ligne+1][colonne]==0 and c[ligne+1][colonne]==0:
                        c[ligne][colonne]=0
                        c[ligne+1][colonne]=1
                    if a[ligne+1][colonne]==-1:
                        c[ligne][colonne]=0
                        score+=1
                if b[ligne][colonne]=="h":
                    if a[ligne-1][colonne]==0 and c[ligne-1][colonne]==0:
                        c[ligne][colonne]=0
                        c[ligne-1][colonne]=1
                    if a[ligne-1][colonne]==-1:
                        c[ligne][colonne]=0
                        score+=1
    return(c,score)

