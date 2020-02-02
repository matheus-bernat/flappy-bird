from Constants import *
import pygame
class ScrollingBackground(pygame.sprite.Sprite):
    def __init__(self,x_pos,speed,orientation):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.image = pygame.transform.scale(pygame.image.load("../res/background.png"), (WINDOW_WIDTH, WINDOW_HEIGHT))
        if orientation == 0:
            self.image = pygame.transform.flip(self.image,True,False)
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = 0

    def update(self):
        self.move()

    def move(self):
        self.rect.x -= self.speed
        if self.is_out_of_screen():
            self.respawn()

    def respawn(self):
        self.rect.x += WINDOW_WIDTH*2

    def is_out_of_screen(self):
        return self.rect.x + WINDOW_WIDTH < 0
