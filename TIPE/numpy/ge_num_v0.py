# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 10:47:45 2019

@author: Clement LAGNEAU
"""

#Nombre
n= 10

#Rapport visible/n
k = 50

#taille de liste
i=20

#nombre d iteration max
it=n*4

import random
import it_num_v0
import st_num_v0
import ba_num_v0

def comp(h):
    return(h[0:1])

def nbvivant(t,n):
    res=0
    for i in range(n):
        for j in range(n):
            if t[i,j]==1:
                res += 1
    return(res)

vivants = nbvivant(ba_num_v0.baground_test1(n),n)

# nb de changement dynamique
changement = 40

def meilleur_init():
    """
    renvoie la liste :
        [0]: score
        [1]: nbiteration max
        [2]: la table de strategie
    """
    liste = []
    for x in range(i):
        a = ba_num_v0.baground_test1(n)
        b = st_num_v0.strategie(a)
        c = principal(it,a,b)
        liste.append((c[1],c[0],b))
    liste.sort(key=comp,reverse=True)
    return(liste)

#def fusion_liste(liste,n):
#    l=[]
#    for x in range(i//2):
#        l.append(liste[x][2])
#    choix=random.sample(liste,i//4)
#    for x in range(i//4):
#        l.append(fusion(choix[x][2],n))
#    for x in range(i//2):
#        l.append(fusion2(liste[x][2],liste[i//2+x][2],n))
#    return(l)
#
def meilleur_apres(liste):
    liste_apres=[]
    for b in liste:
        a = ba_num_v0.baground_test1(n)
        c = principal(it,a,b)
        liste_apres.append((c[1],c[0],b))
    liste_apres.sort(key=comp,reverse=True)
    return(liste_apres)

def fusion_liste(liste,n):
    l=[]
    for x in range(3*i//4):
        l.append(liste[x][2])
    for x in range(i//4):
        l.append(fusion(liste[x][2],liste[x+i//4][2],n))
    return(l)

def fusion(t1,t2,n):
    for x in range(n):
        for y in range(n):
            if random.random()<0.5:
                t1[x,y]=t2[x,y]
    return(t1)


def principal(nbiteration,a,b):
    score=0
    i=0
    while i<nbiteration and score<vivants:
        c,score=it_num_v0.avance(a,b,score)
        i+=1
    return(i,score)


#def fusion(t,n):
#    for k in range(changement):
#        x=random.randint(0,n-1)
#        y=random.randint(0,n-1)
#        t[x,y]=st_num_v0.strategie_case(t,x,y)
#    return(t)
#
#def fusion2(t1,t2,n):
#    for x in range(n):
#        for y in range(n):
#            t=random.random()
#            if t<0.5:
#                t1[x,y]=t2[x,y]
#    return(t1)
#    

en_cours=[]
lapres=meilleur_init()

indice=0
while lapres[0][0]!=vivants and indice<100:
    #changement = (vivants -lapres[0][0])
    print(indice,lapres[0][0],changement)
    en_cours=fusion_liste(lapres,n)
    lapres=meilleur_apres(en_cours)
    indice +=1

print(lapres[0][2])