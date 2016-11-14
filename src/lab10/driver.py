'''Driver program for lab10
Created on Nov 6, 2014
lab10
@author: Mark Davis
'''

import turtle
from solar_system import *

window = turtle.Screen()
window.setworldcoordinates(-1, -1, 1, 1)

sun_name = input('Enter a name for the sun: ')
sun_rad = int(input('Enter a radius for the sun: '))
sun_m = int(input('Enter a mass for the sunL '))
sun_temp = int(input('Enter a temperature for the sun: '))

planet_name = input('Enter a name for your planet: ')
planet_rad = int(input('enter a radius for your planet: '))
planet_m = int(input('Enter a mass for your planet: '))
planet_dist = int(input('enter a distance: '))
planet_color = input('Enter a color: ') 

ss = Solar_System() 
ss.add_sun(Sun(sun_name, sun_rad, sun_m, sun_temp))
ss.add_planet(Planet(planet_name, planet_rad, planet_m, planet_dist, planet_color))

#Keep the window open until it is clicked
window.exitonclick()




