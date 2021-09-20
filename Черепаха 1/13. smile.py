import turtle
import math
turtle.shape('turtle')
turtle.speed(10)

def halfcircle(x):
    for i in range (120):
        turtle.forward(x)
        turtle.left(1)

def circle(x):
    for i in range (360):
        turtle.forward(x)
        turtle.left(1)

turtle.color("black", "yellow")
turtle.begin_fill()
circle(1)
turtle.end_fill()

turtle.penup()
turtle.goto(-25, 65)
turtle.color("black", "blue")
turtle.begin_fill()
circle(0.2)
turtle.end_fill()

turtle.penup()
turtle.goto(25, 65)
turtle.color("black", "blue")
turtle.begin_fill()
circle(0.2)
turtle.end_fill()

turtle.pensize(8)

turtle.penup()
turtle.goto(0, 65)
turtle.pendown()
turtle.goto(0, 55)

turtle.color("red")
turtle.penup()
turtle.goto(-108*math.sin(math.pi/3)/math.pi, 40)
turtle.right(60)
turtle.pendown()
halfcircle(0.6)

