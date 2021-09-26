from random import randint
import turtle as t

number_of_turtles = 15

x = []
y = []
vx = []
vy = []
for i in range(number_of_turtles):
    x.append(randint(-200, 200))
    y.append(randint(-200, 200))
    vx.append(randint(-5, 5))
    vy.append(randint(-5, 5))

t.penup()
t.goto(-200, -200)
t.pendown()
t.goto(-200, 200)
t.goto(200, 200)
t.goto(200, -200)
t.goto(-200, -200)
t.ht()

pool = [t.Turtle(shape='circle') for i in range(number_of_turtles)]
for i, unit in enumerate(pool):
    unit.penup()
    unit.speed(5)
    unit.goto(x[i], y[i])

while True:
    for i, unit in enumerate(pool):
        if x[i] >= 200 or x[i] <= -200:
            vx[i]*=-1
        if y[i] >= 200 or y[i] <= -200:
            vy[i]*=-1
        x[i]+=vx[i]
        y[i]+=vy[i]
        unit.goto(x[i], y[i])

    



