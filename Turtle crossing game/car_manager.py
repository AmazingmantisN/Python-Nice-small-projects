from turtle import Turtle
import random as ra

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3


class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        
        self.create_car()
        self.speed_speed = STARTING_MOVE_DISTANCE
        
    def create_car(self):
        
        self.penup()
        self.color(ra.choice(COLORS))
        self.y_locations = ra.randint(-245, 245)
        self.goto(300,self.y_locations)
        self.shape("square")
        
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setheading(180)
        
        
        
        
            
    
    def move_forward(self):
        
        self.forward(self.speed_speed)
        
    def increase_speed(self):
        
        self.speed_speed += MOVE_INCREMENT
        
        
        
    
    
    
