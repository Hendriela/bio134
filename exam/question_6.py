# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 19:17:25 2021

@author: Hendrik
"""

def find_aa(lys, letter):
    aa = []
    for i in lys:
        if i[0] == letter:
            aa.append(i)
    return aa

def get_shortest_aa(lys):
    min_len = 100
    shortest = None
    for aa in lys:
        if len(aa) < min_len:
            min_len = len(aa)
            shortest = aa
    return shortest

aminoacids = ['alanine', 'cysteine', 'aspartic acid', 'glutamic acid', 
              'phenylalanine', 'glycine', 'histidine', 'isoleucine', 
              'lysine', 'leucine', 'methionine', 'asparagine', 
              'proline', 'glutamine', 'arginine', 'serine', 
              'threonine', 'valine', 'tryptophan', 'tyrosine'] 

# Make all first letters uppercase
for idx in range(len(aminoacids)):
    aminoacids[idx] = aminoacids[idx][0].upper()+aminoacids[idx][1:]

aminoacids.sort()

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# For the first iteration, find all AAs with unique first letter
code = []
for letter in alphabet:
    
    # Find all amino acids that start with this letter
    curr_aa = find_aa(aminoacids, letter)
    if len(curr_aa) == 1:
        code.append(letter+' '+curr_aa[0])
    else:
        code.append(letter+' ---')
# Then go through the alphabet again and fill in the other AAs
for idx, letter in enumerate(alphabet):
    curr_aa = find_aa(aminoacids, letter)
    if len(curr_aa) > 1:
        # Find shortest amino acid
        short = get_shortest_aa(curr_aa)
        # add it to code
        code[idx] = letter+' '+short
        # remove shortest AA from list
        curr_aa.remove(short)
        # Fill in the rest of the AAs
        for next_aa in curr_aa:
            for next_idx in range(len(code)):
                # Find empty spot in code and put in current AA
                if code[next_idx][-3:] == '---':
                    code[next_idx] = code[next_idx][:2]+next_aa
                    # Stop inner for-loop to avoid multiple additions of AA
                    break
                
print(*code, sep='\n')
    