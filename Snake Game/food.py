from turtle import Turtle
import random as ra



class food(Turtle):
  
  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.shapesize(0.5,0.5)
    self.color("blue")
    self.speed("fastest")
    self.penup()
    self.refresh()
    
    
    
  def refresh(self):
    rand_x = ra.randint(-280, 280)
    rand_y = ra.randint(-280, 280)
    self.goto(rand_x, rand_y)
    
  
    
    