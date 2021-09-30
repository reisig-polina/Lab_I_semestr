import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((700, 700))

circle(screen, (255, 255, 0), (350, 350), 200)
circle(screen, (0, 0, 0), (350, 350), 200, 2)
circle(screen, (220, 20, 30), (280, 290), 30)
circle(screen, (220, 20, 30), (420, 290), 45)
circle(screen, (0, 0, 0), (280, 290), 30, 2)
circle(screen, (0, 0, 0), (420, 290), 45, 2)
circle(screen, (0, 0, 0), (280, 290), 10)
circle(screen, (0, 0, 0), (420, 290), 15)
polygon(screen, (0, 0, 0), [(220, 230), (210, 240), (320, 280), (330, 270)])
polygon(screen, (0, 0, 0), [(480, 220), (490, 230), (380, 270), (370, 260)])
rect(screen, (0, 0, 0), (260, 420, 180, 40)) 
    
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
