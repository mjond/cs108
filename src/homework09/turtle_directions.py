'''Turtle file import program
created Fall 2014
homework09
@author Mark Davis (mjd85)
'''
#importing turtle
import turtle 
bob = turtle.Turtle()
#getting the file from the user
file_input = input('Enter your file here: ')
#opening the file and putting the commands into a list called 'commands'
with open(file_input, 'r') as f:
    commands = f.readlines()
#looping through the 'commands' list and assigning the actions to 'bob'
for i in commands:
    #assigning the color to bob
    if 'color' in i:
        list0 = i.split()
        action = 'bob.color(' + "'"+ list0[1] +"')"
        exec(action)
        #assigning the pendown action
    if 'pendown' in i:
        bob.pendown() 
        #determining the values for goto()       
    if 'goto' in i:
        go_lst = i.split()
        bob.goto(int(go_lst[1]), int(go_lst[2]))
        #getting the pointsize 
    if 'point' in i:
        list1 = i.split()
        bob.goto(int(list1[2]), int(list1[3]))
        bob.dot(int(list1[1]))
        
    if 'penup' in i:
        bob.penup()
    
#assigning the window and exiting on click
window = turtle.Screen()

window.exitonclick()