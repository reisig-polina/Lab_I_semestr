import turtle as t
from random import *
t.shape('turtle')
t.speed(10)

for i in range(250):
    t.left(randint(0, 360))
    t.forward(randint(1, 25))