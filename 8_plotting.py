# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 10:37:02 2020

@author: Hendrik
"""

import numpy as np
import matplotlib.pyplot as plt
import math

gamma = 1.52
num = np.linspace(1, 4, 500)
x = gamma**(4*num)*np.cos(2*np.pi*num)
y = gamma**(4*num)*np.sin(2*np.pi*num) 
plt.plot(x,y,'o',color='yellow',markeredgecolor='yellow')
ax = plt.gca()   # stands for get-current-axes 
ax.set_aspect('equal') 
ax.xaxis.set_visible(False) 
ax.yaxis.set_visible(False) 
ax.set_facecolor("black")


import matplotlib.pyplot as pl
from numpy import linspace, pi, cos, sin

growth_factor = 1.54
t = linspace(0, 5)

x = (growth_factor ** (4 * t)) * cos(2 * pi * t)
y = (growth_factor ** (4 * t)) * sin(2 * pi * t)

pl.plot(x, y)




