from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-290, 260)
        self.current_lvl = 0
        self.scoreboard()

    def scoreboard(self):
        self.clear()
        self.write(f"level : {self.current_lvl}", align="left", font=FONT)

    def update_lvl(self):
        self.current_lvl += 1
