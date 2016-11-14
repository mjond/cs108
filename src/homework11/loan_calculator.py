'''loan calculator GUI
Created on Nov 15, 2014
homework11
@author: Mark Davis
'''
from tkinter import *
from loan import *

class driver:
    def __init__(self):
        window = Tk()
        window.title('Loan Calculator')
        
        #input entries
        Label(window, text = "Input loan length in years:").grid(row = 1, sticky = E)
        self.operand1 = StringVar()
        operand1Entry = Entry(window, textvariable = self.operand1, width = 6)
        operand1Entry.grid(row = 1, column = 1, sticky = W)
    
        Label(window, text = "Input loan amount:").grid(row = 2, sticky = E)
        self.operand2 = StringVar()
        operand2Entry = Entry(window, textvariable = self.operand2, width = 6)
        operand2Entry.grid(row = 2, column = 1, sticky = W)

        Label(window, text = "Input interest:").grid(row = 3, sticky = E)
        self.operand3 = StringVar()
        operand3Entry = Entry(window, textvariable = self.operand3, width = 6)
        operand3Entry.grid(row = 3, column = 1, sticky = W)
        
        #calculate button
        Button(window, text = 'Calculate', command = self.loan_calc).grid(row = 4, column = 1, sticky = W)
        
        #result text that shows the calculation
        Label(window, text = 'Result:').grid(row = 4, column = 2, sticky = W)
        self.result_text = StringVar()
        Label(window, textvariable = self.result_text).grid(row = 4, column = 3)
        
        self.calc = Loan()
        
        window.mainloop()
        
    def loan_calc(self):
        try:
            result = self.calc.calculate(self.operand1.get(), self.operand2.get(), self.operand3.get())
            self.result_text.set(result)
        except ValueError as ep:
            self.result_text.set(ep)
        except ZeroDivisionError as x:
            self.result_text.set(x)
        #except TypeError as y:
            #self.result_text.set(y)
            
driver()