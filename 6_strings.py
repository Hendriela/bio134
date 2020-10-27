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


s = 'IpdmtikuLIgSWmffamGyhsinrsyPOrXNrTVnhHdNbKYaiDxDkUZTgFAZKhJzyBuQXoE'
s1 = ''
for i in range(0, len(s), 5):
    if i % 10 == 0:
        s1 += s[i:i+5].upper()
    else:
        s1 += s[i:i+5].lower()
print(s1+'{:10d}'.format(len(s1)))

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
