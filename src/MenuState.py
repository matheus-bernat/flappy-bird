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
        self.a_font = pygame.font.SysFont('Comic Sans MS', 30)

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
        self.window.fill(0)
        x_pos = Constants.WINDOW_WIDTH/2 - 200
        y_pos = Constants.WINDOW_HEIGHT/2 - 200
        textsurface = self.a_font.render('PLAY', False, [143,240,160])
        self.window.blit(textsurface,(x_pos, y_pos))
        textsurface = self.a_font.render('HIGHSCORES', False, [143,240,160])
        self.window.blit(textsurface,(x_pos,y_pos+100))
        textsurface = self.a_font.render('EXIT', False, [143,240,160])
        self.window.blit(textsurface,(x_pos,y_pos+200))
        textsurface = self.a_font.render('*', False, [143,240,160])
        self.window.blit(textsurface,(x_pos-10,y_pos+self.curser_pos*100))

    def update(self):
        self.draw()
        self.input_handler()

