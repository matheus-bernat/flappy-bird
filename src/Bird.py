import pygame
GRAVITY = .1

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
        self.y_vel = -3

    def fall(self):
        self.y_pos += self.y_vel
        if self.y_vel < 2:
            self.y_vel += .1

    def update_score(self):
        self.score += 1

    def kill_flappy(self):
        self.alive = False

    def input_handler(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.flap()

    def update(self):
        self.input_handler()
        self.fall()
