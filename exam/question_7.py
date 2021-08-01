# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 20:21:59 2021

@author: Hendrik
"""
import numpy as np

functional_motifs = ['GAGGTAAAC','TCCGTAAGT','AAGGTTGGA','ACAGTCAGT',\
        'TAGGTCATT','TAGGTACTG','ATGGTAACT','CAGGTATAC','TGTGTGAGT','AAGGTAAGT']

query = 'ACTCAGCCCCAGCGGAGGTGAAGGACGTCCTTCCCCAGGAGCCGGTGAGAAGCGCAGTCGGGGGCACGG'\
        'GGATGAGCTCAGGGGCCTCTAGAAAGATGTAGCTGGGACCTCGGGAAGCCCTGGCCTCCAGGTAGTCTC'\
        'AGGAGAGCTACTCAGGGTCGGGCTTGGGGAGAGGAGGAGCGGGGGTGAGGCCAGCAGCA'

print('Make profile matrix:')
bases = ['A', 'C', 'G', 'T']
matrix = np.zeros((len(bases), len(functional_motifs[0])))

for nuc_idx in range(len(functional_motifs[0])):
    for base_idx in range(len(bases)):
        count = 0
        for motif in functional_motifs:
            if motif[nuc_idx] == bases[base_idx]:
                count += 1
        count /= len(functional_motifs)
        matrix[base_idx, nuc_idx] = count
print(matrix)

print('Find potential binding sites in query')
for i in range(len(query)-9):
    motif = query[i:i+9]
    cum_freq = 0
    for idx, nuc in enumerate(motif):
        cum_freq += matrix[bases.index(nuc), idx]
    if cum_freq > 4.4:
        print(f'position {i}: {motif}, {cum_freq}') 


print('Create ideal motif:')
ideal_motif = ''
for letter in range(matrix.shape[1]):
    ideal_motif += bases[np.argmax(matrix[:, letter])]
print(ideal_motif)
