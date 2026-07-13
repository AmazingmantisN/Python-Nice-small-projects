import turtle
import pandas


screen = turtle.Screen() 

screen.title("US states games")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)       

all_done = True

datacsv = pandas.read_csv("50_states.csv")

def check(guess):
  yes = False
  for value in datacsv['state']:
    if guess.title() == value:
      yes = True
  return yes

counter = 0
guessed_states = []

while len(guessed_states) < 50:
  ans = screen.textinput(title="Guess the state please", prompt="What's another state's name? ")
  if ans is None or ans.title() == "Exit":
    break
  
  elif check(ans) and ans not in guessed_states:
    counter += 1
    t = turtle.Turtle()
    
    t.hideturtle()
    t.pu()
    statedata = datacsv[datacsv.state == ans.title()]
    t.goto(statedata.x.item(), statedata.y.item())
    t.write(ans.title())
    guessed_states.append(ans.title())
    
  
  
  

  
  
screen.mainloop()
