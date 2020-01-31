import pygame

def playercontrols(player):
    key=pygame.key.get_pressed()  #checking pressed keys
    if key[pygame.K_LEFT]:
        if -.18 < player.angle_vel: player.angle_vel-=.04
    if key[pygame.K_RIGHT]:
        if player.angle_vel < .18: player.angle_vel+=.04
    if key[pygame.K_UP]:player.bost=1.1
    if key[pygame.K_s]:
        player.shoot()
    if abs(player.angle_vel)<0.95:
        player.angle_vel *= 0.85+(3*player.angle_vel)**6
    else:
        player.angle_vel *= 0.95
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: player.shoot()
    return None

