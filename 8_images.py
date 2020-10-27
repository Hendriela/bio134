# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 10:38:57 2020

@author: Hendrik
"""
#%% Boundaries
import matplotlib.image as img
import numpy as np 

h = img.imread('hotspring_pattern.jpg')
right = h[:,-1,2]
upper = h[0,:,0]
print('Mean blue right value: {:.2f}\nMean red upper value: {:.4f}'.format(np.mean(right), np.mean(upper)))

#%% Smoothing
import matplotlib.image as img
import numpy as np

#Slow version
h = img.imread('stinkbug.png')
smooth = 1*h
P = h.shape[0]
Q = h.shape[1]

for p in range(1,P-1):
    for q in range(1,Q-1):
        smooth[p,q] = h[p,q] + h[p+1,q] + h[p-1,q] + h[p,q+1] + h[p,q-1] + \
            h[p+1,q-1] + h[p-1,q-1] + h[p-1,q+1] + h[p+1,q+1]
smooth[1:-1,1:-1] = smooth[1:-1,1:-1]/9 

print(smooth[5,499,0])
print(smooth[181,260,1])
print(np.mean(smooth))

#Fast version
h = img.imread('stinkbug.png')
smooth = 1*h
smooth[1:-1,1:-1] = h[1:-1,1:-1] + h[2:,1:-1] + h[:-2,1:-1] + h[1:-1,2:] + h[1:-1,:-2] + \
    h[2:,2:] + h[0:-2,0:-2] + h[2:,0:-2] + h[0:-2,2:]
smooth[1:-1,1:-1] = smooth[1:-1,1:-1]/9 

print(smooth[5,499,0])
print(smooth[181,260,1])
print(np.mean(smooth))