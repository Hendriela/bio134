# -*- coding: utf-8 -*-

import numpy as np

fyle = open(r"C:\Users\hheise\PycharmProjects\bio134\Ana\fMRI_series.txt")
dd = fyle.readlines()
fyle.close()
# print(dd)

lys = []
for line in dd:
    line = line.strip().split()
    line[0] = int(line[0])
    line[1] = float(line[1])
    lys.append(line)

"""
To make our solution work for different numbers of simulation rounds, we have to replace the hard-coded 5 with a 
variable. How can we know how many stimulation rounds there were?

We know from the question text that the sample rate, the time of the first stimulation, and the stimulation length is
always the same. From these three constants, we can figure out how many data points per stimulation round there are, and 
the length of our list after the data point at "170" tells us how many rounds we have in our dataset.
"""
print(type(variable))
samplerate = 5                                  # We get a data point every 5 seconds
first_stim = 170                                # The first data point is always at time point 170 seconds
stim_length = 60                                # A stimulation round is always 60 seconds long
points_per_round = stim_length // samplerate    # Integer division tells us how many data points there are per round

# Until now it was quite easy, but how can we count how many data points AFTER 170s we have in our list?
# Because the sample rate and the time point of first stimulation are constant, we can calculate how many data points
# will be before the first stimulation, and subtract this number from the total length of our data list.
points_before_first = first_stim // samplerate
actual_data_points = len(lys) - points_before_first

# Now we know how many actual data points we have. By dividing it by the points per round, we get the number of rounds
# in our dataset
n_rounds = actual_data_points // points_per_round

# Now we have the shape of our data array as variables. For this case, the values are the same as expected (n_rounds is
# 5, points_per_round is 12), but it is flexible for any dataset with the assumptions given in the question text.
data = np.zeros([n_rounds, points_per_round])
start = False
shape = data.shape

# Initialize both position variables, see explanation in second comment-block
row = 0
col = 0

for l in lys:
    time = l[0]
    level = float(l[1])

    if int(time) == 170:
        start = True

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

