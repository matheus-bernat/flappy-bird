from Bird import *
from Obstacle import *
import pygame

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

    def draw(self):
        pygame.draw.circle(self.game_window, 255, [self.flappy_bird.x_pos, self.flappy_bird.y_pos], 5)


    def spawn_obstacle(self):
        for i in range(0, 5):
            obstacle_x_pos = 100
            self.obstacles_list.append(Obstacle(obstacle_x_pos, OBSTACLE_WIDTH, OBSTACLE_GAP, 3))
            obstacle_x_pos += 50

    def update(self):
        """
        Move obstacles, move bird downwards, redraw screen,
        """
        """for obstacle in self.obstacles_list:
            obstacle.move()
            if obstacle.is_out_of_screen():
                obstacle.x_pos += 250

        self.flappy_bird.fall()"""
        self.draw()
