''' DNA reverse input program
created Fall 2014
homework 03
@author Mark Davis (mjd85)
'''
#getting the sequence and patterns
characters = input('Enter a sequence of characters: ')
pattern = input('Enter the pattern: ')
reverse_pattern = pattern[::-1]

#finding the starting and ending position of the string in between the patterns        
index1 = characters.find(pattern)
index2 = index1 + len(pattern)
index3 = characters.find(reverse_pattern)

#reversing the string in between the patterns
subset = characters[index2:index3]
subset_reverse = subset[::-1]

#putting together the pattern and reversed string
reversed_input = characters[0:index2] + subset_reverse + characters[index3:]

print(reversed_input)