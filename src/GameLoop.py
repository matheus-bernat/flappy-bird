import pygame
from GameState import GameState
import Constants

class GameLoop:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT))
        self.game_state = GameState(self.window)

    def update(self):
        self.game_state.update()

def main():
    game = GameLoop()
    while game.game_state.running:
        game.update()
        pygame.display.flip()

if __name__ == "__main__":
    main()
