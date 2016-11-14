'''Calculator
Created on Nov 13, 2014
lab11
@author: Mark Davis
'''
class Calculator:
    def __init__(self):
        self._memory = 0
   
    def calculate(self, num1, action, num2):
        num1 = float(num1)
        num2 = float(num2)
        
        if action == '/':
            return num1 / num2
        elif action == '*':
            return num1 * num2
        elif action == '-':
            return num1 - num2
        elif action == '+':
            return num1 + num2
        else:
            raise ValueError('Invalid operation: ' + action)

      
if __name__ == '__main__':
    calc = Calculator()
    
    #Test addition good
    try:
        assert calc.calculate('3', '+', '9') == 12
        assert calc.calculate('-4', '+', '-8') == -12
        assert calc.calculate('-7', '+', '9') == 2
        assert calc.calculate('3', '+', '0') == 3
        assert calc.calculate('2.0', '+', '5.3') == 7.3
    except:
        assert False
        
    #Test subtraction good
    try:
        assert calc.calculate('3', '-', '9') == -6
        assert calc.calculate('-4', '-', '-8') == 4
        assert calc.calculate('-7', '-', '9') == -16
        assert calc.calculate('3', '-', '0') == 3
        assert calc.calculate('2.0', '-', '5.3') == -3.3
    except:
        assert False
        
    #Test division good
    try:
        assert calc.calculate('3', '/', '12') == 0.25
        assert calc.calculate('-4', '/', '-8') == 0.5
        assert calc.calculate('16', '/', '-8') == -2
        assert calc.calculate('0', '/', '3') == 0
        assert calc.calculate('-5.0', '/', '2') == -2.5
    except:
        assert False
        
    #Test multiplication good
    try:
        assert calc.calculate('3', '*', '9') == 27
        assert calc.calculate('-4', '*', '-8') == 32
        assert calc.calculate('-7', '*', '9') == -63
        assert calc.calculate('3', '*', '0') == 0
        assert calc.calculate('2.0', '*', '5.3') == 10.6
    except:
        assert False    
    
    #Test operator throws exception
    try:
        calc.calculate(4,'f','9')
        assert False
    except Exception as e:
        assert isinstance(e, ValueError)
        assert e.__str__() == 'Invalid operation: f'
        
    try:
        calc.calculate(4,'sunshine','9')
        assert False
    except Exception as e:
        assert isinstance(e, ValueError)
        assert e.__str__() == 'Invalid operation: sunshine'
    
    #Test divide by zero
    try:
        calc.calculate(5, '/', 0)
        assert False
    except Exception as e:
        assert isinstance(e, ZeroDivisionError)
        assert e.__str__() == 'float division by zero'
        
    
    #Test bad operands
    try:
        calc.calculate('hi', '+', '9')
        assert False
    except Exception as e:
        assert isinstance(e, ValueError)
        assert e.__str__() == "could not convert string to float: 'hi'"
    
    #Test bad operands
    try:
        calc.calculate('9', '+', 'snow')
        assert False
    except Exception as e:
        assert isinstance(e, ValueError)
        assert e.__str__() == "could not convert string to float: 'snow'"
        
    print('All tests passed if this prints!')
    