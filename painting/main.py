import random
import turtle as t

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     # rgb_colors.append(color.rgb)
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
#
# print(rgb_colors)

color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50),
              (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73),
              (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158),
              (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19),
              (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.setheading(225)
tim.penup()
tim.hideturtle()
tim.fd(250)
tim.setheading(0)


# t.fd(100)

def move_to_initial_position():
    tim.penup()
    tim.lt(90)
    tim.fd(50)
    tim.lt(90)
    tim.fd(500)
    tim.setheading(0)


def make_a_dot():
    tim.dot(20, random.choice(color_list))

    tim.penup()
    tim.fd(50)


for i in range(10):
    for j in range(10):
        make_a_dot()
    move_to_initial_position()


t.Screen().exitonclick()
