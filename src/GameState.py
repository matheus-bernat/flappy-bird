from Bird import *
from Obstacle import *
import pygame
import Constants

INIT_BIRD_X_POS = 50
INIT_BIRD_Y_POS = 50
INIT_BIRD_ALIVE = True
BIRD_WIDTH = 5
BIRD_HEIGHT = 5
BIRD_ACCEL = 5
OBSTACLE_WIDTH = 50
OBSTACLE_GAP = 100

class GameState:
    def __init__(self, game_window):
        self.flappy_bird = Bird(50, 50, 0, True, BIRD_WIDTH, BIRD_HEIGHT, 0)
        self.obstacles_list = []
        self.spawn_obstacle()
        self.game_window = game_window
        self.running = True

    def draw(self):
        self.game_window.fill(0) # clean screen
        pygame.draw.circle(self.game_window, Constants.RED, [self.flappy_bird.x_pos, round(self.flappy_bird.y_pos)], 15)
        for obstacle in self.obstacles_list:
            pygame.draw.circle(self.game_window, Constants.BLUE, [obstacle.x_pos, 100], 30)

    def spawn_obstacle(self):
        for i in range(0, 5):
            obstacle_x_pos = 800
            self.obstacles_list.append(Obstacle(obstacle_x_pos, OBSTACLE_WIDTH, OBSTACLE_GAP, 3))
            obstacle_x_pos += 50

    def update(self):
        """
        Move obstacles, move bird downwards, redraw screen,
        """
        for obstacle in self.obstacles_list:
            obstacle.move()
            if obstacle.is_out_of_screen():
                obstacle.x_pos += 800
        self.flappy_bird.update()
        self.draw()
        self.input_handler()

    def input_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.flappy_bird.flap()
                if event.key == pygame.K_ESCAPE:
                    self.running = False
            if event.type == pygame.QUIT:
                self.running = False
