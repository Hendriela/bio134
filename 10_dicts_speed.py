# -*- coding: utf-8 -*-
import numpy.random as rd
import time

def random_list(length):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    l = []
    for i in range(length):
        s = ''
        for j in range(5):
            s += alphabet[rd.randint(0,24)]
        l.append(s)
    return l

def list_to_dict(lys):
    dic = {}
    for i in range(len(lys)):
        if lys[i] in dic:
            dic[lys[i]].append(i)
        else:
            dic[lys[i]] = [i]
    return dic

rd.seed(0)
l1 = random_list(100000)
l2 = random_list(100000)

d1 = list_to_dict(l1)
d2 = list_to_dict(l2)

print(d1['oodms'])

time1 = time.time()
common = []
for fruit in l1:
    if fruit in l2:
        if fruit not in common:
            common.append(fruit)
time2 = time.time()
print(common)
print('time spent on list part:', time2 - time1)

time3 = time.time()
for i in range(100):
    common = []
    for fruit in d1:
        if fruit in d2:
            if fruit not in common:
                common.append(fruit)
time4 = time.time()
print(common)
print('time spent on dict part:', time2 - time1)
print('Dict is faster by a factor of ', (time2 - time1)/((time4 - time3)/100))
