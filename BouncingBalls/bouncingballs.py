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

for i in range(5000):
    speedX = random.randint(-5, 5)
    speedY = random.randint(-5, 5)
    radius = random.randint(10, 20)

    b = random.randint(150, 255)
    g = random.randint(150, 255)
    r = random.randint(230, 255)
    '''
    r = 0
    g = 0
    b = 155'''
    a = random.randint(10, 30)
    col = pygame.Color(r, g, b, a)

    randomBall = ball.Ball(screen, random.randint(5, 495), random.randint(5, 495), radius, speedX, speedY, col)
    balls.append(randomBall)

clock = pygame.time.Clock()

while True:
    clock.tick(30)

    for ev in pygame.event.get():
        if ev.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill ("white")

    for eachBall in balls:
        eachBall.move()

    pygame.display.update()
