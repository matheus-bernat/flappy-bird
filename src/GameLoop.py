import pygame
from StateHandler import StateHandler
import Constants

class GameLoop:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT))
        #self.game_state = GameState(self.window)
        pygame.mixer.music.load('../res/crazy-frog.ogg')
        pygame.mixer.music.play(-1)
        self.state_handler = StateHandler(self.window)

    def update(self):
        self.state_handler.update()

def main():
    game = GameLoop()
    clock = pygame.time.Clock()
    iterator = 0
    while game.state_handler.running:
        clock.tick(600)
        game.update()
        iterator = (iterator + 1) % 6
        if iterator == 0:
            pygame.display.flip() # refresh screen
        #pygame.display.update(game.state_handler.game_state.dirtyrects2)
        #pygame.display.update(game.state_handler.game_state.dirtyrects1)
    pygame.mixer.quit()

if __name__ == "__main__":
    main()
