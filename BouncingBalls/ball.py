import pygame, random

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

        self.setBounds(0, 500, 0, 500)

    def setBounds(self, left, right, top, bottom):
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom

    def move(self):
        self.x += self.speedX
        self.y += self.speedY

        '''self.speedX += random.randint(-3, 3)
        self.speedX += random.randint(-3, 3)'''

        if self.y < self.top or self.y > self.bottom:
            self.speedY = -self.speedY 

        if self.x < self.left or self.x > self.y:
            self.speedX = -self.speedX 

        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)
    