import turtle
turtle.shape('turtle')

def circle():
    for i in range (360):
        turtle.forward(1)
        turtle.left(1)

for i in range(6):
    circle()
    turtle.left(60)

