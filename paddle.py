from turtle import Turtle

STARTING_POSITION = [(350, 0)]
UP = 90
DOWN = 270

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.create_paddle()



    def create_paddle(self):
        for position in STARTING_POSITION:
            self.shape("square")
            self.shapesize(stretch_len=10)
            self.penup()
            self.color("white")
            self.goto(position)



    def up(self):
        self.setheading(UP)


    def down(self):
        self.setheading(DOWN)