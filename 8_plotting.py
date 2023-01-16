# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 10:37:02 2020

@author: Hendrik
"""
#%% DNA damage
import matplotlib.pyplot as plt

# Enter all data from the table
x = [0,5,15,30,60]
y_wild = [0,0,3,10,50]
y_wild_err = [0,0,2,4,9]
y_mut = [0,42,74,89,100]
y_mut_err = [0,2,6,4,0]

### PLOT THE WILD-TYPE DATASET
# only strictly necessary, plt.errorbar() already draws lines between points (try it out without plt.plot())
plt.plot(x, y_wild, 'o', color='blue')
# the "label" keyword tells Python how to label the dataset in the legend
plt.errorbar(x, y_wild, yerr=y_wild_err, color='blue', label='wild-type')

### PLOT THE WILD-TYPE DATASET
# If a plot already exists, Python automatically draws the new dataset into the same window
plt.plot(x, y_mut, 'o', color='orange')
plt.errorbar(x, y_mut, yerr=y_mut_err, linestyle='None', color='orange', label='mutant')

# Give the plot axis labels and a title
plt.ylabel('Embryonic lethality [%]', fontsize=15)
plt.xlabel('X-ray dose [Gy]', fontsize=15)
plt.title('DNA Damage Repair capabilities of LEM-3 mutant', fontsize=16)
# Draw the legend into the window with the labels from "label"
plt.legend()

import numpy as np
a = np.array([3, 6, 0])
a[0] = a[0] + 0.6
a = a / 3
a[2] += 2.2
a = a / 2
print(a)

#%% Nautilus
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




