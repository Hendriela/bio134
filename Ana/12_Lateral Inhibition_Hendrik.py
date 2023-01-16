# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 20:03:59 2021

@author: anaba
"""
# 12_Lateral inhibition PROBLEM
# concentration of Notch and Delta proteins change according
# to given formula.


import numpy as np

# t=np.linspace(0,50,51) #time in 50 units total
a = 0.01;
b = 100;
k = 2;
h = 2

d1 = 0.99
d2 = 1.0
n1 = 1
n2 = 1

# for i in range(1,50, 0.2): #250 steps?  How to break down into steps of 0.2?

# test with one try:
for i in range(1):
    change_d1 = (1 / 1 + (100 * n1 ** 2)) - d1
    change_d2 = (1 / 1 + (100 * n2 ** 2)) - d2
    d1 += change_d1
    d2 += change_d2

    # how to calculate mean delta? Is it just delta, since
    # we only have 1 neighboring cell?
    # Hendrik: Yes, exactly! It is a little bit of a trick question.
    #          Also, you are not using your parameter values a, b, k and h here, but hard-code the number instead
    change_n1 = (d1 ** 2 / 0.01 + d1 ** 2) - n1
    change_n2 = (d2 ** 2 / 0.01 + d2 ** 2) - n2
    n1 += change_n1
    n2 += change_n2
print(d1, d2)
print(n1, n2)

# Hendriks comments:
# You would have gotten some points for this, my guess would be 5 or 6 out of 10.
# You would have gotten points for:
# - The general formula structure
# - Updating the concentrations every loop
# - use the correct initial values and parameters (although you hard-coded them instead of using the variables)
# You would have lost some points for:
# - Not implementing time (not using time steps in your formulas, and having only one for-loop iteration)
# - Some brackets in the formulas are placed wrong. Everything that is below the fraction line should be in one bracket
# - Using Delta of cell 1 itself to calculate Notch in cell 1. Instead you have to use the Delta of surrounding cells (in this case cell 2)
# - Hard-coding of the parameters

# Here is an example how your solution could be expanded to get full points:

# The parameter part is correct
a = 0.01
b = 100
k = 2
h = 2
d1 = 0.99
d2 = 1.0
n1 = 1
n2 = 1

# Also determine time, time step size, and how many steps that would be
time = 50                       # given in question
dt = 0.1                        # delta-T, time step size, text says exact value is not important as long as its small
steps = int(time/dt)            # Number of steps resulting from the other two parameters

# steps determines how often we have to run the for-loop
for i in range(steps):
    # Your formula was nearly correct, the only wrong thing were the brackets. Compare the version below with your
    # version and spot the difference!
    # It is also better to use the variables declared above instead of hard-coding
    # the values. This is good coding practice and would allow you to quickly change the parameters of your simulation
    # without having to go through your whole code and look for all the places where numbers would change.

    change_d1 = (1 / (1 + b * n1 ** h)) - d1
    change_d2 = (1 / (1 + b * n2 ** h)) - d2

    # To implement the step size "dt", we have to multiply the result from our formula by dt. This is because the
    # formula in the question is equal not to change_d1, but to change_d1/dt. Thus, we have to multiply by dt to
    # rearrange the formula to the way we want it.
    change_d1 = change_d1 * dt
    change_d2 = change_d2 * dt

    d1 += change_d1
    d2 += change_d2

    # The same things also apply to the Notch formulas. Be careful that to calculate the change of Notch in cell 1,
    # You need the Delta concentration in cell 2, and vice versa!
    change_n1 = ((d2 ** k / (a + d2 ** k)) - n1) * dt
    change_n2 = ((d1 ** k / (a + d1 ** k)) - n2) * dt
    n1 += change_n1
    n2 += change_n2

# Finally, print out the requested results
print("Final Delta in cell 1:", d1)
print("Final Delta in cell 2:", d2)
print("Final Notch in cell 1:", n1)
