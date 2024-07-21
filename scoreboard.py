from turtle import Turtle
font=("courier",24,"normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=1
        self.hideturtle()
        self.penup()
        self.goto(-280,250)
        self.update()

    def update(self):
        self.write(f"Level={self.score}",font=font)

    def increase_level(self):
        self.clear()
        self.score+=1
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write("Game_over",font=font)










