import re
import datetime
import Constants

def first_column(string):
    return int(string[0:string.find(",")])

class ScoreHandler:
    def __init__(self):
        self.scores_file_name = "res/highscores.txt"

    def add_score(self,new_score):
        scores_file = open(self.scores_file_name, "a")
        scores_file.write("%d" % new_score)
        date = datetime.datetime.now()
        scores_file.write(date.strftime(", %Y-%m-%d %H:%M:%S")+"\n")
        scores_file.close()

    def view_highscores(self, number_of_scores = 10):
        scores_file = open(self.scores_file_name, "r")
        scores = scores_file.readlines()
        latest = scores[-1]
        scores.sort(key = first_column, reverse = True)
        latest_pos = scores.index(latest) + 1
        if scores == []:
            return ""
        output_string = "    SCORE        DATE\n"
        for i in range(min(len(scores),number_of_scores)):
            output_string += \
                    " %d:" % (i + 1) + " "*(7-len(str(first_column(scores[i]))+str(i+1))) + \
                    scores[i].replace("\n","").replace(",","       ") + "\n"
        latest = \
                " %d:" % latest_pos + " "*(7-len(str(first_column(latest))+str(latest_pos))) + \
                latest.replace("\n","").replace(",","       ")
        return output_string, latest, latest_pos

    def blit_highscores(self, surface,x,y,a_font):
        scores_file = open(self.scores_file_name, "r")
        scores = scores_file.readlines()
        latest = scores[-1].replace("\n","  *").replace(",","       ")

        text, latest, latest_pos = self.view_highscores()
        lines = re.findall(".*",text)
        for i in range(0,len(lines)):
            y += 20
            if i == (2*latest_pos):
                surface.blit(a_font.render(lines[i], False, [240,0,160]), (x,y))
            else:
                surface.blit(a_font.render(lines[i], False, Constants.WHITE), (x,y))
        surface.blit(a_font.render(latest, False, [240,0,160]), (x,y))
