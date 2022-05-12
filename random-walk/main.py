import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
directions = [0, 90, 180, 270]
tim.pensize(10)

tim.speed("fastest")
for i in range(500):
    tim.fd(30)
    tim.color(random_colour())
    
    tim.setheading(random.choice(directions))










t.Screen().exitonclick()