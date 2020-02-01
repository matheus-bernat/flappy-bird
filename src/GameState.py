from Bird import *
from Obstacle import *
import pygame
import Constants

INIT_BIRD_X_POS = 50
INIT_BIRD_Y_POS = 50
BIRD_WIDTH = 5
BIRD_HEIGHT = 5
BIRD_ACCEL = 5
OBSTACLE_WIDTH = 50
OBSTACLE_GAP = 200
OBSTACLE_SPACING = 250
OBSTACLE_SPEED = 3


class GameState:
    def __init__(self, game_window):
        self.flappy_bird = Bird(INIT_BIRD_X_POS, INIT_BIRD_Y_POS, 0, True, BIRD_WIDTH, BIRD_HEIGHT, 0)
        self.obstacles_list = []
        self.spawn_obstacles()
        self.game_window = game_window
        self.running = True
        self.sprites_group = []
        pygame.font.init()
        self.a_font = pygame.font.SysFont('Comic Sans MS', 30)

    def draw(self):
        self.game_window.fill(0) # clean screen
        pygame.draw.circle(self.game_window, Constants.RED, [self.flappy_bird.x_pos, round(self.flappy_bird.y_pos)], 15)
        for obstacle in self.obstacles_list:
            pygame.draw.rect(self.game_window, Constants.BLUE, obstacle.shape[0])
            pygame.draw.rect(self.game_window, Constants.BLUE, obstacle.shape[1])
        textsurface = self.a_font.render('SCORE %d' % self.flappy_bird.score, False, [143,240,160])
        self.game_window.blit(textsurface,(0,0))



    def spawn_obstacles(self):
        obstacle_x_pos = Constants.WINDOW_WIDTH
        for i in range(0, 6):
            self.obstacles_list.append(Obstacle(obstacle_x_pos, OBSTACLE_WIDTH, OBSTACLE_GAP, OBSTACLE_SPEED))
            obstacle_x_pos += OBSTACLE_SPACING

    def update(self):
        for obstacle in self.obstacles_list:
            obstacle.move()
            if obstacle.is_out_of_screen():
                obstacle.respawn(OBSTACLE_SPACING*6)

        self.flappy_bird.update()
        self.input_handler()
        self.check_collisions()
        if not self.flappy_bird.alive:
            self.running = False
        self.draw()
        self.give_points()

    def input_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.flappy_bird.flap()
                if event.key == pygame.K_ESCAPE:
                    self.running = False
            if event.type == pygame.QUIT:
                self.running = False

    def check_collisions(self):
        # Bird with walls
        if (self.flappy_bird.y_pos+15 > Constants.WINDOW_HEIGHT) or (self.flappy_bird.y_pos-15 < self.flappy_bird.bird_height):
            self.flappy_bird.kill_flappy()

        # Bird with obstacles
        """for obstacle in self.obstacles_list:
            if pygame.sprite.spritecollide(sprite, group, False, collided = has_collided):
                self.flappy_bird.kill_flappy()"""

    def has_collided(self, object1, object2):
        # if collision:
        return True
        return False
    def give_points(self):
        for obstacle in self.obstacles_list:
            if obstacle.shape[0].x + obstacle.width - self.flappy_bird.x_pos < 0 and \
                obstacle.shape[0].x + obstacle.width - self.flappy_bird.x_pos >= -OBSTACLE_SPEED:
                self.flappy_bird.score += 1
