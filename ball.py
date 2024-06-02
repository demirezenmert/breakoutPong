from turtle import Turtle

SPEED = 2

class BALL(Turtle):

    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)

        
        self.shape('circle')
        self.color('white')
        # self.shapesize(stretch_wid=0.5, stretch_len= 0.5)
        self.penup()
        self.goto(0,0)
        self.x_move = SPEED
        self.y_move = SPEED

    def move(self):
        self.goto(self.xcor()+self.x_move, self.ycor() + self.y_move)

        if self.xcor() > 280 or self.xcor() < -280:
            
            self.x_bounce()
        # if self.ycor() > 380 or self.ycor() < -380:
            # self.y_bounce()
        if self.ycor() > 380:
            self.y_bounce()


    def x_bounce(self):
        self.x_move *= -1
    def y_bounce(self):
        self.y_move *= -1