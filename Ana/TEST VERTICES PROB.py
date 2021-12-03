# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 18:41:02 2021

@author: anaba
"""

#%%
#11_ Chapter 11, problem: cell vertices, areas, and testing cell shape change during growth.

#file names: "cv"and "vp"

import numpy as np
from numpy import polyfit


#1. Open both text file, #make lists of lists:
    
def data_lists(filename):
    fyle=open(filename + ".txt")
    dd=fyle.readlines()
    fyle.close()
    
    dd_list=[]
    for line in dd:
        line=line.strip().split()
        dd_list.append(line)
    return dd_list

vertices=data_lists("cv")
positions=data_lists("vp")


#List of x-positions for every cell
#List of y-positions for every cell
#def cell_positions():
dyct_pos={}
for cell, lyst in enumerate(vertices):
     for vertex in lyst:
        for i, pos in enumerate(positions):
             if vertex==i:
                 dyct_pos[vertex]=pos
print(dyct_pos)

                
                


#%%WARM UP

x_positions = [4.6, 4.5, 9.1, 2.2, 6.2, 7.6, 5.4, 9.3, 2.5, 2.6, 7.1, 
               8.9, 4.2, 3.1, 6.2, 1.4, 2.9, 9.7, 3.5, 5.2, 1.1, 9.3]
vertex_numbers = [2, 4, 11, 16, 18]
value=1
for i, el in enumerate(x_positions):
    for el2 in vertex_numbers:
        if el2==i:
            new_value=value*el
            value=new_value
print(value)