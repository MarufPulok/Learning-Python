import random
from turtle import Turtle, Screen
# tim = Turtle("turtle")
# tim.penup()
is_race_on = False
screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")


colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -70, -40, -10, 20, 50]

turtles = [] #list of multiple turtle instances
for turtle_index in range(6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    turtles.append(new_turtle)
if user_bet:
    is_race_on = True 
while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won. {winning_color} turtle wins!")
            else:
                print(f"You've lost. {winning_color} turtle wins!")
        turtle.fd(random.randint(0,10))
        
    
screen.exitonclick() 