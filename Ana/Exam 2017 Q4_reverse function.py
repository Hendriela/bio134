# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 03:37:23 2022

@author: anaba
"""

languages = ['French', 'Swedish', 'Spanish', 'Greek', 'Italian']
l2=[]
for lang in languages:
    for lang2 in languages:
        if (lang!=lang2):
            s=lang+ " "+ lang2
            s_list=s.split()
            l2.append(s_list)
#print(l2)
for lys in l2:
    reverse=lys.reverse()
    if reverse in l2:
        l2.remove(reverse)
print(l2)

'''"reverse" is empty, function list.reverse() doest not give
a variable to be saved. How do I check for the reverse of "lys" being
in l2?'''

"""
list.reverse() is a method that works "in-place", meaning that it does not return a changed copy of the list, but 
changes the list itself. Many list functions work like that, like list.remove() or list.append().
To keep the original list, you can make a copy of it via slicing and then reverse the copy.
"""

for lys in l2:
    rev_lys = lys[:]    # The slicing makes a copy of the list, so that lys stays untouched if you change rev_lys
    rev_lys.reverse()   # Because .reverse() is an in-place function, you do not need to catch any output
    if rev_lys in l2:
        l2.remove(rev_lys)
print(l2)

