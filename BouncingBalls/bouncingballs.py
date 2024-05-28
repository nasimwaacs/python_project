'''
    Name    : Nasim
    Program : Bouncing Balls
    Date    : May 28, 2024 1:00 PM
'''
import pygame, sys
from pygame.locals import QUIT
import ball

pygame.init()

screen = pygame.display.set_mode((500, 500))

b1 = ball.Ball(screen)

wallX = 400

clock = pygame.time.Clock()

while True:
    clock.tick(30)

    for ev in pygame.event.get():
        if ev.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill ("white")

    b1.move()

    pygame.display.update()