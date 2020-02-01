import pygame
import Constants
from random import randrange

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x_pos, width, gap, speed):
        pygame.sprite.Sprite.__init__(self)
        self.gap = gap
        self.y_pos = randrange(0, Constants.WINDOW_HEIGHT - self.gap)
        self.width = width
        self.speed = speed
        #self.shape = [pygame.Rect(self.x_pos,0,self.width,self.y_pos), pygame.Rect(self.x_pos,self.y_pos+self.gap,self.width,Constants.WINDOW_HEIGHT)]
        self.image_list = [pygame.image.load('../res/obstacle_bottom.png'),\
                           pygame.image.load('../res/obstacle_top.png')]
        self.rect_list = [self.image_list[0].get_rect(),\
                          self.image_list[1].get_rect()]
        self.rect_list[0].x = x_pos
        self.rect_list[1].x = x_pos

    def move(self):
        self.rect_list[0].x -= self.speed
        self.rect_list[1].x -= self.speed

    #    self.shape[0] = self.shape[0].move(-self.speed,0)
    #    self.shape[1] = self.shape[1].move(-self.speed,0)

    def respawn(self, new_x):
        self.y_pos = randrange(0, Constants.WINDOW_HEIGHT - self.gap)
        new_x += self.shape[0].x
        self.shape = [pygame.Rect(new_x,0,self.width,self.y_pos), pygame.Rect(new_x,self.y_pos+self.gap,self.width,Constants.WINDOW_HEIGHT)]

    def is_out_of_screen(self):
        return self.shape[0].x + self.width < 0
