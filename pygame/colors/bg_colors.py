import pygame
from pygame.locals import *

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
background = GRAY

pygame.init()
pygame.display.set_caption('no me gustan los titulos que son muy largos')
key_dict = {K_k:BLACK, K_r:RED, K_g:GREEN, K_b:BLUE,K_y:YELLOW, K_c:CYAN, K_m:MAGENTA, K_w:WHITE}
screen = pygame.display.set_mode((640, 240))

running = True
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        if event.type == pygame.KEYDOWN:
            if event.key in key_dict:
                background = key_dict[event.key]

    screen.fill(background)
    pygame.display.update()
pygame.quit()
