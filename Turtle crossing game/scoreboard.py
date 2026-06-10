from turtle import Turtle

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.hideturtle()
    self.penup()
    self.color("black") 
    self.goto(0, 250)
    self.score = 0

 
  def writing(self):
    self.write(f"Level: {self.score + 1}", align="center", font=("Arial", 24, "bold italic"))
    
  def score_increase(self):
    self.clear()
    self.score += 1
    self.writing()
    
    
  def game_over(self):
    self.clear()
    self.goto(0, 0)
    self.write("GAME OVER.", align="center", font=("Arial", 24, "bold italic"))