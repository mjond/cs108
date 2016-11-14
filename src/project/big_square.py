'''Final Project: Dodging Game - square 1 class
Created Fall 2014
Final Project
@author: Mark Davis (mjd85)
'''

from tkinter import *

class Square:
    '''
    Particle models a single particle that may be rendered to a canvas
    This code was inspired by lab12 - Particle Simulation
    '''

    def __init__(self, x = 235, y = 0, x2 = 265, y2 = 30, fill = 'red'):
        '''
        Constructor
        '''
        self._x = x
        self._y = y
        self._x2 = x2
        self._y2 = y2
        
        self.velY = 2
        
    def render(self, canvas):
        '''creating the square'''
        canvas.create_rectangle(self._x, self._y, self._x2, self._y2, fill = 'red')
        
    def move(self):
        '''making the square move'''
        self._y = self._y + self.velY
        self._y2 = self._y2 + self.velY
        
    def get_x(self):
        '''accessor for x coordinate'''
        return self._x
    
    def get_y(self):
        '''accessor for y coordinate'''
        return self._y
    
    def get_x2(self):
        '''accessor for second x coordinate'''
        return self._x2
    
    def get_y2(self):
        '''accessor for second y coordinate'''
        return self._y2
    
if __name__ == "__main__":
    q = Square()
    assert q.get_x() == 235
    assert q.get_x2() == 265
    assert q.get_y() == 0
    assert q.get_y2() == 30
    print('All tests passed')
