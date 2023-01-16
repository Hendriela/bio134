# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 19:25:47 2022

@author: abalcarc


Question 4 
The file ‘fMRI_series.txt’ contains two numbers on each line, separated by spaces. The first 
number is the timepoint in seconds and the second number is the activity level in arbitrary 
units at that given timepoint, measured by fMRI imaging of a mouse brain.  
Starting at timepoint 170s, an external stimulus was presented to the mouse every 60 seconds 
for 5 times, while continuously recording the activity level every 5 seconds.  

 

Write a program that extracts the data from the file and creates a numpy array data with the 
activity levels as floats, starting with the activity level corresponding to timepoint 170s. The 
array should have 5 rows (one row per round of stimulation), and 12 columns (one column 
per timepoint in 60 seconds). Calculate and print the mean of the 5 stimulation rounds for 
each timepoint during the 60 second period using the following code: 

 

import numpy as np #somewhere in your program, before: 
print(np.mean(data, 0)) 

 

It should then print the following array: 

 

[13622.021218 13924.207528 13901.032028 13897.297232 13978.789918 
 13937.638388 13888.950176 13874.45905  13711.046962 13664.24686 
 13557.45596  13617.378826] 

 

The code should be general enough that it would still work according to the same principle if 
‘fMRI_series.txt’ contained a dataset with a different number of stimulation rounds. You may 
assume that activity levels are always recorded every 5 seconds, stimulations are always 60 
seconds apart, and that the first stimulation is invariably started at the timepoint 170s. 
"""

import numpy as np

fyle = open(r"C:\Users\hheise\PycharmProjects\bio134\Ana\fMRI_series.txt")
dd = fyle.readlines()
fyle.close()
# print(dd)

lys = []
for line in dd:
    line = line.strip().split()
    lys.append(line)

start = False
data = np.zeros([5, 12])
shape = data.shape
# print(shape)

for l in lys:
    time = l[0]
    level = float(l[1])
    if time == 170:
        start = True
    if start:
        for x in range(shape[0]):
            for y in range(shape[1]):  # 12 columns?
                data[x, y] = data[time, level]
print(data)

# %% HENDRIKS SOLUTION

"""
You were already on a good path with your solution! The first part, reading the text file and getting the data out, is
completely correct, you dont have to change anything there. Also the first part of the for-loop, how you determine the
start of the data collection, is correct. The only thing that is left now, is to get the activity values into the 
"data" array in the right shape. But I would say this would give you already 6 or 7 out of 10 points. The data array 
remains empty in your output, which will cost some points.
"""

import numpy as np

fyle = open(r"C:\Users\hheise\PycharmProjects\bio134\Ana\fMRI_series.txt")
dd = fyle.readlines()
fyle.close()
# print(dd)

lys = []
for line in dd:
    line = line.strip().split()
    lys.append(line)

start = False
data = np.zeros([5, 12])
shape = data.shape

# Initialize both position variables, see explanation in second comment-block
row = 0
col = 0

for l in lys:
    time = l[0]
    level = float(l[1])
    """
    Up until here, we can leave everything as-is, its a good solution.
    Now, we get to the error-analysis part. Your code runs fine (no syntax or index errors), but the output array is 
    still empty. What did we say how to fix an output array that is empty but should be filled?
    1. Find the line where you actually fill the array, in your case its "data[x, y] = data[time, level]". 
        Although this line has some problems of its own, it should at least do something with "data", even if its just 
        raising an error. But it does not do anything, which gives us the hint (which is often the reason for an empty 
        output) that this line is never actually called when we run the code.
    2. Why is the line not called? Check the if-statements that control the flow of the code.
        Most of the time, a line is not called because an if-statement is never passed. Here, we have two if-statements,
        lets check both of them to see if there is a mistake that makes them always False.
        -> "if start:" - this is a very straight-forward boolean if-statement. If "start" is True, the code below will
            be executed. As the code is never executed, we can assume that "start" is never actually True. We could test
            that by putting a print statement under "if start:" and see if it prints anything. It does not. This tells 
            us that the syntax of this if-statement is correct, but "start" is never True, even if it should be, so
            we have to check why the line where "start" becomes True is never called.
        -> "if time == 170:" - the second if-statement controls when "start" should become True. This should happen when
            we reach the time point of 170 seconds in our data list "lys". Apparently this if-statement is never passed,
            because "start" is never set to True. To find out what is going wrong, we could put a "print(time)" or
            print(type(time))" before the if-clause to see what is going on during code execution. Now we see what is 
            the problem: "time" is taken out of "lys", which is a list of STRINGS. While you transform "level" to a 
            FLOAT, you do not typecast "time", and thus it remains a string. But in the if-statement you check for
            equality (==) against an integer. Even though the value of the string might be the same as the integer,
            it is not equal because the types do not match. '170' is not the same as 170. To fix this, we just have to
            typecast "time" before comparison, and your code executes: "if int(time) == 170": 
    """
    if int(time) == 170:
        start = True

    """
    Now the big problem: How can we fill our data array?
    Let's first remind ourselves what we have. We have a list of data points that we are iterating over. The problem
    of the start-point is already solved, so we know that from here on we only deal with data points that we need.
    We want to enter these points into a 2D array. The first 12 data points belong to the first stimulation round 
    (and thus in the first row), the second 12 data points to the second round (and in the second row), and so on.
    Can you see the pattern? We have fill the array row-wise, and after every 12 steps, we have to move on to the next
    row. We can do this by having a "row" and "col" variable that keeps track of our current position inside the
    "data" array.
    """
    if start:
        # First, we enter the current activity level (data point) into the current position in our data array
        data[row, col] = level

        # Then, we increment our column variable, because we have to move one column to the right for the next entry
        col += 1

        # Finally, we have to check if this would push us over the "12 steps" threshold. If it does, we move one row
        # further and reset our column to 0 (because we want to start filling the new rows from left to right).
        if col >= 12:   # Because Python starts counting from 0, our columns go from 0 to 11, so column "12" is too far
            row += 1
            col = 0

# Finally, we put the required print statement from the exercise text, which calculates the row-wise mean and gives
# us the desired result. Compare it with the expected output in the exercise text, it matches!
print(np.mean(data, 0))

"""
One last problem:
The question requires your solution to be general enough that it will also work for a different number of stimulation
rounds than 5. Think about what would have to change in your solution if there were more or less than 5 rounds...
 
Stimulation rounds are stored as rows in our "data" array, so the array would have to have a different number of rows. 
Right now, this is hard-coded in your solution when you initialize the array as "data = np.zeros([5, 12])". How can 
we make this general for all numbers of rounds, using the assumptions we are allowed from the question text?

Try to think about it and come up with a solution yourself. I put my final solution into a separate .py file, and you
can have a look if you want to compare solutions, or are stuck.
"""
