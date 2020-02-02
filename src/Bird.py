import pygame
import Constants
import math

GRAVITY = .3

class Bird(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, y_vel, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.bird_width = width
        self.bird_height = height
        self.y_vel = y_vel
        self.image = pygame.transform.scale(pygame.image.load('../res/bird.png'), (48, 36))
        self.rect = self.image.get_rect() # Get the dimensions of the sprite
        self.original_image = self.image
        self.rect.x = x_pos
        self.rect.y = y_pos
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.mask = pygame.mask.from_surface(self.image)
        self.rotation = 0
        self.alive = True
        self.score = 0

    def flap(self):
        self.y_vel = -8

    def fall(self):
        self.y_pos += self.y_vel
        if self.y_vel < 10:
            self.y_vel += GRAVITY
            self.rotate()
        self.rect.x = self.x_pos
        self.rect.y = self.y_pos

    def update_score(self):
        self.score += 1

    def kill_flappy(self):
        self.alive = False

    def update(self):
        self.fall()

    def rotate(self):
        angle = 180/math.pi*math.atan(-self.y_vel/3)
        self.image = pygame.transform.rotate(self.original_image, angle)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
