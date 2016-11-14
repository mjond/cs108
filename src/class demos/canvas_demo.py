'''
Demo of basic canvas elements
Adapted from Liang
Created Fall 2014

@author: smn4
'''

from tkinter import *



class CanvasDemo:
    def __init__(self):
        window = Tk()
        window.title("Canvas Demo")
        
        self.canvas = Canvas(window, width = 600, height = 600, bg = 'white')
        self.canvas.pack()
        self.canvas.create_rectangle(50, 50, 500, 400, 
                                     tags = 'rect', 
                                     fill = 'white', activefill='blue')
        self.canvas.create_oval(10, 10, 500, 250, 
                                fill = 'red', tags = 'oval')
        self.canvas.create_arc(100, 300, 400, 400, 
                               start=0, extent=90, width=8, 
                               fill = 'blue', tags='arc')
        self.canvas.create_polygon(200, 500, 
                                   500, 500, 
                                   400, 300, 
                                   350, 400,  
                                   fill="green")
        self.canvas.create_line(450, 30, 
                                470, 490, width = 9, 
                                arrow='last', 
                                activefill = 'blue', tags='line')
        self.canvas.create_text(250, 425, 
                                text = "ABCDE" , 
                                fill = 'purple', activefill='blue')

        drawHouse(self.canvas, 50, 500)
        window.mainloop()
        
def drawHouse(canvas, x, y):
    # canvas.delete('oval')
    canvas.create_rectangle(x, y, x+50, y+50, fill='brown')
    canvas.create_polygon(x, y, x+25, y-25, x+50, y, fill='black')
    canvas.create_rectangle(x+20, y+30, x+30, y+50, fill='navy')
    canvas.create_arc(x+10, y+10, x+40, y+30, start=0, extent=180,fill='white')
        
        
CanvasDemo()