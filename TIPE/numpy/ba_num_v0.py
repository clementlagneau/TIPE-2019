# -*- coding: utf-8 -*-
"""
Created on Mon May 20 09:02:03 2019

@author: Clement LAGNEAU
"""

import numpy as np

"""
-1: sortie
0 : libre
2 : mur
"""

def baground(n):
    t=np.zeros((n,n),int)
    for x in range(n):
        t[0,x]=2
        t[x,0]=2
        t[n-1,x]=2
        t[x,n-1]=2
    return(t)

def baground_test1(n):
    a=baground(n)
    a[n//2,n//2]=-1
    for x in range(1,n-1):
        a[1,x]=1
        a[x,1]=1
        a[n-2,x]=1
        a[x,n-2]=1
    return(a)



