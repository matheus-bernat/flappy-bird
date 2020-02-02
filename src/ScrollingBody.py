import Constants
import pygame
import math
class ScrollingBody:
    def __init__(self,size,color,angle,radius = Constants.WINDOW_HEIGHT*1.5):
        self.radius = radius
        self.angle = angle
        self.size = size
        self.color = color
        self.x_pos = self.radius*math.cos(self.angle)
        self.y_pos = self.radius*math.sin(self.angle)

    def draw(self, window):
        pygame.draw.circle(window,self.color,(round(self.x_pos),round(self.y_pos)),self.size)

    def update(self):
        self.angle -= .001
        self.x_pos = Constants.WINDOW_WIDTH/2 + self.radius*math.cos(self.angle)
        self.y_pos = Constants.WINDOW_HEIGHT*2 + self.radius*math.sin(self.angle)
