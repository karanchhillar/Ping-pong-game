from turtle import Turtle,Screen
import time


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed(1)
        self.xmove = 10
        self.ymove = 10
        self.x_direction = +1
        self.y_direction = +1


    def move(self):
        new_x = self.xcor() + self.x_direction*self.xmove
        new_y = self.ycor() + self.y_direction*self.ymove
        self.goto(new_x,new_y)
            
    def bounce_y(self):
        self.y_direction *= -1
    
    def bounce_x(self):
        self.x_direction *= -1
        

    def stop(self):
        self.goto(0,0)
        self.x_direction *= -1
        self.xmove = 10
        self.ymove = 10
        
    def increase_speed(self):
        self.xmove += 2
        self.ymove += 2
        print(self.xmove , self.ymove)
        
        
