#%% Numpy indexing

import numpy as np
import time

a=np.array(int(1e6)*[3,5,2,5,6,2])
b=np.array(int(1e6)*[8,4,1,7,6,8])
t0 = time.time()
for i in range(len(a)):
    if b[i]>=a[i]:
        a[i]+=2
t1 = time.time()
print(t1-t0)

a=np.array(int(1e6)*[3,5,2,5,6,2])
b=np.array(int(1e6)*[8,4,1,7,6,8])
t2 = time.time()
a[b>=a] += 2
t3 = time.time()
print(t3-t2)

print('Indexing is {:.1f}x faster than looping!'.format((t1-t0)/(t3-t2)))


#%% Plotting polygons
import matplotlib.pyplot as plt
from numpy import array
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection

triangle_positions = [[0,0],[0.3,0.3],[0.5,0.1]]
quadrilateral_positions = [[0.5,0.1],[0.3,0.3],[0.6,0.5],[0.8,0.4]]
pentagon_positions =[[0.6,0],[0.5,0.1],[0.8,0.4],[0.9,0.3],[0.7,0.02]]

polygs = []
polygs.append(Polygon(triangle_positions))
polygs.append(Polygon(quadrilateral_positions))
polygs.append(Polygon(pentagon_positions))
patches = PatchCollection(polygs)
patches.set_cmap('jet')
# patches.set_array(array([1,3,2.5])) #for colors
patches.set_array(array([1, 5, 2.5]))

fig=plt.figure()
panel=plt.gca()
panel.add_collection(patches)
fig.colorbar(patches)
panel.autoscale(True)
panel.set_aspect('equal')
plt.show()