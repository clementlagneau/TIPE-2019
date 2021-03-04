# -*- coding: utf-8 -*-
"""

TIPE LAGNEAU CLEMENT 2019

Creation des fond

"""

"""
Sur les fonds :    
    0 : libre
    -1 : mur
"""

def fond(n):
    """
    Cree un fond avec des murs sur les cotes
    """
    t=[[1 for x in range(n)] for x in range(n)]
    for x in range(n):
        t[0][x]=2
        t[x][0]=2
        t[n-1][x]=2
        t[x][n-1]=2
    return(t)

def fond_1(n):
    """
    Cree un fond avec des 1 sur les bords et une sortie au centre
    """
    a=fond(n)
    a[n//2][n//2]=-1
    for x in range(1,n-1):
        a[1][x]=1
        a[x][1]=1
        a[n-2][x]=1
        a[x][n-2]=1
    return(a)

def fond_2(n):
    """
    Cree un fond avec des 1 dans les coins et une sortie dans le dernier coin
    """
    a=fond(n)
    a[n-2][n-2]=-1
    a[1][1]=1
    a[1][n-2]=1
    a[n-2][1]=1
    return(a)

def fond_3(n):
    """
    Cree un fond avec des 1 dans les coins et une sortie dans le dernier coin
    avec un mur
    """
    a=fond(n)
    a[n-2][n-2]=-1
    a[1][1]=1
    a[1][n-2]=1
    a[n-2][1]=1
    for x in range(n//2):
        a[x][n//2-1]=2
    return(a)


def avion(n):
    """
    Cree un fond de type avion
    """
    a=[[0 for x in range(n)]for x in range(n)]
    for x in range(n):
        a[0][x]=2
        a[x][0]=2
        a[n-1][x]=2
        a[x][n-1]=2
    for x in range(n//2):
        for y in range(1,n-1):
            a[2*x][y]=2
            a[2*x+1][y]=1
            a[n-1][y]=2
    for x in range(1,n-1):
        a[x][n//2]=0
        a[x][n//2-1]=0
    a[n-1][n//2]=-1
    a[n-1][n//2-1]=-1
#    a[0][n//2]=-1
#    a[0][n//2-1]=-1
    return(a)



