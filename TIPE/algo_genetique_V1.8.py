# -*- coding: utf-8 -*-
"""

TIPE CLEMENT LAGNEAU 2019

Algorithme genetique
"""

#Nombre
n= 10

#Rapport visible/n
k = 50

#taille de liste
i=30

it=n*n

import os
import random 
import fond
import iteration
import strategie
from copy import deepcopy

def cle(x):
    return(x[0:2])

def nbvivant(t,n):
    res=0
    for i in range(n):
        for j in range(n):
            if t[i][j]==1:
                res += 1
    return(res)

fd=fond.fond_2

vivants = nbvivant(fd(n),n)

# nb de changement dynamique
changement = 10

def meilleur_init():
    """
    Renvoie la liste initiale avec comme liste de sortie :
        [0]: score
        [1]: nbiteration max
        [2]: la table de strategie
    """
    liste = []
    for x in range(i):
        a = fd(n)
        b = strategie.strategie(a)
        c = principal(it,a,b)
        liste.append((c[1],c[0],b))
    liste=sorted(liste,key=cle,reverse=True)
    return(liste)

def fusion_liste(liste,n):
    """
    Renvoie la liste apres la mutation
    """
    l=[]
    for x in range(3*i//4):
        l.append(deepcopy(liste[x][2]))
    choix=random.sample(liste,i//8)
    for x in range(i//8):
        l.append(fusion(choix[x][2],n))
    for x in range(i//8):
        l.append(fusion2(liste[x][2],liste[i//8+x][2],n))
    return(l)

def meilleur_apres(liste):
    """
    Renvoie la liste apres une iteration de l algorithme genetique
    """
    liste_apres=[]
    for b in liste:
        a = fd(n)
        c = principal(it,a,b)
        liste_apres.append((c[1],c[0],b))
    liste_apres=sorted(liste_apres,key=cle,reverse=True)
    return(liste_apres)

def principal(nbiteration,a,b):
    """
    Renvoie le nombre max d iteration et le score pour une table
    """
    c = deepcopy(a)
    score=0
    i=0
    while i<nbiteration and score<vivants:
        c,score=iteration.avance(c,b,score)
        i+=1
    return(i,score)


def fusion(liste,n):
    """
    Renvoie la liste en effectuant /changement/ changements sur les cases
    """
    r=deepcopy(liste)
    for k in range(changement):
        x=random.randint(0,n-1)
        y=random.randint(0,n-1)
        r[x][y]=strategie.strategie_case(liste,x,y)
    return(r)

def fusion2(liste1,liste2,n):
    """
    Renvoie la liste fusionne de l1 et l2 suivant une proba 1/2
    """
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

nom="Res_"+str(n)+"_fond_2_"+str(i)+"_1"


os.chdir("D:/Cours/MPBIS/TIPE/")
res = open(nom,"w")
res.close()

while lapres[0][0]!=vivants and indice<50000:
    res = open(nom,"a")
    res.writelines(str((indice,lapres[0][0],changement))+"\n")
    res.close()
    changement = vivants-lapres[0][0]
    print(indice,lapres[0][0],changement)
    en_cours=fusion_liste(lapres,n)
    lapres=meilleur_apres(en_cours)
    indice +=1

res = open(nom,"a")
res.writelines(str(lapres[0][2]))
res.close()


print(lapres[0][2])

