'''Loan Calculator
Created on Nov 15, 2014
homework11
@author: Mark Davis
'''

class Loan:
    def __init__(self):
        self._memory = 0
        
    def calculate(self, loan_yrs, loan_amount, interest):
        loan_yrs = float(loan_yrs)
        loan_amount = float(loan_amount)
        interest = float(interest)
        
        if loan_yrs < 0 or loan_amount < 0 or interest < 0:
            raise ValueError('Enter a proper amount')
        
        else:
            n = loan_yrs * 12
            i = interest/100/12
            D = (((1 + i)**n) - 1)/(i*(1 + i)**n)
            monthly_Payment = loan_amount / D
            
            return monthly_Payment
        
        
if __name__ == '__main__':
    calc = Loan()
    
    try:
        f = calc.calculate(12.0,30.0,5)
        assert f == 0.27746712407095636
        print(f)
    except TypeError as ep:
        print(ep)
        
    try:
        p = calc.calculate(5.0,6.0,0.9)
        assert p == 0.10230436342042698
        print(p) 
    except TypeError as x:
        print(x)
        
    try:
        j = calc.calculate('h',6.0,0.4)
        print(j)
    except ValueError as k:
        print(k)
        
        
    try:
        i = calc.calculate(-4,5,2)
        print(i)
    except ValueError as l:
        print(l)
        
        
    
    
        
        
       
        





