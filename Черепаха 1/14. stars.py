import turtle
import math
turtle.shape('turtle')

def star(x):
    turtle.right(90 - 90/x)
    for i in range(x):
        turtle.forward(100)
        turtle.right(180 - 180/x)
    turtle.left(90 - 90/x)

turtle.penup()
turtle.goto(-150, 0)
turtle.pendown()

star(5)

turtle.penup()
turtle.goto(150, 0)
turtle.pendown()

star(11)
