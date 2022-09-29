from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 15, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        with open('high_score.txt') as file:
            self.high_score = int(file.read())
        self.display()

    def display(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.display()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open('high_score.txt', 'w') as file:
            file.write(f"{self.high_score}")
        self.score = 0
        self.display()
