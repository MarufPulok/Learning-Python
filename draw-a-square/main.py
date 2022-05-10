#####Turtle Intro######

# import turtle as t

# timmy_the_turtle = t.Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.backward(200)
# timmy_the_turtle.right(90)
# timmy_the_turtle.left(180)
# timmy_the_turtle.setheading(0)


######## Challenge 1 - Draw a Square ############

from turtle import Turtle, Screen

t = Turtle()
t.shape("turtle")
t.color("cyan")

for i in range(0,4):
    t.fd(100)
    t.right(90)

# t.fd(100)

screen = Screen()
screen.exitonclick()