'''
Interactive animation
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
        
        self.canvas = Canvas(window, width = 400, height = 110)
        self.canvas.pack()
        
        frame = Frame(window)
        frame.pack()
        btStop = Button(frame, text="Stop", command = self.stop)
        btStop.pack(side=LEFT)
        btResume = Button(frame, text="Resume", command = self.resume)
        btResume.pack(side=LEFT)
        btFaster = Button(frame, text="Faster", command = self.faster)
        btFaster.pack(side=LEFT)
        btSlower = Button(frame, text="Slower", command = self.slower)
        btSlower.pack(side=LEFT)
        
        #Animation variables
        self.carX = -50
        self.sleepTime = 100
        self.speedX = 5
        self.isStopped = False
        self.animate()
                    
        window.mainloop()
        
    def stop(self):
        self.isStopped = True
        
    def resume (self):
        self.isStopped = False
        self.animate()
        
    def faster(self):
        if self.sleepTime > 5:
            self.sleepTime -= 20
    
    def slower(self):
        self.sleepTime += 20
        
    def animate(self):    
        while not self.isStopped:
            self.canvas.delete(ALL)
            self.carX = (self.speedX + self.carX) % 400
            drawCar(self.canvas, self.carX, 100)
            self.canvas.after(self.sleepTime)
            self.canvas.update() 
        
CarAnimation()