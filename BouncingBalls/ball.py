import pygame

class Ball():
    # Constructor
    def __init__(self, screen, x=0, y=0, radius=10, speedX=1, speedY=1, color=(0, 0, 255) ):
        self.screen = screen
        self.x = x
        self.y = y
        self.radius = radius
        self.speedX = speedX
        self.speedY = speedY
        self.color = color

    def move(self):
        self.x += self.speedX
        self.y += self.speedY

        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)
    