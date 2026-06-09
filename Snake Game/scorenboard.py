from turtle import Turtle

class scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.hideturtle()
    self.penup()
    self.color("white") 
    self.goto(0, 270)
    self.score = 0

 
  def writing(self):
    self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "bold italic"))
    
  def score_increase(self):
    self.clear()
    self.score += 1
    self.writing()
    
    
  def game_over(self):
    self.clear()
    self.goto(0, 0)
    self.write("GAME OVER.", align="center", font=("Arial", 24, "bold italic"))
    
      