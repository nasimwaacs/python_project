'''
    Name    : Nasim
    Program : Do Graphics
    Date    : May 22, 2024 1:00 PM
'''
import pygame, sys
from pygame.locals import QUIT

pygame.init()

screen = pygame.display.set_mode((500, 500))

blockX = 10
blockY = 300

wallX = 400

clock = pygame.time.Clock()

while True:
    clock.tick(30)

    for ev in pygame.event.get():
        if ev.type == QUIT:
            pygame.quit()
            sys.exit()


    screen.fill ("white")

    # Draw the boundary 
    pygame.draw.line(screen, "red", (wallX, 0), (wallX, wallX))

    # Draw the block
    pygame.draw.rect(screen, "blue", (blockX, blockY, 50, 50))
    blockX = blockX + 1

    pygame.display.update()