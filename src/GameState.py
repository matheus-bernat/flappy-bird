from Bird import *
from Obstacle import *
import pygame

INIT_BIRD_X_POS = 50
INIT_BIRD_Y_POS = 50
BIRD_WIDTH = 50
BIRD_HEIGHT = 50
OBSTACLE_WIDTH = 50
OBSTACLE_GAP = 200

class GameState:
    def __init__(self, game_window):
        self.flappy_bird = Bird(INIT_BIRD_X_POS, INIT_BIRD_Y_POS, 0, True, BIRD_WIDTH, BIRD_HEIGHT, 0)
        self.obstacles_list = []
        self.spawn_obstacles()
        self.game_window = game_window
        self.running = True
        self.sprites_group = []

    def draw(self):
        self.game_window.fill(0) # clean screen
        pygame.draw.rect(self.game_window, Constants.RED, self.flappy_bird.shape)
        for obstacle in self.obstacles_list:
            pygame.draw.rect(self.game_window, Constants.BLUE, obstacle.shape[0])
            pygame.draw.rect(self.game_window, Constants.BLUE, obstacle.shape[1])

    def spawn_obstacles(self):
        obstacle_x_pos = 800
        for i in range(0, 6):
            self.obstacles_list.append(Obstacle(obstacle_x_pos, OBSTACLE_WIDTH, OBSTACLE_GAP, 3))
            obstacle_x_pos += 250

    def update(self):
        for obstacle in self.obstacles_list:
            obstacle.move()
            if obstacle.is_out_of_screen():
                obstacle.respawn(1200)

        self.flappy_bird.update()
        self.input_handler()
        self.check_collisions()
        if not self.flappy_bird.alive:
            self.running = False
        self.draw()

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
        if (self.flappy_bird.shape.y + self.flappy_bird.bird_height > Constants.WINDOW_HEIGHT) or (self.flappy_bird.shape.y < 0):
            self.flappy_bird.kill_flappy()

        # Bird with obstacles
        """for obstacle in self.obstacles_list:
            if pygame.sprite.spritecollide(sprite, group, False):
                self.flappy_bird.kill_flappy()"""

        for obstacle in self.obstacles_list:
            if obstacle.shape[0].colliderect(self.flappy_bird.shape) or \
               obstacle.shape[1].colliderect(self.flappy_bird.shape):
                self.flappy_bird.kill_flappy()

    def has_collided(self, object1, object2):
        # if collision:
        return True
        return False
