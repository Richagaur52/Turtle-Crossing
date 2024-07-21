from turtle import Turtle
import random
color=["red","orange","purple","yellow","blue","pink"]
starting_move_dis=5
move_increment=10

class CarManager:
    def __init__(self):
        self.all_cars=[]
        self.car_speed=starting_move_dis

    def create_cars(self):
        random_chance=random.randint(1,6)
        if random_chance==1:
            new_car=Turtle("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(color))
            random_y=random.randint(-250,+250)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def car_speed_increase(self):
        self.car_speed+=move_increment


