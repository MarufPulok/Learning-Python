from turtle import *
from random import *
t = Turtle()

# def draw_triangle(length):
#     t.pencolor("red")
#     for i in range(3):
#         t.fd(length)
#         t.rt(360/3)
    

# def draw_square(length):
#     t.pencolor("blue")
#     for i in range(4):
        
#         t.fd(length)
#         t.rt(360/4)
    
   
# def draw_pentagon(length):
#     t.pencolor("green")
#     for i in range(5):
#         t.fd(length)
#         t.rt(360/5) 
    

# def draw_hexagon(length):
#     t.pencolor("yellow")
#     for i in range (6):
#         t.fd(length)
#         t.rt(360/6)

# def draw_heptagon(length):
#     t.pencolor("purple")
#     for i in range(7):
#         t.fd(length)
#         t.rt(360/7)
        

# def draw_octagon(length):
#     t.pencolor("orange")
#     for i in range(8):
#         t.fd(length)
#         t.rt(360/8)

# def draw_nonagon(length):
#     t.pencolor("brown")
#     for i in range(9):
#         t.fd(length)
#         t.rt(360/9)

# def draw_decagon(length):
#     t.pencolor("black")
#     for i in range(10):
#         t.fd(length)
#         t.rt(360/10)
        
        
# draw_triangle(100)
# draw_square(100)
# draw_pentagon(100)
# draw_hexagon(100)
# draw_heptagon(100)
# draw_octagon(100)
# draw_nonagon(100)
# draw_decagon(100)


def draw_shape(length, sides):
    r = random()
    g = random()
    b = random()
    t.pencolor(r, g, b)
    for i in range(sides):
        t.fd(length)
        t.rt(360/sides)

for i in range(3, 11):
    draw_shape(100, i)

screen = Screen()
screen.exitonclick()