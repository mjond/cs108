'''Driver program for lab09
Created Fall 2014
lab09
@author Mark Davis
'''

import employee
# function for finding the average salary
def print_average(counts, totals, outFile):
    '''(dict, dict, outFile) --> None
    Prints the average into a table to the given outFile'''
    
    outFile.write('Rank\tAverage Salary\n')
    
    for rank in totals:
        average = totals[rank] / counts[rank]
        outFile.write('%s\t %d\n' % (rank, average))

    
    
employees = []
#opening the salary txt file and reading each line. Storing the lines in a list and printing the length
with open('salary.txt') as file:
    lines = file.readlines()
    for each_line in lines:
        employees.append(employee.Employee(each_line))
    print(len(employees))
    # if the list is empty, return an error
if employee == []:
    print('Error')
    #otherwise updating the corresponding salaries with each rank and number of each rank to the two dictionaries
else:
    totals = {}
    counts = {}
    max_employee = employees[0]
    min_employee = employees[0]
    #looping through each employee to update the dictionaries
    for each in employees:
        if each.get_rank() in totals:
            totals[each.get_rank()] += each.get_salary() 
            counts[each.get_rank()] += 1
            
        else:
            totals[each.get_rank()] = each.get_salary()
            counts[each.get_rank()] = 1
            #finding the max and min employee
        if max_employee.get_salary() < each.get_salary():
            max_employee = each
        if min_employee.get_salary() > each.get_salary():
            min_employee = each
            
            #writing the max and min salaries to a file with the corresponding ranks
with open('employee_stats.txt', 'w') as outFile:
    print_average(counts,totals,outFile)
    outFile.write('The employee with lowest salary is' + str(min_employee) + '\n')
    outFile.write('The employee with highest salary is' + str(max_employee) + '\n')