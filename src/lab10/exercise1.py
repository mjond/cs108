'''Excercise 1
Created on Nov 6, 2014
lab10 - exercise 1
@author: Mark Davis
'''

try: 
    'hi' + 4
except TypeError as ex:
    print('Cannot add integers to strings', ex)
    
try:
    10 / 0
except ZeroDivisionError as z:
    print('Cannot divide by 0', z)
    
try:
    'person'.find_first('e')
except AttributeError as ex:
    print('Attribute Error', ex)
    
try:
    [0,1,2]['summer']
except TypeError as p:
    print('List must be integer', p)

try:     
    ['hi','there','student'][5]
except IndexError as p:
    print('Index out of range', p)
   
try: 
    print(name)
except NameError as x:
    print('name is not defined', x)
    
try:
    9 <= (3,4)
except TypeError as t:
    print('type error', t)

try: 
    f = open('missingFile.txt')
except FileNotFoundError as k:
    print('File does not exist', k)
    
    


    


