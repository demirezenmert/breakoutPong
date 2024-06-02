from turtle import Turtle

LIMIT_OF_X = -240
BEGIN_OF_X = -255
BEGIN_OF_Y = 350

class BLOCK:
    
    def __init__(self):
        self.block_segments = []
    
    def create_blocks(self):
        
        pos_x = BEGIN_OF_X
        pos_y = BEGIN_OF_Y
        for i in range(4):
            for i in range(8):
                
                block = Turtle()
                block.shape('square')
                block.color('white')
                block.shapesize(stretch_wid=1, stretch_len= 3)
                block.penup()
                block.goto(pos_x, pos_y)
                self.block_segments.append(block)
                pos_x += 70
            pos_y -= 30
            pos_x = BEGIN_OF_X
        # print(self.block_segments)
        
        




   
   
