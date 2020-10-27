# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 10:37:02 2020

@author: Hendrik
"""

import numpy as np
import matplotlib.pyplot as plt

gamma = 1.79 
num = np.linspace(0,5,500) 
x = gamma**(4*num)*np.cos(2*np.pi*num) 
y = gamma**(4*num)*np.sin(2*np.pi*num) 
plt.plot(x,y,'o',color='yellow',markeredgecolor='yellow') 
ax = plt.gca()   # stands for get-current-axes 
ax.set_aspect('equal') 
ax.xaxis.set_visible(False) 
ax.yaxis.set_visible(False) 
ax.set_facecolor("black")


def sum_average(l):
    return sum(l), sum(l)/len(l)

l = [5.75, 5.37, 2.45, 8.22, 7.45, 1.89, 3.82, 2.49]
summe, mean = sum_average(l)
print(int(summe * mean))