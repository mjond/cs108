'''Validation Program
Created Fall 2014
Lab 07
@author Mark Davis (mjd85)
'''

def print_menu():
    print('Please select from the following list of options (type the appropriate character)')
    print('A. Print a nice message')
    print('B. Validate a SSN')
    print('C. Validate a password')
    print('D. Validate a Credit Card Number')
    print('Q. Quit')
    
def isVallidSSN(string):
    if (string[0:3].isdigit()) and (string[3] == '-') and (string[4:6].isdigit()) and (string[6] == '-') and (string[7:12].isdigit()):
        return(True)
    else:
        return(False)
    
def isValidPassword(string):
    num = 0
    for i in string:
        if i.isdigit() == True:
            num += 1
    if len(string) >= 8 and string.isalnum() and num >= 2:
        return(True)
    else:
        return(False)
    
def isValidPrefix(string):
    if string.startswith('37') or string.startswith('4') or string.startswith('5') or string.startswith('6'):
        return(True)
    else:
        return(False)
    
def sum_of_odds(string):
    odd_list = string[::-2]
    
    int_list = []
    for i in odd_list:        
        int_list.append (int(i))
    return (sum(int_list)) 
   
def sum_of_double_events(string):
    even_list = string[-2::-2]
    even = []
    for i in even_list:
        number = int(i)*2
        if number > 9:
            number = (number % 10) + 1
        even.append(number)
    return(sum(even))

def isValidCC(credit):
    if (isValidPrefix(credit) == True) and (13<=len(credit)<=16) and (credit.isalnum()) and ((sum_of_odds(credit) + sum_of_double_events(credit)) // 10 == 0):
        return(True)
    else:
        return(False)
    
while True:
    print_menu()
    user_input = input('Choice: ')
    if user_input == 'A':
        print('Have a great day!')
    elif user_input == 'Q':
        print('Good-bye!')
        break
    elif user_input == 'B':
        SSN_input = input('Enter a SSN: ')
        if isVallidSSN(SSN_input) == True:
            print('Valid SSN')
        else:
            print('Invalid SSN')
    elif user_input == 'C':
        pass_input = input('Enter a password: ')
        if isValidPassword(pass_input) == True:
            print('Valid Password')
        else:
            print('Invalid Password')
    elif user_input == 'D':
        cc = int(input('Enter a credit card number: '))
        if isValidCC(cc) == True:
            print('Valid Credit Card')
        else:
            print('Invalid Credit Card')
    else:
        print('That was not a valid option')