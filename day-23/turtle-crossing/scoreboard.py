from turtle import Turtle

MAIN_FONT = ("Courier", 20, "normal")
GO_FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update()

    def level_up(self):
        self.level += 1
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level: {self.level}", move=False, align='left', font=MAIN_FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align='center', font=GO_FONT)
