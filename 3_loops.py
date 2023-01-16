#%% 3 complex loops / Nested and variable loops / Counting codons

bases = ['A','T','C','G']
count = 1
for b1 in bases:
    for b2 in bases:
        for b3 in bases:
            if (b1 == b2 or b2 == b3) and not b1 == b2 == b3:
                print(count, (b1+b2+b3))
                count += 1

#%% 3 complex loops / Stochastic conditions / Heads and tails

import numpy.random as rd
rd.seed(5)
counter = []
for n in range(500):
    r = rd.randint(1,3)
    if r == 1:
        counter.append(counter[-1] + 1)
    else:
        counter.append(0)
    # print(counter[-1])
print('sum:', sum(counter))

import numpy.random as rd
rd.seed(5)
maximum = 0
for n in range(500):
    r = rd.randint(1, 5000)
    if r > maximum:
        maximum = r
    # print(r)
print('Max', maximum)

import numpy.random as rd
rd.seed(15)
counter = []
maximum = 0
for n in range(1000):
    r = rd.randint(1,3)
    if r == 1:
        new_num = counter[-1] + 1
    else:
        new_num = 0

    if new_num > maximum:
        maximum = new_num

    counter.append(new_num)
    # print(counter[-1])
print(maximum)

#%% 3 Turing
import numpy as np
result = 0
for i in range(10000):
    count = 0
    for j in range(400):
        if np.random.uniform(0,1) < 0.25:
            count += 1
    if count >= 117:
        result += 1
print(result/10000)
