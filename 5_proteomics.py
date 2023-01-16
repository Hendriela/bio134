# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 15:29:43 2020

@author: Hendrik
"""

with open(r'human_brain_proteins.csv') as file:
    brain_all = file.readlines()
    
with open(r'human_plasma_proteins.csv') as file:
    plasma_all = file.readlines()

# Isolate protein IDs
brain_all_id = (len(brain_all)-1) * [0]
for line in range(1, len(brain_all)):
    brain_all_id[line-1] = brain_all[line].split(',')[0]
    
plasma_all_id =  (len(plasma_all)-1) * [0]
for line in range(1, len(plasma_all)):
    plasma_all_id[line-1] = plasma_all[line].split(',')[0]

# Look for duplicate IDs
brain_only = []
plasma_only = []
brain_and_plasma = []

for name in brain_all_id:
    if name in plasma_all_id: 
        brain_and_plasma.append(name)
    else:
        brain_only.append(name)

for name in plasma_all_id:
    if name not in brain_all_id: 
        plasma_only.append(name)

# Sort and print results
brain_only.sort()
plasma_only.sort()
brain_and_plasma.sort()

print(brain_only[943])
print(plasma_only[943])
print(brain_and_plasma[943])

#%% Ana refactoring

brain = open("human_brain_proteins.csv")
brain = brain.readlines()
plasma = open("human_plasma_proteins.csv")
plasma = plasma.readlines()
B = []
P = []
both = []
BO = []
PO = []

def load_list(fname):
    lyst = open(fname)
    names = []
    for line in lyst[1:]:
        line = line.split(",")
        names.append(line[0])
    return names

def match_proteins(brain_name, plasma_name):

    brain = load_list(brain_name)
    plasma = load_list(plasma_name)

    BO = []
    PO = []
    both = []

    for name in brain:
        if name in plasma:
            both.append(name)
        else:
            BO.append(name)
    for name2 in plasma:
        if name2 not in brain:
            PO.append(name2)
    return BO, PO, both


# call the function
brain_only, plasma_only, both = match_proteins("human_brain_proteins.csv", "human_plasma_proteins.csv")

b_list, p_list = Z(brain, plasma)
answer = X(b_list, p_list)
# or, if you want to separate X's outputs:
brain_only, plasma_only, both = X(b_list, p_list)

answer = X(Z(brain, plasma)[0], Z(brain, plasma)[1])
print(answer)