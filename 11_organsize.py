import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection

def get_list(filename):
    fyle = open(filename)
    lines = fyle.readlines()
    # nested list comprehension to extract data (split line x into a list y, remove empty strings in y)
    lys = [[float(y) if '.' in y else int(y) for y in x.strip().split(' ') if len(y) > 0] for x in lines]
    return lys


def cell_positions(cv, vp):
    x_coord = []
    y_coord = []
    for cell in cv:
        x_cell_coord = []
        y_cell_coord = []
        for vert in cell:
            x_cell_coord.append(vp[vert][0])
            y_cell_coord.append(vp[vert][1])
        x_coord.append(x_cell_coord)
        y_coord.append(y_cell_coord)
    return x_coord, y_coord


def get_data(x, y):
    areas = []
    centroids = []
    distances = []
    for cell in range(len(x)):
        curr_x = x[cell]
        curr_y = y[cell]
        a = 0
        cx = 0
        cy = 0
        for i in range(len(curr_x)):
            # Sum up area for current cell
            a += curr_x[i] * curr_y[i-1] - curr_y[i] * curr_x[i-1]
            # Sum up x and y coordinates of centroid for current cell
            cx += (curr_x[i] + curr_x[i - 1]) * (curr_x[i] * curr_y[i-1] - curr_y[i] * curr_x[i-1])
            cy += (curr_y[i] + curr_y[i - 1]) * (curr_x[i] * curr_y[i-1] - curr_y[i] * curr_x[i-1])
        # Apply factors
        a /= 2
        cx /= 6*a
        cy /= 6*a
        # Append the area of the current cell (a/2)
        areas.append(a)
        # Append the x and y coordinates of the centroid of the current cell (c / 6x area)
        centroids.append((cx, cy))
        # Append distance of centroid (sqrt of sum of x and y coordinates)
        distances.append((cx**2 + cy**2)**0.5)
    return np.array(areas), np.array(centroids), np.array(distances)

x = []
y = []

areas = []
for cell in range(len(x)):
    curr_x = x[cell]        # Temporarily save x and y coordinates for the current cell vertices
    curr_y = y[cell]
    a = 0                   # Initialize the starting area for the current cell
    for i in range(len(curr_x)):
        # Here is the formula implemented. It is executed once per vertex of each cell
        a += curr_x[i] * curr_y[i-1] - curr_y[i] * curr_x[i-1]            # Sum up area for current cell

    a /= 2                 # Apply factor
    areas.append(a)        # Append the area of the current cell


def get_centroid(x, y, a):
    centroids = []
    for cell in range(len(x)):
        curr_x = x[cell]
        curr_y = y[cell]
        cx = 0
        cy = 0
        for i in range(len(curr_x)):
            # Sum up x and y coordinates of centroid for current cell
            cx += (curr_x[i] + curr_x[i - 1]) * (curr_x[i] * curr_y[i - 1] - curr_y[i] * curr_x[i - 1])
            cy += (curr_y[i] + curr_y[i - 1]) * (curr_x[i] * curr_y[i - 1] - curr_y[i] * curr_x[i - 1])
        # Append the x and y coordinates of the centroid of the current cell (c / 6x area)
        centroids.append((cx / (6 * a[cell]), cy / (6 * a[cell])))
    return np.array(centroids)


def distance_center(coords):
    return np.sum(coords**2, axis=1)**0.5


def plotting(area, distance, size):
    # Plot data (ignore outlier cells that are in mitosis (area larger than 14 µm²)
    plt.figure()
    plt.plot(distance, area, '.')
    plt.xlabel('Distance from center [µm]')
    plt.ylabel('Cell area [µm²]')
    plt.title('Cell area distribution over distance to center in '+size+' wing disc')

    # Get fit and plot
    fit = np.polyfit(distance, area, 1)
    x_fit = np.linspace(min(distance), max(distance), len(distance))
    y_fit = fit[0]*x_fit + fit[1]
    plt.plot(x_fit, y_fit, label='Linear fit: y = {:.3f}x + {:.2f}'.format(fit[0], fit[1]))
    plt.legend()


def t_test(area, distance):
    close = area[distance < max(distance)*0.5]
    far = area[distance >= max(distance)*0.5]
    t, p = stats.ttest_ind(close, far)
    return t, p

def draw_disc(cpx, cpy, area, size):
    # input arguments:
    ## cpx, cpy: x,y/positions of the vertices of all cells
    # format: list (1 element per cell) of sublists (1 number per vertex, eg 3 numbers for a triangle).
    ## area: cell area
    # format: 1-dimentsional numpy array (1 number per cell)
    ## size: 'large' for the large disc and 'small' for the small disc

    polygs = []
    for i in range(len(cpx)):
        polyg = []
        for j in range(len(cpx[i])):
            polyg.append([cpx[i][j], cpy[i][j]])
        polygs.append(Polygon(polyg))
    patches = PatchCollection(polygs)
    patches.set_cmap('jet')
    colors = 1 * area
    colors[colors > 14] = 14  # color value for all the mitotic cells (area>14) is set to 14
    patches.set_array(np.array(colors))  # for colors

    fig = plt.figure()
    panel = fig.add_subplot(1, 1, 1)
    panel.add_collection(patches)
    fig.colorbar(patches)
    panel.set_xlim(min(min(cpx)) - 5, max(max(cpx)) + 5)
    panel.set_ylim(min(min(cpy)) - 5, max(max(cpy)) + 5)
    panel.set_aspect('equal')
    plt.title(size+' wing disc')


def analyze_disc(folder, size):

    # Load data
    cell_vertex = get_list(folder+'\\cv.txt')
    vertex_pos = get_list(folder+'\\vp.txt')

    # Get x and y positions of vertices of all cells
    x, y = cell_positions(cell_vertex, vertex_pos)

    # Get areas, centroids and center distances for all cells
    area, centroid, dist = get_data(x, y)

    # Perform Student's t-test on cells with larger vs cells smaller than half-maximum area
    t, p = t_test(area, dist)
    print('t-test for {} wing disc: \n\tt={:.2f}, p={:.2e}'.format(size, t, p))

    # Plot distribution with linear fit and wing disc itself
    plotting(area, dist, size)
    draw_disc(x, y, area, size)

# Call entire program
analyze_disc('wingdisc\\wd-small', 'small')

#%% tests für Autochecker

cell_vertex = get_list('wingdisc\\wd-large\\cv.txt')
vertex_pos = get_list('wingdisc\\wd-large\\vp.txt')
print('The first cell has {} vertices.'.format(len(cell_vertex[0])))
print('The last cell has {} vertices.'.format(len(cell_vertex[-1])))
print('Vertex 0 has the y position {}.'.format(vertex_pos[0][1]))

# x-y-positions
x, y = cell_positions(cell_vertex, vertex_pos)
print(x[0])
print(y[0])

# area, centroids and distance
area, centroid, dist = get_data(x, y)
cent = get_centroid(x,y,area)
print('Areas: first cell: {:.3f}, second cell: {:.3f}, last cell: {:.3f}'.format(area[0], area[1], area[-1]))
print('Cell 1: {:.2f} {:.2f} {:.2f}'.format(centroid[0,0], centroid[0, 1], dist[0]))
print('Cell 2: {:.2f} {:.2f} {:.2f}'.format(centroid[1,0], centroid[1, 1], dist[1]))

# Statistics
plotting(area, dist)
t, p = t_test(area, dist)
print('t-test: t={:.2f}, p={:.2e}'.format(t, p))


#%% warm-ups

# data format
x_positions = [4.6, 4.5, 9.1, 2.2, 6.2, 7.6, 5.4, 9.3, 2.5, 2.6, 7.1,
               8.9, 4.2, 3.1, 6.2, 1.4, 2.9, 9.7, 3.5, 5.2, 1.1, 9.3]
vertex_numbers = [2, 4, 11, 16, 18]

prod = 1
for m in vertex_numbers:
    prod *= x_positions[m]
print(prod)

import pickle
import mysql.connector
my_connect = mysql.connector.connect(
      host="130.60.53.47",
      user="hheise",
      passwd="Crushable-Yapping9-Amnesty",
      database="common_img"
    )
import pandas as pd
import os


def get_data(table):
    dic = pd.read_sql(f"SELECT * FROM {table} WHERE day = '2021-08-02'", my_connect).to_dict()

    backup_path = r'W:\Neurophysiology-Storage1\Wahl\Datajoint\backups\restore_del_entries'
    with open(os.path.join(backup_path, f'entry_{table}.pickle'), 'wb') as handle:
        pickle.dump(dic, handle)
    return dic