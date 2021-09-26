import turtle as t
import math
t.shape('turtle')

with open('input.txt') as f:
    lines = f.readlines()
    
for line in lines:
    a = line.split(", ")
    x = int(a[0])
    y = int(a[1])
    if x == 0:
        t.penup()
    elif x == 1:
        t.pendown()
    else:
        t.goto(x, y)
