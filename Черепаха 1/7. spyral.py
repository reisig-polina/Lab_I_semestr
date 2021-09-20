import turtle
import math

turtle.speed(10)

turtle.shape('turtle')
for i in range(2000):
    turtle.goto(i*math.cos(math.pi*i/180)/10, i*math.sin(math.pi*i/180)/10)
    
    

