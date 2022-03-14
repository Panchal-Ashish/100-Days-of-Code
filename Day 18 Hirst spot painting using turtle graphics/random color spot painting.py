import turtle
from turtle import *
import random

# import colorgram
#
# color_list = []
# colors = colorgram.extract('image.jpg',30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_list.append((r,g,b))
#
# print(color_list)


### this code is written to extract the colors from the image and copy the color codes below
### starting 4 color codes are deleted as they are very close to white


turtle.colormode(255)
timmy = Turtle()
timmy.hideturtle()
timmy.shape('circle')
turtle.speed(0.3)
timmy.penup()           # to prevent showing the path
timmy.hideturtle()      # to dont show the turtle at the end
color_list = [ (225, 214, 111), (142, 81, 47), (199, 163, 107), (117, 165, 203), (175, 174, 27), (14, 36, 85), (42, 92, 151), (116, 176, 125), (61, 39, 22), (187, 92, 106), (187, 141, 153), (59, 119, 40), (94, 175, 64), (199, 93, 73), (241, 173, 161), (100, 121, 167), (28, 97, 17), (175, 209, 173), (104, 35, 55), (140, 85, 97), (235, 170, 175), (26, 56, 112), (78, 20, 37), (164, 190, 228), (17, 68, 17), (134, 40, 25)]

# setting the starting position
timmy.setheading(225)
timmy.forward(325)
timmy.setheading(0)

number_of_dots = 100
for dot_count in range(1,number_of_dots + 1):
    timmy.dot(10,random.choice(color_list))
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.left(90)
        timmy.forward(50)
        timmy.left(90)
        timmy.forward(500)
        timmy.left(180)


my_screen = Screen()
my_screen.exitonclick()