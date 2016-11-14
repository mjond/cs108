'''
How to get key events
Created Fall 2014
@author: smn4
'''
from tkinter import *

class Key_Event_Demo:
    def __init__(self):
        window = Tk()
        window.title("Key Events")
        window.geometry('+1500+100')
        
        canvas = Canvas(window, bg='white',
                        width = 300, height = 200)
        canvas.pack()
        
        canvas.bind("<Key>", self.processKeyEvent)   
        canvas.focus_set() 
        window.mainloop()
    
    def processKeyEvent(self, event):
        print("keysym?", event.keysym)
        print("char?", event.char)
        print("keycode?", event.keycode)

Key_Event_Demo()