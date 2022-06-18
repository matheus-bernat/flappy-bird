import pygame
import Constants
from ScoreHandler import ScoreHandler

class ScoreState:
    def __init__(self, window):
        self.window = window
        self.score_handler = ScoreHandler()
        self.name = "score"
        self.curr_st_str = "score"
        self.curser_pos = 0
        pygame.font.init()
        self.flappy_font = pygame.font.Font('res/04B_19__.TTF', 20)
        self.mono_font = pygame.font.SysFont('Courier', 30)
        self.background_surface = pygame.transform.scale((pygame.image.load('res/background.png')), (Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT))
        self.scoreboard_surface = pygame.Surface((715,500))
        self.scoreboard_surface.set_alpha(225)
        self.scoreboard_surface.fill(0)

    def input_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.curser_pos = (self.curser_pos + 1) % 2
                if event.key == pygame.K_UP:
                    self.curser_pos = (self.curser_pos - 1) % 2
                if event.key == pygame.K_RETURN:
                    if self.curser_pos == 0:
                        self.curr_st_str = "menu"
                    if self.curser_pos == 1:
                        pygame.quit()

    def draw(self):
        self.window.blit(self.background_surface, (0, 0))
        self.window.blit(self.scoreboard_surface, (Constants.WINDOW_WIDTH/2-320,20))
        #pygame.draw.rect(self.window,(0,0,0),(Constants.WINDOW_WIDTH/2-320,20,715,500))
        self.score_handler.blit_highscores(self.window,Constants.WINDOW_WIDTH/2-300,20,self.mono_font)
        x_pos = 50
        y_pos = Constants.WINDOW_HEIGHT - 120
        textsurface = self.flappy_font.render('MENU', False, Constants.WHITE)
        self.window.blit(textsurface,(x_pos, y_pos))
        textsurface = self.flappy_font.render('EXIT', False, Constants.WHITE)
        self.window.blit(textsurface,(x_pos,y_pos+50))
        textsurface = self.flappy_font.render('*', False, Constants.WHITE)
        self.window.blit(textsurface,(x_pos-20,y_pos+self.curser_pos*50))

    def update(self):
        self.draw()
        self.input_handler()
