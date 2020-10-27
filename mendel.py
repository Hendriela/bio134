# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 14:40:23 2020

 

@author: JanaF
"""

 

import numpy as np

#%% First part
men_rec = 1850
men_dom = 5474

plantnumber=men_rec+men_dom
expected_dom=plantnumber*3/4
mendel_closer=0
sim_closer =0
equal_dist = 0

for j in range(10000):
    sim_dom = 0
    sim_rec = 0
    
    for i in range(plantnumber):
        a = np.random.uniform(0,1)
        if a < 0.75:
            sim_dom += 1
        else:
            sim_rec += 1
    
    if abs(men_dom-expected_dom)<abs(sim_dom-expected_dom):
         mendel_closer += 1
    elif abs(men_dom-expected_dom)>abs(sim_dom-expected_dom):
        sim_closer += 1
    else:
        equal_dist += 1

print(mendel_closer, sim_closer, equal_dist)

#%% second part
men_dom = [5474,6022,705,882,428,651,787,372,353,64,71,60,67,72,65]
men_rec = [1850,2001,224,299,152,207,277,193,166,36,29,40,33,28,35]
plantnumber = len(men_dom)*[0]
expected_dom = len(men_dom)*[0]
mendel_closer=len(men_dom)*[0]
sim_closer = len(men_dom)*[0] 
 

#Plantnumber and expected loop
for i in range(len(men_dom)):
    plantnumber[i] = men_dom[i]+men_rec[i]
    if i < 7:
        expected_dom[i] = plantnumber[i]*3/4
    else:
        expected_dom[i] = plantnumber[i]*2/4

 

#simulation
for i in range(1000):
    for j in range(len(plantnumber)):
        sim_dom = 0
        if j < 7:           
            for k in range(plantnumber[j]):
                a = np.random.randint(1,5)
                if a != 1:
                    sim_dom += 1
        else:
            for k in range(plantnumber[j]):
                a = np.random.randint(1,4)
                if a != 1:
                    sim_dom += 1
        if abs(expected_dom[j]-men_dom[j]) < abs(expected_dom[j]-sim_dom):
            mendel_closer[j] += 1
        elif abs(expected_dom[j]-men_dom[j]) > abs(expected_dom[j]-sim_dom):
            sim_closer[j] += 1
            
print(mendel_closer)
print(sim_closer)