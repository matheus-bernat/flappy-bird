import pygame
import Constants

GRAVITY = .3

class Bird:
    def __init__(self, x_pos, y_pos, y_vel, alive, width, height, score):
        self.bird_width = width
        self.bird_height = height
        self.alive = True
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.y_vel = y_vel
        self.score = score
        #self.sprite = sprite
        self.shape = pygame.Rect(self.x_pos, 300, self.bird_width, self.bird_height)

    def flap(self):
        self.y_vel = -8

    def fall(self):
        self.shape = self.shape.move(0, self.y_vel)
        self.y_pos += self.y_vel
        if self.y_vel < 10:
            self.y_vel += GRAVITY

    def update_score(self):
        self.score += 1

    def kill_flappy(self):
        self.alive = False

    def update(self):
        self.fall()
