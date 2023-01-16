# -*- coding: utf-8 -*-

#--------
#load libraries

from scipy import stats
import matplotlib.pyplot as plt
import numpy as np

#------
#set variables

#number of images to be analyzed 
#(different channels do not count as different images)
number_of_images=6

#folder with fiji results
fol="output/"

#infection threshold
inf_thr=12

#cell size threshold
cell_low=10 
cell_high=1000 

#bin sizes
bin_area=100
bin_width=48 #for advanced
bin_height=52 #for advanced

#---------
#load fiji results and save in arrays
area=[]
intensity=[]
center_x=[]
center_y=[]
image_number=[]

for i in range(6):
    data=open(fol+"MHV_measurements_"+str(i)+".csv")
    datalist = data.readlines()
    for j in range(1,len(datalist)):
        line = datalist[j]
        numbers=line.strip().split(',')
        if float(numbers[1])>cell_low and float(numbers[1])<cell_high:
            area.append(float(numbers[1]))
            intensity.append(float(numbers[2]))
            center_x.append(float(numbers[3]))#for advanced
            center_y.append(float(numbers[4]))#for advanced
            image_number.append(i)#for advanced
area=np.array(area)
intensity=np.array(intensity)
center_x=np.array(center_x)
center_y=np.array(center_y)
image_number=np.array(image_number)

#--------
#determine the total number of cells (cnum)
cnum=len(area)

#--------
#Determine correlation between area and intensity

#view correlation area-intensity
plt.figure()
plt.plot(area,intensity,'.')
plt.xlabel('Area')
plt.ylabel('Infection intensity')

#spearman's rank on area-intensity
(rho,Ps)=stats.spearmanr(area, intensity)
print ('spearman rho',rho,'p',Ps)

#--------
#per cell: infection occurrence
infection=1*intensity
infection[intensity<inf_thr]=0
infection[intensity>=inf_thr]=1

#-------
#infection rate per area group

#make 10 area groups
area_group=(area-1)//100
area_group=area_group.astype(int)

#determine infection per area group
inf_per_area_group=(np.bincount(area_group, infection))
tot_per_area_group=(np.bincount(area_group))
inf_rate_per_area_group=inf_per_area_group/tot_per_area_group

print ('infection rate per area group:',inf_rate_per_area_group)
plt.figure()
plt.title('Infection rate per area group')
plt.xlabel('Area')
plt.ylabel('Infection rate')
plt.plot(range(1,len(inf_rate_per_area_group)+1),inf_rate_per_area_group)

#-------
#infection rate per density group (for advanced question)

#assign a number to each cell according to the square it is localized in
x_group=center_x//bin_width
y_group=center_y//bin_height
square_numb=y_group+(max(y_group)+1)*x_group
square_numb+=(max(square_numb)+1)*image_number
square_numb=square_numb.astype(int)

#determine cell density per square
density_per_square=np.bincount(square_numb)

#determine infected cells per square
inf_per_square=np.bincount(square_numb,infection)

#determine infection rate per density group
inf_per_density_group=(np.bincount(density_per_square, inf_per_square))
tot_per_density_group=(np.bincount(density_per_square, density_per_square))
inf_rate_per_density_group=inf_per_density_group[1:]/tot_per_density_group[1:]

print ('infection rate per density group:',inf_rate_per_density_group)
plt.figure()
plt.plot(range(1,len(inf_rate_per_density_group)+1),inf_rate_per_density_group)
plt.title('Infection rate per density group')
plt.xlabel('Density')
plt.ylabel('Infection rate')

plt.show()
