# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 17:54:12 2020

@author: Hendrik
"""

#%% Gamows diamonds 
 
# Make codons 
bases = ['A', 'T', 'C', 'G'] 
codons = [] 
for base1 in bases: 
    for base2 in bases: 
        for base3 in bases: 
            codons.append(base1+base2+base3) 
 
# Make diamond for each codon 
main_diamonds = [] 
for codon in codons: 
    # Make anti-codon 
    anti = [] 
    for base in codon: 
        if base == 'A': 
            anti.append('T') 
        elif base == 'T': 
            anti.append('A') 
        elif base == 'C': 
            anti.append('G') 
        else: 
            anti.append('C') 
    # Make diamond (first 2 codon-bases and last 2 anti-codon-bases) 
    main_diamonds.append(codon[0]+codon[1]+anti[-1]+anti[-2]) 
 
# Go through all codons. Make all equivalent diamonds and sort the corresponding 
# codons together (if they are not somewhere in the list already) 
gamow = [[] for i in range(20)] 
count = 0 
for cod_idx, codon in enumerate(codons): 
    # See if this codon has already been sorted 
    if not any(codon in sublist for sublist in gamow): 
        dia = main_diamonds[cod_idx] 
        # Make equivalent diamonds 
        equi_diamonds = [dia[0]+dia[3]+dia[2]+dia[1], 
                         dia[2]+dia[1]+dia[0]+dia[3], 
                         dia[2]+dia[3]+dia[0]+dia[1]] 
        equi_codons = [codon] 
        # Find the original codons of the equivalent diamonds 
        for d in equi_diamonds: 
            equi_codons.append(codons[main_diamonds.index(d)]) 
        # Remove duplicates with set() and order list 
        equi_codons = list(set(equi_codons)) 
        equi_codons.sort() 
        gamow[count] = equi_codons 
        count += 1 
 
# Sort and print final result 
gamow.sort() 
print(gamow[6][3]) 

#%%  short version
bases = ['A','C','G','T']
bases0 = ['T','G','C','A'] 

gamow = []
for b1 in bases:
    for b2 in bases:
        for b3 in bases:
            list0 = []
            # add the converted diamond
            a1 = bases0[bases.index(b1)]
            a2 = bases0[bases.index(b2)]
            a3 = bases0[bases.index(b3)]
            # create codons
            codon0 = str(b1+b2+b3)
            codon1 = str(a3+a2+a1)
            codon2 = str(b1+a2+b3)
            codon3 = str(a3+b2+a1)
            
            # list0.extend([codon0,codon1])
            list0.append(codon0)
            if codon1 not in list0:
                list0.append(codon1)
            if codon2 not in list0:
                list0.append(codon2)
            if codon3 not in list0:
                list0.append(codon3)
            
            list0.sort()

            if list0 not in gamow:
                gamow.append(list0)

list_sorted = sorted(gamow)
print(list_sorted[1][2])

#%% My version

# Make codons
bases = ['A', 'T', 'C', 'G']
codons = []
for base1 in bases:
    for base2 in bases:
        for base3 in bases:
            codons.append(base1+base2+base3)

# Make diamond for each codon
main_diamonds = []
for codon in codons:
    # Make anti-codon
    anti = []
    for base in codon:
        if base == 'A':
            anti.append('T')
        elif base == 'T':
            anti.append('A')
        elif base == 'C':
            anti.append('G')
        else:
            anti.append('C')
    # Make diamond (first 2 codon-bases and last 2 anti-codon-bases)
    main_diamonds.append(codon[0]+codon[1]+anti[-1]+anti[-2])

# Go through all codons. Make all equivalent diamonds and sort the corresponding
# codons together (if they are not somewhere in the list already)
gamow = [[] for i in range(20)]
count = 0
for cod_idx, codon in enumerate(codons):
    # See if this codon has already been sorted
    if not any(codon in sublist for sublist in gamow):
        dia = main_diamonds[cod_idx]
        # Make equivalent diamonds
        equi_diamonds = [dia[0]+dia[3]+dia[2]+dia[1],
                         dia[2]+dia[1]+dia[0]+dia[3],
                         dia[2]+dia[3]+dia[0]+dia[1]]
        equi_codons = [codon]
        # Find the original codons of the equivalent diamonds
        for d in equi_diamonds:
            equi_codons.append(codons[main_diamonds.index(d)])
        # Remove duplicates with set() and order list
        equi_codons = list(set(equi_codons))
        equi_codons.sort()
        gamow[count] = equi_codons
        count += 1

# Sort and print final result
gamow.sort()
print(gamow[6][3])
