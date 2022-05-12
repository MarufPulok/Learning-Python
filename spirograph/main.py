import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

########### Challenge 5 - Spirograph ########
t.speed("fastest")

def draw_spirograph(side):
    
    for i in range(int(360/side)):
        t.color(random_color())
        
        t.circle(100)
        t.setheading(t.heading() + side)
    

draw_spirograph(100)







t.Screen().exitonclick()