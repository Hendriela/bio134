# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 18:00:12 2021

@author: Hendrik
"""
print("Solution: ")
planets = [['Earth', 12742, 149598262], ['Jupiter', 139822, 778340821], 
           ['Mars', 6779, 227943824], ['Mercury', 4878, 57909227], 
           ['Neptune', 49244, 4498396441], ['Saturn', 116464, 1426666422], 
           ['Uranus', 50724, 2870658186], ['Venus', 12104, 108209475]]
   
# extract distances and sort them 
distances = [x[2] for x in planets]
distances.sort()

# find planet based on current distance
sorted_planets = []
for dist in distances:
    for p in planets:
        if p[2] == dist:
            sorted_planets.append(p)
            break
    
for planet in sorted_planets:
    if planet == sorted_planets[0]:
        middle = 'km in diameter'
        end = 'km away from the sun'
    else:
        middle = len(middle)*'.'
        end = len(end)*'.'
        
    name = planet[0]+' '+(9-len(planet[0]))*'.'
    
    print(name, '{:6d} '.format(planet[1])+middle, '{:10d} '.format(planet[2])+end)
    
#%% exam
def Sort(lista):
    lista.sort(key=lambda x: x[2])
    return lista


def distance(list1):
    list2 = Sort(list1)
    print(list2[0][0], "." * (10 - 1 - len(list2[0][0])), end=" ")
    print("{:6d}".format(list2[0][1]), "km in diameter", end=" ")
    print("{:10d}".format(list2[0][2]), "km away from the sun")
    for i in range(1, len(list2)):
        print(list2[i][0], "." * (10 - 1 - len(list2[i][0])), end=" ")
        print("{:6d}".format(list2[i][1]), "." * 14, end=" ")
        print("{:10d}".format(list2[i][2]), "." * 20)


planets = [['Earth', 12742, 149598262], \
           ['Mars', 6779, 227943824], \
           ['Saturn', 116464, 1426666422], \
           ['Uranus', 50724, 2870658186], ['Venus', 12104, 108209475]]

distance(planets)