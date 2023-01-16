# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 18:38:01 2021

@author: Hendrik
"""
import numpy as np 

filename = 'fMRI_series.txt'
samplerate = 5      # sample rate in seconds
first_stim = 170    # time in s of first stimulation
stim_rate = 60      # stimulation rate in seconds
data_per_stim = stim_rate//samplerate

fyle = open(filename)
datapoints = fyle.readlines()[first_stim//samplerate:]
fyle.close()

data = []
for stim in range(0, len(datapoints)//data_per_stim, 12):
    curr_stim = datapoints[stim:stim+12]
    data.append([float(x.split()[1]) for x in curr_stim])

data = np.array(data)
print(np.mean(data, 0))
