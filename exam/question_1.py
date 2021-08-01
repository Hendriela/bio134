# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 16:14:31 2021

@author: Hendrik
"""
# question 1

text = 'tgovoyd vlwucqk'
numbers = [3, 9, 7, 0, 9, 5, 7, 8, 2, 8, 3, 6, 7, 0, 6]

new_string = ''
for i in range(len(numbers)):
    if numbers[i] > 5:
        new_string += text[i]
print(new_string)