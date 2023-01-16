# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 21:45:11 2022

@author: anaba
"""
#1
""" 
Write a program that creates, based on string s, a list with all possible substrings of length 6 in the 
order that they occur in s. It should then print the list: 

['AATGAG', 'ATGAGC', 'TGAGCC', 'GAGCCG', 'AGCCGT', 'GCCGTA'] 
 
The program should be general enough that it would still work according to the same principle if s 
would be replaced by another string with a different length. 

"""

s = 'AATGAGCCGTA'
l=[]
for i in range(len(s)):
    string=s[i:i+6]
    if len(string)==6:
        l.append(string)
print(l)
#%%
#2
"""
Write a program that uses the dictionary en_de to translate the words in en to German and create a 
string that contains the German sentence. The words should be separated by a space. The end of 
the sentence may also contain a space. At the end, the program should print this string: 

es schneit und es ist kalt  

The program should be general enough that it would still work according to the same principle if en 
and en_de are replaced by other lists and dictionaries of different lengths (>0). You may assume 
that the dictionary contains a translation for each of the words in en. """
""

en_de = {'it': 'es', 'they': 'sie', 'and': 'und', 'is': 'ist',
'was': 'war', 'snows': 'schneit', 'cold': 'kalt'}

en = ['it', 'snows', 'and', 'it', 'is', 'cold']

for word in en:
    if word in en_de:   # This if-clause is technically not necessary, because you can assume that there always is a translation
        print(en_de[word]+" ", end="")
#%%
#3. 
"""
Write a function, compare(), that takes a positive (>0) integer n as argument and then calculates 
two values, sn and tn, according to the following equations: 

sum = ∑ n**3  (add all cubed values, If n=3 : 1 squared + 2 squared +3 squared)

t=2**n

This implies that s1 = 1, s2 = 9, s3 = 36, etc. The function should then test whether sn is larger than tn.  
Call your function using the following code: 
 
for num in [1, 2, 3, 12, 13, 14, 15]: 
    if compare(num): 
        print(1, end=",") 
    else: 
        print(0, end=",") 
 
The program should now print: 


0,1,1,1,1,0,0, 
"""
l=[1, 2, 3, 12, 13, 14, 15]

def compare(n):
    summ=0
    for i in range(1,n+1):
        summ+=i**3
    if summ > 2**(i):   # Here, "i" should be "n" instead
        return True
    else:
        return False

for num in [1, 2, 3, 12, 13, 14, 15]:
    if compare(num):
        print(1, end=",")
    else:
        print(0, end=",")
#%% 4
#DONT HAVE THE text FILE. CANT DO THIS QUESTION
#%%
#5
"""
The array im represents an image with RGB values, where numbers range from 0 to 1. The array 
threshold contains thresholds for the red, green and blue values of the pixels, respectively. Write a 
program that creates a new image array by thresholding the array im with threshold: if the value in 
im is larger or equal to the respective threshold, the value should become 1, otherwise 0. The 
program should print the new array: 

 

[[[1. 1. 0.] 
  [1. 1. 1.] 
  [0. 1. 0.] 
  [0. 1. 0.]] 
 
 [[1. 0. 0.] 
  [0. 1. 1.] 
  [0. 1. 0.] 
  [1. 1. 0.]]] 

 

The printed array may also contain integers instead of floats. The program should be general 
enough that the thresholding still works if im is replaced by another image array with different 
numbers of pixels in the x- and y-direction. In addition, it must be possible to replace threshold by 
another array with three floats between 0 and 1. """


import numpy as np
im = np.array(
[[[0.7, 0.4, 0.2], [0.5, 0.8, 0.8], [0.1, 0.9, 0.2], [0.3, 0.4, 0.5]],
[[0.7, 0.3, 0.2], [0.4, 0.4, 0.8], [0.1, 0.8, 0.3], [0.9, 0.9, 0.3]]])
threshold = np.array([0.5, 0.4, 0.8])

h,w,n=im.shape
# Remember to remove intermediate print statements. You will lose points in the exam if you produce not exactly the
# output that the question requires, even it you print the correct solution.
print(h,w,n)
#2 blocks, 4 rows, 3 columns
a=np.zeros(shape=(im.shape))
for i, block in enumerate(im):
    for i2,lys in enumerate(block):
        for i3, el in enumerate(lys):
                if el>=threshold[i3]:
                        a[i][i2][i3]=1
                else:
                    a[i][i2][i3]=0
print(a)
#%%
#6.
"""
Assume that you infected cell culture cells with a virus and stained for this virus. In addition, you 
stained the cells for the expression of Your Favorite Gene (YFG).  
Write a program that counts how many cells have virus intensities in the intervals [0, 2), [2, 4), [4, 
6), etc. until [10, 12), where ‘[‘ means including and ‘)’ means not including and the last interval 
contains the highest virus intensity. In addition to counting the cells in the intervals, the program 
should calculate the mean YFG intensities for these groups of cells. To give an example, there are 
three cells with virus intensities in interval [4, 6) and their mean YFG intensity is (4.8 + 8.7 + 5.1) / 3 
= 6.2. The results should be stored in arrays and the program should print these as follows: 

counts: [8 6 3 4 5 4] 
means: [7.45 6.35 6.2  4.85 2.82 2.75] 

The array with the counts may also contain floats instead of integers. The program should be 
general enough that it would still work according to the same principle if virus and yfg are replaced 
by other arrays of floats of different lengths. It may be assumed though that the length of virus is 
the same as the length of yfg and that both arrays contain floats (>=0) only. The first interval is 
always [0, 2), but, since the maximum virus intensity may vary, the number of intervals may vary as 
well. It may be assumed that each interval contains at least one cell. 

The points for this question are based on the counts and means the program prints. So, if the 
program does not print any arrays (or lists) with numbers, you will not get any points for this 
question.  
"""

# In the exam, you have one dedicated script for each question. This means that you also have to import libraries
# for every question separately. Here, you need to import numpy again, even though you did it already for Q5
import numpy as np

#30 floats, virus intensity for each cell
virus = np.array([3.32, 6.00, 5.23, 0.00, 0.00, 0.92, 2.08, 9.36, 9.96, 11.76, 2.92, 8.44, 1.04, 3.12, 11.40, 6.60, 
                  3.92, 0.92, 1.76, 7.64, 8.84, 11.68, 0.44, 11.92, 1.38, 6.84, 9.68, 4.08, 3.12, 4.00])

#30 floats fave gene intensity:
yfg = np.array([5.6, 6.3, 4.8, 7.4, 6.9, 9.9, 8.2, 2.4, 1.9, 1.2, 7.3, 2.4, 6.2, 5.2, 0.1, 4.5, 5.0, 8.6, 9.7, 2.6, 4.2, 
                0.8, 8.5, 8.9, 2.4, 6.0, 3.2, 8.7, 6.8, 5.1])

#intervals= [0, 2), [2, 4), [4, 6)        

counts=np.zeros(shape=(len(virus),6)) #6 intervals = 6 columns, FILL WITH COUNT
means=np.zeros(shape=(len(virus),6))  #same but fill with with INTENSITIES OF YGF
for i, intensity in enumerate(virus):   #rows                                  
    for i2 in range(0,12,2): #6 columns with ranges
        if i2 <=intensity< i2+2: #check ranges
            col=i2/2      #column number depends on range!
            counts[i,col]+=1  # FILL WITH COUNT
            means[i,col]=yfg[i]  #FILL with yfg at SAME POSITION

count_total=np.sum(counts,0) #sum of each column with counts
print(count_total)

summs=np.sum(means,0) #sum of each column with yfg intensities
actual_mean=summs/count_total #array divided by count array
print(actual_mean)

"""
Hendriks comments:
Your solution is already pretty good. You get an IndexError at counts[i,col]+=1, think about how you can fix this.
If you get this error fixed, your solution is nearly correct. The only problem is that you hard-coded the virus 
intensity intervals when you put the for-loop with range(0,12,2). As stated in the question, virus intensities could be
higher than 12, so your hard-coding would not work for these solutions.

Try to figure out how you could adapt your code so that it can accommodate also higher intensities, not be capped at 12.
Tip: Which array, "virus" or "yfg", is related to the cap of 12, and how could you find out the cap of a new array with
different values?

If you can figure it out, just write to me, I will send you a solution. 
"""

#%%
#7.
"""
The list vertices_of_polygons contains information about the arrangement of vertices in the polygons 
in the image above. Each sublist contains vertex numbers arranged clockwise. Sublist 0 contains 
information about polygon 0, sublist 1 about polygon 1, etc. 

Write a function, neighbors(), that calculates the number of neighboring polygons (that share at least 
one vertex) for each of the polygons as well as the number of second neighbors for each of the 
polygons. Second neighbors are neighbors of neighbors that are not direct neighbors. For example, 
polygon 0 has two neighbors, polygon 1 and polygon 2, and two second neighbors, polygon 3 and 
polygon 5. The function should return the numbers in two lists. As input it should take a list of lists 
that contains the same kind of information as vertices_of_polygons, but that may contain information 
about a different number (>0) of polygons. 

When vertices_of_polygons is defined as above and the function is called as follows: 

first_neigh, second_neigh = neighbors(vertices_of_polygons) 
print(first_neigh) 
print(second_neigh) 

then the program should print: 

[2, 3, 4, 4, 1, 2] 
[2, 2, 1, 1, 3, 3] 

Note that elements zero of these lists contain neighbor information about polygon 0, elements 1 
about polygon 1, etc. You can only get points for this question if your function makes a reasonable 
calculation and your program prints two lists when calling it as above. If you only know how to 
calculate the number of direct neighbors, you can still get points if you return the list with these data 
together with an empty list. """
 
vertices_of_polygons = [[0, 1, 2, 6, 5], [2, 3, 4, 8, 7, 6],
[5, 6, 7, 14, 13, 12], [7, 8, 9, 17, 16, 15, 14],
[9, 10, 11, 18, 17], [13, 14, 15, 20, 19]]

#def neighbors(inputlist):

first_neigh=[0]*6
second_neigh=[0]*6

firstneigh_list=[]

for i,poly in enumerate(vertices_of_polygons):
    for vert in poly:     
        count=0
        first_list=[]
        for i2, poly2 in enumerate(vertices_of_polygons):          
            if poly!=poly2:              
                for vert in poly2:                     
                        count+=1
                        firstneigh_list.append(poly2)
        first_neigh[i]=count
print(first_neigh)

"""
Hendriks solution:

This exercise was a real pain. It took me a long time to get through what they even want, and then the logic of it is so
convoluted, that I had to really take it step by step. I tried everything with the first polygon before adding the outer
loop to test everything. To understand what was going on, it was helpful for me to put the two print statements that 
I commented out now, when I found a first or second neighbor. This gave me an overview about which neighbors my code
correctly found, which ones were wrong, and how I had to adapt my if-clauses to correctly ignore the false ones.

I tried to comment my code as much as possible, so you can try to understand what is going on (un-comment the print
statements if you like, they helped me), but dont worry if it is too much. You would not learn too much anyway from it.

Again, this exercise is a real pain in the ass, and I think a really bad question in general. It does not require much
actual thought, just a lot of concentration to get through all of these for-loops and chained if-clauses. I am pretty 
sure that such a question would not be in the exam anymore, I think Maria has improved in her question-making.
"""

vertices_of_polygons = [[0, 1, 2, 6, 5], [2, 3, 4, 8, 7, 6],
[5, 6, 7, 14, 13, 12], [7, 8, 9, 17, 16, 15, 14],
[9, 10, 11, 18, 17], [13, 14, 15, 20, 19]]

    
def neighbors(inputList):

    # These lists will be the output lists and store the number of 1st and 2nd neighbors of each polygon
    first = []
    second = []

    # this outermost loop runs once per element and fills "first" and "second"
    for poly in inputList:

        # These lists store the neighbors found. They will contain the actual sublists, so that we can remember if we
        # counted a neighboring polygon already
        first_neighbors = []
        second_neighbors = []

        # For each vertex in the current polygon, we look through all other polygons
        for vertex in poly:
            for neighbor_poly in inputList:
                # The current "other" neighbor_polygon is a neighbor of "poly", if three conditions are met:
                # 1. "poly" and "neighbor_poly" cant be equal (a polygon cant be the neighbor of itself)
                # 2. The current vertex of poly is also present in neighbor_poly ("poly" and "neighbor_poly" share a vertex)
                # 3. "neighbor_poly" is not in "first_neighbors" (we did not count "neighbor_poly" as a neighbor already before)
                if (poly != neighbor_poly) and (vertex in neighbor_poly) and (neighbor_poly not in first_neighbors):
                    # If these three conditions are met, we have found a first neighbor, and add the whole sublist to the list
                    first_neighbors.append(neighbor_poly)
                    # print("First neighbor found. {} is a neighbor of {}".format(poly, neighbor_poly))

        # Now we checked all vertices of "poly", and thus found all first neighbors of "poly"
        # To find all second neighbors, we have to do the same again, for all neighbor_polys (sublists in first_neighbors)
        for neighbor_poly in first_neighbors:
            # We again check all vertices for each neighbor_poly...
            for second_vertex in neighbor_poly:
                # ...and try to find it in other polygons (sublists of inputList)
                for second_neighbor_poly in inputList:
                    # The current polygon "second_neighbor_poly" is actually a second-neighbor to our current "poly"
                    # (remember, we are still inside the outermost for-loop), if four conditions are met:
                    # 1. "Poly" is not the same as "second_neighbor_poly" (a polygon cannot be the second neighbor of itself)
                    # 2. "Second_neighbor_poly" is not the same as "neighbor_poly" (the current neighbor polygon cannot be a neighbor of itself)
                    # 3. "Second_neighbor_poly" is not in "second_neighbors" (we have not counted it as a second neighbor before)
                    # 4. "Second_neighbor_poly" is not in "first_neighbors" (a polygon cannot be a second neighbor if it is already a first, direct neighbor)
                    if (poly != second_neighbor_poly) and \
                            (second_neighbor_poly != neighbor_poly) and \
                            (second_vertex in second_neighbor_poly) and \
                            (second_neighbor_poly not in second_neighbors) and \
                            (second_neighbor_poly not in first_neighbors):
                        # If all four criteria are met, we have found a second neighbor of our original "poly", and add the sublist to the list
                        second_neighbors.append(second_neighbor_poly)
                        # print("\tSecond neighbor found. {} is also a neighbor of {}".format(neighbor_poly, second_neighbor_poly))

        # Now we found all first neighbors and checked all of them to find second neighbors. We can now count the
        # first and second neighbors and save these counts to the respective lists.
        first.append(len(first_neighbors))
        second.append(len(second_neighbors))

    # After doing all of this for all polygons, we found all neighbors of every polygon and can return the counts
    return first, second

first_neigh, second_neigh = neighbors(vertices_of_polygons) 
print(first_neigh) 
print(second_neigh) 
