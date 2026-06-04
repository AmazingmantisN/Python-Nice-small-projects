from turtle import Turtle, Screen
import random as r


screen = Screen()
race_on = False
screen.setup(width = 500, height = 400)

user_bet = screen.textinput(title= "Make your bet", prompt=  "Type which color turtle would win")
ys = -130
colours = ["red", "blue", "green", "yellow", "orange", "purple"]

timmies = []

for turtle_index in range(0,6):
  tim = Turtle(shape = 'turtle')
  tim.penup()
  xs = -230
  tim.goto(x = xs, y = ys)
  ys = ys + 50
  tim.color(colours[turtle_index])  
  timmies.append(tim)

if user_bet :
  race_on = True
  
while race_on:
  for i in timmies:
    
   rand_distance = r.randint(0, 50)
   i.forward(rand_distance)
   
   if i.xcor() >= 210:
     winner = i
     race_on = False
     break
   
   
if user_bet == winner.pencolor():
  print("You won the bet. ENJOY")
  
else:
  print("You loser")
     
   
  

screen.exitonclick()
