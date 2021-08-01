# -*- coding: utf-8 -*-

#--------
#load libraries

from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
            
#------
#Defining the different functions


#stores the data from each of the images to large arrays containing data of
#all of the images
def get_arrays(data_folder,filenamepart,number_of_images,nuc_low, nuc_high):
    area=[]
    intensity=[]
    #center_x, center_y, image_number for advanced question (cell density and
    #infection rate)
    center_x=[]
    center_y=[]
    image_number=[]
    
    for i in range(number_of_images):
        data=open(data_folder+filenamepart+str(i)+".csv")
        datalist = data.readlines()[1:]
        for line in datalist:
            linelist=line.strip().split(',')
            if float(linelist[1])>nuc_low and float(linelist[1])<nuc_high:
                area.append(float(linelist[1]))
                intensity.append(float(linelist[2]))
                center_x.append(float(linelist[3]))
                center_y.append(float(linelist[4]))
                image_number.append(i)
        data.close()
    area=np.array(area)
    intensity=np.array(intensity)
    center_x=np.array(center_x)
    center_y=np.array(center_y)
    image_number=np.array(image_number)
    return area,intensity,center_x,center_y, image_number
   
def analyze_correlation(x_data, y_data, labelx, labely):
    #view correlation area-intensity
    plt.figure()
    plt.plot(x_data, y_data, '.')
    plt.xlabel(labelx)
    plt.ylabel(labely)
    
    #spearman's rank on area-intensity
    (rho,Ps)=stats.spearmanr(x_data, y_data)
    print ('spearman rho',rho,'p',Ps)
   
def infection_rates(x_data, intensity, infection_threshold, binsize, x_label, title):
    #this function calculates the infection rate for binned x_data; in the 
    #exercise the x_data are the areas. Since the function is kept general, it 
    #could also be used for other kinds of data, such as the mean distance of
    #a cell to it's neighbors.
    
    #per cell: infection occurrence
    infection=1*intensity
    infection[intensity<infection_threshold]=0
    infection[intensity>=infection_threshold]=1
    
    #infection rate per area group

    #assign each cell to a group
    group=(x_data-1)//binsize
    group=group.astype(int)
    
    #determine infection rate per group
    infection_per_group=(np.bincount(group, infection))
    cells_per_group=(np.bincount(group))
    infection_rates_per_group=infection_per_group/cells_per_group
    
    #plot the results
    plt.figure()
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel('Infection rate')
    plt.plot(range(1,len(infection_rates_per_group)+1),infection_rates_per_group)
    
    return infection_rates_per_group

def infection_rates_density(center_x, center_y, image_number, intensity, infection_threshold):
    #this function calculates and plots the infection rate for different 
    #density groups (for advanced part only);
    
    #per cell: infection occurrence
    infection=1*intensity
    infection[intensity<infection_threshold]=0
    infection[intensity>=infection_threshold]=1
    
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
    
    #plot the results
    plt.figure()
    plt.plot(range(1,len(inf_rate_per_density_group)+1),inf_rate_per_density_group)
    plt.title('Infection rate per density group')
    plt.xlabel('Density')
    plt.ylabel('Infection rate')
    
    return inf_rate_per_density_group
    

#------------   
#set variables

#number of images to be analyzed 
#(different channels do not count as different images)
number_of_images=6

#folder with fiji results
data_folder="output/"

#part of output file name that will be used for systematic naming
filenamepart = "MHV_measurements_"

#infection threshold
inf_threshold=12

#nucleus size threshold
nucleus_low=10 
nucleus_high=1000 

#bin sizes
bin_area=100
bin_width=48 #for advanced part
bin_height=52 #for advanced part

#---------
#call functions

area,intensity,center_x,center_y, image_number = get_arrays(data_folder,\
                        filenamepart,number_of_images,nucleus_low, nucleus_high)
#determine the total number of nuclei (nuc_num)
nuc_num=len(area)
print('total number of nuclei:', nuc_num)
analyze_correlation(area, intensity, 'Area', 'Infection intensity')
infection_rates_per_area_group = infection_rates(area, intensity, inf_threshold,\
                bin_area, 'Area group', 'Infection rate per area group')
print ('infection rates per area group:', infection_rates_per_area_group)
inf_rate_per_density_group = infection_rates_density(center_x, center_y,\
                image_number, intensity, inf_threshold)
print ('infection rate per density group:',inf_rate_per_density_group)


plt.show()
