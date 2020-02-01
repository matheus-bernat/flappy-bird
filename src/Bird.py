import pygame
import Constants

GRAVITY = .3

class Bird(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, y_vel, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.bird_width = width
        self.bird_height = height
        self.y_vel = y_vel
        self.alive = True
        self.score = 0
        #self.shape = pygame.Rect(self.x_pos, 300, self.bird_width, self.bird_height)
        self.image = pygame.transform.scale(pygame.image.load('../res/bird.png'), (48, 36))
        #self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect() # Get the dimensions of the sprite
        self.rect.x = x_pos
        self.rect.y = y_pos

    def flap(self):
        self.y_vel = -8

    def fall(self):
        #self.shape = self.shape.move(0, self.y_vel)
        self.rect.y += self.y_vel
        if self.y_vel < 10:
            self.y_vel += GRAVITY

    def update_score(self):
        self.score += 1

    def kill_flappy(self):
        self.alive = False

    def update(self):
        self.fall()
