# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 10:19:34 2019

@author: Clement LAGNEAU
"""

#Nombre
n= 20

#Rapport visible/n
k = 50

#taille de liste
i=n*n

it=n

import baground
import iteration
import strategie
from copy import deepcopy

def nbvivant(t,n):
    res=0
    for i in range(n):
        for j in range(n):
            if t[i][j]==1:
                res += 1
    return(res)

vivants = nbvivant(baground.baground_test1(n),n)


def meilleur_init():
    """
    renvoie la liste :
        [0]: score
        [1]: nbiteration max
        [2]: la table de strategie
    """
    liste = []
    for x in range(i):
        a = baground.baground_test1(n)
        b = strategie.strategie(a)
        c = principal(it,a,b)
        liste.append((c[1],c[0],b))
    liste=sorted(liste,reverse=True)
    return(liste)

def fusion_liste(liste,n):
    l=[]
    i = len(liste)
    for x in range(i//4):
        l.append(deepcopy(liste[x][2]))
    for x in range(i//4):
        l.append(fusion1(deepcopy(liste[2*x][2]),deepcopy(liste[2*x+1][2]),n))
    for x in range(i//4):
        l.append(fusion2(deepcopy(liste[x][2]),deepcopy(liste[x+i//2][2]),n))
    for x in range(i//4):
        l.append(strategie.strategie(baground.baground_test1(n)))
    return(l)

def meilleur_apres(liste):
    liste_apres=[]
    for b in liste:
        a = baground.baground_test1(n)
        c = principal(it,a,b)
        liste_apres.append((c[1],c[0],b))
    liste_apres=sorted(liste_apres,reverse=True)
    return(liste_apres)

def principal(nbiteration,a,b):
    c = deepcopy(a)
    score=0
    i=0
    while i<nbiteration and score<vivants:
        c,score=iteration.avance(c,b,score)
        i+=1
    return(i,score)


def fusion1(a,b,n):
    """
    fusions horizontale
    """
    c=[]
    e=n//2
    for x in range(e):
        c.append(deepcopy(a[x]))
    for x in range(n-e):
        c.append(deepcopy(b[e+x]))
    return(c)

def fusion2(a,b,n):
    """
    fusions verticale
    """
    c=[]
    e=n//2
    for x in range(n):
        c.append([])
        for y in range(e):
            c[x].append(a[x][y])
    for x in range(n):
        for y in range(e):
            c[x].append(b[x][y+e])
    return(c)

en_cours=[]
l=meilleur_init()

indice=0
while l[0][0]!=vivants and indice<1000000:
    print(indice,l[0][0])
    en_cours=fusion_liste(l,n)
    l=meilleur_apres(en_cours)
    indice +=1

print(l[0][2])




