# -*- coding: utf-8 -*-
"""
Possible code for the wing disc exercise.
Compared to the movie, it shows some minor changes:
- area() returns a numpy array instead of a list
- The files are closed in get_list()
- open(filename, 'r') is used instead of open(filename, 'rU')
"""

import numpy as np
from scipy import polyfit, stats
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection

def get_list(filename, number_type):
    file = open(filename, 'r')
    full = file.readlines()
    file.close()
    lyst = []
    for i, lyne in enumerate(full):
        l = []
        for s in lyne.split():
            if number_type == 'f':
                v = float(s)
            elif number_type == 'i':    
                v = int(s)
            l.append(v)
        lyst.append(l)
    return lyst

def cell_positions(cv, vp, p):
    cp=[]
    for i, c in enumerate(cv):
        cp.append([])
        for v in c:
            if p == 'x':
                cp[i].append(vp[v][0])
            else:
                cp[i].append(vp[v][1])
    return cp
    
def area(cpx, cpy):
    a = len(cpy) * [0]
    for i in range(len(cpy)):
        for j in range(len(cpy[i])):
            a[i] += cpx[i][j] * cpy[i][j-1] - cpx[i][j-1] * cpy[i][j]
        a[i] = a[i] * 0.5
    return np.array(a)
    
def centroid(cpx, cpy, area):
    xcenter = len(cpy) * [0]
    ycenter = len(cpy) * [0]
    for i in range(len(cpy)):
        for j in range(len(cpy[i])):
            xcenter[i] += (cpx[i][j] + cpx[i][j-1]) * (cpx[i][j] * cpy[i][j-1]\
                          -cpy[i][j] * cpx[i][j-1]) / (6 * area[i])
            ycenter[i] += (cpy[i][j] + cpy[i][j-1]) * (cpx[i][j] * cpy[i][j-1]\
                          -cpy[i][j] * cpx[i][j-1]) / (6 * area[i])
    return np.array(xcenter),np.array(ycenter)

def distance_center(xcenter, ycenter):
    dist_cent=(xcenter**2 + ycenter**2)**0.5
    return dist_cent

def plotting(x, y, afit, bfit, size):
    plt.figure()
    plt.plot(x[y<14],y[y<14],'.') #cells with larger sizes are in mitotic
    x0 = min(x)
    x1 = max(x)
    y0 = afit * x0 + bfit
    y1 = afit * x1 + bfit
    plt.plot([x0,x1],[y0,y1], label = 'linear fit: y = {:.3f}*x + {:.3f}'.format(afit, bfit))
    plt.title('Cell area distribution in the '+size+' wing disc')
    plt.xlabel('Distance to the center of the disc')
    plt.ylabel('Cell area (um2)')
    plt.legend()
    
def statistical_test(areas, dist_center):
    (afit, bfit) = polyfit(dist_center, areas, 1)
    dmax = max(dist_center)
    (t,Pt) = stats.ttest_ind(areas[dist_center<=0.5*dmax], areas[dist_center>0.5*dmax])# axis = None
    return afit, bfit, t, Pt
    
def draw_disc(cpx, cpy, area, size):
    polygs = []
    for i in range(len(cpx)):
        polyg = []
        for j in range(len(cpx[i])):
            polyg.append([cpx[i][j], cpy[i][j]])
        polygs.append(Polygon(polyg))
    patches = PatchCollection(polygs)
    patches.set_cmap('jet')
    colors = 1 * area
    colors[colors>14] = 14
    patches.set_array(np.array(colors)) #for colors
 
    fig = plt.figure()
    panel = plt.gca()
    panel.add_collection(patches)
    fig.colorbar(patches)
    panel.set_xlim(min(min(cpx)) - 5, max(max(cpx)) + 5)
    panel.set_ylim(min(min(cpy)) - 5, max(max(cpy)) + 5)
    panel.set_aspect('equal')
    plt.title(size+' wing disc')

def analyze_disc(size):    
    cv = get_list('wingdisc/wd-'+size+'/cv.txt', 'i')
    vp = get_list('wingdisc/wd-'+size+'/vp.txt', 'f')
    cpx = cell_positions(cv, vp, 'x')
    cpy = cell_positions(cv, vp, 'y')
    areas = area(cpx, cpy)
    xcenter, ycenter = centroid(cpx, cpy, areas)
    dist_center = distance_center(xcenter, ycenter)
    afit, bfit, t, Pt = statistical_test(areas, dist_center)
    plotting(dist_center, areas, afit, bfit, size)
    draw_disc(cpx, cpy, areas, size)
    ans = cpx, cpy, areas, xcenter, ycenter, dist_center, afit, bfit, t, Pt
    return ans


cpx_l, cpy_l, area_l, xcenter_l, ycenter_l, dist_center_l, afit_l, bfit_l,\
t_l, Pt_l = analyze_disc('large')
print ('values for the large disc:')
print ('x-positions first cell in large disc:',cpx_l[0])
print ('y-positions first cell in large disc:',cpy_l[0])
print ('first two cell areas large disc:',area_l[:2])
print ('last area large disc:',area_l[-1])
print ('x-postion centroid first cell in large disc',xcenter_l[0])
print ('y-postion centroid first cell in large disc',ycenter_l[0])
print ('distance to disc center of first cell in large disc',dist_center_l[0])
print ('x-postion centroid first cell in large disc',xcenter_l[1])
print ('y-postion centroid first cell in large disc',ycenter_l[1])
print ('distance to disc center of first cell in large disc',dist_center_l[1])
print ('y-intercept fit distance-area large disc', bfit_l)
print ('slope fit distance-area large disc', afit_l)
print ('t-value large disc', t_l)
print ('t-test p-value large disc', Pt_l)
print ()


cpx_s,cpy_s,area_s,xcenter_s,ycenter_s,dist_center_s,afit_s,bfit_s,\
t_s,Pt_s=analyze_disc('small')
print ('values for the small disc:')
print ('y-intercept fit distance-area small disc', bfit_s)
print ('slope fit distance-area small disc', afit_s)
print ('t-value small disc', t_s)
print ('t-test p-value small disc', Pt_s)

plt.show()