import turtle
import math

turtle.shape('turtle')

def polygon(n):
    turtle.penup()
    #turtle.goto(10*(n-2), 0)
    turtle.forward(10)
    turtle.pendown()
    turtle.left(180 - 90*(n-2)/n)
    for i in range (n):
        turtle.forward(20*(n-2)*math.sin(math.pi/n))
        turtle.left(180 - 180*(n-2)/n)
    turtle.right(180 - 90*(n-2)/n)

    

for k in range(3, 16, 1):
    polygon(k)
