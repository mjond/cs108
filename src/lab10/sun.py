'''
Model a sun
Created Fall 2014

@author: smn4
'''
import turtle

class Sun:
    def __init__(self, name, rad, m, temp):
        
        self._name = name
        
        if rad < 0:
            raise ValueError('Radius must be positive')
        elif m < 0:
            raise ValueError('Mass must be positive')
        elif temp < -273.15:
            raise ValueError('Temperature must be above absolute zero')
        else:
            self._rad = rad
            self._m = m
            self._color = 'yellow'
            self._x = 0
            self._y = 0
            self._turtle = turtle.Turtle()
            self._turtle.penup()
            self._turtle.color(self._color)
            self._turtle.shape('circle')
            self._turtle.shapesize(self._rad, self._rad)
            self._turtle.goto(self._x, self._y)
       
        
    def get_mass(self):
        return self._mass
    
    def __str__(self):
        return self._name
        
        
        
        

if __name__ == '__main__':        
    
    try:
        sunny1 = Sun('Billy', 34, 4, -628)        
        print(sunny1)        
    except ValueError as ve:
        print('Dealt with ValueError:', ve)         
            
    try:
        sunny3 = Sun('Mark', -23, 84, 237)       
        print(sunny3)    
    except ValueError as ve:
        print('Dealt with ValueError:', ve)         
    
    try:
        sunny5 = Sun('Chuck Norris', 2, 12, 543)       
        print(sunny5)    
    except ValueError as ve:
        print('Dealt with ValueError:', ve)         
                    
        
        
        