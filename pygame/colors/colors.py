import pygame
from pygame.locals import *
import random

pygame.init()
WIDHT = 1920
HEIGHT = 1080
screen = pygame.display.set_mode((WIDHT, HEIGHT))
clock = pygame.time.Clock()

run = True
while run: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    color = (random.randint(0,255),random.randint(0,255), random.randint(0,255))
    screen.fill(color)
    pygame.display.update()
    clock.tick(10)
