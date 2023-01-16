# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 18:00:12 2021

@author: Hendrik
"""
planets = [['Earth', 12742, 149598262], ['Jupiter', 139822, 778340821], 
           ['Mars', 6779, 227943824], ['Mercury', 4878, 57909227], 
           ['Neptune', 49244, 4498396441], ['Saturn', 116464, 1426666422], 
           ['Uranus', 50724, 2870658186], ['Venus', 12104, 108209475]]
    
needs_more_sorting =  True

while needs_more_sorting:
    needs_more_sorting = False
    for i in range(0, len(planets)-1):
        first = planets[i]
        second = planets[i+1]        
        if first[2] > second[2]:
            planets[i] = second
            planets[i+1] = first
            needs_more_sorting = True
            
for planet in planets:
    if planet == planets[0]:
        middle = 'km in diameter'
        end = 'km away from the sun'
    else:
        middle = len(middle)*'.'
        end = len(end)*'.'
        
    name = planet[0]+' '+(9-len(planet[0]))*'.'
    
    print(name, '{:6d} '.format(planet[1])+middle, '{:10d} '.format(planet[2])+end)
    
    

            