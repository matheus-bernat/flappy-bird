from GameState import GameState
from ScoreState import ScoreState
from MenuState import MenuState

class StateHandler:
    def __init__(self,window):
        self.window = window
        self.menu_state = MenuState(self.window)
        self.game_state = GameState(self.window)
        self.score_state = ScoreState(self.window)
        self.current_state = self.menu_state
        self.running = True

    def update(self):
        self.current_state.update()
        if self.current_state.curr_st_str == "menu":
            self.current_state.curr_st_str = self.current_state.name
            self.current_state = self.menu_state
        elif self.current_state.curr_st_str == "game":
            self.current_state.curr_st_str = self.current_state.name
            self.current_state = self.game_state
        elif self.current_state.curr_st_str == "score":
            self.current_state.curr_st_str = self.current_state.name
            self.current_state = self.score_state
