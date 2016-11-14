''' program to calculate change
September 15, 2014
homework 02
@authors Mark Davis (mjd85)'''
#made variables for the charged and payed amounts.
charged = int(input('Please enter the charged amount: '))
payed = int(input('Please enter the amount payed: '))

original_change = (payed - charged)
change = original_change
#computing the amount of twenties needed for the change
twenties = change//20 
change = change % 20
#computing the amount of tens needed
tens = change//10
change = change % 10
#computing the amount of fives needed
fives = change//5
change = change % 5
#computing the amount of ones needed
ones = change//1
change = change % 1

#print the change 
print('Change is: $',original_change, twenties , '20(s),', tens, '10(s)', fives, '5(s)', ones, '1(s).' )


