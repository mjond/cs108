'''
Movement based on key events
Created Fall 2014

@author: smn4
'''
from tkinter import *

class LinesWithArrowKeys:
    def __init__(self):
        self.window = Tk()
        self.window.title("Lines with arrow keys")
        #window.geometry('+1500+100')
        self.window.protocol('WM_DELETE_WINDOW', self.exitClean)
        self.canvas = Canvas(self.window, bg='white',
                        width = 300, height = 300)
        self.canvas.pack()
        self.canvas.bind('<Up>', self.processUp)
        self.canvas.bind('<Down>', self.processDown)
        self.canvas.bind('<Left>', self.processLeft)
        self.canvas.bind('<Right>', self.processRight)
        self.canvas.focus_set()

        #instance variables to control animation
        self.terminate = False
        self.x = 150
        self.y = 150
        
        self.window.mainloop()
    
    def processUp(self, event):
        self.canvas.create_line(self.x, self.y, self.x, self.y - 1)
        self.y += -1
        
    def processDown(self, event):
        self.canvas.create_line(self.x, self.y, self.x, self.y + 1)
        self.y += 1
            
    def processLeft(self, event):
        self.canvas.create_line(self.x, self.y, self.x - 1, self.y)
        self.x += -1
        
    def processRight(self, event):
        self.canvas.create_line(self.x, self.y, self.x + 1, self.y)
        self.x += 1
        
    def exitClean(self):
        self.terminate = True
        self.window.destroy()
        
LinesWithArrowKeys()