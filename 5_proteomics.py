# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 15:29:43 2020

@author: Hendrik
"""
import os

# Load files
os.getcwd()
os.chdir(r'C:\Users\Hendrik')

with open(r'C:\Users\Hendrik\Documents\Bio134\human_brain_proteins.csv') as file:
    brain_all = file.readlines()
    
with open(r'.\Documents\Bio134\human_plasma_proteins.csv') as file:
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
        