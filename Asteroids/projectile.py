from math import *
import numpy as np

class Projectile:
    def __init__(self,pos,angle):
        self.vel = np.array([cos(angle),sin(angle)])*7
        self.pos = pos
        self.health = 100
    def update_pos(self):
        self.pos = self.pos + self.vel
        self.health -= 1
    def draw(self):
        (x1,y1)=self.pos - self.vel*0.7
        (x2,y2)=self.pos
        return ((x1,y1),(x2,y2))
    def hit(self,asteroid):
        if sqrt((self.pos[0]-asteroid.pos[0])**2+(self.pos[1]-asteroid.pos[1])**2) < asteroid.size:
            asteroid.hit()
            self.health = 0
            return True
        return False
