import turtle
from turtle import *
import random

timmy = Turtle()
timmy.shape('square')
timmy.color("red","blue")


# #Challenge 1 : Draw square
# for x in range(4):
#     timmy.forward(100)
#     timmy.right(90)



# # Challenge 2 = dashed line
# for x in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()



# # Challenge 3: draw square, pentagon, octagon, nonagon, decagon with 1 side common
# colors = ['red','green','blue','black','cyan','orange','seagreen','pink','purple']
#
#
# def draw_shapes(num_sides):
#     timmy.color(random.choice(colors))
#     angle = 360 / num_sides
#     for x in range (num_sides):
#         timmy.forward(100)
#         timmy.right(angle)
#
# timmy.penup()
# timmy.goto(0,50)
# timmy.pendown()
# for y in range (3,10):
#     draw_shapes(y)



# # Challenge 4: Generate a random walk
# turn_angle = [0,90,180,270]
# colors = ['red','green','blue','black','cyan','orange','seagreen','pink','purple']
#
# def random_walk():
#     timmy.color(random.choice(colors))
#     timmy.speed(5.0)
#     timmy.setheading(random.choice(turn_angle))
#     # timmy.right(random.choice(turn_angle))
#     timmy.forward(30)
#
# for steps in range(0,100):
#     timmy.pensize(10)
#     random_walk()
#


# # Challenge 5: generating random colors (not previously defining set the colors)
#
# turtle.colormode(255)      # note here we have to call original module and pass (1 to 255)... not the object or class
# # Note: it works only with 255... shows error for others... Don't know why
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r,g,b)
#
# turn_angle = [0,90,180,270]
#
# def random_walk():
#     timmy.color(random_color())
#     timmy.speed(5.0)
#     timmy.right(random.choice(turn_angle))
#     timmy.forward(30)
#
# for steps in range(0,100):
#     timmy.pensize(10)
#     random_walk()



# Challenge 6: Draw a spirograph circular pattern

turtle.colormode(255)      # note here we have to call original module and pass (1 to 255)... not the object or class
timmy.speed(0.5)    #("fastest")
timmy.pensize(2)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)

def draw_spirograph(size_of_gap):

    for x in range(int(360/size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        current_heading = timmy.heading()
        timmy.setheading(current_heading + size_of_gap)

draw_spirograph(5)





screen = Screen()
screen.exitonclick()
