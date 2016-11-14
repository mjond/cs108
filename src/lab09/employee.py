'''employee salary class
lab09   
created Fall 2014
@author Mark Davis (mjd85)
'''

import sys

class Employee:
    '''Models an employee generator
    Invariants:
        Salary must be greater than 20,000
        First is a string
        Last is a string
        Rank is a string
        '''
    
    def __init__(self, line):
        '''() -> Employee
        Constructor'''
        
        if line == '':
            self._first = 'Mark'
            self._last = 'Davis'
            self._rank = 'Freshman'
            self._salary = 40000
        else:
            strings = line.split()
            self._first = strings[0]
            self._last = strings[1]
            self._rank = strings[2]
            self._salary = float(strings[3])
            if self._salary < 20000:
                print('Not a valid salary', file=sys.stderr)
                sys.exit(-1)
            #string method
    def __str__(self):
        '''prints out employee name, rank and salary'''
        return (self._last + ', ' + self._first[0] + '.: ' + self._rank + ' (' + str(self._salary) + ')')
    
    #accessors
    def get_rank(self):
        '''accessor for rank'''
        return self._rank
    
    def get_salary(self):
        '''accessor for salary'''
        return self._salary
    

#----------main code ------------ 
#testing the class
if __name__ == '__main__':
    emp1 = Employee('Tim DaBoi 8thGrader 80000')
    print(emp1)
    
    print(emp1.get_rank())
    print(emp1.get_salary())
    
    emp2 = Employee('Chuck Jones King 100000')
    print(emp2)
    print(emp2.get_rank())
    print(emp2.get_salary())
    