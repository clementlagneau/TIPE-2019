# -*- coding: utf-8 -*-
"""
Created on Mon May 20 08:38:02 2019

@author: Clement LAGNEAU
"""

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
import numpy as np

def avance(a,b,score):
    """
    Fonction qui prend en argument un baground a et une table de stategie b
    et un score
    Renvoie le prochain itere et le score
    """
    n=len(a)
    c=np.copy(a)
    #On fait tous les indices
    for ligne in range(n):
        for colonne in range(n):
            if a[ligne,colonne]==1:
                # On avance
                if b[ligne,colonne]==5:
                    if a[ligne,colonne+1]==0 and c[ligne,colonne+1]==0:
                        c[ligne,colonne]=0
                        c[ligne,colonne+1]=1
                    if a[ligne,colonne+1]==-1:
                        c[ligne,colonne]=0
                        score+=1
                if b[ligne,colonne]==6:
                    if a[ligne,colonne-1]==0 and c[ligne,colonne-1]==0:
                        c[ligne,colonne]=0
                        c[ligne,colonne-1]=1
                    if a[ligne,colonne-1]==-1:
                        c[ligne,colonne]=0
                        score+=1
                if b[ligne,colonne]==3:
                    if a[ligne+1,colonne]==0 and c[ligne+1,colonne]==0:
                        c[ligne,colonne]=0
                        c[ligne+1,colonne]=1
                    if a[ligne+1,colonne]==-1:
                        c[ligne,colonne]=0
                        score+=1
                if b[ligne,colonne]==4:
                    if a[ligne-1,colonne]==0 and c[ligne-1,colonne]==0:
                        c[ligne,colonne]=0
                        c[ligne-1,colonne]=1
                    if a[ligne-1,colonne]==-1:
                        c[ligne,colonne]=0
                        score+=1
    return(c,score)


