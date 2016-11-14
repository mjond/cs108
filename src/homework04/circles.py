'''Circle drawing program
Created Fall 2014
Homework 04    
@author Mark Davis
'''

import turtle
#getting the coordinates for circle 1
x1 = int(input('Enter an x coordinate for circle 1: '))
y1 = int(input('Enter a y coordinate for circle 1: '))
rad1 = int(input('Enter a radius length for circle 1: '))
#getting the coordinates for circle 2
x2 = int(input('Enter another x coordinate for circle 2: '))
y2 = int(input('Enter another y coordinate for circle 2: '))
rad2 = int(input('Enter another radius length for circle 2: '))

window = turtle.Screen()
chuck = turtle.Turtle()
#Drawing the first circle        
chuck.penup()
chuck.goto(x1,y1 - rad1)
chuck.pendown()
chuck.circle(rad1)
#Drawing the second circle
chuck.penup()
chuck.goto(x2,y2 - rad2)
chuck.pendown()
chuck.circle(rad2)
#finding out if the circles overlap, contain each other or are disjoint
if chuck.distance(x1,y1)>= rad1 + rad2:
    chuck.write('Circles are disjoint.',0, 'left', font = ('Arial',18,'normal'))
    
elif chuck.distance(x1,y1) <= rad1 - rad2:
    chuck.write('Circle 1 contains circle 2', 0 , 'left', font = ('Arial',18,'normal'))
    
elif chuck.distance(x1,y1) <= rad1 + rad2:
    chuck.write('Circle 1 and circle 2 overlap',0, 'left', font = ('Arial',18,'normal'))
#font=(<font_name>, <font_size>, <font_descriptor>)
window.exitonclick()