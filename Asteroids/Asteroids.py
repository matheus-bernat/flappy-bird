from math import *
import numpy as np
import random as rnd

def rotate(array,angle):
    array=np.dot(np.matrix([[cos(angle),-sin(angle)],[sin(angle),cos(angle)]]),array)
    return array
class Asteroid:
    def __init__(self,pos,angle,size=20):
        self.size = size
        self.pos = pos
        self.vel = np.array([cos(angle),sin(angle)])
        self.health = 1
        self.edges = []
        for angle in range(10):
            r = 15*rnd.random()
            self.edges = self.edges + [(int(r*cos(angle)),int(r*sin(angle)))]
        self.edges = np.array(self.edges)
    def update_pos(self):
        self.pos = self.pos + self.vel
    def draw(self):
        return ((int(self.pos[0]),int(self.pos[1])),self.size)
#    def draw(self):
#        return np.array(points)
    def hitbox(self):
        return ((int(self.pos[0]),int(self.pos[1])),size)
    def hitbox(self):
        return self.edges
    def hit(self):
        self.health = 0
