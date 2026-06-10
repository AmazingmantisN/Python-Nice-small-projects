import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

player = Player()
scores = Scoreboard()
scores.writing()



all_cars = []

game_is_on = True

screen.listen()

screen.onkeypress(player.moveup, "Up")
screen.onkeypress(player.movedown, "Down")

counter = 0

while game_is_on:
    
    time.sleep(0.1)
    screen.update()
    
    if counter % 6 == 0:
        car = CarManager()
        if scores.score > 0:
            for r in range(scores.score):
                car.increase_speed()
        all_cars.append(car)
    
  
            
            
            
                
    for c in all_cars:
        c.move_forward()
        if abs(c.ycor() - player.ycor()) < 22:
            
            # Left edge of the car (front bumper)
            front_bumper = c.xcor() - 20 
            # Right edge of the car PLUS the massive jump it just took
            back_tail = c.xcor() + c.speed_speed + 20 
            
            # If the player is anywhere inside that horizontal zone, CRASH!
            if front_bumper <= player.xcor() <= back_tail:
                game_is_on = False
                scores.game_over()
                screen.onkeypress(None, "Up")
                screen.onkeypress(None, "Down")
        
    
    if player.ycor() >= 280:
        player.reached_finishline()
        scores.score_increase()
        
        
        
        
    counter += 1


screen.exitonclick()