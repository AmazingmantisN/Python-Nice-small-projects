from turtle import Turtle, Screen
from snake import Snake
from food import food
from scorenboard import scoreboard

import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("SNAKE GAME")  
screen.tracer(0)


snake = Snake()
foodd = food()
scores = scoreboard()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True 
score = 0
while game_on:
  
  screen.update()
  time.sleep(0.1)
  
  scores.writing()
  
  
  snake.move()
  
  if snake.head.distance(foodd) < 15:
    
    foodd.refresh()
    snake.extend()
    scores.score_increase()
    
  #detect collision with wall
  if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
    game_on = False
    scores.game_over()
    
    
    
  #tail collision
  
  for segments in snake.segments:
    if segments == snake.head:
      pass
    elif snake.head.distance(segments) < 10:
      game_on = False
      scores.game_over()
    
  
  
  
  
  
    
    
    
    
  

      






screen.exitonclick()

