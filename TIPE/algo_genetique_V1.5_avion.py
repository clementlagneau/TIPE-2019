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
n= 20

#Rapport visible/n
k = 50

#taille de liste
i=100

it=n*n

import random 
import iteration
import strategie
from copy import deepcopy
from avion import baground


def nbvivant(t,n):
    res=0
    for i in range(len(t)):
        for j in range(len(t[0])):
            if t[i][j]==1:
                res += 1
    return(res)

vivants = nbvivant(baground,n)

# nb de changement dynamique
changement = vivants

def meilleur_init():
    """
    renvoie la liste :
        [0]: score
        [1]: nbiteration max
        [2]: la table de strategie
    """
    liste = []
    for x in range(i):
        a = deepcopy(baground)
        b = strategie.strat2(a)
        c = principal(it,a,b)
        liste.append((c[1],c[0],b))
    liste=sorted(liste,reverse=True)
    return(liste)

def fusion_liste(liste,n): #  3*i//4  i//8  i//8
    l=[]
    for x in range(i//2):
        l.append(deepcopy(liste[x][2]))
    choix=random.sample(liste,i//4)
    for x in range(i//4):
        l.append(fusion(choix[x][2],n))
    for x in range(i//4):
        l.append(fusion2(liste[i//8+x][2],liste[i//4+x][2],n))
    return(l)

def meilleur_apres(liste):
    liste_apres=[]
    for b in liste:
        a = deepcopy(baground)
        c = principal(it,a,b)
        liste_apres.append((c[1],c[0],b))
    liste_apres=sorted(liste_apres,reverse=True)
    return(liste_apres)

def principal(nbiteration,a,b):
    c = deepcopy(a)
    score=0
    i=0
    while i<nbiteration and score<vivants:
        c,score=iteration.avance2(c,b,score)
        i+=1
    return(i,score)


def fusion(liste,n):
    r=deepcopy(liste)
    for k in range(changement):
        x=random.randint(0,len(baground)-1)
        y=random.randint(0,len(baground[0])-1)
        r[x][y]=strategie.strategie_case(liste,x,y)
    return(r)

def fusion2(liste1,liste2,n):
    r=deepcopy(liste1)
    for x in range(len(baground)):
        for y in range(len(baground[0])):
            t=random.random()
            if t<0.5:
                r[x][y]=liste2[x][y]
    return(r)
    

en_cours=[]
lapres=meilleur_init()

indice=0
while lapres[0][0]!=vivants and indice<1000000:
    changement = (vivants -lapres[0][0])
    print(indice,lapres[0][0],changement)
    en_cours=fusion_liste(lapres,n)
    lapres=meilleur_apres(en_cours)
    indice +=1

print(lapres[0][2])

