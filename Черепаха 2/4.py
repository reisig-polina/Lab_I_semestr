import turtle as t
import math
t.shape('circle')
t.speed(1)

v_x = 20
v_y = 70
j = 0 

for i in range(500):
	if(v_y - 10*(j/10) <= -v_y):
		j = 0
		v_y = ((v_y*0.9)//1)*(-1)
	t.goto(v_x*(i/10), v_y*(j/10)-5*(j/10)**2)
	j+=1
