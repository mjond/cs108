'''Fraction program
Created Fall 2014
Lab08
@author Mark Davis (mjd85)
'''

import sys

def computeGCD(alpha, beta):
    '''
    (int, int) -> int
    This function finds the greatest common divisor of two integers, using
    Euclid’s algorithm
    '''
    alpha = abs(alpha)
    beta = abs(beta)
    remainder = alpha % beta
    while (remainder != 0):
        alpha = beta
        beta = remainder
        remainder = alpha % beta
    return beta

class Fraction:
    '''models  a fraction'''
    
    def __init__ (self, numerator = 0, denominator = 1):
        '''initializes a fraction object
        if denominator doesn't equal 0'''
        if denominator != 0:
            self._numerator = numerator
            self._denominator = denominator
            self.simplify() #simplifying the fraction 
        else:
            print('Unable to create invalid fraction', file=sys.stderr)
            sys.exit(-1)
            
    def __str__ (self):
        '''returns the fraction as a string'''
        return (str(self._numerator) + '/' + str(self._denominator))
    
    #accessors
    def get_denominator(self):
        '''accessor for denominator'''
        return self._denominator
    
    def get_numerator(self):
        '''accessor for numerator'''
        return self._numerator
    
    #mutators
    def simplify(self):
        '''fraction simplification
        finds the GCD and reduces the fraction'''
        gcd = computeGCD(self._numerator, self._denominator)
        if gcd != 0:
            self._numerator = self._numerator//gcd
            self._denominator = self._denominator//gcd
        if self._denominator < 0:
            self._numerator = self._numerator * -1
            self._denominator = self._denominator * -1
    
    def __mul__ (self, other):
        new_numerator = self._numerator * other.get_numerator()
        new_denominator = self._denominator * other.get_denominator()
        
        new_fraction = Fraction(new_numerator, new_denominator)
        
        return new_fraction
    
#-----------main code ----------

f1 = Fraction()
print(f1)

f2 = Fraction(1,2) # construct a fraction object for one half
print(f2) #print the object

print(f2.get_denominator()) #testing the accessors
print(f2.get_numerator()) #testing the accessors

f3 = Fraction (2,4) #testing the fraction simplifier
print(f3) #printing the object

f4 = Fraction (6,-12) #test
print(f4)#printing the test

f5 = Fraction(-3,-9)
print(f5)

f6 = f1 * f2
print(f6)