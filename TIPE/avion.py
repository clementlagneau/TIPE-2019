# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 11:18:56 2018

@author: Clement LAGNEAU
"""

n=10
"""
-1 : sortie
0 : libre
1 : il y a quelqu un
2 : mur
"""

A=[[0 for x in range(n)]for x in range(n)]
for x in range(1,n//2):
    for y in range(9):
        A[2*x][y]=1
        A[2*x+1][y]=2

for x in range(n):
    A[x][0]=2
    A[x][8]=2
    A[0][x]=-1
    A[1][x]=2
    A[n-2][x]=2
    A[n-1][x]=-1

for x in range(n):
    A[x][4]=0

baground=[]
for x in range(n):
    baground.append(A[x][:9])
baground[n-1][4]=-1
