from Bird import *
from Obstacle import *
from ScoreHandler import ScoreHandler
from ScrollingBackground import ScrollingBackground
from ScrollingBody import ScrollingBody
from random import randrange
import pygame
import Constants
import math

INIT_BIRD_X_POS = 50
INIT_BIRD_Y_POS = 50
BIRD_WIDTH = 50
BIRD_HEIGHT = 50
OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = 500
OBSTACLE_GAP = 200
OBSTACLE_SPACING = OBSTACLE_GAP + OBSTACLE_WIDTH
OBSTACLE_SPEED = 3

SCROLLING_BACKGROUND = False

IMG_OBSTACLE_BOTTOM = '../res/obstacle_bottom.png'
IMG_OBSTACLE_TOP = '../res/obstacle_top.png'

class GameState:
    def __init__(self, game_window):
        self.game_window = game_window
        self.obstacles_sprite_group = pygame.sprite.Group()
        self.flappy_sprite_group = pygame.sprite.Group()
        self.flappy_bird = Bird(INIT_BIRD_X_POS, INIT_BIRD_Y_POS, 0, BIRD_WIDTH, BIRD_HEIGHT)
        self.obstacles_list = []
        self.spawn_obstacles()
        self.backgrounds = []
        self.spawn_backgrounds(False)
        self.background_sprites_group = pygame.sprite.Group()
        self.add_sprites_to_groups()
        pygame.font.init()
        self.running = True
        self.a_font = pygame.font.SysFont('Courier', 30)
        self.flappy_font = pygame.font.Font('../res/04B_19__.TTF', 50)
        self.score_handler = ScoreHandler()
        self.curr_st_str = "game"
        self.name = "game"
        self.stars = []
        self.spawn_stars()

    def draw(self):
<<<<<<< HEAD
        #self.background_sprites_group.draw(self.game_window)
        self.draw_background()
        text_surface = self.flappy_font.render('%d' % self.flappy_bird.score, False, Constants.WHITE)
        self.game_window.blit(text_surface, (Constants.WINDOW_WIDTH/2, Constants.WINDOW_HEIGHT/2))
=======
        if SCROLLING_BACKGROUND:
            self.background_sprites_group.draw(self.game_window)
        else:
            self.draw_background()
            self.draw_stars(self.game_window)
        text_surface = self.a_font.render('SCORE %d' % self.flappy_bird.score, False, [143,240,160])
        self.game_window.blit(text_surface, (0, 0))
>>>>>>> 93289e834c295c10260570fd5e73dce9e04ad63f
        self.flappy_sprite_group.draw(self.game_window)
        self.obstacles_sprite_group.draw(self.game_window)

    def draw_background(self):
        self.game_window.fill(Constants.DAY_BLUE)
        grass = pygame.draw.rect(self.game_window, Constants.GREEN, (0, 500, 1000, 100))

    def add_sprites_to_groups(self):
        self.flappy_sprite_group.add(self.flappy_bird)
        for obstacle in self.obstacles_list:
            self.obstacles_sprite_group.add(obstacle)
        for background in self.backgrounds:
            self.background_sprites_group.add(background)

    def update(self):
        i = 0
        for obstacle in self.obstacles_list:
            obstacle.move()
            if obstacle.is_out_of_screen():
                if i % 2 == 0:
                    new_y = randrange(-450, -250)
                    obstacle.respawn((OBSTACLE_SPACING * 6), new_y)
                else:
                    obstacle.respawn((OBSTACLE_SPACING * 6), new_y + OBSTACLE_GAP + OBSTACLE_HEIGHT)
                i += 1
        self.flappy_bird.update()
        self.update_stars()
        if SCROLLING_BACKGROUND:
            for background in self.backgrounds:
                background.update()
        self.input_handler()
        self.check_collisions()
        self.give_points()
        if not self.flappy_bird.alive:
            self.running = False
            self.reset()
        self.draw()

    def has_collided(self, sprite1, sprite2):
        return pygame.sprite.collide_mask(sprite1, sprite2)

    def check_collisions(self):
        # Bird with walls
        if (self.flappy_bird.rect.y + self.flappy_bird.rect.size[1]  > Constants.WINDOW_HEIGHT) or (self.flappy_bird.rect.y < 0):
            self.end_game()
        # Bird with obstacles
        hit_sprite = pygame.sprite.spritecollideany(self.flappy_bird, self.obstacles_sprite_group, collided=self.has_collided)
        if not (hit_sprite == None): self.end_game()

    def spawn_obstacles(self):
        obstacle_x_pos = Constants.WINDOW_WIDTH
        for i in range(0, 12):
            if i % 2 == 0:
                obstacle_y_pos = randrange(-400, -200)
                obstacle = Obstacle(obstacle_x_pos, obstacle_y_pos, OBSTACLE_SPEED, IMG_OBSTACLE_TOP)
                self.obstacles_list.append(obstacle)
            else:
                obstacle = Obstacle(obstacle_x_pos, obstacle_y_pos + OBSTACLE_HEIGHT + OBSTACLE_GAP, OBSTACLE_SPEED, IMG_OBSTACLE_BOTTOM)
                self.obstacles_list.append(obstacle)
                obstacle_x_pos += OBSTACLE_SPACING

    def spawn_backgrounds(self, scrolling_background):
        if scrolling_background:
            x_pos = 0
            self.backgrounds.append(ScrollingBackground(x_pos, 1, False))
            x_pos += Constants.WINDOW_WIDTH
            self.backgrounds.append(ScrollingBackground(x_pos, 1, True))
            return


    def give_points(self):
        for obstacle in self.obstacles_list:
            if obstacle.rect.x + (obstacle.rect.width/2) - self.flappy_bird.rect.x < 0 and \
                obstacle.rect.x + (obstacle.rect.width/2) - self.flappy_bird.rect.x >= -obstacle.speed:
                self.flappy_bird.score += 0.5
                if self.flappy_bird.score % 10 == 0 and self.flappy_bird.score != 0:
                    for obstacle in self.obstacles_list:
                        obstacle.increase_speed(1)

    def end_game(self):
        self.flappy_bird.kill_flappy()
        self.score_handler.add_score(self.flappy_bird.score)
        self.curr_st_str = "score"

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
        self.flappy_bird.rect.y = INIT_BIRD_Y_POS
        self.flappy_bird.y_pos = INIT_BIRD_Y_POS
        self.flappy_bird.y_vel = 0
        self.flappy_bird.score = 0
        self.flappy_bird.alive = True
        self.running = True
        self.obstacles_list.clear()
        self.spawn_obstacles()
        self.flappy_sprite_group.empty() # remove all sprites from group
        self.obstacles_sprite_group.empty() # remove obstacle-sprites from group
        self.add_sprites_to_groups()

    def update_dirty_rects(self):
        self.dirtyrects1 = self.dirtyrects2
        self.dirtyrects2 = []
        for flappy in self.flappy_sprite_group.sprites():
            self.dirtyrects2.append(flappy.rect)
        for obstacle in self.obstacles_sprite_group.sprites():
            self.dirtyrects2.append(obstacle.rect)

    def spawn_stars(self):
        suns = 18
        for i in range(0,suns):
            self.stars.append(ScrollingBody(100,Constants.SUN_ORANGE,2*i*math.pi/suns+ math.pi/suns))
        for i in range(0,suns):
            self.stars.append(ScrollingBody(100,Constants.GREY,-2*i*math.pi/suns))
        for i in range(0,100):
            self.stars.append(ScrollingBody(2,(255,255,255),randrange(0,1000),True))

    def update_stars(self):
        for star in self.stars:
            star.update()

    def draw_stars(self,window):
        for star in self.stars:
            star.draw(window)
