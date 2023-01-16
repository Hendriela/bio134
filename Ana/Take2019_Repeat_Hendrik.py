# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 02:26:28 2022

@author: anaba
"""
#1
''' Write a program that creates two lists based on the list numbers. The first new list should contain all the positive 
numbers, the second list all the negative numbers in the order they occur in numbers; the zeros should be ignored.
The program should then print both new lists, first the list containing the positive numbers then the list with the negative numbers.
[5, 4, 1, 8]
[-2, -3, -7]
The program should still work according to the same principle if numbers was replaced by another list of different length and content.'''

numbers = [5, -2, -3, 0, 4, 1, -7, 0, 8]
lpos=[]
lneg=[]
for el in numbers:
    if el<0:
        lneg.append(el)
    elif el>0:
        lpos.append(el)
print(lpos)
print(lneg)
#%%
#2
'''
Here is a list of UZH rectors (presidents) in chronological order:
rectors = [['Weder', 'Fischer', 'Jarren', 'Hengartner'],
['Hans', 'Andreas', 'Ottfried', 'Michael'],
[2000, 2008, 2013, 2014]]
new_rector = ['Schaepmann', 'Michael', 2020]
Write a program that adds the new rector from the list new_rector to the list rectors and prints the updated list. Thus, the program should print:
[['Weder', 'Fischer', 'Jarren', 'Hengartner', 'Schaepmann'], ['Hans', 'Andreas', 'Ottfried', 'Michael', 'Michael'], [2000, 2008, 2013, 2014, 2020]]
The program should still work if the list rectors contained information about a different number of past rectors.
'''
rectors = [['Weder', 'Fischer', 'Jarren', 'Hengartner'],
           ['Hans', 'Andreas', 'Ottfried', 'Michael'],
           [2000, 2008, 2013, 2014]]
new_rector = ['Schaepmann', 'Michael', 2020]

for i in range(len(rectors)):
    rectors[i].append(new_rector[i])
print(rectors)
#%%
#3
'''
Write a function affordable() that takes a non-empty list of numbers plus a single number as input arguments. The function should test whether the sum of the numbers in the list is not larger (but rather smaller or equal) than the single number.
Call the function using the following code:
groceries = [2.50, 5.95, 0.6, 19.95, 3.20, 1.50]
limit = 30
if affordable(groceries, limit):
print('You can afford it!')
else:
print('Sorry, too expensive...')
You are not allowed to use sum() or any other related function that sums up numbers in a list.
'''
groceries = [2.50, 5.95, 0.6, 19.95, 3.20, 1.50]
limit = 30


def affordable(groceries, limit):
    summ=0
    for price in groceries:
        """
        Here is a mistake that you did not spot.
        You loop over "groceries", with each element called "price". However, you sum up not "price", but "el".
        This is not shown as an error, because you have a variable in question 1 called "el", which this code takes.
        It happens to give the same result (because you sum up 8, the value of "el", six times, which is above 30),
        but is not correct.
        
        This can happen if you put all questions of the exam in one file like you did here, and you run the code for
        each question consecutively without clearing the variable space or console in between. This makes it possible
        for variables of previous questions to contaminate your code and give false results like this.
        
        What you should do in the exam (and they tell you this also before) is to have a separate .py file for each
        question, and run the code by pressing the green "Run" button at the top menu bar in Spyder. This way, the
        variables are cleared before each run, and you can be sure you have no contamination. 
        
        It is very important to do this! If you do not submit separate files for each question, your exam might not
        be graded at all, because the tutors will look at each question separately.
        """
        summ+=el    # has to be summ+=price
    #print(summ)
    if summ<=limit:
        return True
    else:
        return False


if affordable(groceries, limit):
    print('You can afford it!')
else:
   print('Sorry, too expensive...')
#%%
#4
'''
The file microbe_identifiers.txt contains microbial identifiers separated by spaces.
S97-cy101 S97-cy10339 S97-ga15914 S97-fi20693 ...
Each identifier starts with the prefix S97- and is followed by a taxon ID that consists of two letters and an integer number, eg cy101 for the first microbe in the file.
Write a program that opens the file, extracts all the identifiers and creates a dictionary to store the taxon IDs without the prefix. The dictionary should use the two letters of the taxon ID as keys. The values should be lists containing all the taxon IDs that start with the respective two letters in the order they occur in the original file.
It should then print this dictionary:
{'cy': ['cy101', 'cy10339', 'cy57'], 'ga': ['ga15914', 'ga2201'], 'fi': ['fi20693', 'fi7767'], 'de': ['de32927', 'de522', 'de7777'], 'ac': ['ac375', 'ac47381', 'ac517', 'ac8603']}
Note that a dictionary does not have a specified order, so that the same dictionary can be printed in many different ways.
Your program should still work if the file contained a different number of other microbial identifiers.
'''
  
fyle=open("microbe_identifiers.txt")
data=fyle.readlines()
fyle.close()
#print(data)
#print(type(data))

d={}
for line in data:
    line=line.split()
    for string in line:
        string=string.split("-")
        key=string[1][:2]
        value=string[1]
        if key in d:
            d[key].append(value)
        else:
            d[key]=[value]
print(d)
        
#%%
#5. THIS TOOK ME FOREVER, BUT I still had 15 minutes left (out of 2hrs)
'''
The array im represents an image with RGB (red, green, blue) values, where numbers range from 0 to 1. Write a program that creates a new numpy array representing an image in grayscale, where the pixel values are the minima of the respective red, green and blue values.
The program should print the new numpy array:
[[0.2 0.5 0.1 0.3]
[0.2 0.4 0.1 0.3]]
Your program should still work if the original image array had different dimensions and pixel values. You are not allowed to use any pre-existing function that returns a minimum (eg. numpy.min(), min()).
 '''           
import numpy as np
im = np.array(
[[[0.7, 0.4, 0.2],[0.5, 0.8, 0.8],[0.1, 0.9, 0.2],[0.3, 0.4, 0.5]],
[[0.7, 0.3, 0.2],[0.4, 0.4, 0.8],[0.1, 0.8, 0.3],[0.9, 0.9, 0.3]]]) 

sh=im.shape
#print(sh)
#array (to new array
#rows=4, columns=3
arai=np.zeros(shape=[sh[0],sh[1]])
#print(arai)

for i, block in enumerate(im): #2 blocks-> 2 rows in new arai
    for i2,line in enumerate(block): #4 rows in each block-> 4 columnd in new arai
         #print(i2,line)
         minn=1
         for value in line: #8 values (2blocks*4rows)
             if value<minn:
                 minn=value
                 arai[i,i2]=minn

print(arai)
#%%
#6
'''Write a program to find out, how many different words there are in the above string hand_wash, which of the words occurs the most often and at which positions in the text the most common word occurs. A word is defined here as a group of letters of the English alphabet without any special characters, separated from the next word by a space. Positions start with 0, so the 0th word is You. Please note that You and you should be counted as the same word. You may assume that there is only one most common word.
Next, generate a copy of the string hand_wash, where the most common word as well as the word preceding the most common word at each of the occurrences is highlighted by capital letters. Everything else including the punctuation marks should remain as in the original string.
Your program should thus generate the following output:

Number of different words: 33
Most common word: hands
Its positions in the text: [3, 9, 17, 26, 33]
You wash YOUR HANDS properly by first wetting YOUR HANDS under running water, soaping and rubbing YOUR HANDS together until you get a lather. Rinse YOUR HANDS thoroughly with running water. Dry THE HANDS, with a clean towel, if possible a disposable paper towel or a cloth roller towel.
The program should be general enough that it would still work if the string hand_wash was replaced by another string of English text. You may assume that the text does not contain any additional difficulties when compared to the text above (eg. the text will not start with the most common word).
'''


hand_wash = 'You wash your hands properly by first wetting your hands under running water, soaping and rubbing your ' \
            'hands together until you get a lather. Rinse your hands thoroughly with running water. Dry the hands, ' \
            'with a clean towel, if possible a disposable paper towel or a cloth roller towel.'

#make all lowers so You and you are not counted twice
hand_wash=hand_wash.lower()


#1 string to list of unique words. How many total?
hand_wash=hand_wash.strip(".").split()
hand_wash2=[]
for string in hand_wash:
    string=string.strip(".").strip(",")
    hand_wash2.append(string)
print(hand_wash2)

#strip the remaining perids and commas:
l_unique=[]
for string in hand_wash2:
    string=string.strip(".")
    string=string.strip(",")
    if string not in l_unique:
        l_unique.append(string)
print("Number of different words:", len(l_unique))

#2 identify most common  word ........................... HELP PLEASE
"""
One possible solution: For every unique word (elements in l_unique), you loop through the list of all words (hand_wash2)
and count how often it occurs, while keeping track of the highest count with a variable.
"""
highest_occurrence = 0          # this variable will keep track of the highest number of occurrences of any unique word
most_common_word = ""           # this variable will keep track of what that word is
for unique in l_unique:         # check all unique words
    current_occurrence = 0      # this variable keeps track of the number of occurrences of the current unique word
    for word in hand_wash2:     # for every unique word, check all words
        if word == unique:              # if the current word is the same as the current unique word, we found one 
            current_occurrence += 1     # occurrence of our current unique word, so we increase the counter by one
    if current_occurrence > highest_occurrence:     # if the current unique word occurred more times than the previous
        highest_occurrence = current_occurrence     # record, we overwrite the variables
        most_common_word = unique
print("Most common word:", most_common_word)
                    

#at which indices is the most common word (list)............HELP PLEASE
"""
Because we now know the most common word, we can just loop through our word list once and remember the positions where
we found it.
"""
positions = []
for pos, word in enumerate(hand_wash2):
    if word == most_common_word:
        positions.append(pos)
print("Its positions in the text:", positions)
    
#3 make copy of string with common word and word preceeding it in caps
"""
Your solution is nearly correct. However, you have to use the original provided string hand_wash, which you overwrote 
when you said "hand_wash=hand_wash.lower()". It is thus better to rename the string up there and have something like
"hand_wash_lower = hand_wash.lower()".

Also, the words preceding HANDS are double, once in lowercase once in uppercase.
"""
s=""
for i, word in enumerate(hand_wash2):
    if word==most_common_word:
        previous=hand_wash2[i-1]
        s+=previous.upper() +" " + most_common_word.upper()+ " "
    else:
        s+=word+ " "
print(s)

"""
Hendriks version
My approach is to split the original string into its words, but without removing the commas and dots, because we still
need them, and they are not affected by upper(). Then, we use the position of "hands" from the previous part to put 
that word and the word before it in upper case. Finally, we merge the list together to one string again with a space as
separator.
"""
# I re-post the original string because it was overwritten above. This would probably cost you a point or two, so do not
# overwrite it next time in the exam.
hand_wash = 'You wash your hands properly by first wetting your hands under running water, soaping and rubbing your ' \
            'hands together until you get a lather. Rinse your hands thoroughly with running water. Dry the hands, ' \
            'with a clean towel, if possible a disposable paper towel or a cloth roller towel.'

hand_wash_words = hand_wash.split()
for common_pos in positions:
    hand_wash_words[common_pos] = hand_wash_words[common_pos].upper()
    hand_wash_words[common_pos-1] = hand_wash_words[common_pos-1].upper()
new_string = ' '.join(hand_wash_words)
print(new_string)

#%%
#7.FILLING array with gut oral microbes.
"""
I dont have the text file microbial_samples.txt, so cannot check your solution. Sorry!
"""

subset = ['Oral 1 0 351 0 0 258 1608 0 0 0 0 0 0 0',
          'Gut 0 0 0 2 0 0 0 16 0 3974 0 0 153 676',
          'Skin 0 280 0 0 2 1 0 0 0 0 0 0 0 0']

#open file
fyle=open("microbial_samples.txt")
samples=fyle.readlines()
fyle.close()
#print(samples) #30 samples, lines

import numpy as np
l_samples=[]
for line in samples:
    line=line.strip().split()
    l_samples.append(line)
print(l_samples)

#make array:
row=0     
for l in l_samples:
    for i in range(1,len(l)):
        arai[row,i]=float(l[i])
        if i>=14:
            row+=1
print(arai)
