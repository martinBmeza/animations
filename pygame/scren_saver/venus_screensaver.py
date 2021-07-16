import pygame
from pygame.locals import * 

pygame.init()
pygame.display.set_caption('VENUS SCREENSAVER')
GREEN = (0, 255, 0)
RED = (255, 0, 0)

size = int(1920), int(1080)
width, height = size

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

ball = pygame.image.load('venus.jpeg')
ball = pygame.transform.scale(ball, (300,300))
rect = ball.get_rect()
speed = [2,2]

def bounce_colors(speed):
    if ((speed[0] > 0) and (speed[1] > 0)):
        bg_color = (0, 100, 0)
    if ((speed[0] < 0) and (speed[1] < 0)):
        bg_color = (100, 0, 0)
    if ((speed[0] < 0) and (speed[1] > 0)):
        bg_color = (0,0,100)
    if ((speed[0] > 0) and (speed[1] < 0)):
        bg_color = (100, 100, 100)
    return bg_color

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    rect = rect.move(speed)
    if rect.left < 0 or rect.right > width:
        speed[0] = -speed[0]
    if rect.top < 0 or rect.bottom > height:
        speed[1] = -speed[1]
     
    screen.fill(bounce_colors(speed))
    pygame.draw.rect(screen, RED, rect, 1)
    screen.blit(ball, rect)

    pygame.display.update()
    clock.tick(150)
pygame.quit()


