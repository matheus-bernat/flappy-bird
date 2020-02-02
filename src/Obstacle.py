import pygame
import Constants
from random import randrange

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, speed, image_file):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.image = pygame.transform.scale(pygame.image.load(image_file), (50, 500))
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        self.rect.x -= self.speed

    def respawn(self, new_x, new_y):
        self.rect.x += new_x
        self.rect.y = new_y

    def is_out_of_screen(self):
        return self.rect.x + self.rect.size[0] < 0
