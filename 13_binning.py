#%% demo

import numpy as np

ages=np.array([1,25,26,13,8,14,20,10,3,0,29,11,24,16,22])
weights=np.array([4.5,13.1,12.9,10.7,8.2,11.0,10.1,9.3,6.3,3.2,12.8,10.8,12.2,\
                12.3,12.2])

ind=ages//6
no=np.bincount(ind)
tot=np.bincount(ind,weights)
print ('means:',tot/no)

#%% exercise

import numpy as np

def count_bins(arr, interval=0.2):
    norm = np.floor(arr/interval)   # np.floor instead of // to avoid floating point rounding error
    return np.bincount(norm.astype(int))

a = np.array([0.13,0.4,0.52])
a = np.array([0.3,0.2,0.4,0.1,0.5,0.5,0.7,1.0,0.3,0.3,0.2,0.1,0.8,0.8,0.7,0.6,0.3,0.0,0.1,0.2,0.7,0.4])**2
counts = count_bins(a, 0.2)
print(counts)


# More binning
sex = np.array([0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0]) # male: 0; female: 1
height = np.array([1.83, 1.72, 1.61, 1.68, 1.79, 1.75, 1.92, 1.76, 1.66, 1.68, 1.69, 1.61, 1.70, 1.78]) # in meters

no = np.bincount(sex)               # Numbers of males and females
tot = np.bincount(sex, height)      # Summed weights
mean_men = tot[0]/no[0]
mean_women = tot[1]/no[1]
print('Male: {:.2f}m, female: {:.2f}m. A difference of {:.2f}'.format(mean_men, mean_women, abs(mean_women-mean_men)*100))


test = ['1', '2', '5', '10', '17']
test_int = []
for i in test:
    test_int.append(int(i))

test_int2 = [int(i) for i in test if int(i)%2==0]
