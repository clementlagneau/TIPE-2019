# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 11:09:00 2018

@author: Clement LAGNEAU
"""

"""
En cours d'écriture
ne foncionne pas
"""

import baground
import iteration
import strategie

def est_cycle(b,i,j,n):
    for indice in range(n):
        ic,jc=incr(b,i,j)
        if i==ic and j==jc:
            return True
    return False
    
def incr(b,i,j):
    if b[i][j]=="d":
        return(i,j+1)
    if b[i][j]=="g":
        return(i,j-1)
    if b[i][j]=="b":
        return(i+1,j)
    if b[i][j]=="h":
        return(i-1,j)
    
    
