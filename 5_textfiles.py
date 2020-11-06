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


with open('.\Documents\Bio134\crick.txt') as file:
    crick = file.readlines()

s = ''
for line in crick:
    s = s + ' ' + line.strip()
    
crick_copy = open('.\Documents\Bio134\crick_copy.txt', 'w')
crick_copy.write(s)
crick_copy.close()

fyle = open('.\Documents\Bio134\crick_copy.txt')
l_fyle = fyle.readlines()
print(str(l_fyle).strip("'[]"))
fyle.close()

#%% split and join
s = 'dfkfje*jfdn*pwndnv*sfkjadjbvbjbajbfkaj*nkd*nvndlanakndndhnfajnja*lsdkjf*cevgfjh**nfe*en*m\r\n'
s1 = s.split()[0].split('*')
s2 = "".join(s1)
print(len(s2))

#%% HTML

with open('.\Documents\Bio134\headings.html') as file:
    html = file.readlines()
    
print(html[1])
