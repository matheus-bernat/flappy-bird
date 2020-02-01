import re
import datetime

def first_column(string):
    i = 0
    while string[i] != ",":
        i += 1
    return int(string[0:i])

class ScoreHandler:
    def __init__(self):
        self.scores_file_name = "../res/highscores.txt"

    def add_score(self,new_score):
        scores_file = open(self.scores_file_name, "a")
        scores_file.write("%d" % new_score)
        date = datetime.datetime.now()
        scores_file.write(date.strftime(", %Y-%m-%d %H:%M:%S")+"\n")
        scores_file.close()

    def view_highscores(self, number_of_scores = 10):
        scores_file = open(self.scores_file_name, "r")
        scores = scores_file.readlines()
        scores.sort(key = first_column, reverse = True)
        if scores == []:
            return ""
        output_string = \
                "*"*40+"\n" \
                "     SCORE        DATE\n"
        for i in range(min(len(scores),number_of_scores)):
            output_string += \
                    " %d:" % (i + 1) + " "*(7-len(str(first_column(scores[i]))+str(i+1))) + \
                    scores[i].replace("\n","  *").replace(",","       ") + "\n"
        output_string  += "\n" + "*"*40+"\n"
        return output_string

    def blit_highscores(self, surface,x,y,a_font):
        text = self.view_highscores()
        lines = re.findall(".*",text)
        for i in range(0,len(lines)):
            y += 20
            surface.blit(a_font.render(lines[i], False, [143,240,160]), (x,y))




