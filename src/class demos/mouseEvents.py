'''
Mouse event demo
Created Fall 2014

@author: smn4
'''
from tkinter import *

class Mouse_Event_Demo:
    def __init__(self):
        window = Tk()
        window.title("Mouse Events")
        window.geometry('+1500+100')
        
        canvas = Canvas(window, bg='white',
                        width = 300, height = 200)
        canvas.pack()
        
        canvas.bind("<Button-1>", self.processMouseEvent)
        canvas.bind("<Button-2>", self.processMouseEvent)
        
        window.mainloop()
    
    def processMouseEvent(self, event):
        print("Clicked at", event.x, event.y)
        print("Position in the screen", event.x_root, event.y_root)
        print("Which button was clicked? ", event.num)

Mouse_Event_Demo()