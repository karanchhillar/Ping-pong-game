from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.speed(0)
        self.penup()
        self.color("white")
        self.setheading(90)
        self.goto(position)
        self.shapesize(stretch_len=5,stretch_wid=1)

    def go_up(self):
        self.fd(20)
    
    def go_down(self):
        self.back(20)
