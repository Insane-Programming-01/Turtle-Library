# Installing the turtle library
# Run 'pip install turtle' in the terminal

# Importing the turtle
import turtle
# from turtle import *

t = turtle.Turtle()

# Setting the title for our window
turtle.title('My First Lesson')

# Moving the turtle, forward and backward functions

t.forward(90)
# t.fd(90)
t.backward(180)
# t.back(180)

# Changing the direction of turtle, right and left

for i in range(4):
    t.forward(180)
    t.right(90) # short hand - rt

# Getting the position

print(t.position())

# Solving automatic screen termination of the window

turtle.done()
