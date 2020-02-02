import Constants
from random import randrange
import pygame
import math
class ScrollingBody:
    def __init__(self,size,color,angle,snow=False,radius = Constants.WINDOW_HEIGHT*9.5):
        self.radius = radius
        self.angle = angle
        self.size = size
        self.color = color
        if snow:
            self.x_pos = randrange(0,Constants.WINDOW_WIDTH)
            self.y_pos = -randrange(0,Constants.WINDOW_HEIGHT)
            self.fall_speed = randrange(1,200)/100
        else:
            self.x_pos = self.radius*math.cos(self.angle)
            self.y_pos = self.radius*math.sin(self.angle)
        self.snow = snow

    def draw(self, window):
        pygame.draw.circle(window,self.color,(round(self.x_pos),round(self.y_pos)),self.size)

    def update(self):
        if not self.snow:
            self.angle -= .0002
            self.x_pos = Constants.WINDOW_WIDTH/2 + self.radius*math.cos(self.angle)
            self.y_pos = Constants.WINDOW_HEIGHT*10 + self.radius*math.sin(self.angle)
        else:
            if self.y_pos > Constants.WINDOW_HEIGHT:
                self.y_pos = 0
            else:
                self.y_pos = self.y_pos + self.fall_speed
