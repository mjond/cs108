'''Find Prefix program
Created Fall 2014
homeowork07
@author Mark Davis (mjd85)
'''

def find_prefix(string1,string2):
    letters = ""
    
    if len(string1) > len(string2):
        short_len = len(string2)
    else:
        short_len = len(string1)
    
    for i in range(0,short_len):
        if string1[i] == string2[i]:
            letters = letters + string1[i]
        else:
            return letters
    return letters
        
        
    
    
string_one = input('Enter a string: ')
string_two = input('Enter another string: ')

print(find_prefix(string_one,string_two))

