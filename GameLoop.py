import Game_State

class GameLoop:
    def __init__(self):
        pygame.init()
        width  = 400
        height = 400
        window = pygame.display.set_mode((width,height))
        game_state = Game_State(window)
    def update():
        game_state.update()

def main():
    game = GameLoop(something)
    while True:
        game.update()

if __name__ = "__main__":
    main()
