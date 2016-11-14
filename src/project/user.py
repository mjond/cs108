'''Final Project: Dodging Game - User's square class
Created Fall 2014
final project
@author: Mark Davis (mjd85)
'''

class User:
    def __init__(self):
        '''constructor for creating the user's square'''
        self._x = 285
        self._y = 285
        self._x2 = 315
        self._y2 = 315
        
        self._vel = 7
        
    def create_user(self, canvas):
        '''creating the square on the canvas'''
        canvas.create_rectangle(self._x, self._y, self._x2, self._y2, fill = 'blue')
        
    def moveLeft(self, canvas):
        self._x -= self._vel
        self._x2 -= self._vel
    
    def moveRight(self, canvas):
        self._x += self._vel
        self._x2 += self._vel
        
    def moveDown(self, canvas):
        self._y += self._vel
        self._y2 += self._vel
        
    def moveUp(self, canvas):
        self._y -= self._vel
        self._y2 -= self._vel
        
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
    q = User()
    assert q.get_x() == 285
    assert q.get_x2() == 315
    assert q.get_y() == 285
    assert q.get_y2() == 315
    print('All tests passed')
