from Bird import *
from Obstacle import *
from ScoreHandler import ScoreHandler
import pygame
import Constants
import os
from random import randrange

INIT_BIRD_X_POS = 50
INIT_BIRD_Y_POS = 50
BIRD_WIDTH = 50
BIRD_HEIGHT = 50
OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = 500
OBSTACLE_GAP = 200
OBSTACLE_SPACING = 250
OBSTACLE_SPEED = 3

IMG_OBSTACLE_BOTTOM = '../res/obstacle_bottom.png'
IMG_OBSTACLE_TOP = '../res/obstacle_top.png'

class GameState:
    def __init__(self, game_window):
        self.game_window = game_window
        self.sprites_group = pygame.sprite.Group()
        self.flappy_bird = Bird(INIT_BIRD_X_POS, INIT_BIRD_Y_POS, 0, BIRD_WIDTH, BIRD_HEIGHT)
        self.obstacles_list = []
        self.spawn_obstacles()
        self.add_sprites_to_group()
        pygame.font.init()
        self.running = True
        self.a_font = pygame.font.SysFont('Courier', 30)
        self.score_handler = ScoreHandler()
        self.curr_st_str = "game"
        self.name = "game"

    def draw(self):
        self.game_window.fill(0) # clear screen
        text_surface = self.a_font.render('SCORE %d' % self.flappy_bird.score, False, [143,240,160])
        self.game_window.blit(text_surface, (0, 0))

        self.sprites_group.draw(self.game_window) # draw all sprites on the game window

    def add_sprites_to_group(self):
        self.sprites_group.add(self.flappy_bird)
        for obstacle in self.obstacles_list:
            self.sprites_group.add(obstacle)

    def update(self):
        i = 0
        for obstacle in self.obstacles_list:
            obstacle.move()
            if obstacle.is_out_of_screen():
                new_y = randrange(-400, -200)
                if i % 2 == 0:
                    obstacle.respawn((OBSTACLE_SPACING * 6), new_y)
                else:
                    obstacle.respawn((OBSTACLE_SPACING * 6), new_y + OBSTACLE_GAP + OBSTACLE_HEIGHT)
                i += 1

        self.flappy_bird.update()
        self.input_handler()
        self.check_collisions()
        if not self.flappy_bird.alive:
            self.running = False
            self.reset()
        self.draw()
        self.give_points()

    def check_collisions(self):
        # Bird with walls
        if (self.flappy_bird.rect.y + self.flappy_bird.rect.size[1]  > Constants.WINDOW_HEIGHT) or (self.flappy_bird.rect.y < 0):
            self.flappy_bird.kill_flappy()
            self.score_handler.add_score(self.flappy_bird.score)
            self.curr_st_str = "score"

        # Bird with obstacles
        """hit_sprite = pygame.sprite.spritecollisionany(self.flappy_bird, self.sprite_group)
        if (not hit_sprite == None):
            self.flappy_bird.kill_flappy()
            """

    def has_collided(self, sprite1, sprite2):
        return pygame.sprite.collide_mask(sprite1, sprite2)

    def spawn_obstacles(self):
        obstacle_x_pos = Constants.WINDOW_WIDTH
        for i in range(0, 12):
            if i % 2 == 0:
                obstacle_y_pos = randrange(-400, -200)
                obstacle = Obstacle(obstacle_x_pos, obstacle_y_pos, OBSTACLE_SPEED, IMG_OBSTACLE_TOP)
                self.obstacles_list.append(obstacle)
                print("(obstacle_x, obstacle_y): " + str(obstacle.rect.x) + ", " + str(obstacle.rect.y))
            else:
                obstacle = Obstacle(obstacle_x_pos, obstacle_y_pos + OBSTACLE_HEIGHT + OBSTACLE_GAP, OBSTACLE_SPEED, IMG_OBSTACLE_BOTTOM)
                self.obstacles_list.append(obstacle)
                print("(obstacle_x, obstacle_y): " + str(obstacle.rect.x) + ", " + str(obstacle.rect.y))
                obstacle_x_pos += OBSTACLE_SPACING

    def give_points(self):
        """for obstacle in self.obstacles_list:
            if obstacle.shape[0].x + obstacle.width - self.flappy_bird.x_pos < 0 and \
                obstacle.shape[0].x + obstacle.width - self.flappy_bird.x_pos >= -OBSTACLE_SPEED:
                self.flappy_bird.score += 1"""

    def input_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.flappy_bird.flap()
                if event.key == pygame.K_ESCAPE:
                    self.running = False
            if event.type == pygame.QUIT:
                self.running = False
                self.flappy_bird.score += 1

    def reset(self):
        self.obstacles_list = []
        self.spawn_obstacles()
        self.flappy_bird.x_pos = 50
        self.flappy_bird.y_pos = 50
        self.flappy_bird.x_vel = 0
        self.flappy_bird.y_vel = 0
        self.flappy_bird.score = 0
        self.flappy_bird.alive = True
