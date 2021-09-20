import turtle
turtle.shape('turtle')
turtle.speed(10)

def circle(x):
    for i in range (360):
        turtle.forward(x/10)
        turtle.left(1)

turtle.left(90)

for i in range(10, 20, 1):
    for j in range(2):
        circle(i)
        turtle.left(180)


