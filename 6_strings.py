# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 21:24:05 2020

@author: Hendrik
"""

with open(r'riddle.txt') as file:
    riddle = file.read()
riddle = riddle.replace('\n','')
special = '_!$%&/()^°@+#*{}[]'   
target = riddle.partition('*****')[2].partition('#####')[0]
for c in special:
    target = target.replace(c, '')

#%% string formatting
s = 'vTrXAXoWheCnXpDUclYfNPnSmFdZBanqCQcUFKayimnqTzMFjVxbpkrxLmvZDuYO'
s1 = ''
for i in range(0, len(s), 5):
    print(i)
    if i % 10 == 0:
        s1 += s[i:i+5].upper()
    else:
        s1 += s[i:i+5].lower()
print(s1+'{:10d}'.format(len(s1)))

s = 'vTrXAXoWheCnXpDUclYfNPnSmFdZBanqCQcUFKayimnqTzMFjVxbpkrxLmvZDuYO'
new = []
for i in range(0, len(s), 10):
    new.append(s[i:i+5].upper())
    new.append(s[i+5:i+10].lower())
s_new = ''.join(new)
print(s_new+'{:10d}'.format(len(s_new)))

#%% dicts

# First dict
births = [['darwin','12 February 1809'],['shakespeare','26 April 1564'],\
          ['cervantes','29 September 1547'],['lincoln','12 February 1809'],
          ['darwin', 'test']]

birth_dic = dict(births)

# Second dict
rev_dict = {}
for item in births:
    if item[1] not in rev_dict:
        rev_dict[item[1]] = [item[0]]
    else:
        rev_dict[item[1]].append(item[0])

# Third dict
person = {}

person['darwin'] = 'Charles Darwin'
person['shakespeare'] = 'William Shakespeare'
person['cervantes'] = 'Miguel de Cervantes'
person['lincoln'] = 'Abraham Lincoln'

person_rev = {}
for key, value in person.items():
    person_rev[value] = key       
        
#Fifth dict
person = {}

person['darwin'] = ['Charles Darwin',
                    '12 February 1809','19 April 1882']
person['shakespeare'] = ['William Shakespeare',
                    '26 April 1564','23 April 1616']
person['cervantes'] = ['Miguel de Cervantes',
                    '29 September 1547','23 April 1616']
person['lincoln'] = ['Abraham Lincoln',
                    '12 February 1809','15 April 1865']

d = {}  # has deaths as keys and long names as values


for i in person:
    for j in person:
        death = person[i][2:]
        name = person[i][0]
        d[tuple(death)] = [name]
print(d)


death_dic = {}
for key, value in person.items():
    if value[2] not in death_dic.keys():
        death_dic[value[2]] = [key]
    else:
        death_dic[value[2]].append(key)

#%% reverse genetic code

cdn = {}
cdn['ttt'] = cdn['ttc'] = 'F phenylalanine'
cdn['tta'] = cdn['ttg'] = 'L leucine'
cdn['tct'] = cdn['tcc'] = cdn['tca'] = cdn['tcg'] = 'S serine'
cdn['tat'] = cdn['tac'] = 'Y tyrosine'
cdn['taa'] = cdn['tag'] = '* stop'
cdn['tgt'] = cdn['tgc'] = 'C cysteine'
cdn['tga'] = '* stop'
cdn['tgg'] = 'W tryptophan'
cdn['ctt'] = cdn['ctc'] = cdn['cta'] = cdn['ctg'] = 'L leucine'
cdn['cct'] = cdn['ccc'] = cdn['cca'] = cdn['ccg'] = 'P proline'
cdn['cat'] = cdn['cac'] = 'H histidine'
cdn['caa'] = cdn['cag'] = 'Q glutamine'
cdn['cgt'] = cdn['cgc'] = cdn['cga'] = cdn['cgg'] = 'R arginine'
cdn['att'] = cdn['atc'] = cdn['ata'] = 'I isoleucine'
cdn['atg'] = 'M methionine'
cdn['act'] = cdn['acc'] = cdn['aca'] = cdn['acg'] = 'T threonine'
cdn['aat'] = cdn['aac'] = 'N asparagine'
cdn['aaa'] = cdn['aag'] = 'K lysine'
cdn['agt'] = cdn['agc'] = 'S serine'
cdn['aga'] = cdn['agg'] = 'R arginine'
cdn['gtt'] = cdn['gtc'] = cdn['gta'] = cdn['gtg'] = 'V valine'
cdn['gct'] = cdn['gcc'] = cdn['gca'] = cdn['gcg'] = 'A alanine'
cdn['gat'] = cdn['gac'] = 'D aspartic acid'
cdn['gaa'] = cdn['gag'] = 'E glutamic acid'
cdn['ggt'] = cdn['ggc'] = cdn['gga'] = cdn['ggg'] = 'G glycine'

aacid = {}
for codon, acid in cdn.items():
    ac = acid[2:]
    if ac not in aacid.keys():
        aacid[ac] = [codon]
    else:
        aacid[ac].append(codon)
print(aacid['glutamic acid'])


########## Rewriting strings:

# task:
# from a given string:
### make the first 5 chars uppercase, next 5 lower ...etc.
### finally the string length is written with a width of 10 characters


# s = 'EzHsPsKyTvKJKqoVzwRavQTzHDtHQyvhrFUIeTBRkSRpJPlLEocbyJBiRlngqmfUKcd'
s = 'vTrXAXoWheCnXpDUclYfNPnSmFdZBanqCQcUFKayimnqTzMFjVxbpkrxLmvZDuYO'

# Step 1.1 make list of lists which contains 5 elements each!
a = 0
b = 5

ran = int((len(s) / 5)+5)
# round up without package
ran = int((len(s) / 5)+5) + int(len(s) % 5 > 0)
# round up with package
import math
ran = math.ceil(len(s)/5)

s_complete = ''
for i in range(ran):
    if i % 2 == 0:
        s_complete += s[a:b].upper()
    else:
        s_complete += s[a:b].lower()
    a += 5
    b += 5

print(s_complete+'{:10d}'.format(len(s_complete)))


########## Rewriting strings:

# task:
# from a given string:
### make the first 5 chars uppercase, next 5 lower ...etc.
### finally the string length is written with a width of 10 characters


# s = 'EzHsPsKyTvKJKqoVzwRavQTzHDtHQyvhrFUIeTBRkSRpJPlLEocbyJBiRlngqmfUKcd'
s = 'vTrXAXoWheCnXpDUclYfNPnSmFdZBanqCQcUFKayimnqTzMFjVxbpkrxLmvZDu'

# Step 1.1 make list of lists which contains 5 elements each!


lyst_s2 = []
a = 0
b = 5

# round up without package
ran = int((len(s) / 5)+5) + int(len(s) % 5 > 0)
# round up with package
import math
ran = math.ceil(len(s)/5)

for i in range(ran):
    lyst_s2.append(s[a:b])
    a += 5
    b += 5

print(lyst_s2)

# Step 2: iterate the list indexes to make them upper/lowercase


lyst_s3 = []

for i, element in enumerate(lyst_s2):
    if i % 2 == 0:  # checks if index is even
        lyst_s3.append(element.upper())
    else:  # if i is odd
        lyst_s3.append(element.lower())
print(lyst_s3)

# Step 2.1: now add all the elements from this list into one string again:


s_complete = ''

for i in lyst_s3:
    s_complete += i

print(s_complete)

# Step 3: append a count number at the end with a number block of 10 -> 8 blankspaces


count = 0
for i in s_complete:
    count += 1
    print(i, count)
c = str(count)

### print with the count number of 10 char blocks:
k = '{:10d}'.format(count)  # makes it a 10 char block
print(s_complete + k)
