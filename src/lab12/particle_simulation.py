'''
GUI controller for a particle simulation
Created Fall 2014

@author: smn4
'''

from tkinter import *
from random import randint
from particle import *
from helpers import *

class ParticleSimulation:
    def __init__(self):
        self.window = Tk()
        self.window.title("Particle Simulation") #making the window
        self.window.protocol('WM_DELETE_WINDOW', self.exitClean)
        self.width = 400
        self.canvas = Canvas(self.window, bg='black',
                        width = self.width, height = self.width) #making the canvas and giving it dimensions
        self.canvas.pack()
        self.terminate = False
        self.p_list = []
        add_bt = Button(self.window, text = 'Add particle', command = self.addParticle) #making the button to add particle
        add_bt.pack() 
        self.canvas.bind('<Button-1>', self.checkRemoveParticle)#binding the first-click function to remove the particle clicked 
        self.animate()#calling the animate method
        
        self.window.mainloop()
        
    def exitClean(self):
        self.terminate = True#exiting the window
        self.window.destroy()
        
    def animate(self):
        '''gives the particles the illusion that they move
        deletes the previous position then moves and renders it then updates the window'''
        while not self.terminate:
            self.canvas.delete(ALL)
            for i in self.p_list:
                i.move(self.canvas)
                i.render(self.canvas)
            self.canvas.after(40)
            self.canvas.update()
            
    def addParticle(self):
        '''adds a particle each time the button is clicked'''
        self.p_list.append(Particle(randint(0,400), randint(0,400), randint(-25,25), randint(-25,25), randint(10,30), color = getRandomColor()))   
        
    def checkRemoveParticle(self, event):
        '''method that removes the particle clicked'''
        copy = self.p_list[:]
        for i in copy:
            if distance(i.get_x(), i.get_y(), event.x, event.y) < i.get_radius():
                self.p_list.remove(i)
        
ParticleSimulation()