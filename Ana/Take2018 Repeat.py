# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 19:51:28 2022

@author: anaba
"""

#1.
'''lys = ['g', 't', 's', 'r', 'q', 'c', 's', 'a', 'g']
Write a program that prints each of the characters in lys before the first 
occurrence of s. It should thus print:
g
t
The program should still work according to the same principle if lys 
is replaced by another list of different length.
'''

lys = ['g', 't', 'b', 'r', 'q', 'c', 's', 'a', 'g']
for i in range(len(lys)):
    if lys[i]=="s":
        break
    else:
        print(lys[i])
#%%
#2.
'''
Write a program that prints a list that is the same as lys, 
but with 1 added to each of the numbers. The program should thus print:
[[6, 3, 4], [3, 5], [6, 10, 4]]
The program should still work according to the same principle if lys is 
replaced by another list of lists with integers. The length of the new lys 
as well as the length of the sublists may be different.   
'''     
    
lys = [[5, 2, 3], [2, 4], [5, 9, 3]]
new_lys=[]
for l in lys:
    newl=[]
    for el in l:
        el+=1
        newl.append(el)
    new_lys.append(newl)
print(new_lys)
#%%
#3. 
'''Write a function, sum_squares(n), that takes a positive integer as input 
and returns the sum of squares from 1 to n-1.
Call the function at the end of your program as follows:
print(sum_squares(4))
The program should now print:
14
'''

def sum_squares(n):
    summ=0
    for i in range(1,n):
        summ+=i**2
    return summ

print(sum_squares(4))
#%%
#4
'''
Write a program that, based on lys, prints the following lines in which each
consecutive line loses the last word from lys:
24. which road leads to Rome ?
19. which road leads to .... ?
16. which road leads ....... ?
10. which road ............. ?
5. which .................. ?
Note that the numbers are the length of the text part, which consists of words from 
lys separated by spaces. The last digit of the number should be on the 5th position 
of the line. The numbers are followed by a dot and a space, whereas the text is followed 
by one space, a number of dots, another space and a question mark. The number of dots must
be such, that the above alignment is achieved.
The program should still print lines according to the same logic if lys is replaced by
another list with a different length. You may assume that the text part is never longer 
than 1000 characters.
'''

lys = ['which', 'road', 'leads', 'to', 'Rome']
reversel=lys.reverse()
#print(lys)
string=""
for i in lys:
    string+=i+ " "
print(string)

# You already had the right idea with the for-loop, but reversing the list is not necessary if you loop through the list in reverse
for i in range((len(lys)+1),0,-1):
    first_word=lys[i:i+1]
    print(first_word)
    numm= len(string)-len(lys[i:i+1])
    print(numm)
    numm="{:5d}".format(numm)
    s=lys[0:]
    #print(numm, ". ", firdt_Word, s, " ?")
    
#COME BACK TO THIS

### Hendriks solution
lys = ['which', 'road', 'leads', 'to', 'Rome']
max_length = len(" ".join(lys))

# Nearly the same as your for-loop. However, we do not have to add 1 to len(lys), because indexing already excludes the last element
for i in range(len(lys), 0, -1):

    # join the words together, one word less per loop
    words = " ".join(lys[:i])

    # construct the string
    word_count = len(words)

    # The first line has no dots and has to be treated differently
    if i == len(lys):
        line = f"{word_count}. {words} ?"
        line = "{:5d}. {} ?".format(word_count, words)

    else:
        n_dots = (max_length - 1) - word_count    # -1 because of the space between the last word and the first dot
        dots = n_dots*'.'

        line = f"{word_count}. {words} {dots} ?"
        line = "{:5d}. {} {} ?".format(word_count, words, dots)
    print(line)


#%%
#5
'''
Write a program that, based on s, creates and prints a dictionary with the words in s as keys and lists with positions 
of the words as values. Words are defined as groups of characters separated by spaces. Positions start with 0, so the 
0th word is Kate,.
The program should thus print:
{'Kate,': [0], 'when': [1], 'France': [2, 12], 'is': [3, 11], 'mine': [4, 16], 'and': [5, 13], 'I': [6], 'am': [7], 'yours': [8, 10], 'then': [9], 'you': [14], 'are': [15]}
Please note that the order of elements in dictionaries is not important, so that a correct program may also print a 
dictionary in which the elements are ordered differently. The program should still generate a dictionary according to 
the same principle if s is replaced by a string of different length consisting of a different number of words.
'''

s = 'Kate, when France is mine and I am yours then yours is France and you are mine'

s=s.split()

# This part is unnecessary, because you do not have to remove the comma from "Kate,". Look closely in the question text
s1=[]
for el in s:
    el=el.strip(",")
    s1.append(el)
print(s1)   # Also be careful that you remove any intermediate print statements before submitting a question during the
            # exam. If you leave them in, you will lose points for it.
#####################################

d={}
for i,word in enumerate(s1):
    if word in d:
        d[word].append(i)
    else:
        d[word]=[i]
print(d)
#%%
#6.
'''
Program a function named reorganize() that takes as input a greyscale image, stored as a two-dimensional numpy array. 
It should exchange the upper left and the lower right quadrant of this image, as well as the upper right and the lower 
left quadrant, and return the new image. In case the height of the image is uneven, the middle row should be left 
unchanged. The same holds true for the width.

Call the function as follows:
image1 = np.array([[0.2, 0.9, 0.1, 0.6, 0.3, 0.9], \
[0.3, 0.4, 0.8, 0.2, 0.1, 0.1], [0.7, 0.5, 0.1, 0.3, 0.2, 0.8], \
[0.2, 0.5, 0.2, 0.1, 0.5, 0.6]])
new_image1 = reorganize(image1)
print('original image 1')
print(image1)
print()
print('new image 1')
print(new_image1)
print()
image2 = np.array([[0.2, 0.3, 0.1, 0.4, 0.6], \
[0.5, 0.4, 0.7, 0.1, 0.1], [0.8, 0.9, 0.0, 0.4, 0.5]])
new_image2 = reorganize(image2)
print ('original image 2')
print(image2)
print()
print('new image 2')
print(new_image2)
The program should now print:
original image 1
[[ 0.2 0.9 0.1 0.6 0.3 0.9]
[ 0.3 0.4 0.8 0.2 0.1 0.1]
[ 0.7 0.5 0.1 0.3 0.2 0.8]
[ 0.2 0.5 0.2 0.1 0.5 0.6]]
new image 1
[[ 0.3 0.2 0.8 0.7 0.5 0.1]
[ 0.1 0.5 0.6 0.2 0.5 0.2]
[ 0.6 0.3 0.9 0.2 0.9 0.1]
[ 0.2 0.1 0.1 0.3 0.4 0.8]]
original image 2
[[ 0.2 0.3 0.1 0.4 0.6]
[ 0.5 0.4 0.7 0.1 0.1]
[ 0.8 0.9 0. 0.4 0.5]]
new image 2
[[ 0.4 0.5 0.1 0.8 0.9]
[ 0.5 0.4 0.7 0.1 0.1]
[ 0.4 0.6 0. 0.2 0.3]]
'''
import numpy as np

image1 = np.array([[0.2, 0.9, 0.1, 0.6, 0.3, 0.9], \
[0.3, 0.4, 0.8, 0.2, 0.1, 0.1], [0.7, 0.5, 0.1, 0.3, 0.2, 0.8], \
[0.2, 0.5, 0.2, 0.1, 0.5, 0.6]])
r,c=image1.shape
print(r,c)
print(image1)
#def reorganize(imagename):
new_image1=np.zeros(shape=image1.shape)
for row in range(len(image1)):
    for i,column in enumerate(row):
        if (row<=2) and (i<=3):
            new_image1[row,i]=image1[row+2,i+3]
        else:
            new_image1[row,i]=image1[row-2,i-3]
print(new_image1)

    
# #new_image1 = reorganize(image1)
# print('original image 1')
# print(image1)
# print()
# print('new image 1')
# print(new_image1)
# print()

image2 = np.array([[0.2, 0.3, 0.1, 0.4, 0.6], \
[0.5, 0.4, 0.7, 0.1, 0.1], [0.8, 0.9, 0.0, 0.4, 0.5]])
# #new_image2 = reorganize(image2)
# print ('original image 2')
# print(image2)
# print()
# print('new image 2')
# print(new_image2)

### Hendriks solution
"""
The key here is to use numpys convenient slicing options. You can slice arrays like lists, and thus take subsets of 
arrays and put them back together.
"""

def reorganize(im):    
    # Get the half-size of the array to determine how big the quarters should be. Use integer division or int() to get 
    # an integer index and round down to let the middle row untouched.
    quad_x = im.shape[0] // 2
    quad_y = im.shape[1] // 2
    
    # Make copies of the four quadrants
    upper_left = im[:quad_x, :quad_y]
    upper_right = im[:quad_x, -quad_y:] # Use negative indices to start counting from the right
    lower_left = im[-quad_x:, :quad_y]
    lower_right = im[-quad_x:, -quad_y:]
    
    # Make a copy of the whole original image, to avoid overwriting, and fill in the quadrants
    # If you are allowed to use numpy functions, you can use np.copy:
    new_im = np.copy(im)
    # If not, you can initialize new_im with zeros and copy the values of im into it via slicing
    new_im = np.zeros(im.shape)
    new_im[:] = im[:]
    # Initializing new_im immediately as a complete slice of im with: new_im = im[:] does not work, new_im would still 
    # overwrite im.
    
    new_im[:quad_x, :quad_y] = lower_right      # The lower right quadrant should go to the upper left
    new_im[:quad_x, -quad_y:] = lower_left      # The lower left quadrant should go to the upper right
    new_im[-quad_x:, :quad_y] = upper_right     # The upper right quadrant should go to the lower left
    new_im[-quad_x:, -quad_y:] = upper_left     # The upper left quadrant should go to the lower right
    
    return new_im

# Execute the code from the question text
image1 = np.array([[0.2, 0.9, 0.1, 0.6, 0.3, 0.9], \
[0.3, 0.4, 0.8, 0.2, 0.1, 0.1], [0.7, 0.5, 0.1, 0.3, 0.2, 0.8], \
[0.2, 0.5, 0.2, 0.1, 0.5, 0.6]])
new_image1 = reorganize(image1)
print('original image 1')
print(image1)
print()
print('new image 1')
print(new_image1)
print()

image2 = np.array([[0.2, 0.3, 0.1, 0.4, 0.6], \
[0.5, 0.4, 0.7, 0.1, 0.1], [0.8, 0.9, 0.0, 0.4, 0.5]])
new_image2 = reorganize(image2)
print ('original image 2')
print(image2)
print()
print('new image 2')
print(new_image2)


#%%
#7
'''Program a function, special_sort(), that takes a list of lowercase words as argument and sorts the words in the list 
according to word length, starting with the shortest word. If two words have the same length, it should sort the words 
further in alphabetical order. It may be assumed that the input list does not contain any words of the same length that 
also start with the same letter of the alphabet. Finally, the function should print the sorted words.

Call the function as follows:
l = ['cows', 'are', 'eating', 'brown', 'grass', 'in', 'the', 'sun']
special_sort(l)
The program should now print:
in
are
sun
the
cows
brown
grass
eating
You are not allowed to use .sort(), sorted() or any other related function that already 
performs some kind of sorting. You can only get points for this question if your program 
prints words that show at least some sorting.
'''
l = ['cows', 'are', 'eating', 'brown', 'grass', 'in', 'the', 'sun']
#def special_sort(l):
alpha="abcdefghijklmnopqrstuvwxyz"
newl=[]
for word in l:
    longest_length=0
    for word2 in l:
        if len(word)>len(word2):
            longest_word=word
            for el in newl:
                if len(longest_word)> len(el):
                    #
        elif len(word)<len(word2):
            longest_word=word2
           
        else:
            flag=False
            for el in word:
                if el in alpha:
                    break
                    newl.append(word)
        newl.append(longest_word)
print(newl)
            
# Hendriks solution
"""
This is a very classic computer science question, writing a sorting algorithm. There are many different sorting 
algorithms out there with different efficiencies, like quick-sort, insertion-sort or bubble-sort. Selection-sort is a 
quite inefficient algorithm, but very easy to implement and very intuitive for me personally. Because we do not care 
about efficiency here, its okay to use selection-sort here. You can have a look at other algorithms if you want to, you 
might like others like insertion-sort or bubble-sort more.

Selection-sort works like this: You go through the list and look for the lowest number (in our case the shortest string).
After you went through the whole list, you remove the lowest number from the list and put it into a new list. You then 
go through the old list again, looking again for the lowest number (which now will actually be the second-lowest), etc.
Because in our case, we do not have to actually return the sorted list, just print it, we can modify the algorithm a bit,
but the logic remains the same.

This strategy is inefficient, because you have to go through the whole list one per element, which means that the 
runtime increases quadratically with the length of the list. If you double the length, you need to perform 4x more 
comparisons (look into Big-O-notation if you want to know more, I can recommend this excellent and entertaining 9-min
video: https://youtu.be/RGuJga2Gl_k.
"""

l = ['cows', 'are', 'eating', 'brown', 'grass', 'in', 'the', 'sun']


def special_sort(lys):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for i in range(len(lys)):
        # The outer loop goes through the original list once per element and finds the shortest word each time
        min_word = None     # Initialize the min_word variable with None, should be re-set for every outer loop

        # The inner loop finds the shortest word in the current list lys
        for word in lys:
            # save the current wort if if there is no previous shortest word, or if it is shorter than the previous shortest
            if (min_word is None) or (len(word) < len(min_word)):
                min_word = word
            # If the words have the same length, we have to do an additional test
            elif len(word) == len(min_word):
                # Get the index of the starting letter of both words in the alphabet string
                start_letter_word = alphabet.index(word[0])
                start_letter_min_word = alphabet.index(min_word[0])
                # Compare the indices to sort the words alphabetically
                if start_letter_word < start_letter_min_word:
                    min_word = word

        # After the inner loop, "min_word" is the shortest word in list lys. We remove it from the list so that the next
        # time we can find the second-shortest word, etc.
        lys.remove(min_word)

        # Because the question text requires us to only print out the words, not store them, we just print it out.
        # Because it will be the currently shortest word, the printout will be automatically in order
        print(min_word)

# Call the function according to the question text
special_sort(l)

    