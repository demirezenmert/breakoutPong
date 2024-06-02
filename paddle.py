
from turtle import Turtle
PADDLE_SPEED = 20
class PADDLE(Turtle):

    def __init__(self,pos_x, pos_y, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)

        
        
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=1, stretch_len= 5)
        self.penup()
        self.goto(pos_x, pos_y)

    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())
    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    
