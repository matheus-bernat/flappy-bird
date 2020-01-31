import pygame, player, Asteroids, controls, explosion
from math import *
import numpy as np
pygame.init()
width = 400
height = 400
screen = pygame.display.set_mode((width,height))
running = True
BLACK = 0, 0, 0
screen.fill(BLACK)
clock = pygame.time.Clock()
player = player.Player(startpos=(300,200))
asteroids = []
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
sound_explosion = pygame.mixer.Sound('erase2.wav')
for i in range(20):
    asteroids = asteroids + [Asteroids.Asteroid(pos=np.array([i*50,50]),angle=i,size=30)]
score = 0
playing = True
k = 0
while playing:
    screen.fill(BLACK)
    expl = explosion.Explosion()
#    asteroids = asteroids + [Asteroids.Asteroid(pos=np.array([50,50]),angle=1,size=30)]
    if len(asteroids) == 0:
        for i in range(20):
            asteroids = asteroids + [Asteroids.Asteroid(pos=np.array([i*50,50]),angle=i,size=30)]

    controls.playercontrols(player)
    player.update_pos()
    for thing in [player]+player.shots+asteroids:
        extra = 5
        if thing.pos[0] > width+extra:
            thing.pos[0] = 0
        if thing.pos[0] < 0-extra:
            thing.pos[0] = width+extra
        if thing.pos[1] > height+extra:
            thing.pos[1] = 0-extra
        if thing.pos[1] < 0-extra:
            thing.pos[1] = height+extra


    for shoot in player.shots:
        for a in asteroids:
            if shoot.hit(a):
                sound_explosion.play()
                for pos in expl.draw(shoot.pos):
                    pygame.draw.circle(screen, player.color, pos, 5,5)
        if shoot.health == 0:
            player.shots.remove(shoot)
        shoot.update_pos()
    for asteroid in asteroids:
        player.hit(asteroid)



    if player.health <= 0:
        print("dead")
        playing = False
    if asteroids == []:
        print("win!")
        playing = False
    for asteroid in asteroids:
        if asteroid.health == 0:
            asteroids.remove(asteroid)
            score += 1
        asteroid.update_pos()

    textsurface = myfont.render('SCORE %d  HEALTH %d' % (score,player.health), False, [143,240,160])
    pygame.draw.lines(screen,player.color,True,player.draw(), 2)

#    for i in explosion.drawexplosion(100,100):
  #      #print(int(i[0]),int(i[1]))
 #       pygame.draw.circle(screen, player.color, (int(i[0]),int(i[1])), 0)

    for shoot in player.shots:
        pygame.draw.line(screen,player.color,shoot.draw()[0],shoot.draw()[1],5)
    for asteroid in asteroids:
        pygame.draw.circle(screen,[13,240,60],asteroid.draw()[0],asteroid.draw()[1],2)
    screen.blit(textsurface,(0,0))
    pygame.display.flip()

    pygame.time.wait(16)
