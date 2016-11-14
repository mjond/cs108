''' planet program
lab10
created fall 2014
@author Mark Davis (mjd85)
'''

import turtle 
class Planet:
      
    def __init__(self, name, rad, m, dist, color):
        self._name = name
        if rad < 0:
            raise ValueError('Planet numeric properties must be positive (radius)')
        elif m < 0:
            raise ValueError('Planet numeric properties must be positive (mass)')
        elif dist < 0:
            raise ValueError('Planet numeric properties must be positive (distance)')
        elif color not in 'green pink red purple black blue orange yellow':
            raise TypeError('Planet color properties must remain within given bounds (color)')
        else:
            self._rad = rad
            self._m = m
            self._dist = dist
            self._color = color
            self._x = dist
            self._y = 0
            self._turtle = turtle.Turtle()
            self._turtle.penup()
            self._turtle.color(self._color)
            self._turtle.shape('circle')
            self._turtle.shapesize(self._rad, self._rad)
            self._turtle.goto(self._x, self._y)
       
    def get_name(self):
        return self._name
    
    def get_radius(self):
        return self._radius
    
    def get_mass(self):
        return self._mass
    
    def get_distance(self):
        return self._distance
    
    def set_name(self, newname):
        self._name = newname
    
    def __str__(self):
        return self._name
    
    
    
    
    
#----------- Test Code ------------
if __name__ == '__main__':
    try:
        planet = Planet('Bob', 13, 34, 1, 'green')
        print(planet)
    except ValueError as ve:
        print('dealt with ValueError:', ve)
    try:
        planet2 = Planet('Joe', 5, 16, 333, 'blue')
        print(planet2)
    except ValueError as ve:
        print('dealt with ValueError:', ve)
    try:    
        planet3 = Planet('Wrong1', -51, 74, 30, 'green')
        print(planet3)
    except ValueError as ve:
        print('dealt with ValueError:', ve)
    try:    
        planet4 = Planet('Wrong2', 34, -8, 150, 'yellow')
        print(planet4)
    except ValueError as ve:
        print('dealt with ValueError:', ve)
    try:   
        planet5 = Planet('Wrong3', 14, 29, -320, 'red')
    except ValueError as ve:
        print('dealt with ValueError:', ve)
        
