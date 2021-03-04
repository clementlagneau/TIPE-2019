# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 13:30:39 2018

@author: Clement LAGNEAU
"""
#Nombre
n= 10

#Rapport visible/n
k = 50

vivants = 2

import baground
import iteration
import strategie

def principal(nbiteration):
    a = baground.baground_test1(n)
    b = strategie.strategie(a)
    c = iteration.deepcopy(a)
    score=0
    i=0
    while i<nbiteration and score<vivants:
        c,score=iteration.avance(c,b,score)
        i+=1
    return(a,b,c,score,i)


