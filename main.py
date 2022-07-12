from turtle import Turtle,Screen
import time
from paddle import Paddle
from ball import Ball
from score import Score



screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)


l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))
print(l_paddle.pos())

screen.listen()
screen.onkey(fun= r_paddle.go_up,key="Up")
screen.onkey(fun=r_paddle.go_down,key="Down")
screen.onkey(fun= l_paddle.go_up,key="w")
screen.onkey(fun=l_paddle.go_down,key="s")

ball = Ball()
score = Score()



game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    # collision with the upper surface
    if ball.ycor() > 280 or ball.ycor() < - 280:
        ball.bounce_y()

    # collision with the paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330:
        ball.increase_speed()
        ball.bounce_x()
    elif ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.increase_speed()
        ball.bounce_x()


    # collision with the right side wall
    if ball.xcor() > 380:
        ball.stop()
        score.left_score()
        
    # collision with the left side wall
    if ball.xcor() < -380:
        ball.stop()
        score.right_score()

   
screen.exitonclick()