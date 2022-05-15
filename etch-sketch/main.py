from turtle import *

screen = Screen()
tim = Turtle()
tim.pencolor("red")
tim.pensize(5)

# jim = Turtle()
# jim.shape("turtle")
# jim.fd(100)

def forwards():
    tim.fd(10)
    
def backwards():
    tim.back(10)
    
def clockwise():
    tim.right(10)
    
def anticlockwise():
    tim.left(10)
    
def clear():
    tim.reset()
    
    
screen.listen()  
screen.onkey(forwards, "w")
screen.onkey(backwards, "s")
screen.onkey(clockwise, "d")
screen.onkey(anticlockwise, "a")
screen.onkey(clear, "c")
screen.exitonclick()