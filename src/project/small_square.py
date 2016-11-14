'''models a small square 
Created on Dec 4, 2014
Final Project
@author: Mark Davis (mjd85)
'''


from tkinter import *

class SmallSquare:
    '''
    Particle models a single particle that may be rendered to a canvas
    This code was inspired by lab12 - Particle Simulation
    '''

    def __init__(self, x = 250, y = 585, x2 = 265, y2 = 600, fill = 'orange'):
        '''
        Constructor
        '''
        self._x = x
        self._y = y
        self._x2 = x2
        self._y2 = y2
        
        self.velY1 = 2
        
    def render(self, canvas):
        '''creating the square'''
        canvas.create_rectangle(self._x, self._y, self._x2, self._y2, fill = 'orange')
        
    def move(self):
        '''making the square move'''
        self._y = self._y - self.velY1
        self._y2 = self._y2 - self.velY1
        
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
    q = SmallSquare()
    assert q.get_x() == 250
    assert q.get_x2() == 265
    assert q.get_y() == 585
    assert q.get_y2() == 600
    print('All tests passed')
