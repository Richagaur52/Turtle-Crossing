from turtle import Turtle
starting_position=(0,-280)
move_distance=10
first_line_y=280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(starting_position)
        self.setheading(90)

    def go_up(self):
        self.forward(move_distance)
    def go_left(self):
        pass
    def go_right(self):
        pass

    def go_to_start(self):
        self.goto(starting_position)

    def is_complete(self):
        if self.ycor()>first_line_y:
            return True
        else:
            return False
