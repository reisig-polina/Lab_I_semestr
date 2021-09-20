import turtle
turtle.shape('turtle')
turtle.speed(10)

def halfcircle(x):
    for i in range (180):
        turtle.forward(x)
        turtle.right(1)

turtle.left(90)

for i in range(10):
    halfcircle(2)
    halfcircle(0.3)


