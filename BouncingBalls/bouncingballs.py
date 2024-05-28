'''
    Name    : Nasim
    Program : Bouncing Balls
    Date    : May 28, 2024 1:00 PM
'''
import pygame, sys, random
from pygame.locals import QUIT
import ball

pygame.init()

screen = pygame.display.set_mode((500, 500))

balls = []

for i in range(10000):
    #r = random.randint(0, 255)
    #g = random.randint(0, 255)
    #b = random.randint(0, 255)
    r = 0
    g = 0
    b = 155
    a = random.randint(10, 255)

    b = ball.Ball(screen, random.randint(50, 300), random.randint(50, 400), random.randint(2, 10), random.randint(-5, 5), random.randint(-5, 5), (r, g, b, a))
    balls.append(b)

clock = pygame.time.Clock()

while True:
    clock.tick(30)

    for ev in pygame.event.get():
        if ev.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill ("white")

    for b in balls:
        b.move()

    pygame.display.update()