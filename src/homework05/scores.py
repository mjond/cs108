'''Scoring Generator
Created Fall 2014
homeowork05
@author Mark Davis (mjd85)
'''

#creating an empty dictionary
dict = {}
#getting the number of students
num_student = int(input('Enter the number of students: '))

#creating the loop for the names of students and their score
for c in range(1,num_student + 1):
    #because one can't put commas in an input statement, I put the question into a string and made it a variable
    question = 'Enter the name and score of student ' + str(c) + ':' 
    #putting the string variable into the input statement
    name, score = input(question).split()
    #adding the score and name into the empty dictionary
    dict[score] = name
    
#finding the max value in the dictionary
max_value = max(dict)

print('The highest value is', max_value, 'by', dict[max_value])
#deleting the highest value from the dictionary so the second highest value can be found
del dict[max_value]
new_max_value = max(dict)
#printing the second highest value
print('The second highest value is', max(dict), 'by', dict[new_max_value])


