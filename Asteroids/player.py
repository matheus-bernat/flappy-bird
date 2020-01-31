#import physics
from math import *
import numpy as np
import projectile
class Player:
    def __init__(self,startpos=[0,0],color=[13,240,60],size=(18,10)):
        self.pos = np.array(startpos)
        self.color = color
        self.acc = np.array([0,0])
        self.vel = np.array([0,0])
        self.size = size
        self.bost = 0
        self.orientation = 0
        self.angle_vel = 0
        self.shots = []
        self.health = 10
    def update_pos(self):
        self.orientation += self.angle_vel
        a  = self.orientation
        self.acc = np.array([cos(a),sin(a)])*self.bost
        self.vel = self.vel + self.acc
        self.bost = 0
        self.pos = self.pos + self.vel
        self.vel = self.vel*0.95
    def draw(self):
        pos =self.pos
        length =self.size[0]
        width =self.size[1]
        orientation = self.orientation
        (x1,y1)=(pos[0]-width*sin(orientation+.3),pos[1]+width*cos(orientation+.3))
        (x2,y2)=(pos[0]+length*cos(orientation),pos[1]+length*sin(orientation))
        (x3,y3)=(pos[0]+width*sin(orientation-.3),pos[1]-width*cos(orientation-.3))
        (x4,y4)=(pos[0],pos[1])
        return ((x1,y1),(x2,y2),(x3,y3),(x4,y4))
    def shoot(self):
        self.shots = self.shots + [projectile.Projectile(self.pos+10*np.array([cos(self.orientation),sin(self.orientation)]),self.orientation)]
    def hit(self,asteroid):
        pos =self.pos
        length =self.size[0]
        width =self.size[1]
        orientation = self.orientation
        (x1,y1)=(pos[0]-width*sin(orientation+.3),pos[1]+width*cos(orientation+.3))
        (x2,y2)=(pos[0]+length*cos(orientation),pos[1]+length*sin(orientation))
        (x3,y3)=(pos[0]+width*sin(orientation-.3),pos[1]-width*cos(orientation-.3))
        if sqrt((x1-asteroid.pos[0])**2+(y1-asteroid.pos[1])**2) < asteroid.size \
            or sqrt((x2-asteroid.pos[0])**2+(y2-asteroid.pos[1])**2) < asteroid.size \
            or sqrt((x3-asteroid.pos[0])**2+(y3-asteroid.pos[1])**2) < asteroid.size:
            self.health -= 1
