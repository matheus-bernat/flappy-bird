from ScoreHandler import ScoreHandler
import Constants
import pygame

class MenuState:
    def __init__(self, window):
        self.window = window
        self.score_handler = ScoreHandler()
        self.name = "menu"
        self.curr_st_str = "menu"
        self.curser_pos = 0
        pygame.font.init()
        self.flappy_font = pygame.font.Font('../res/04B_19__.TTF', 35)

    def input_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.curser_pos = (self.curser_pos + 1) % 3
                if event.key == pygame.K_UP:
                    self.curser_pos = (self.curser_pos - 1) % 3
                if event.key == pygame.K_RETURN:
                    if self.curser_pos == 0:
                        self.curr_st_str = "game"
                    if self.curser_pos == 1:
                        self.curr_st_str = "score"
                    if self.curser_pos == 2:
                        pygame.quit()

    def draw(self):
        background_surface = pygame.transform.scale((pygame.image.load('../res/background.png')), (Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT))
        self.window.blit(background_surface, (0, 0))
        x_pos = Constants.WINDOW_WIDTH/2 - 30
        y_pos = Constants.WINDOW_HEIGHT/2
        text_surface = self.flappy_font.render(' PLAY', False, Constants.WHITE)
        self.window.blit(text_surface, (x_pos, y_pos))
        text_surface = self.flappy_font.render(' HIGHSCORES', False, Constants.WHITE)
        self.window.blit(text_surface,(x_pos, y_pos + 50))
        text_surface = self.flappy_font.render(' EXIT', False, Constants.WHITE)
        self.window.blit(text_surface,(x_pos, y_pos + 100))
        text_surface = self.flappy_font.render('*', False, Constants.WHITE)
        self.window.blit(text_surface, (x_pos - 20, y_pos + self.curser_pos*50))

    def update(self):
        self.draw()
        self.input_handler()
