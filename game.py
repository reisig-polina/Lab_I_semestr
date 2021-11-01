import math as np
import pygame
from pygame.draw import *
from random import randint, choice
pygame.init()

width = 1000 # параметры экрана
height = 700

FPS = 10
screen = pygame.display.set_mode((width, height))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

class Ball:

    def __init__(self, r, v_x, v_y, timer):
        '''
        r - радиус шарика
        x - координата по OX
        y - координата по OY
        v_x - скорость по ОХ
        v_y - скорость по ОY
        timer - время нахождения шарика по экране
        '''
        self.color = choice(COLORS)
        self.x = r + randint(0, width - 2*r)
        self.y = r + randint(0, height - 2*r)
        self.r = r
        self.v_x = v_x
        self.v_y = v_y
        self.timer = timer

    def move(self):
        '''
        двигает шарик по экрану
        '''
        circle(screen, self.color, (self.x, self.y), self.r)
        self.x += self.v_x
        self.y += self.v_y

    def collision(self):
        '''
        разворачивает шарик при столкновении со стеной
        '''
        if self.x <= self.r or self.x >= width - self.r:
            self.v_x *= -1
        if self.y <= self.r or self.y >= height - self.r:
            self.v_y *= -1

    def disappear(self):
        '''
        уничтожает шарик по прошествии определенного времени
        '''
        self.timer -= 1
        if self.timer == 0:
            return(True)
        else:
            return(False)

    def disappear_on_click(self, mouse_x, mouse_y):
        '''
        уничтожает шарик при клике мышкой
        '''
        if (self.x - mouse_x)**2 + (self.y - mouse_y)**2 <= self.r**2:
            return(True)

    def pulsation(self, R):
        circle(screen, WHITE, (self.x, self.y), R)
                                                                                

print("ENTER YOUR NAME:")
name = input()
        

pygame.display.update()
screen.fill(BLACK)
clock = pygame.time.Clock()
finished = False
num = 0

pool = []
score = 0
time = 0
ind = 1
x_whiteball = randint(35, width - 35)
y_whiteball = randint(35, height - 35)
time_limit = 500 # время игры

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_coor = event.pos
            for ball in pool:
                if (ball.disappear_on_click(mouse_coor[0], mouse_coor[1])):
                    pool.remove(ball)
                    score += 1
         
    v_x = randint(-10, 10)
    v_y = randint(-10, 10)
    pool.append(Ball(randint(10, 20), v_x, v_y, 20))

    for ball in pool:
         ball.move()
         ball.collision()
         if ball.disappear():
             pool.remove(ball)

    pygame.display.update()
    screen.fill(BLACK)
    time += 1

    if time%100 == 0:
        x_whiteball = randint(35, width - 35)
        y_whiteball = randint(35, height - 35)

    if time%100 < 21 and ind == 1:
        r_whiteball = randint(25, 35)
        circle(screen, WHITE, (x_whiteball, y_whiteball), r_whiteball)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_coor = event.pos
                if (x_whiteball - mouse_coor[0])**2 + (y_whiteball - mouse_coor[1])**2 <= r_whiteball**2:
                    score+=2
                    ind = 0
                    
    if time%100 == 21:
        ind = 1
                
    if time == time_limit:
        finished = True

    if finished:
        output = open('score.txt', 'w')
        print(name, ": ", score, file=output)
        output.close()
        pygame.quit()


        








    
