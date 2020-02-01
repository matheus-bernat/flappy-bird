import pygame
GRAVITY = .01

class Bird:
    def __init__(self, x_pos, y_pos, y_vel, alive, width, height, score):
        self.bird_width = width
        self.bird_height = height
        self.alive = True
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.y_vel = y_vel
        self.score = score

    def flap(self):
        self.y_vel = -2

    def fall(self):
        self.y_pos += self.y_vel
        if self.y_vel < 2:
            self.y_vel += GRAVITY

    def update_score(self):
        self.score += 1

    def kill_flappy(self):
        self.alive = False

    def update(self):
        self.fall()
