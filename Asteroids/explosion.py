from math import *
import numpy as np
import random

class Explosion:
    def __init__(self):
        h = 0
    def draw(self,pos):
        points = []
        for angle in range(15):
            r = random.gauss(0,5)**2
            points = points + [(int(pos[0]+r*cos(angle)),int(pos[1]+r*sin(angle)))]
        return np.array(points)
