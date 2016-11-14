'''Calculator Driver
Created on Nov 13, 2014
lab11
@author: Mark Davis
'''

from tkinter import *
from calculator import *

class Driver:
    def __init__(self):
        window = Tk()
        window.title('Calculator')
       
        #making input 1
        Label(window, text = "Input 1:").grid(row = 1, sticky = E)
        self.operand1 = StringVar()
        operand1Entry = Entry(window,textvariable = self.operand1, width = 6)
        operand1Entry.grid(row = 1, column = 1, sticky = W)    
       
        #making input 2
        Label(window, text = "Input 2:").grid(row = 2, sticky = E)
        self.operand2 = StringVar()
        operand2Entry = Entry(window, textvariable = self.operand2, width = 6)
        operand2Entry.grid(row = 2, column = 1, sticky = W)  
        
        #making a new frame for the radio buttons
        frame = Frame(window)
        frame.grid(row = 3, columnspan = 2)
        
        #string variable for the buttons
        self.operation = StringVar()
        self.operation.set('+')
        
        #making the radio buttons
        add_rb = Radiobutton(frame, text="+", variable = self.operation, value = '+')
        add_rb.pack(side = LEFT)
        
        subtract_rb = Radiobutton(frame, text="-", variable = self.operation, value = '-')
        subtract_rb.pack(side = LEFT)
        
        multiply_rb = Radiobutton(frame, text="*", variable = self.operation, value = '*')
        multiply_rb.pack(side = LEFT)
        
        divide_rb = Radiobutton(frame, text="/", variable = self.operation, value = '/')
        divide_rb.pack(side = LEFT)
        
        #making a empty label called operator
        Label(window, text = 'Operator:').grid(row = 3, column = 2, sticky = E)
        
        #creating a label and attaching to window
        opLabel = Label(window, textvariable = self.operation, width = 3)
        opLabel.grid(row = 3, column = 3)
        # the calculate button
        Button(window, text = 'Calculate', command = self.doCalculation).grid(row = 4, column = 1)
        #result label
        Label(window, text = 'Result:').grid(row = 4, column = 2)
        
        self.result_text = StringVar()
        Label(window, textvariable = self.result_text).grid(row = 4, column = 3)
        
        self.calc = Calculator()
        
        #changing label at bottom of calculator
        self.change = StringVar()
        self.change.set("Let's calculate")
        Label(window, textvariable = self.change).grid(row=5, column = 1)
        
        
               
        window.mainloop()
        
    def doCalculation(self):
        try:
            result = self.calc.calculate(self.operand1.get(), self.operation.get(), self.operand2.get())
            self.result_text.set(result)
        except ValueError as ep:
            self.change.set(ep)
        except ZeroDivisionError as x:
            self.change.set(x)
        
        
#---------------main code-------
Driver()  