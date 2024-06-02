from turtle import Screen, Turtle
from paddle import PADDLE
from ball import BALL
from block import BLOCK


screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height=800)
screen.title('Breakout Pong')
screen.tracer(0)

paddle = PADDLE(0, -350)
ball = BALL()
block = BLOCK()
block.create_blocks()

screen.listen()
screen.onkey(paddle.go_left, 'Left')
screen.onkeypress(paddle.go_left, 'Left')
screen.onkey(paddle.go_right, 'Right')
screen.onkeypress(paddle.go_right, 'Right')
screen.onkey(screen.bye,'q')

game_is_on = True

while game_is_on:

    ball.move()
    if ball.distance(paddle)< 50  and ball.ycor() < -320 :
        ball.y_bounce()
    if ball.ycor() < -380:
        game_is_on = False

    for brick in block.block_segments:
        if ball.distance(brick) < 30:
            ball.x_bounce()
            brick.hideturtle()
            x_axis_difference = ball.distance(brick)
            y_axis_difference = ball.distance(brick)
            if x_axis_difference > y_axis_difference:
                # If the ball ditches at the side of the brick then ball's x-axis will be switched.
                ball.x_bounce()
                
                
            else:
                # If the ball ditches on the top or bottom of the brick then ball's y-axis will be switched.
                ball.x_bounce()
                ball.y_bounce()
                
            block.block_segments.remove(brick)
            
            break
    if len(block.block_segments) == 0:
        game_is_on = False 



    screen.update()

screen.exitonclick()