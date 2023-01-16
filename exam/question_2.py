# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 16:16:58 2021

@author: Hendrik
"""

rna = 'AUGUUCGAA'

dic = {}

for i in range(len(rna)):
    if rna[i] not in dic:
        dic[rna[i]] = [i]
    else:
        dic[rna[i]].append(i)
        
print(dic)
