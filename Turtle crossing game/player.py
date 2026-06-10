from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280



class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.color("black")
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        self.setheading(90)
        
        
    def moveup(self):
        self.forward(MOVE_DISTANCE)
    
    def movedown(self):
        self.backward(MOVE_DISTANCE)
        
        
    def reached_finishline(self):
        self.goto(STARTING_POSITION)