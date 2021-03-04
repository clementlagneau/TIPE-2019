# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 11:16:25 2018

@author: Clement LAGNEAU
"""
bof=4
def cake():
    global bof
    bof =4
    def modify(p):
        #global bof
        bof = p
        return None
    modify(2018)
    print(bof)
    
    
cake   ()
 