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
            # vertex is a string, because you read it from a text file, but the iterator i is an integer. Thus, your
            # comparison vertex == i will never be True, because for Python '1' is not the same as 1. You have to
            # typecast vertex to int for the comparison, and probably also for the dict key, since you want the
            # vertex number, and not a string, as the key.

            # How can you find this error during the exam:
            # Check what exactly the wrong output is instead of saying "something didnt work". In this case, the dict
            # remained empty. However, the code still took a long time to run, so you know that the loops worked fine.
            # This suggests that the line of code where you actually add stuff to the dict is not being called.
            # Often, this "adding stuff" is controlled by an if-clause, like here. When you notice that your code is not
            # adding things, it is most likely because your if-condition is not formulated correctly and is False when
            # it should be True. Once you know in which line your error is (the if-condition), you can play around it,
            # change stuff, put print statements there to check individual values, etc. for bug fixing.
            if int(vertex)==i:
                dyct_pos[int(vertex)] = pos
# print(dyct_pos)


# Now your code works, but I want to point out an inefficiency in your code. I know that this is not part of the exam,
# but it might help you think properly about the data you are handling.
# This is related to your previous bug, the fact  that "vertex" is actually an integer, not a string. Even more, it is
# the index of each vertex, meaning that it is a continuous iterator. You intuitively knew that already, that is why
# you are testing "vertex==i" to find the positions for each vertex!
# However, to do this, you are looping through the whole "positions" list with 13,000 entries, until you reach the right
# index. This is unnecessary, because "vertex" is already the iterator that you want, you dont have to create a new "i"
# in a new loop and compare it with "vertex". So, the line "positions[int(vertex)]" gives you already the position,
# without looping through the whole list.

# For comparison, I put your version and the efficient version after each other and timed the runtime with the "time"
# library. If you run this piece of code, you can see how much faster the code gets!

### SLOW VERSION ###
import time

start = time.perf_counter()     # Start the timer
dyct_pos={}
for cell, lyst in enumerate(vertices):
     for vertex in lyst:
        for i, pos in enumerate(positions):
            if int(vertex)==i:
                dyct_pos[int(vertex)] = pos
end = time.perf_counter()       # End the timer
slow_runtime = end-start        # The runtime is the difference between the start and end times

### FAST VERSION ###
start = time.perf_counter()     # Start the timer
dyct_pos_new={}                 # Change the name of the dict to avoid overwriting
for cell, lyst in enumerate(vertices):
    for vertex in lyst:
        dyct_pos_new[int(vertex)] = positions[int(vertex)]
end = time.perf_counter()       # End the timer
fast_runtime = end-start        # The runtime is the difference between the start and end times

### RESULTS ###
print(f"Are the dictionaries of both methods exactly the same? {dyct_pos==dyct_pos_new}!")
print(f"Slow version runtime: {slow_runtime} seconds")
print(f"Fast version runtime: {fast_runtime} seconds")
print(f"The fast version is {int(slow_runtime/fast_runtime)} times faster than the slow version!")



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