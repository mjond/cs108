'''
Model a single particle
Created Fall 2014

@author: smn4
'''

from tkinter import *

class Particle:
    '''
    Particle models a single particle that may be rendered to a canvas
    '''

    def __init__(self, x = 50, y = 50, velX = 10, velY = 15, radius = 15, color = '#663977'):
        '''
        Constructor
        creating the circle
        '''
        self._x = x
        self._y = y
        self._velX = velX
        self._velY = velY
        self._radius = radius
        self._color = color
        
    def render(self, canvas):
        canvas.create_oval(self._x - self._radius,
                        self._y - self._radius,
                        self._x + self._radius,
                        self._y + self._radius,
                        fill = self._color)
        
    def move(self, canvas):
        self._x += self._velX
        self._y += self._velY
        if self._x - self._radius < 0 or self._x + self._radius > canvas.winfo_reqwidth():
            self._velX = -self._velX
        if self._y - self._radius < 0 or self._y + self._radius > canvas.winfo_reqwidth():
            self._velY = -self._velY
            
    def get_x(self):#accesor
        return self._x
    
    def get_y(self):#accessor
        return self._y
    
    def get_radius(self):#accessor
        return self._radius
            