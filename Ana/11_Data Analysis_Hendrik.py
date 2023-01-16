# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 17:56:31 2021

@author: anaba
"""
#11_ Cell Polygons

#1. import libraries:

#for plotting the polygons:
import numpy as np   
import matplotlib.pyplot as plt
from numpy import array
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
# triangle_positions = [[0,0],[0.3,0.3],[0.5,0.1]]
# quadrilateral_positions = [[0.5,0.1],[0.3,0.3],[0.6,0.5],[0.8,0.4]]
# pentagon_positions =[[0.6,0],[0.5,0.1],[0.8,0.4],[0.9,0.3],[0.7,0.02]]

# polygs = []
# polygs.append(Polygon(triangle_positions))
# polygs.append(Polygon(quadrilateral_positions))
# polygs.append(Polygon(pentagon_positions))
# patches = PatchCollection(polygs)
# patches.set_cmap('jet') #color map
# patches.set_array(array([3,2.5,1])) #for colors

# fig=plt.figure()
# panel=plt.gca()
# panel.add_collection(patches)
# fig.colorbar(patches)
# panel.autoscale(True)
# panel.set_aspect('equal')
# plt.show()

#calculating regression/fit?
import numpy as np
from numpy import polyfit


#Define functions:

#open both text files
#make lists of lists: cv with integers, vp with floats
def data_lists(filename):
    fyle=open(filename + ".txt")
    dd=fyle.readlines()
    fyle.close()
    
    dd_list=[]
    for line in dd:
        line=line.strip().split()
        dd_list.append(line)
    return dd_list

cell_vertices=data_lists("cv")
positions=data_lists("vp")

#print(cell_vertices[1])
#print(positions[1])

#List of x-positions for every cell
#List of y-positions for every cell
#def cell_positions():
lyst_x=[]
lyst_y=[]
for lyst in cell_vertices: 
    cell_x=[]
    cell_y=[]
    for vertex in lyst:
        print(vertex)
        for i, coords in enumerate(positions):
#             if vertex==i:
#                 print(vertex, i)
#                 xpos=coords[0]
#                 ypos=coords[1]
#                 cell_x.append(xpos) 
#                 cell_y.append(ypos)
# lyst_x.append(cell_x)
# lyst_y.append(cell_y)
# print(lyst_x[:5])

# Hendriks solution
x_coord = []
y_coord = []
for cell in cell_vertices:
    x_cell_coord = []
    y_cell_coord = []
    for vert in cell:
        # use the vertex index "vert" as an index for the positions list to save yourself looping through positions.
        # See TEST VERTICES PROB for explanation. 
        x_cell_coord.append(positions[int(vert)][0])
        y_cell_coord.append(positions[int(vert)][1])
    x_coord.append(x_cell_coord)
    y_coord.append(y_cell_coord)
                
    
    
    
    



#def cell_area():
    
#def centroid():
    
#def dist_center():
    
#plot cell area vs dist to disc center, fit line
#def plotting():
    
#do t-test
#def ttest():
    
#draw the disc?
#def drawdisc():
    
#analyze small and large discs:COMBINE ALL DEFS:
    #def analyze_disc():


    

    
#dist cell to wingdisc center: 
#first get cell centroid:








#%%
#numpy, scipy = fitting and statistical tools 
#matplotlib = data representation

import numpy as np
from numpy import polyfit

'''
numpy.polyfit(x,y,deg) returns an array of polynomial coefficients
if degree=2, the highest degree is x**2
in array, highest degree listed first: [6.5 3.2 4.1]

answer: y = 4.1 + 3.2 * x + 6.5 * x**2 
'''

'''
t-tests are usually done to determine if two samples are significantly different from each other. 
Using scipy.stats.ttest_ind(a, b). 
Returns the t-statistic and the two-tailed p-value.
Assumes equal variance: parametric. 
scipy.stats must be imported - 
not  scipy only.'''

#and, or, &, |
#(a[b]) =integer array indexing
#(a[(c>2) & (a>5)]) #boolean array indexing

#INTEGER ARRAY INDEXING:
import numpy as np
    
a=np.array([3,5,2,5,6,2])
b=np.array([8,4,1,7,6,8])
#for i in range(len(a)):
    #if b[i]>=a[i]:
        #a[i]+=2
#print(a)
print(a[b>=a]+2)

#%% INTEGER INDEXING
import numpy as np
import tim

a=np.array(int(1e6)*[3,5,2,5,6,2])
b=np.array(int(1e6)*[8,4,1,7,6,8])
t0 = time.time()
for i in range(len(a)):
    if b[i]>=a[i]:
        a[i]+=2
t1 = time.time()
print(t1-t0)


import numpy as np
import time
#%%
a=np.array(int(1e6)*[3,5,2,5,6,2])
b=np.array(int(1e6)*[8,4,1,7,6,8])
t0 = time.time()
#for i in range(len(a)):
    
#MUCH FASTER COMPUTATIONAL TIME:
print(a[b>=a]+2)
t1 = time.time()
print(t1-t0)
#%%
#polygon plot figures color map:
    
import matplotlib.pyplot as plt
from numpy import array
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection

triangle_positions = [[0,0],[0.3,0.3],[0.5,0.1]]
quadrilateral_positions = [[0.5,0.1],[0.3,0.3],[0.6,0.5],[0.8,0.4]]
pentagon_positions =[[0.6,0],[0.5,0.1],[0.8,0.4],[0.9,0.3],[0.7,0.02]]

polygs = []
polygs.append(Polygon(triangle_positions))
polygs.append(Polygon(quadrilateral_positions))
polygs.append(Polygon(pentagon_positions))
patches = PatchCollection(polygs)
patches.set_cmap('jet') #color map
patches.set_array(array([3,2.5,1])) #for colors

fig=plt.figure()
panel=plt.gca()
panel.add_collection(patches)
fig.colorbar(patches)
panel.autoscale(True)
panel.set_aspect('equal')
plt.show()