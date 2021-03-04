# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 10:47:45 2019

@author: Clement LAGNEAU
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 10:19:34 2019

@author: Clement LAGNEAU
"""

#Nombre
n= 10

#Rapport visible/n
k = 50

#taille de liste
i=200

it=n*8

import os
import random 
import baground
import iteration
import strategie
from copy import deepcopy

def comp(x):
    return(x[0:2])

def nbvivant(t,n):
    res=0
    for i in range(n):
        for j in range(n):
            if t[i][j]==1:
                res += 1
    return(res)

bag=baground.avion

vivants = nbvivant(bag(n),n)

# nb de changement dynamique
changement = n

def meilleur_init():
    """
    renvoie la liste :
        [0]: score
        [1]: nbiteration max
        [2]: la table de strategie
    """
    liste = []
    for x in range(i):
        a = bag(n)
        b = strategie.strategie(a)
        c = principal(it,a,b)
        liste.append((c[1],c[0],b))
    liste=sorted(liste,key=comp,reverse=True)
    return(liste)

def fusion_liste(liste,n): #  3*i//4  i//8  i//8
    l=[]
    for x in range(7*i//8):
        l.append(deepcopy(liste[x][2]))
    for x in range(i//8):
        l.append(fusion2(liste[x][2],liste[i//8+x][2],n))
    return(l)

def meilleur_apres(liste):
    liste_apres=[]
    for b in liste:
        a = bag(n)
        c = principal(it,a,b)
        liste_apres.append((c[1],c[0],b))
    liste_apres=sorted(liste_apres,key=comp,reverse=True)
    return(liste_apres)

def principal(nbiteration,a,b):
    c = deepcopy(a)
    score=0
    i=0
    while i<nbiteration and score<vivants:
        c,score=iteration.avance(c,b,score)
        i+=1
    return(i,score)


def fusion2(liste1,liste2,n):
    r=deepcopy(liste1)
    for x in range(10):
        for y in range(10):
            t=random.random()
            if t<0.5:
                r[x][y]=liste2[x][y]
    return(r)
    

en_cours=[]
lapres=meilleur_init()

indice=0


os.chdir("D:/Cours/MPBIS/TIPE/")
res = open("resultats_test1_4","w")


while lapres[0][0]!=vivants and indice<500:
    res.writelines(str((indice,lapres[0][0],changement))+"\n")
    changement = (vivants -lapres[0][0])*3
    print(indice,lapres[0][0],changement)
    en_cours=fusion_liste(lapres,n)
    lapres=meilleur_apres(en_cours)
    indice +=1

res.writelines(str(lapres[0][2]))
res.close()

print(lapres[0][2])

