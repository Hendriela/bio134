# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 13:08:29 2020

@author: Hendrik
"""

with open('darwin.txt') as file:
    darwin = file.readlines()

lengths = 0 
for line in darwin:
    words = line.split(' ')
    lengths += len(words[2])
print(lengths/len(darwin))

#%% copy
with open('crick.txt') as file:
    crick = file.readlines()
print(crick)
s = ''
for line in crick:
    s = s + ' ' + line.strip()

for i in range(len(crick)):
    crick[i] = crick[i].strip()
print(crick)

crick_copy = open('crick_copy.txt', 'w')
crick_copy.write(crick)
crick_copy.close()

fyle = open('.\Documents\Bio134\crick_copy.txt')
l_fyle = fyle.readlines()
print(str(l_fyle).strip("'[]"))
fyle.close()

#%% split and join
s = 'dfkfje*jfdn*pwndnv*sfkjadjbvbjbajbfkaj*nkd*nvndlanakndndhnfajnja*lsdkjf*cevgfjh**nfe*en*m\r\n'
s1 = s.strip().split('*')
s2 = "".join(s1)
print(len(s2))

#%% HTML

with open('headings.html') as file:
    html = file.readlines()
    
print(html[1])
