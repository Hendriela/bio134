
import numpy as np

def import_data(file):
    with open(file) as f:
        cont = f.readlines()

    cont_list = []

    for el in cont:
        el_list = el.strip().split(' ')
        cont_list.append([int(el_list[0]), el_list[1], float(el_list[2])])

    return cont_list

l_after = import_data('bif_after.txt')
print(l_after[36])

l_before = import_data('bif_before.txt')

#%% Lists
for i in l_before:
    if i[0] == 5 and i[1] == 'V3':
        bif_before = i[2]
        break

for i in l_after:
    if i[0] == 5 and i[1] == 'V3':
        bif_after = i[2]
        break

print(bif_after/bif_before)

#%% Dicts

def make_dict(data):
    dic = {}
    for i in data:
        if i[1] not in dic:
            dic[i[1]] = {}
        dic[i[1]][i[0]] = i[2]
    return dic

print(make_dict(l_before)['V9'])

d_before = make_dict(l_before)
d_after = make_dict(l_after)
ratio = d_after['V3'][5] / d_before['V3'][5]


#%% Array

def ray_dictionary():
    rays = {}
    for i in range(9):
        s = 'D' + str(i+1)
        rays[s] = i
    for i in range(9):
        s = 'V' + str(9-i)
        rays[s] = i + 9
    return rays


def make_array(data):
    arr = np.zeros((18,7)) + np.nan
    rays = ray_dictionary()
    for i in data:
        arr[rays[i[1]],i[0]-1] = i[2]
    return arr

rays = ray_dictionary()
a_before = make_array(l_before)
print(a_before[:,4])
a_after = make_array(l_after)
ratio = a_after[rays['V3'],4]/a_before[rays['V3'],4]


#%% Calculations and plotting

ratios = a_after/a_before
means = np.nanmean(ratios, axis=1)

print(means)

import matplotlib.pyplot as plt

def plotting(ratios, mean_ratios, ray_names):
    plt.figure()
    ax = plt.gca()
    # plot the bifurcation ratios for all the rays for one fish after the other
    for fishindex in range(ratios.shape[1]):
        ax.plot(ratios[:,fishindex] , '.', label='fish {:d}'.format(fishindex+1))
    ax.plot(mean_ratios,'k', label='mean')
    plt.ylim([0, 1.6])
    plt.legend()
    plt.title('Change in bifurcation distances upon fin regeneration.')
    plt.xlabel('Ray')
    plt.ylabel('Relative change in bifurcation distance')
    ax.set_xticks(range(len(ray_names)))
    ax.set_xticklabels(ray_names)

def names_of_rays(rays):
    ray_names = 18*['']
    for ray in rays:
        ray_names[rays[ray]] = ray
    return ray_names

plotting(ratios, means, names_of_rays(rays))
