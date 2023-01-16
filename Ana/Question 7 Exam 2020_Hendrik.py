# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 14:59:37 2021

@author: anaba

Question 7
aminoacids=['alanine','cysteine','aspartic acid','glutamic acid',
'phenylalanine','glycine','histidine','isoleucine','lysine',
'leucine','methionine','asparagine','proline','glutamine',
'arginine','serine','threonine','valine','tryptophan','tyrosine']
The list aminoacids contains the 20 standard amino acids. In addition to their full name, there
is a standard one letter code, that uniquely identifies the amino acids.
Write a program to create your own one letter code. Use the following rules for this:
1. If the first letter of the name is unique, use it as a one letter code (eg P for Proline)
2. For the other amino acids that share the first letter:
a. Assign the first letter as code to the amino acid with the shortest name in the
group of amino acids with the same first letter (eg. ['Glycine’, Glutamic acid',
'Glutamine']: G for Glycine). You may assume that there is exactly one shortest
name per group.
b. For the remaining amino acids: assign them in alphabetical order to the next
free letter in the alphabet (eg. B for Arginine).
The program should print your one letter code in the following manner (note the alphabetical
order in the one letter code and the capital letter in the full names):
A Alanine
B Arginine
C Cysteine
D Asparagine
E Aspartic acid
F Glutamic acid
G Glycine
H Histidine
I Isoleucine
J Glutamine
K Leucine
L Lysine
M Methionine
N Phenylalanine
O Threonine
P Proline
Q Tryptophan
R ---
S Serine
T Tyrosine
U ---
V Valine
W ---
X ---
Y ---
Z ---
Your program should still work if amino acids were named differently or if there was a
different number of amino acids. You may assume that there are not more than 26 amino
acids.
Please note, that the points you get for this question are largely based on your printed output
and you will be given 0 points if the program prints nothing. In case not all the printed values
are correct, you may still get part of the points.
"""

#THIS IS THE SOLUTION I WOULD GIVE IF I RAN OUT OF TIME IN THE EXAM. :-( 
#wrong output but I cannot figure out how to index properly with the alphabet..

aminoacids = ['alanine', 'cysteine', 'aspartic acid', 'glutamic acid', \
              'phenylalanine', 'glycine', 'histidine', 'isoleucine', \
              'lysine', 'leucine', 'methionine', 'asparagine', \
              'proline', 'glutamine', 'arginine', 'serine', \
              'threonine', 'valine', 'tryptophan', 'tyrosine'] 

#1 Sort list
aminoacids=sorted(aminoacids)
#print(aminoacids)

#2. Capitalize first letter of all aminos
Aminoacids=[]
for amino in aminoacids:
    new_amino=amino[0][0].upper() +amino[1:]
    Aminoacids.append(new_amino)
print(Aminoacids)
#print(len(Aminoacids))

alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
code=[]
d={}
for i, let in enumerate(alphabet[:len(Aminoacids)]):
        print(let, Aminoacids[i])

"""
This exercise was indeed quite tricky.

I am posting my solution below. 

Notice how I separated two actions, that are logically contained, into two small functions: find_aa(), which returns all 
amino acids that start with a given letter, and get_shortest_aa(), which returns the shortest string from a list of 
strings/amino acids. This is not necessary, but doing this helps keep the code organized and clea. Extracting logical 
steps of your program helps you to get the processes of your program ordered in your head and your code is easier to 
read, and if you have to do the same action multiple times (like finding all amino acids with a given letter), it also 
makes your code shorter because you only have to write it once. 
"""

def find_aa(lys, letter):
    """This function takes a list of strings (amino acids) and returns all strings that start with the given letter."""
    aa = []
    for i in lys:
        if i[0] == letter:
            aa.append(i)
    return aa


def get_shortest_aa(lys):
    """This function takes a list of strings (amino acids) and returns the shortest string."""
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
    aminoacids[idx] = aminoacids[idx][0].upper() + aminoacids[idx][1:]

aminoacids.sort()

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# This is the variable that will contain the final strings to be printed
code = []

# For the first iteration, find all AAs with unique first letter
for letter in alphabet:

    # Find all amino acids that start with this letter
    curr_aa = find_aa(aminoacids, letter)
    if len(curr_aa) == 1:
        # If there is only one AA with this letter, add the to-be-printed string to the list
        code.append(letter + ' ' + curr_aa[0])
    else:
        # Otherwise, put '---' as a placeholder
        code.append(letter + ' ---')
    
# We already have a list of all letters of the alphabet, with unique amino acids at their letters (rule 1). Now we go 
# through the alphabet again and fill in the other AAs (rule 2).
for idx, letter in enumerate(alphabet):
    curr_aa = find_aa(aminoacids, letter)
    # Now we only process letters that have more than one AA
    if len(curr_aa) > 1:
        # Find shortest amino acid (rule 2a)
        short = get_shortest_aa(curr_aa)
        # add it to the code together with the first letter
        code[idx] = letter + ' ' + short
        # remove shortest AA from list
        curr_aa.remove(short)
        # Now, curr_aa includes all amino acids with the same letter except the shortest one. These leftovers are 
        # filled in at the next nearest unclaimed letter (rule 2b)
        for next_aa in curr_aa:
            for next_idx in range(len(code)):
                # Find empty spot in code and put in current AA
                if code[next_idx][-3:] == '---':
                    code[next_idx] = code[next_idx][:2] + next_aa
                    # Stop inner for-loop to avoid multiple additions of AA
                    break

# At the end, add all letter-AA combinations to one string, separated by line breaks
final_code = '\n'.join(code)
print(final_code)

#%%
More failed attempts:

        
aminoacids = ['alanine', 'cysteine', 'aspartic acid', 'glutamic acid', \
              'phenylalanine', 'glycine', 'histidine', 'isoleucine', \
              'lysine', 'leucine', 'methionine', 'asparagine', \
              'proline', 'glutamine', 'arginine', 'serine', \
              'threonine', 'valine', 'tryptophan', 'tyrosine'] 
    
    
#make a list of the first letters of each amino
firstlett=[]
for amino in aminoacids:
    firstlett.append(amino[0])

#separate unique letters:
unique=[] #fist instance of letter
doubles=[] #duplicates
for i in firstlett:
    if i not in unique:
        unique.append(i)
    else:
        doubles.append(i)
#print(unique)
#print(doubles) #duplicates

#separate true unique from duplicates
for i in unique:
    if i in doubles:
        unique.remove(i)
#print(unique)
#print(doubles)
    
#loop through aminoacids and unique to select matching letter to amino
lyst=[]
for amino in aminoacids:
     if amino[0] in unique:
         lyst.append(amino[0] +" " + amino)
print(lyst)

for amino2 in aminoacids:
        lyst_matches=[]
        if amino2[0] in doubles:
            lyst_matches.append(amino2) #trying to make a list of aminos starting with the same letter
            #then trying to select "min" length from the list....
        #then append to "lyst"above.

print(lyst_matches)           
         
         #lyst.append(amino[0]+)
         #print(amino[0].upper(), amino.upper())
