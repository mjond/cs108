'''Geometric program
Created Fall 2014
homeowork06
@author Mark Davis
'''

#function calculates the geometric mean by the length of the list
def geo_mean(lists):
    '''list -> float
    computes the geometric mean from a list of values   
    '''
    gmean = 1
    for each_value in lists:
        each_value = int(each_value)
        gmean = each_value * gmean
    return gmean**(1/len(lists))


#receiving the user input
values = [] 
values = input('Enter a list of numbers: ').split()


print(geo_mean(values))
    