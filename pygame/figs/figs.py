import pygame
from pygame.locals import *

pygame.init()
width = 1920
height = 1080
pygame.display.set_mode((width, height))
pygame.display.set_caption('Figuritas :)')
clock = pygame.time.Clock()

run = True
while run: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    clock.tick(60)
