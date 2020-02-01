from random import randrange

class Obstacle:
    def __init__(self, x_pos, width, gap, speed):
        self.x_pos = x_pos
        #self.y_pos = randrange(0,screen_height)
        self.width = width
        self.gap = gap
        self.speed = speed
        #self.sprite = sprite

    def move(self):
        self.x_pos -= self.speed

    def is_out_of_screen(self):
        return self.x_pos + self.width < 0
