'''
    Name    : Nasim
    Program : Do Graphics
    Date    : May 22, 2024 1:00 PM
'''
import pygame, sys
from pygame.locals import QUIT

pygame.init()

screen = pygame.display.set_mode((500, 500))

while True:

    for ev in pygame.event.get():
        if ev.type == QUIT:
            pygame.quit()
            sys.exit()


    screen.fill ((255, 15, 255))
    pygame.display.update()