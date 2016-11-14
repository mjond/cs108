''' Abstraction drawing program
Created September 8, 2014
homework01
@author: Mark Davis (mjd85)
'''
#getting the turtle and naming it tim
import turtle
window = turtle.Screen()
chuck = turtle.Turtle()
chuck.pensize(8)

#drawing the red triangle
chuck.color("red")
chuck.forward(150)
chuck.left(120)
chuck.forward(150)
chuck.left(120)
chuck.forward(150)

#repositioning the pen
chuck.penup()
chuck.left(30)
chuck.forward(40)
chuck.pendown()
chuck.color('green')
#drawing the green triangle
chuck.left(90)
chuck.forward(150)
chuck.left(120)
chuck.forward(150)
chuck.left(120)
chuck.forward(150)

#repositioning the pen
chuck.left(120)
chuck.penup()
chuck.forward(30)
chuck.left(90)
chuck.forward(15)
chuck.pendown()
chuck.color('blue')
#drawing the blue triangle
chuck.right(90)
chuck.forward(150)
chuck.left(120)
chuck.forward(150)
chuck.left(120)
chuck.forward(150)

window.exitonclick()