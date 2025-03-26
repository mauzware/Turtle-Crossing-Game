from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.penup()
        self.color("black")
        self.update_score()

    def update_score(self): #just a scoreboard updating
        self.clear()
        self.goto(-280, 260)
        self.write(f"Level {self.score}", align="left", font=FONT)

    def level_increase(self): #score increase
        self.score += 1
        self.update_score()

    def game_over(self): #game over
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER", align="center", font=FONT)

