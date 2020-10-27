rabbit = 1000
fox = 100
for i in range(10):
    changerabbits = 0.05*rabbit-0.0002*fox*rabbit
    rabbit = rabbit + changerabbits

for i in range(6):
    print ('hello')
    if i<=3:
        for j in range(3):
            print ('hi')
            break
        print ('bye')
        
bases = ['A', 'T', 'C', 'G']
count = 1
for b1 in bases:
    for b2 in bases:
        for b3 in bases:
            if (b1 == b2 or b2 == b3) and b1 != b3:
                print(count, b1+b2+b3)
                count += 1
                
import numpy.random as rd
rd.seed(0)

max_h = 0
max_t = 0
run = 0

while (max_t or max_h) <= 8:
    max_h += 0.25
    max_t += 3
r = rd.randint(1,3)

import numpy.random as rd
rd.seed(141)

for m in range(10):
    six = 0
    for n in range(30):
        r = rd.randint(1,7)
        if r==6:
            six += 1
    print(six)
    
    
a = 0
a116 = 0
for i in range(10000):
    for n in range(400):
        r = np.random.randint(1,5)
        if r == 1:
            a += 1
    if a >= 116:
        a116 += 1
    a = 0
print(a116/10000)

test = [[1,4,6], 6,8]
