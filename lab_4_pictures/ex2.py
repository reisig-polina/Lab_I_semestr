import pygame
from pygame.draw import *
import random
from random import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 550))

rect(screen, (200, 170, 55), (0, 75, 400, 220))
rect(screen, (95, 190, 210), (0, 0, 400, 75))
rect(screen, (55, 200, 115), (0, 295, 400, 255))

width = 0
while width < 400:
    x = randint(25, 35)
    rect(screen, (0, 0, 0), (width, 75, x, 220), 1)
    width += x

polygon(screen, (215, 70, 0), [(250, 350), (290, 290), (330, 370)])
polygon(screen, (0, 0, 0), [(250, 350), (290, 290), (330, 370)], 2)

polygon(screen, (215, 70, 0), [(330, 370), (290, 290), (340, 260), (380, 340)])
polygon(screen, (0, 0, 0), [(330, 370), (290, 290), (340, 260), (380, 340)], 2)

polygon(screen, (200, 170, 55), [(250, 350), (330, 370), (330, 460), (250, 430)])
polygon(screen, (0, 0, 0), [(250, 350), (330, 370), (330, 460), (250, 430)], 2)

polygon(screen, (200, 170, 55), [(330, 370), (330, 460), (380, 425), (380, 340)])
polygon(screen, (0, 0, 0), [(330, 370), (330, 460), (380, 425), (380, 340)], 2)

ellipse(screen, (0, 0, 0), (270, 380, 40, 45))

ellipse(screen, (110, 105, 85), (55, 400, 85, 50))
ellipse(screen, (110, 105, 85), (110, 390, 60, 40))
ellipse(screen, (110, 105, 85), (145, 410, 30, 30))
ellipse(screen, (110, 105, 85), (165, 430, 10, 30))
ellipse(screen, (110, 105, 85), (155, 455, 15, 10))
ellipse(screen, (110, 105, 85), (90, 430, 20, 50))
ellipse(screen, (110, 105, 85), (50, 410, 20, 50))
ellipse(screen, (110, 105, 85), (110, 400, 30, 30))
ellipse(screen, (110, 105, 85), (130, 420, 10, 30))
ellipse(screen, (110, 105, 85), (120, 445, 15, 10))
ellipse(screen, (110, 105, 85), (80, 470, 20, 15))
ellipse(screen, (110, 105, 85), (40, 450, 20, 15))
rect(screen, (110, 105, 85), (60, 380, 40, 40))
rect(screen, (0, 0, 0), (60, 380, 40, 40), 1)
ellipse(screen, (110, 105, 85), (55, 380, 10, 15))
ellipse(screen, (110, 105, 85), (95, 380, 10, 15))
ellipse(screen, (0, 0, 0), (55, 380, 10, 15), 1)
ellipse(screen, (0, 0, 0), (95, 380, 10, 15), 1)
ellipse(screen, (255, 255, 255), (65, 397, 10, 5))
ellipse(screen, (255, 255, 255), (85, 397, 10, 5))
ellipse(screen, (0, 0, 0), (65, 397, 10, 5), 1)
ellipse(screen, (0, 0, 0), (85, 397, 10, 5), 1)
ellipse(screen, (0, 0, 0), (68, 397, 5, 5))
ellipse(screen, (0, 0, 0), (88, 397, 5, 5))
polygon(screen, (255, 255, 255), [(72, 412), (76, 412), (74, 407)])
polygon(screen, (255, 255, 255), [(88, 412), (84, 412), (86, 407)])
line(screen, (0, 0, 0), (70, 412), (90, 412), 1)

ellipse(screen, (0, 0, 0), (270, 420, 20, 10), 1)
ellipse(screen, (0, 0, 0), (260, 425, 20, 20), 1)
ellipse(screen, (0, 0, 0), (255, 436, 10, 15), 1)
ellipse(screen, (0, 0, 0), (235, 442, 25, 15), 1)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
