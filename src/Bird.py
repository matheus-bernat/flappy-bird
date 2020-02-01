import pygame

GRAVITY = 10

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
        self.y_vel = -10

    def fall(self):
        if self.y_pos < 550:
            self.y_vel += 1
            self.y_pos += self.y_vel

    def update_score(self):
        self.score += 1

    def kill_flappy(self):
        self.alive = False

    def update(self):
        self.fall()
        event = pygame.event.poll()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.flap()
                print("hi")
