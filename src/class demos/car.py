'''
Created Fall 2014

@author: smn4
'''

from tkinter import *

def drawCar(canvas, x, y):
    canvas.create_oval(x+10, y-10, x+20, y, fill='black') #wheel one
    canvas.create_oval(x+30, y-10, x+40, y, fill='black') #wheel two
    canvas.create_rectangle(x, y-20, x+50, y-10, fill="blue") #body
    canvas.create_polygon(x+10, y-20, 
                          x+20, y-30, 
                          x+30, y-30, 
                          x+40, y-20, 
                          outline='black', fill='white') #windows
    
    
class CarAnimation:
    def __init__(self):
        window = Tk()
        window.title('Road Trip')
        
        canvas = Canvas(window, width = 200, height = 110)
        canvas.pack()
        
        #Animation variables
        carX = -50
        speedX = 5
        
        while True:
            canvas.delete(ALL) #remove smear
            carX += speedX
            drawCar(canvas, carX, 100)
            canvas.after(100)
            canvas.update()
                    
        window.mainloop()
        
CarAnimation()