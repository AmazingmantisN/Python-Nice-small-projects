from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0






class Snake():
  
  STARTING_POS= [(0,0), (-20,0), (-40,0)]
  DISTANCE = 20
  
  def __init__(self):
    
    self.segments = []
    self.create_snake()
    self.head = self.segments[0]
      
  def create_snake(self):
    for position in self.STARTING_POS:
      seg_1 = Turtle(shape="square")
      seg_1.color("White")  
      seg_1.penup()
      seg_1.goto(position)
      seg_1.speed(0)
      self.segments.append(seg_1)
    
  def move(self):
    for segnum in range(len(self.segments)- 1, 0, -1):
      ecks = self.segments[segnum - 1].xcor()
      why = self.segments[segnum-1].ycor()
      self.segments[segnum].goto(ecks, why)
    
    self.head.forward(self.DISTANCE)
    
    
  def up(self):
    if self.head.heading() != DOWN: 
      self.head.setheading(UP)
    
  def down(self):
    if self.head.heading() != UP:
      self.head.setheading(DOWN)

  def right(self):
    if self.head.heading() != LEFT:
     self.head.setheading(0)
    
  def left(self):
    if self.head.heading() != RIGHT:
     self.head.setheading(180)    
     
  def extend(self):
      seg_1 = Turtle(shape="square")
      seg_1.color("White")  
      seg_1.penup()
      seg_1.goto(self.segments[-1].position())
      seg_1.speed(0)
      self.segments.append(seg_1)
    
    
  

