import pygame

class Ball():

    def __init__(self, _screen, _x=0, _y=0, _radius=10, _speedX=1, _speedY=1, _color=(0, 0, 255)):
        self.screen = _screen
        self.x = _x
        self.y = _y
        self.radius = _radius
        self.speedX = _speedX
        self.speedY = _speedY
        self.color = _color



    def update(self):
        self.x += self.speedX
        self.y += self.speedY

        self.draw()

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)