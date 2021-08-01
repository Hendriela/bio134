# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 17:51:19 2021

@author: Hendrik
"""
import numpy as np 
np.random.seed(0)

def n_times_to_threshold(thresh, max_num):
    summe = 0
    count = 0
    
    while summe <= thresh:
        summe += np.random.randint(1, max_num+1)
        count += 1
    return count

k = n_times_to_threshold(43, 10)
print('The '+str(k)+'th number has brought the sum above the threshold!')
