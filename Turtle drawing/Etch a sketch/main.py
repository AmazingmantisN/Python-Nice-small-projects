from turtle import Turtle, Screen


tim = Turtle()
screen = Screen()
tim.pensize(15)
tim.pencolor("red")
  

def forwards():
  tim.forward(10)

def backwards():
  tim.backward(10)
  
def turnleft():
  new_heading = tim.heading() + 10
  tim.setheading(new_heading)
  
def turnright():  
  new_heading = tim.heading() - 10
  tim.setheading(new_heading)


screen.listen()
screen.onkeypress(key="w", fun=forwards)
screen.onkeypress(key="a", fun=turnleft)
screen.onkeypress(key="s", fun=backwards)
screen.onkeypress(key="d", fun=turnright)

screen.exitonclick()
